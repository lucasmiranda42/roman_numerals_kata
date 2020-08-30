from main import *


def test_one():
    assert to_roman(1) == "I"


def test_five():
    assert to_roman(5) == "V"


def test_ten():
    assert to_roman(10) == "X"


def test_fifty():
    assert to_roman(50) == "L"


def test_hundred():
    assert to_roman(100) == "C"


def test_fivehundred():
    assert to_roman(500) == "D"


def test_thousand():
    assert to_roman(1000) == "M"


def test_seven():
    assert to_roman(7) == "VII"


def test_nine():
    assert to_roman(9) == "IX"


def test_find_max_digit():
    assert find_digit(8, reverse=True) == 5


def test_find_min_digit():
    assert find_digit(8, reverse=False) == 10


def test_199():
    assert to_roman(199) == "CXCIX"


def test_42():
    assert to_roman(42) == "XLII"


def test_valid_roman():
    assert is_valid_roman("XIX")


def test_invalid_roman():
    assert not is_valid_roman("VIIIXL")


def test_to_dec_basic():
    assert to_decimal("I") == 1
    assert to_decimal("V") == 5
    assert to_decimal("X") == 10
    assert to_decimal("L") == 50
    assert to_decimal("C") == 100
    assert to_decimal("D") == 500
    assert to_decimal("M") == 1000


def test_XI():
    assert to_decimal("XI") == 11


def test_MCCCDV():
    assert to_decimal("MCCCLV") == 1355


def test_IX():
    assert to_decimal("IX") == 9


def test_all_to_decimal():
    for i in range(1, 3999):
        assert i == to_decimal(to_roman(i))
