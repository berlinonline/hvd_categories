# High-Value Dataset Categories

Code for crawling the SKOS scheme for high-value dataset categories.

- [bin/crawl_scheme.py](bin/crawl_scheme.py): Start with the URI of the scheme itself, then continue by download the top-level concepts and their sub-concepts. Output a complete Turtle file.
- [bin/skos2mermaid.py](bin/skos2mermaid.py): Convert the Turtle file with the SKOS scheme to a mermaid graph. Specify a language code to decide which language to use for the labels.

## Charts for various languages:

* [Bulgarian](charts/hvd_scheme_bg.md) (bg)
* [Czech](charts/hvd_scheme_cs.md) (cs)
* [Danish](charts/hvd_scheme_da.md) (da)
* [German](charts/hvd_scheme_de.md) (de)
* [Greek](charts/hvd_scheme_el.md) (el)
* [English](charts/hvd_scheme_en.md) (en)
* [Spanish](charts/hvd_scheme_es.md) (es)
* [Estonian](charts/hvd_scheme_et.md) (et)
* [Finnish](charts/hvd_scheme_fi.md) (fi)
* [French](charts/hvd_scheme_fr.md) (fr)
* [Irish](charts/hvd_scheme_ga.md) (ga)
* [Croatian](charts/hvd_scheme_hr.md) (hr)
* [Hungarian](charts/hvd_scheme_hu.md) (hu)
* [Italian](charts/hvd_scheme_it.md) (it)
* [Lithuanian](charts/hvd_scheme_lt.md) (lt)
* [Latvian](charts/hvd_scheme_lv.md) (lv)
* [Maltese](charts/hvd_scheme_mt.md) (mt)
* [Dutch](charts/hvd_scheme_nl.md) (nl)
* [Polish](charts/hvd_scheme_pl.md) (pl)
* [Portuguese](charts/hvd_scheme_pt.md) (pt)
* [Romanian](charts/hvd_scheme_ro.md) (ro)
* [Slovak](charts/hvd_scheme_sk.md) (sk)
* [Slovenian](charts/hvd_scheme_sl.md) (sl)
* [Swedish](charts/hvd_scheme_sv.md) (sv)

## Context

* scheme: http://data.europa.eu/bna/asd487ae75
* regulation: https://eur-lex.europa.eu/eli/reg_impl/2023/138/oj?uri=CELEX:32023R0138#enc_1

## License

All code in this repository is published under the [MIT License](License).

