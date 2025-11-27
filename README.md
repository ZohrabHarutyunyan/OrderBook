# OrderBook Project

Simple Python implementation of an Order Book with:
- Business logic (`OrderBook`)
- Data model (`Order`)
- POM layer (`OrderBookPO`)
- Pytest tests with fixtures and parametrization
- Positive/negative test separation and markers

## Quick start

Install in editable mode:
```
pip install -e .
```

Run tests locally:
```
pytest -q
```

Build & run via Docker:
```
docker build -t orderbook .
docker run --rm orderbook bash -c "pytest -q"
```

Project structure:
```
orderbook/
tests/
Dockerfile
docker-compose.yaml
requirements.txt
README.md
```
