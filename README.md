# My Django Project

## Установка

1. Клонируйте репозиторий:
   git clone https://github.com/ftox121/weather.git
Создайте виртуальное окружение и активируйте его:
python -m venv env
source env/bin/activate  # Для Windows: env\Scripts\activate

Установите зависимости:
pip install -r requirements.txt

Выполните миграции базы данных:
python manage.py migrate

Запустите сервер:

python manage.py runserver

В данном проекте была выполнено автодополнение , выполнено пару тестов , также есть история предыдущего запроса.
Также API ключ был оставлен в проекте специально, чтобы было проще запустить проект, в масштабном проекте следует использовать dotenv
