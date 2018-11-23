FROM python:3.6

COPY ./requirements.txt ./
COPY ./serve.sh ./

RUN pip install -r requirements.txt

CMD ["sh", "serve.sh"]
