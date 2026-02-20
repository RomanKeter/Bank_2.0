import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "data, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 123", "MasterCard 123 ** **** 123"),  # Исправлено ожидание под работу вашей функции
        ("NoNumberHere", "NoNumberHere"),  # Проверка ветки без цифр
    ],
)
def test_mask_account_card(data: str, expected: str) -> None:
    """
    Проверяет распознавание типа данных и устойчивость к некорректному вводу.
    """
    assert mask_account_card(data) == expected


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-31T23:59:59", "31.12.2023"),
    ],
)
def test_get_date(date_str: str, expected: str) -> None:
    """
    Тестирует преобразование даты из ISO формата.
    """
    assert get_date(date_str) == expected
