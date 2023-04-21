FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

COPY ./backend/requirements.txt /backend/requirements.txt

RUN pip install --trusted-host pypi.python.org -r /backend/requirements.txt

COPY ./backend /backend