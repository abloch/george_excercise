from pytest import raises
from excercise import str2int

def test_one_digit():
    assert str2int('1') == 1

def test_two_digits():
    assert str2int('54') == 54

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
