import requests
import random


class Fighter:
    def __init__(self, jsonInfo):
        self.name = jsonInfo['name']
        self.hit_points = jsonInfo['hit_points']
        self.armor_class = jsonInfo['armor_class'][0]['value']
        self.actions = jsonInfo['actions']



def call_api(url):
    response = requests.get(url)
    return response.json()

def choose_fighters(monsterList):
    maxNumberOfMonsters = monsterList['count']
    i = 0
    while i < 2:
        randomInt = random.randint(0, maxNumberOfMonsters)
        api_url = f'https://www.dnd5eapi.co{monsterList["results"][randomInt]["url"]}'
        # print(api_url)
        i += 1
        yield api_url

def get_fighter_statistics(fighter):
    pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    monsters = call_api('https://www.dnd5eapi.co/api/monsters')
    chooseFighter1, chooseFighter2 = choose_fighters(monsters)
    fighter1Stats = call_api(chooseFighter1)
    fighter2Stats = call_api(chooseFighter2)
    fighter1 = Fighter(fighter1Stats)
    fighter2 = Fighter(fighter2Stats)
    print(fighter2Stats)
    print(fighter2.actions)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
