import pytest
from hometask.calculator.calculator import Calculator

Calc = Calculator()

@pytest.mark.parametrize(
    'first_num, second_num, result',
    [
        (1, 2, 3),
        (5, 3, 8),
    ]
)
def test_add(first_num, second_num, result):
    assert Calc.add(first_num, second_num) == result


@pytest.mark.parametrize(
    'first_num, second_num, result',
    [
        (1, 2, -1),
        (5, 3, 2),
    ]
)
def test_subtract(first_num, second_num, result):
    assert Calc.subtract(first_num, second_num) == result


@pytest.mark.parametrize(
    'first_num, second_num, result',
    [
        (8, 2, 4),
        (-10, 5, -2),
    ]
)
def test_divide(first_num, second_num, result):
    assert Calc.divide(first_num, second_num) == result


@pytest.mark.parametrize(
    'first_num, second_num, result',
    [
        (3, 2, 6),
        (-5, 3, -15),
    ]
)
def test_multiply(first_num, second_num, result):
    assert Calc.multiply(first_num, second_num) == result


@pytest.mark.parametrize(
    'first_num, second_num, result',
    [
        (11, 2, 1),
        (31, 3, 1),
    ]
)
def test_mod(first_num, second_num, result):
    assert Calc.mod(first_num, second_num) == result


@pytest.mark.parametrize(
    'first_num, second_num, result',
    [
        (3, 2, 9),
        (5, 3, 125),
    ]
)
def test_power(first_num, second_num, result):
    assert Calc.power(first_num, second_num) == result


@pytest.mark.parametrize(
    'first_num, result',
    [
        (9, 3),
        (25, 5),
    ]
)
def test_root(first_num, result):
    assert Calc.root(first_num) == result
