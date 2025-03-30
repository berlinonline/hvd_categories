data/hvd_scheme.ttl:
	python bin/crawl_scheme.py > $@

charts/hvd_scheme_%.md: data/hvd_scheme.ttl
	python bin/skos2mermaid.py --scheme_path=$< --lang="$*" > $@

all_charts: charts/hvd_scheme_bg.md charts/hvd_scheme_cs.md charts/hvd_scheme_da.md charts/hvd_scheme_de.md charts/hvd_scheme_el.md charts/hvd_scheme_en.md charts/hvd_scheme_es.md charts/hvd_scheme_et.md charts/hvd_scheme_fi.md charts/hvd_scheme_fr.md charts/hvd_scheme_ga.md charts/hvd_scheme_hr.md charts/hvd_scheme_hu.md charts/hvd_scheme_it.md charts/hvd_scheme_lt.md charts/hvd_scheme_lv.md charts/hvd_scheme_mt.md charts/hvd_scheme_nl.md charts/hvd_scheme_pl.md charts/hvd_scheme_pt.md charts/hvd_scheme_ro.md charts/hvd_scheme_sk.md charts/hvd_scheme_sl.md charts/hvd_scheme_sv.md 
