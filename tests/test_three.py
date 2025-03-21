from functions.api_func import *
import pytest


@pytest.mark.parametrize('gender, is_work', [
    (1, True),
    ('Female', 0),
    ('Female', '-'),
])
def test_three(gender, is_work):
    all_hero_data = APIGetAllData()
    #Здесь ожидаем, что тест не пройдет из за ошибки в скобках
    with pytest.raises(TypeError):
        result = GetHeroWithMaxHeight(all_hero_data, gender, is_work)