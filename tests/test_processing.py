from typing import Any, Dict, List

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(sample_data: List[Dict[str, Any]]) -> None:
    """
    Тестирует фильтрацию по статусу, включая пустые результаты.
    """
    # Стандартная фильтрация
    assert len(filter_by_state(sample_data, "EXECUTED")) == 2
    # Фильтрация по отсутствующему статусу
    assert filter_by_state(sample_data, "NON_EXISTENT") == []


def test_sort_by_date(sample_data: List[Dict[str, Any]]) -> None:
    """
    Тестирует сортировку по дате в обоих направлениях.
    """
    # По убыванию (новые первые)
    sorted_desc = sort_by_date(sample_data)
    assert sorted_desc[0]["date"] == "2019-08-26T10:50:58.294041"

    # По возрастанию
    sorted_asc = sort_by_date(sample_data, reverse=False)
    assert sorted_asc[0]["date"] == "2018-06-30T02:08:58.425572"
