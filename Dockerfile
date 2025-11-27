FROM python:3.10-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip && pip install -r requirements.txt && pip install -e .
CMD ["python","-c","print('OrderBook project ready!')"]
