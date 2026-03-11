import requests


class YandexDiskAPI:
    BASE_URL = "https://cloud-api.yandex.net/v1/disk"

    def __init__(self, token):
        self.headers = {
            "Authorization": f"OAuth {token}",
            "Content-Type": "application/json",
        }

    def get_disk_info(self):
        return requests.get(self.BASE_URL, headers=self.headers)

    def create_folder(self, path):
        params = {"path": path}
        return requests.put(
            f"{self.BASE_URL}/resources", headers=self.headers, params=params
        )

    def upload_file(self, path, file_url):
        params = {"path": path, "url": file_url}
        return requests.post(
            f"{self.BASE_URL}/resources/upload",
            headers=self.headers,
            params=params,
        )

    def delete_resource(self, path, permanently=True):
        params = {"path": path, "permanently": permanently}
        return requests.delete(
            f"{self.BASE_URL}/resources", headers=self.headers, params=params
        )
