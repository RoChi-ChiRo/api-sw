import requests


def get_token_and_file():
    token = files = None
    # import things
    try:
        from file import token
    except Exception:
        pass
    try:
        from file import files
    except Exception:
        pass
    # or ask things
    if token is None:
        token = input('put token to cloud: ')
    if files is None:
        files = input('put path to file on computer: ')
    return token, files


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def headers(self):
        return {'Authorization': self.token}

    def get_url_upload(self, path_on_disk='%2Ff'):
        """Метод получает ссылку для загрузки файла на яндекс диск"""
        url = f'https://cloud-api.yandex.net/v1/disk/resources/'
        url += 'upload?path=' + path_on_disk
        try:
            req = requests.get(url, headers=self.headers())
        except Exception as ex:
            return ex
        return req

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = self.get_url_upload(file_path)
        try:
            url = url.json()['href']
        except Exception as ex:
            return url

        try:
            files = {'file': (file_path, open(file_path, 'rb'))}
        except Exception as ex:
            return ex

        try:
            req = requests.put(url, files=files, headers=self.headers())
        except Exception as ex:
            return ex
        return req


if __name__ == '__main__':
    TOKEN, FILES = get_token_and_file()
    path_to_files = FILES
    token = TOKEN
    for file in FILES:
        uploader = YaUploader(token)
        result = uploader.upload(file)
        print(result)
