import requests


url = 'https://superheroapi.com/api/'
try:
    from file import characters
except Exception as ex:
    characters = ['Thanos', 'Hulk', 'Captain America']
try:
    from file import TOKEN
except Exception as ex:
    TOKEN = ''


class ApiSH:
    def __init__(self, token: str):
        self.TOKEN = token

    def search_name(self, name):
        r = requests.get(url + str(self.TOKEN) + '/search/' + name)
        return r


if __name__ == '__main__':
    apish = ApiSH(TOKEN)
    result = dict()
    for character_name in characters:
        try:
            req = apish.search_name(character_name)
            json = req.json()
        except Exception as ex:
            print(character_name, ' ERROR ', ex)
            continue

        try:
            result[character_name] = json['results'][0]['powerstats']['intelligence']
        except Exception:
            result[character_name] = None

    # maximum intelligence
    mem_intelligence = None
    mem_name = 'None'
    for name, intelligence in result.items():
        if intelligence is not None:
            if mem_intelligence is None \
            or int(intelligence) > mem_intelligence:
                mem_intelligence = int(intelligence)
                mem_name = name
    print('The most intelligence person in list is:')
    print(f'name = {mem_name}, '
          f'intelligence = {mem_intelligence}')
