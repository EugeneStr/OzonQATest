import pytest
import requests
import json

def APIGetAllData():
    data_request = requests.get('https://akabab.github.io/superhero-api/api/all.json')
    if data_request.status_code != 200:
        raise ConnectionError('Ошибка запроса к API')

    all_hero_data = json.loads(data_request.text)
    return all_hero_data

def GetHeroWithMaxHeight(all_hero_data, gender: str, is_work: bool):
    # Проверка на типы
    if type(gender) != str:
        raise TypeError('Ошибка типа')
    if type(is_work) != bool:
        raise TypeError('Ошибка типа')

    max_height = 0.0
    hero_height = 0.0

    for hero in all_hero_data:
        if hero['appearance']['gender'] == gender:
            is_hero_work = (hero['work']['occupation']) != '-'
            if is_hero_work == is_work:
                hero_height = float(hero['appearance']['height'][1].split()[0])
                if hero_height > max_height:
                    max_height = hero_height
    return max_height
