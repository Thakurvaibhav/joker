FROM python:2.7-slim
WORKDIR /app

COPY app /app
RUN pip install -r requirements.txt
