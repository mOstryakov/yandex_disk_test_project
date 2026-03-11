import pytest
from requests import codes
from api.disk_api import YandexDiskAPI


class TestYandexDisk:

    def test_get_disk_info(self, api_client):
        response = api_client.get_disk_info()
        assert response.status_code == codes.ok
        assert "user" in response.json()

    def test_create_folder_put(self, api_client, temp_folder):
        response = api_client.create_folder(temp_folder)
        assert response.status_code in (codes.created, codes.conflict)

    def test_upload_file_post(self, api_client, temp_folder):
        path = f"{temp_folder}/image.jpg"
        image_url = "https://yandex.ru/favicon.ico"
        response = api_client.upload_file(path, image_url)
        assert response.status_code == codes.accepted

    def test_delete_folder_delete(self, api_client, temp_folder):
        response = api_client.delete_resource(temp_folder)
        assert response.status_code in (codes.accepted, codes.no_content)

    def test_unauthorized_request(self):
        bad_client = YandexDiskAPI(token="fake_invalid_token_123")
        response = bad_client.get_disk_info()
        assert response.status_code == codes.unauthorized

    def test_create_already_existing_folder(self, api_client, temp_folder):
        test_folder = temp_folder + "_conflict"
        api_client.create_folder(test_folder)
        response = api_client.create_folder(test_folder)
        assert response.status_code == codes.conflict
        api_client.delete_resource(test_folder)

    def test_delete_nonexistent_folder(self, api_client):
        response = api_client.delete_resource("Some_Fake_Folder_Name_12345")
        assert response.status_code == codes.not_found
