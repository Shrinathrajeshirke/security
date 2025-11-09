FROM python:3.10-slim-bullseye
WORKDIR /app
COPY . /app

RUN apt-get update -y && apt install awscli -y

RUN pip install --no-cache-dir -r requirements.txt awscli

EXPOSE 8000

CMD ["python3", "app.py"]