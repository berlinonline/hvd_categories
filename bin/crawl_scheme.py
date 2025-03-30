import argparse
import logging
from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import SKOS

LOG = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

DEFAULT_SCHEME_URI = 'http://data.europa.eu/bna/asd487ae75'
EUVOC = Namespace('http://publications.europa.eu/ontology/euvoc#')
HVD = Namespace('http://data.europa.eu/bna/')
SKOSXL = Namespace('http://www.w3.org/2008/05/skos-xl#')

parser = argparse.ArgumentParser(
    description="Crawl the HVD category scheme into one graph and output as nice turtle file")
parser.add_argument('--scheme',
                    help="URI of the scheme",
                    type=str,
                    default=DEFAULT_SCHEME_URI
                    )
args = parser.parse_args()
scheme_uri = args.scheme


g = Graph()
g.bind('hvd', HVD)
g.bind('skosxl', SKOSXL)
g.bind('euvoc', EUVOC)
g.parse(scheme_uri, format='xml')
LOG.info(f'downloading Scheme from : {scheme_uri}')

scheme_res = URIRef(scheme_uri)

for concept, p, o in g.triples( (None, SKOS.inScheme, scheme_res) ):
    LOG.info(f'downloading Concept from : {concept}')
    g.parse(concept, format='xml')

print(g.serialize(format='turtle'))

