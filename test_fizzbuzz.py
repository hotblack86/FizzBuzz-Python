import pytest
from fizzbuzz import *

def test_fizzbuzz1():
    assert fizzbuzz(3) == 'fizz'

def test_fizzbuzz2():
    assert fizzbuzz(5) == 'buzz' 

def test_fizzbuzz3():
    assert fizzbuzz(15) == 'fizzbuzz'

def test_fizzbuzz4():
    assert fizzbuzz(37) == 37

def test_fizzbuzz5():
    assert fizzbuzz(6) == 'fizz'

def test_fizzbuzz6():
    assert fizzbuzz(10) == 'buzz'

def test_fizzbuzz7():
    assert fizzbuzz(45) == 'fizzbuzz'        
