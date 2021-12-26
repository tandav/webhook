FROM python:3-alpine

RUN pip install fastapi uvicorn

EXPOSE 8090

COPY server.py /app/

WORKDIR /app
#CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8090", "--ssl-certfile", "fullchain.pem", "--ssl-keyfile", "privkey.pem"]
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8090", "--limit-concurrency", "2"]
