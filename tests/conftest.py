import pytest
from orderbook.book import OrderBook
from orderbook.po import OrderBookPO

@pytest.fixture
def orderbook():
    return OrderBook()

@pytest.fixture
def po(orderbook):
    return OrderBookPO(book=orderbook)

@pytest.fixture
def sample_orders():
    return [
        {"id":10,"type":"bid","price":100,"volume":5},
        {"id":11,"type":"bid","price":101,"volume":2},
        {"id":12,"type":"bid","price":100,"volume":3},
        {"id":20,"type":"ask","price":105,"volume":4},
        {"id":21,"type":"ask","price":106,"volume":1},
        {"id":22,"type":"ask","price":105,"volume":6},
    ]
