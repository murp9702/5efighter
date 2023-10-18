import requests
import random

#TODO
# need to implement check for "multiattack" to reduce attack_bonus key errors
# need to rebuild attack_damage, the dice are hidden inside another layer of the object

class Fighter:
    def __init__(self, jsonInfo):
        self.name = jsonInfo['name']
        self.hit_points = jsonInfo['hit_points']
        self.armor_class = jsonInfo['armor_class'][0]['value']
        self.attack_bonus = jsonInfo['actions'][0]['attack_bonus']
        self.initiative = roll_die(20) + proficiency_math(jsonInfo['dexterity'])
        self.attack_damage = [jsonInfo['actions'][0]['damage_dice'].split('d')[0],
                              jsonInfo['actions'][0]['damage_dice'].split('d')[1].split('+')[0],
                              jsonInfo['actions'][0]['damage_dice'].split('+')[1]
        ]

        


def roll_die(die, numberOfDie=1):
    return random.randint(1, die)

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


def set_initiative(fighter1, fighter2):
    if fighter2.initiative > fighter1.initiative:
        fighter2, fighter1 = fighter1, fighter2


def conscious_check(fighter):
    if fighter.hit_points <= 0:
        return False


def attack_vs_armor_class(attack, armorClass):
    attack += roll_die(20)
    if attack >= armorClass:
        return True
    else:
        return False

def fight(fighter1, fighter2):

    if attack_vs_armor_class(fighter1.attack_bonus, fighter2.armor_class):
        print("HIT")
        roll_die(fighter1.attack_damage)






if __name__ == '__main__':
    # grab the list of all monsters from the api. this will be used to generate random encounters
    monsters = call_api('https://www.dnd5eapi.co/api/monsters')
    fighter1, fighter2 = build_fighters(monsters)
    set_initiative(fighter1, fighter2)
    fight(fighter1, fighter2)
    print(fighter1.attack_bonus)
    print("||||||||||||||||||||||||||||")
    print(fighter2.attack_bonus)
