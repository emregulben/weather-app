FROM python:3.8

WORKDIR /weather-app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT ["python3"]

CMD ["app.py"]