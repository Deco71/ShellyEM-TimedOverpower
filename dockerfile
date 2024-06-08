FROM python:latest
WORKDIR /usr/app/src

COPY main.py ./
COPY .env ./

CMD [ "python", "./main.py"]