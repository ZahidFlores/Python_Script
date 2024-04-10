FROM python:3.12

WORKDIR /app

COPY requeriements.txt /app

RUN pip install -r requeriements.txt

COPY Script.py /app/

EXPOSE 3000

CMD [ "python", "./Script.py"]