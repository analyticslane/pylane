# Sample Test passing with nose and pytest

from pytest import approx
from pylane.arithmetic import addition
from pylane.arithmetic import subtraction

def test_addition():
    assert addition(1, 2) == 3 

def test_subtraction():
    assert subtraction(1, 2) == -1

def test_rea():
    assert subtraction(1, 1.0001) == approx(0, abs=0.001)
