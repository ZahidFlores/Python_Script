FROM python:3.12

WORKDIR /app

RUN pip install mysql-connector

COPY Script.py /app/


CMD [ "python", "./Script.py"]