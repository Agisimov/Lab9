
import pytest
from calculator import Calculator


calc = Calculator()


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (10, 20, 30),
    (-5, 5, 0),
    (0, 0, 0)
])
def test_add(a, b, expected):
    assert calc.add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (9, 3, 3),
    (7, 2, 3.5)
])
def test_divide(a, b, expected):
    assert calc.divide(a, b) == expected


@pytest.mark.parametrize("number, expected", [
    (2, True),
    (7, True),
    (10, False),
    (1, False),
    (0, False),
    (-5, False)
])
def test_is_prime_number(number, expected):
    assert calc.is_prime_number(number) == expected


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)
