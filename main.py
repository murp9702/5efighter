import requests
import random


class Fighter:
    def __init__(self, jsonInfo):
        self.name = jsonInfo['name']
        self.hit_points = jsonInfo['hit_points']
        self.armor_class = jsonInfo['armor_class'][0]['value']
        self.actions = jsonInfo['actions']


def roll_dice():
    pass

def call_api(url):
    response = requests.get(url)
    return response.json()

def choose_fighters(monsterList):
    maxNumberOfMonsters = monsterList['count']
    i = 0
    while i < 2:
        randomInt = random.randint(0, maxNumberOfMonsters)
        api_url = f'https://www.dnd5eapi.co{monsterList["results"][randomInt]["url"]}'
        monster = call_api(api_url)
        if monster["challenge_rating"] <= 5:
            i += 1
            yield Fighter(monster)
        else:
            print("too high")




if __name__ == '__main__':
    monsters = call_api('https://www.dnd5eapi.co/api/monsters')
    fighter1, fighter2 = choose_fighters(monsters)
    print(fighter2.actions)
    print(fighter1.actions)

