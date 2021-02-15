FROM python:3

ADD src /src

RUN pip install pystrich

CMD ["python", "./src/main.py"]