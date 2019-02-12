import pytest
from fizzbuzz import *

class TestFizzBuzz(object):
  def test_1(self):
    assert fizzbuzz(3) == 'fizz'

  def test_2(self):
    assert fizzbuzz(5) == 'buzz' 

  def test_3(self):
    assert fizzbuzz(15) == 'fizzbuzz'

  def test_4(self):
    assert fizzbuzz(37) == 37

  def test_5(self):
    assert fizzbuzz(6) == 'fizz'

  def test_6(self):
    assert fizzbuzz(10) == 'buzz'

  def test_7(self):
    assert fizzbuzz(45) == 'fizzbuzz'        
