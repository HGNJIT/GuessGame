FROM python:3

WORKDIR /usr/src/app

RUN pip install pystrich

CMD [ "python", "./main.py" ]