FROM python:3.12

WORKDIR /app

COPY Script.py .

CMD ["python", "./Script.py"]