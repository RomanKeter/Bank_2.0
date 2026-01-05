from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data_string: str) -> str:
    """
    Принимает строку с названием и номером счета/карты и возвращает
    строку с замаскированным номером.
    """
    # Шаг 1: Разделяем строку на название и номер.
    # Номер всегда идет в конце строки.
    parts = data_string.rsplit(" ", 1)

    # Проверка: если в строке только одно слово, значит, номер отсутствует
    if len(parts) == 1 or not parts[-1].isdigit():
        return data_string

    name_part = parts[0]
    number_part = parts[-1]

    # Шаг 2: Определяем, что это: карта или счет?
    if name_part.lower().startswith("счет"):
        # Это счет. Используем функцию маскировки счета.
        masked_number = get_mask_account(number_part)

    else:
        # Это карта. Используем функцию маскировки карты.
        masked_number = get_mask_card_number(number_part)

    # Шаг 3: Собираем финальную строку
    return f"{name_part} {masked_number}"


def get_date(date_str: str) -> str:
    """
    Принимает строку с датой в формате "ГГГГ-ММ-ДДTHH:MM:SS..."
    и возвращает дату в формате "ДД.ММ.ГГГГ".
    """
    # 1. Парсим дату из строки
    date_obj = datetime.fromisoformat(date_str)

    # 2. Форматируем дату в нужный вид (strftime)
    return date_obj.strftime("%d.%m.%Y")
