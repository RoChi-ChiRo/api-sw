import requests


url = 'https://superheroapi.com/api/'
characters = ['Hulk', 'Captain America', 'Thanos']
TOKEN = 0
# from file import TOKEN


class ApiSH:
    @staticmethod
    def search_name(_name):
        r = requests.get(url + str(TOKEN) + '/search/' + _name)
        return r.json()


if __name__ == '__main__':
    result = dict()
    for character_name in characters:
        try:
            json = ApiSH.search_name(character_name)
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
    print('The most intelligence person is:')
    print(f'name = {mem_name},'
          f' intelligence = {mem_intelligence},'
          f' id = {json["results"][0]["id"]}')
