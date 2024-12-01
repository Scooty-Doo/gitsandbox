# tests/test_calc.py

import pytest
from calc.calculator import add, sub, mul, div


def test_add():
    assert add(2, 3) == 5
    assert add(-2, -3) == -5


def test_sub():
    assert sub(5, 3) == 2
    assert sub(-3, -7) == 4


def test_mul():
    assert mul(4, 3) == 12
    assert mul(-2, 3) == -6


def test_div():
    assert div(10, 2) == 5
    assert div(-10, -2) == 5

    with pytest.raises(ValueError):
        div(10, 0)
