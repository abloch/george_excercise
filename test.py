from pytest import raises
from random import randint
from excercise import str2int

def test_one_digit():
    assert str2int('1') == 1

def test_two_digits():
    assert str2int('54') == 54

def test_three_digits():
    assert str2int('621') == 621

def test_four_digits():
    assert str2int('9124') == 9124

def test_100_random_ints():
    for _ in range(100):
        s = str(randint(0, 99999999))
        assert str2int(s) == int(s)

def test_bad_number():
    with raises(ValueError):
        assert str2int('8987987sd')

def test_empty_string():
    with raises(ValueError):
        assert str2int('')

def test_dict():
    with raises(ValueError):
        assert str2int(dict())

def test_float():
    with raises(ValueError):
        assert str2int('2.2')
