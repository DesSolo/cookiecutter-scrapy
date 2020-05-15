scrapy {{ cookiecutter.project_name }}
=====
### View target url
`scrapy view url`
### Run crawler
`scrapy crawl {{ cookiecutter.project_name }} -o {{ cookiecutter.project_name }}.csv -t csv --logfile "{{ cookiecutter.project_name }}.log" --loglevel INFO`
