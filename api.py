import requests, config
from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            "Contens-Type": 'application/json',
            "Authorization": f'OAuth {self.token}'
        }


    def get_new_folder(self, folder_name):
        folder_url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        params = {"path": folder_name}
        response = requests.put(folder_url, headers=headers, params=params)
        return response.status_code

    def get_file_info(self,folder_name):
        folder_url = f"https://cloud-api.yandex.net/v1/disk/resources?path=disk:/{folder_name}"
        headers = self.get_headers()
        response = requests.get(folder_url, headers=headers)
        return response.status_code
        # if response.raise_for_status() == 201:
        #     return response.json()
        # elif response.raise_for_status() == 404:
        #     return "Папка с таким названием не существует"


if __name__ == '__main__':
    uploader = YaUploader(config.TOKEN)

