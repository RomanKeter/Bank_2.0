import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        (1111222233334444, "1111 22** **** 4444"),
        ("", " ** **** "),  # Граничный случай: пустая строка (исправлен пробел)
    ],
)
def test_get_mask_card_number(card: str, expected: str) -> None:
    """
    Тестирует маскирование номера карты для различных форматов и типов.
    """
    assert get_mask_card_number(card) == expected


@pytest.mark.parametrize(
    "account, expected",
    [
        ("73654108430135874305", "**4305"),
        (1234567890, "**7890"),
        ("123", "**123"),  # Номер счета меньше ожидаемой длины
    ],
)
def test_get_mask_account(account: str, expected: str) -> None:
    """
    Тестирует маскирование номера счета, включая короткие номера.
    """
    assert get_mask_account(account) == expected
