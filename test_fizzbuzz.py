import pytest
from fizzbuzz import *

def test_fizzbuzz1():
    assert fizzbuzz(3) == 'fizz'

def test_fizzbuzz2():
    assert fizzbuzz(5) == 'buzz' 

def test_fizzbuzz3():
    assert fizzbuzz(15) == 'fizzbuzz'

def test_fizzbuzz4():
    assert fizzbuzz(1) == 1     