FROM python:3.8-slim

# Set the working directory
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

CMD fastapi run --reload