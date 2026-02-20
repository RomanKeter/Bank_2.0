from typing import Any, Dict, List

import pytest


@pytest.fixture
def sample_data() -> List[Dict[str, Any]]:
    """
    Фикстура, предоставляющая список банковских операций для тестирования
    фильтрации и сортировки. Содержит разные статусы и даты.
    """
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594223477, "state": "CANCELED", "date": "2019-07-03T18:35:29.512328"},
    ]