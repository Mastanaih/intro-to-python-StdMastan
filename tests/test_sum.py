# tests/test_sum.py

from sum_of_two_numbers import sum_two_numbers

def test_sum_positive():
    assert sum_two_numbers(3, 5) == 8

def test_sum_zero():
    assert sum_two_numbers(0, 0) == 0

def test_sum_large_numbers():
    assert sum_two_numbers(100000, 200000) == 300000
