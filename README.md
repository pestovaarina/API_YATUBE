# REST API для работы с веб-сайтом YaTube.
### Описание
Позволяет просматривать, добавлять, редактировать и удалять следующие ресурсы:
- посты
- комментарии к постам
- группы (только в режиме чтения)
### Виды запросов к API
1. Эндпойнт api/v1/api-token-auth/
- GET - получение токена
2. Эндпойнт api/v1/posts/
- GET - получение списка постов
- POST - создание нового поста
3. Эндпойнт api/v1/posts/{post_id}/
- GET - получение поста с указанным id
- PUT - полное изменение поста
- PATCH - частичное изменение поста
- DELETE - удаление поста
4. Эндпойнт api/v1/groups/
- GET - получение списка доступных сообществ
5. Эндпойнт api/v1/groups/{group_id}/
- GET - получение информации о сообществе по id
6. Эндпойнт api/v1/posts/{post_id}/comments/
- GET - получение списка комментариев для поста с указанным id
- POST - создание нового нового комментария для поста с указанным id
7. Эндпойнт api/v1/posts/{post_id}/comments/{comment_id}/
- GET - получение комментария с указанным id
- PUT - полное изменение комментария
- PATCH - частичное изменение комментария
- DELETE - удаление комментария
### Технологии
- Python 3.9
- Django REST framework 3.12
- Django 2.2
### Запуск проекта
1. Клонировать репозиторий и перейти в его директорию:
```
git clone git@github.com:pestovaarina/api_yatube.git
``` 
2. Создать и активировать виртуальное окружение
```
python -m venv env
source venv/Scripts/activate
``` 
3. Установить зависимости из файла requirements.txt
```
python -m pip install --upgrade pip
pip install -r requirements.txt
``` 
4. Выполнить миграции:
```
python manage.py migrate
``` 
5. Запустить проект:
``` 
python manage.py runserver
``` 
### Автор
Пестова Арина Витальевна