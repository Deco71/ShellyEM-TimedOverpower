FROM python:latest
WORKDIR /usr/app/src

COPY main.py ./
COPY .env ./
RUN pip3 install python-dotenv requests
CMD [ "python", "-u", "./main.py"]