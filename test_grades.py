"""Тесты для модуля grades."""
import pytest
from grades import get_average, get_grade, is_passed

def test_get_average():
    # Проверьте обычный список, список из одного элемента, дробные значения
    assert get_average([4, 5, 3]) == 4.0
    assert get_average([10]) == 10.0

def test_get_average_empty():
    with pytest.raises(ValueError):
        get_average([])

def test_get_grade():
    # Проверьте все границы: 90, 70, 50, а также значения выше/ниже
    assert get_grade(95) == "Отлично"
    assert get_grade(80) == "Хорошо"
    assert get_grade(60) == "Удовлетворительно"
    assert get_grade(40) == "Неудовлетворительно"
    # граничные случаи
    assert get_grade(90) == "Отлично"
    assert get_grade(70) == "Хорошо"
    assert get_grade(50) == "Удовлетворительно"

def test_is_passed():
    assert is_passed(70) is True
    assert is_passed(50) is True
    assert is_passed(49) is False
    assert is_passed(0) is False
