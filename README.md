# Описание
__Приложение для бронирования комнат в отеле.__
## Функционал
```
* Пользователи могут фильтровать и сортировать комнаты по цене, по количеству мест.
* Пользователи могут получить список свободных комнаты.
* Пользователи могут бронировать свободную комнату.
* Суперюзер может добавлять/удалять/редактировать комнаты и редактировать
  записи о бронях через админ-панель Django.
* Брони могут быть отменены как самим юзером, так и суперюзером.
* Пользователи умееют регистрироваться и авторизовываться (логиниться).
```
```
## Подготовка и запуск проекта
#### Клонирование репозитория
Склонируйте репозиторий на локальную машину:
```bash
git clone https://github.com/Slavchick12/hotel.git
```
#### Подготовка базы данных PostgreSQL
##### Шаг 1. Скачайте и установите PostreSQL 14.5
```
https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
```
##### Шаг 2. Запустите PostgreSQL и создайте БД "hotel"
#### Настройка виртуального окружения и проведение миграций
##### Шаг 1. Установка виртуального окружения
```bash
cd <path_to_project/>booking/
```
```bash
python -m venv venv
```
##### Шаг 2. Активация виртуального окружения
```bash
. venv/Scripts/activate
```
##### Шаг 3. Обновление пакетов pip
```bash
python -m pip install -U pip
```
##### Шаг 4. Установка зависимостей проекта
```bash
pip install -r requirements.txt
```
##### Шаг 6. Перейдите в директорию с файлом manage.py с запущенным виртуальным окружением
```bash
cd <path_to_project>/booking/
```
##### Шаг 7. Проведение миграции
```bash
python manage.py makemigrations
python manage.py migrate
```
#### Подготовка секретных переменных
##### Шаг 1. Перейдите в директорию с файлом __settings.py__
```bash
cd <path_to_project>/booking/booking/
```

##### Шаг 2. Заполните *settings.py* следующем образом
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=<DB_NAME>
POSTGRES_USER=<POSTGRES_USER>
POSTGRES_PASSWORD=<POSTGRES_PASSWORD>
DB_HOST=127.0.0.1
DB_PORT=5432
SECRET_KEY=<SECRET_KEY>
DEBUG=True
```
#### Запуск проекта на локальной машине
```bash
python manage.py runserver
```
#### Создание суперюзера
```bash
python manage.py createsuperuser
```
#### Админ-панель Django
```bash
http://127.0.0.1:8000/admin
```
## Используемый стек
```
Python, Django, DRF, PostgreSQL, Simple-JWT
```
#### Также используется
```
django-filter, psycopg2-binary
```