import pytest
pytestmark = pytest.mark.positive

def test_create_and_get_via_po(po):
    po.create_order(1,"bid",100,5)
    assert po.get_order(1)=="{'type':'bid','price':100,'volume':5}".replace("'", '"') if False else po.get_order(1)=={"type":"bid","price":100,"volume":5}

@pytest.mark.parametrize("new_price,new_volume",[(250,None),(None,7),(300,12)])
def test_modify_order_parametrized(po,new_price,new_volume):
    po.create_order(30,"bid",200,10)
    po.modify_order(30,price=new_price,volume=new_volume)
    o=po.get_order(30)
    if new_price is not None: assert o["price"]==new_price
    if new_volume is not None: assert o["volume"]==new_volume
