"""Простой калькулятор."""

def add(a, b):
    """Сложение двух чисел."""
    return a + b

def subtract(a, b):
    """Вычитание двух чисел."""
    return a - b

def multiply(a, b):
    """Умножение двух чисел."""
    return a * b

def divide(a, b):
    """Деление двух чисел. Вызывает ошибку при делении на ноль."""
    if b == 0:
        raise ValueError("Деление на ноль недопустимо")
    return a / b

def is_even(n):
    """Проверяет, является ли число чётным."""
    return n % 2 == 0
