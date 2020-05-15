FROM python:3.7-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY scrapy.cfg .
ADD {{ cookiecutter.project_name }} ./{{ cookiecutter.project_name }}

ENTRYPOINT ["scrapy"]
CMD ["crawl", "{{ cookiecutter.project_name }}", "-o", "{{ cookiecutter.project_name }}.csv", "--loglevel", "INFO"]
