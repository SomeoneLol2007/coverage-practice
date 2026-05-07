"""Модуль для работы с оценками студентов."""

def get_average(scores):
    """Вычислить средний балл из списка оценок."""
    if not scores:
        raise ValueError("Список оценок не может быть пустым")
    return sum(scores) / len(scores)

def get_grade(score):
    """Вернуть оценку по числовому баллу (0-100)."""
    if score >= 90:
        return "Отлично"
    if score >= 70:
        return "Хорошо"
    if score >= 50:
        return "Удовлетворительно"
    return "Неудовлетворительно"

def is_passed(score):
    """Проверить, сдан ли экзамен (порог — 50 баллов)."""
    return score >= 50
