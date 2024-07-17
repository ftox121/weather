# My Django Project

## Установка

1. Клонируйте репозиторий:
   git clone https://github.com/ftox121/weather.git
   cd weather
Создайте виртуальное окружение и активируйте его:
python -m venv env
source env/bin/activate  # Для Windows: env\Scripts\activate

Установите зависимости:
pip install -r requirements.txt

Выполните миграции базы данных:
python manage.py migrate

Запустите сервер:

python manage.py runserver
