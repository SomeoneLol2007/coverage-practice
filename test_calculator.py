"""Тесты для модуля calculator."""
import pytest
from calculator import add, subtract, multiply, divide, is_even

def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 3) == 7
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 100) == 0
