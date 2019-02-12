import pytest
from fizzbuzz import *

def test_fizzbuzz1():
    assert fizzbuzz(3) == 'fizz'

def test_fizzbuzz2():
    assert fizzbuzz(5) == 'buzz'   