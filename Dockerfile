# python:alpine is 2.7.{latest}
FROM python:2.7-alpine

COPY requirements.txt  /src/requirements.txt
COPY static /src/static/
COPY templates /src/templates/
COPY cytek.py  /src/cytek.py

WORKDIR /src

RUN pip install -Ur requirements.txt
RUN pip install gunicorn

EXPOSE 8000

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0", "cytek:app"]
