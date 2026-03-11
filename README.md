# Auto tests for the Yandex.Disk service

## 1. Clone repository
``` bash
git clone https://github.com/mOstryakov/yandex_disk_test_project.git
cd yandex_disk_test_project
```

## 2. Install Poetry
```bash
pip install poetry
```

## 3. Install dependencies
```bash
poetry install
```

## 4. Create ```.env``` file in the project root
```bash
YANDEX_TOKEN=your_token
```
Get OAuth token: [Yandex OAuth](https://yandex.ru/dev/disk/poligon/)  
Do not use your personal account for tests!

## 5. Run tests
```bash
poetry run pytest -v
```