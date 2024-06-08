FROM python:3.8-slim
WORKDIR /usr/app/src

COPY main.py ./
COPY .env ./
RUN pip3 install python-dotenv requests
CMD [ "python", "-u", "./main.py"]