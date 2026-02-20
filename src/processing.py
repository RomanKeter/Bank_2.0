from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    Args:
        data: Список словарей с данными о банковских операциях.
        state: Статус, по которому нужно отфильтровать (по умолчанию 'EXECUTED').

    Returns:
        Список словарей, содержащих только операции с указанным статусом.

    Example:
        >>> filter_by_state([{'id': 1, 'state': 'EXECUTED'}], 'EXECUTED')
        [{'id': 1, 'state': 'EXECUTED'}]
    """
    filtered_data = []
    for item in data:
        if item.get("state") == state:
            filtered_data.append(item)
    return filtered_data


def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по дате.

    Args:
        data: Список словарей с данными о банковских операциях.
        reverse: Порядок сортировки (True — убывание, False — возрастание).

    Returns:
        Отсортированный список словарей.
    """
    return sorted(data, key=lambda x: x["date"], reverse=reverse)
