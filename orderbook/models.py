from dataclasses import dataclass

@dataclass
class Order:
    id: int
    type: str
    price: int
    volume: int
