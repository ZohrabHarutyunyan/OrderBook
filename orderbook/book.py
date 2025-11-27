from typing import Dict, List, Optional, Union
from collections import defaultdict
from .models import Order

class OrderBook:
    def __init__(self):
        self._orders: Dict[int, Order] = {}

    def add(self, orders: Union[Order, dict, List[Union[Order, dict]]]):
        if isinstance(orders, (Order, dict)):
            orders = [orders]
        for o in orders:
            if isinstance(o, dict):
                order = Order(id=int(o["id"]), type=o["type"], price=int(o["price"]), volume=int(o["volume"]))
            else:
                order = o
            if order.id in self._orders:
                raise ValueError(f"Order with id {order.id} already exists")
            if order.type not in ("bid","ask"):
                raise ValueError("Order type must be 'bid' or 'ask'")
            if order.price < 0 or order.volume < 0:
                raise ValueError("Price and volume must be non-negative")
            self._orders[order.id] = order

    def remove(self, order_id: int):
        if order_id not in self._orders:
            raise KeyError(f"Order with id {order_id} not found")
        del self._orders[order_id]

    def get(self, order_id: int):
        if order_id not in self._orders:
            raise KeyError(f"Order with id {order_id} not found")
        o = self._orders[order_id]
        return {"type": o.type, "price": o.price, "volume": o.volume}

    def update(self, order_id: int, *, price=None, volume=None):
        if order_id not in self._orders:
            raise KeyError(f"Order with id {order_id} not found")
        o = self._orders[order_id]
        if price is not None:
            if price < 0:
                raise ValueError("Price must be non-negative")
            o.price = price
        if volume is not None:
            if volume < 0:
                raise ValueError("Volume must be non-negative")
            o.volume = volume

    def snapshot(self):
        asks = defaultdict(int)
        bids = defaultdict(int)
        for o in self._orders.values():
            if o.volume == 0:
                continue
            (asks if o.type=='ask' else bids)[o.price] += o.volume
        return {
            "Asks":[{"price":p,"volume":v} for p,v in sorted(asks.items())],
            "Bids":[{"price":p,"volume":v} for p,v in sorted(bids.items(), reverse=True)]
        }
