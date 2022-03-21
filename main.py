import requests


url = 'https://superheroapi.com/api/'
characters = ['Hulk', 'Captain America', 'Thanos']
TOKEN = ''
# from file import TOKEN


class ApiSH:
    def __init__(self, token: str):
        self.TOKEN = token

    def search_name(self, name):
        r = requests.get(url + self.TOKEN + '/search/' + name)
        return r.json()


if __name__ == '__main__':
    apish = ApiSH(TOKEN)
    result = dict()
    for character_name in characters:
        try:
            json = apish.search_name(character_name)
        except Exception as ex:
            print(ex)
            continue

        result[character_name] = json['results'][0]['powerstats']['intelligence']
    # print(result)

    # maximum intelligence
    mem_intelligence = -1
    mem_name = 'None'
    for name, intelligence in result.items():
        if int(intelligence) > mem_intelligence:
            mem_intelligence = int(intelligence)
            mem_name = name
    print('The most intelligence person in list is:')
    print(f'name = {mem_name},'
          f' intelligence = {mem_intelligence},'
          f' id = {json["results"][0]["id"]}')
