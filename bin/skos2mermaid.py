import argparse
import logging
from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import RDF, SKOS

LOG = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

DEFAULT_SCHEME_PATH = 'data/hvd_scheme.ttl'
DEFAULT_LANGUAGE = 'en'
EUVOC = Namespace('http://publications.europa.eu/ontology/euvoc#')
HVD = Namespace('http://data.europa.eu/bna/')
SKOSXL = Namespace('http://www.w3.org/2008/05/skos-xl#')

class MermaidFlowchartConverter(object):

    def __init__(self, config: dict):
        self.lang = config['lang']

    def header(self) -> str:
        header = f"""
# High-Value Dataset Categories
## Language code: **{lang}**

```mermaid
flowchart LR"""
        return header
    
    def scheme(self, scheme_uri: str, scheme_label: str) -> str:
        scheme = f"""        
{scheme_uri}[{result['scheme_label']}]
click {scheme_uri} href \"{scheme_uri}\""""
        return scheme

    def top_level_concept(self, scheme_uri: str, top_concept_uri: str, top_concept_label: str) -> str:
        concept = f"""{scheme_uri}-->{top_concept_uri}
{top_concept_uri}[\"{top_concept_label}\"]
click {top_concept_uri} href \"{top_concept_uri}\""""
        return concept

    def sub_level_concept(self, top_concept_uri: str, sub_concept_uri: str, sub_concept_label: str) -> str:
        concept = f"""{top_concept_uri}-->{sub_concept_uri}
{sub_concept_uri}[\"{sub_concept_label}\"]
click {sub_concept_uri} href \"{sub_concept_uri}\""""
        return concept

    def footer(self) -> str:
        footer = """```"""
        return footer
    
parser = argparse.ArgumentParser(
    description="Iterate a SKOS scheme and generate a mermaid diagram from it.")
parser.add_argument('--scheme_path',
                    help="Path to the turtle file with the SKOS scheme",
                    type=str,
                    default=DEFAULT_SCHEME_PATH
                    )
parser.add_argument('--language',
                    help="Language to use for the diagram",
                    type=str,
                    default=DEFAULT_LANGUAGE
                    )
args = parser.parse_args()
scheme_path = args.scheme_path
lang = args.language

g = Graph()
g.parse(scheme_path)

scheme_query = '''
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?scheme ?scheme_label
WHERE {
    ?scheme
        a skos:ConceptScheme ;
        skos:prefLabel ?scheme_label ;
    .
}
'''

top_concept_query = f'''
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?concept ?concept_label
WHERE {{
    ?scheme skos:hasTopConcept ?concept .
    ?concept skos:prefLabel ?concept_label .
    FILTER (lang(?concept_label) = "{lang}")
}}
'''

sub_concept_query = f'''
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?concept ?concept_label
WHERE {{
    ?top_concept skos:narrower ?concept .
    ?concept skos:prefLabel ?concept_label .
    FILTER (lang(?concept_label) = "{lang}")
}}
'''

converter = MermaidFlowchartConverter({'lang': lang})

print(converter.header())
for result in g.query(scheme_query):
    scheme_uri = result['scheme'].toPython()
    LOG.info(f"Scheme:  {result['scheme_label']} ({scheme_uri})")
    print(f"{scheme_uri}[{result['scheme_label']}]")
    print(f'click {scheme_uri} href "{scheme_uri}"')
    query = top_concept_query.replace("?scheme", f"<{scheme_uri}>")
    for result in g.query(query):
        top_concept_uri = result['concept'].toPython()
        LOG.info(f"    Top concept: {result['concept_label']} ({top_concept_uri})")
        print(converter.top_level_concept(scheme_uri, top_concept_uri, result['concept_label']))
        query = sub_concept_query.replace('?top_concept', f"<{top_concept_uri}>")
        for result in g.query(query):
            sub_concept_uri = result['concept'].toPython()
            LOG.info(f"        Sub-concept: {result['concept_label']} ({sub_concept_uri})")
            print(converter.sub_level_concept(top_concept_uri, sub_concept_uri, result['concept_label']))
            query = sub_concept_query.replace('?top_concept', f"<{sub_concept_uri}>")
            for result in g.query(query):
                sub_sub_concept_uri = result['concept'].toPython()
                LOG.info(f"            Sub-concept: {result['concept_label']} ({sub_sub_concept_uri})")
                print(converter.sub_level_concept(sub_concept_uri, sub_sub_concept_uri, result['concept_label']))

print(converter.footer())

