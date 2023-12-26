FROM python:3.10.2-slim-buster

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    python3-setuptools

RUN pip install --upgrade pip

RUN pip install \
    Flask \
    scikit-learn \
    numpy==1.26.2 \
    joblib

WORKDIR /app

COPY . .

CMD ["python", "app.py"]
