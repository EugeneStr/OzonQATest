from functions.api_func import *
import pytest

def test_one():
    try:
        data_heroes = APIGetAllData()
    except ConnectionError:
        pytest.fail('Ошибка запроса к API')