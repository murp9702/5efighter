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
        # self.attack_damage = [jsonInfo['actions'][0]['damage'][0]['damage_dice'].split('d')[0],
        #                       jsonInfo['actions'][0]['damage'][0]['damage_dice'].split('d')[1].split('+')[0],
        #                       jsonInfo['actions'][0]['damage'][0]['damage_dice'].split('+')[1]]
        self.actions = jsonInfo['actions']

        self.calculate_damage_die(jsonInfo)

    def calculate_damage_die(self,jsonInfo):
        base_name = jsonInfo['actions'][0]['damage'][0]['damage_dice']
        if '+' in base_name:
            self.damage_dice = (base_name.split('d')[0],base_name.split('d')[1].split('+')[0])
            self.damage_modifier = (base_name.split('+')[1])
        elif 'd' in base_name:
            self.damage_dice = (base_name.split('d')[0],base_name.split('d')[1])
        else:
            self.damage_dice = base_name



def roll_die(die, numberOfDie=1):
    sum = 0
    for _ in range(0, numberOfDie):
        sum += random.randint(1, die)
    return sum

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
        if monster["challenge_rating"] <= 2 and monster['actions'][0]['name'] != 'Multiattack':
            i += 1
            yield Fighter(monster)


def set_initiative(fighter1, fighter2):
    if fighter2.initiative > fighter1.initiative:
        fighter2, fighter1 = fighter1, fighter2


def conscious_check(fighter):
    if fighter.hit_points <= 0:
        return False


def attack_vs_armor_class(attackBonus, armorClass):
    attack = roll_die(20) + attackBonus
    if attack>= armorClass:
        return True
    else:
        print("missed")
        return False

def fight(fighter1, fighter2):

    if attack_vs_armor_class(fighter1.attack_bonus, fighter2.armor_class):
        print("HIT")
        damage = roll_die(int(fighter1.damage_dice[1]),int(fighter1.damage_dice[0]))
        print(damage)






if __name__ == '__main__':
    # grab the list of all monsters from the api. this will be used to generate random encounters
    monsters = call_api('https://www.dnd5eapi.co/api/monsters')
    fighter1, fighter2 = build_fighters(monsters)
    set_initiative(fighter1, fighter2)
    fight(fighter1, fighter2)
    # print(fighter1.attack_bonus)
    # print("||||||||||||||||||||||||||||")
    # print(fighter2.attack_bonus)
    # print(fighter1.actions)
