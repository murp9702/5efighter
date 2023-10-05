import requests
import random

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
    fighter1, fighter2 = choose_fighters(monsters)
    fighter1Stats = call_api(fighter1)
    fighter2Stats = call_api(fighter2)
    print(fighter1Stats)
    print(fighter2Stats)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
