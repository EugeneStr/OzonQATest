from functions.api_func import *
import pytest

@pytest.fixture
def api_get_all_data():
    return  APIGetAllData()

@pytest.fixture
def get_hero_with_max_height(all_heroes_data, gender, is_work):
    return  GetHeroWithMaxHeight(all_heroes_data, gender, is_work)