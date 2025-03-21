from functions.api_func import *


@pytest.mark.parametrize('gender, is_work, true_reference', [
    ('Female', True, 366),
    ('Female', False, 193),
    ('Male', True, 876),
    ('Male', False, 975),
])
def test_two(gender, is_work, true_reference):
    all_hero_data = APIGetAllData()
    assert GetHeroWithMaxHeight(all_hero_data, gender, is_work) == true_reference