FROM python:3.12.0

WORKDIR /app

COPY requirements.txt .

ENV CORL_ENV=

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "main.py"]
