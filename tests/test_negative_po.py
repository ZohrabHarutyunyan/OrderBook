import pytest
pytestmark = pytest.mark.negative

@pytest.mark.parametrize("order",[
    {"id":1,"type":"wrong","price":10,"volume":1},
    {"id":2,"type":"bid","price":-10,"volume":1},
    {"id":3,"type":"ask","price":10,"volume":-5},
])
def test_invalid_orders_parametrized(po,order):
    with pytest.raises(ValueError):
        po.create_orders([order])

def test_duplicate_id(po):
    po.create_order(1,"bid",10,1)
    with pytest.raises(ValueError):
        po.create_order(1,"ask",5,1)

@pytest.mark.parametrize("bad_id",[999,-1,12345])
def test_cancel_unknown_id(po,bad_id):
    with pytest.raises(KeyError):
        po.cancel_order(bad_id)
