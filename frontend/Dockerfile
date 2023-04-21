FROM python:3.10

COPY ./frontend/requirements.txt /frontend/requirements.txt

RUN pip install --trusted-host pypi.python.org -r /frontend/requirements.txt

WORKDIR /frontend

COPY ./frontend /frontend
