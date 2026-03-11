import pytest
import os
import uuid
from dotenv import load_dotenv
from api.disk_api import YandexDiskAPI

load_dotenv()


@pytest.fixture(scope="session")
def api_client():
    token = os.getenv("YANDEX_TOKEN")
    if not token:
        pytest.fail("YANDEX_TOKEN не найден в .env. Тестирование невозможно.")
    return YandexDiskAPI(token)


@pytest.fixture
def temp_folder(api_client):
    folder_name = f"test_folder_{uuid.uuid4().hex[:8]}"
    api_client.create_folder(folder_name)

    yield folder_name

    api_client.delete_resource(folder_name)
