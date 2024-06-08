FROM python:latest
WORKDIR /usr/app/src

COPY main.py ./
RUN pip3 install python-dotenv requests
CMD [ "python", "./main.py"]