FROM python:3.6

COPY ./requirements.txt /web/
COPY ./serve.sh /web/

WORKDIR /web

RUN pip install -r requirements.txt

ENTRYPOINT ["./serve.sh"]
