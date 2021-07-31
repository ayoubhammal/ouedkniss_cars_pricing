FROM python:3.8-buster

RUN mkdir /home/api

COPY . /home/api/

RUN pip install pip --upgrade

RUN pip install -r /home/api/requirements.txt

CMD cd /home/api; python index.py