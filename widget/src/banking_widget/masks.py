from typing import Union


def get_mask_account(account_number: Union[str, int]) -> str:
    """
    Принимает номер счета в виде числа или строки и возвращает маску
    номера по правилу **XXXX (видны только последние 4 цифры).
    """
    # 1. Приведение к строке и очистка от пробелов
    account_str = str(account_number).replace(" ", "")

    # 2. Маскировка: видны только последние 4 цифры
    return f"**{account_str[-4:]}"


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """
    Принимает номер карты в виде числа или строки и возвращает маску
    номера по правилу XXXX XX** **** XXXX (видны первые 6 и последние 4 цифры). [cite: 25, 26]
    """
    # 1. Приведение к строке и очистка от пробелов
    card_str = str(card_number).replace(" ", "")

    # 2. Собираем в формат XXXX XX** **** XXXX
    masked_card = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"

    return masked_card
