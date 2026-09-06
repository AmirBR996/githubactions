from src.math import add, sub


def test_add():
    assert add(2, 3) == 5
    assert add(4, 7) == 11
    assert add(4, 2) == 6
    assert add(4, 9) == 13
    assert add(2, 2) == 4
    assert add(2, 1) == 3


def test_sub():
    assert sub(5, 3) == 2
    assert sub(10, 4) == 6
    assert sub(7, 2) == 5
    assert sub(9, 4) == 5
    assert sub(6, 2) == 4
    assert sub(10, 1) == 9
