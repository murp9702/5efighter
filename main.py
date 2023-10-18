import requests
import random


class Fighter:
    def __init__(self, jsonInfo):
        self.name = jsonInfo['name']
        self.hit_points = jsonInfo['hit_points']
        self.armor_class = jsonInfo['armor_class'][0]['value']
        self.actions = jsonInfo['actions']
        self.initiative = roll_die(20) + proficiency_math(jsonInfo['dexterity'])
        


def roll_die(dN):
    return random.randint(1, dN)

def proficiency_math(rawScore):
    return int((rawScore - 10) / 2)

def call_api(url):
    response = requests.get(url)
    return response.json()

def build_fighters(monsterList):
    maxNumberOfMonsters = monsterList['count']
    i = 0
    while i < 2:
        randomInt = random.randint(0, maxNumberOfMonsters)
        api_url = f'https://www.dnd5eapi.co{monsterList["results"][randomInt]["url"]}'
        monster = call_api(api_url)
        if monster["challenge_rating"] <= 5:
            i += 1
            yield Fighter(monster)

def fight(fighter1, fighter2):
    if int(fighter1.hit_points) and int(fighter2.hit_points) > 0:
        fighter1.hit_points -= 5
        print(fighter1.hit_points)





if __name__ == '__main__':
    # grab the list of all monsters from the api. this will be used to generate random encounters
    monsters = call_api('https://www.dnd5eapi.co/api/monsters')
    fighter1, fighter2 = build_fighters(monsters)
    print(fighter2.initiative)
    # print(fighter1.actions)
    # fight(fighter1, fighter2)

