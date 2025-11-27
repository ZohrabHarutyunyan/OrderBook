from typing import List, Dict, Optional
from .book import OrderBook

class OrderBookPO:
    def __init__(self, book: Optional[OrderBook] = None):
        self.book = book or OrderBook()
    def create_order(self, id: int, type: str, price: int, volume: int):
        self.book.add({"id":id,"type":type,"price":price,"volume":volume})
    def create_orders(self, orders: List[Dict]):
        self.book.add(orders)
    def cancel_order(self, id: int):
        self.book.remove(id)
    def modify_order(self, id: int, *, price=None, volume=None):
        self.book.update(id, price=price, volume=volume)
    def get_order(self, id:int):
        return self.book.get(id)
    def view_snapshot(self):
        return self.book.snapshot()
