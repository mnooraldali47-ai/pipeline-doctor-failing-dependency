from main import add, subtract


def test_add_positive():
    assert add(1, 2) == 3


def test_add_negative():
    assert add(-1, -2) == -3


def test_subtract():
    assert subtract(10, 4) == 6
