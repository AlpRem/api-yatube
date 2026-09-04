# api_yatube
API для учебного проекта работы с постами. С помощью API можно получать, создавать, изменять и удалять посты и комментарии к ним, а также получать информацию о группах.

Для доступа к API используется токенная аутентификация.

## Установка

### Клонирование репозитория
https://github.com/AlpRem/api-yatube.git

### Создание виртуального окружения

python3 -m venv venv

### Активация виртуального окружения

Linux/macOS:
source venv/bin/activate

Windows: 
venv\Scripts\activate

### Установка зависимостей

pip install -r requirements.txt

## Запуск

python homework.py

## Для взаимодействия с ресурсами cуществуют следующие эндпоинты:
- `api/v1/api-token-auth/` - **POST**: передаём логин и пароль, получаем токен.
- `api/v1/posts/` - **GET, POST**: получаем список всех постов или создаём новый пост.
- `api/v1/posts/{post_id}/` - **GET, PUT, PATCH, DELETE**: получаем, редактируем или удаляем пост с идентификатором{post_id}.
`api/v1/groups/` - **GET**: получаем список всех групп.
`api/v1/groups/{group_id}/` - **GET**: получаем информацию о группе с идентификатором {group_id}.
- `api/v1/posts/{post_id}/comments/` - **GET**: получаем список всех комментариев поста с идентификатором post_id - **POST**: создаём новый комментарий для поста с идентификатором {post_id}.
- `api/v1/posts/{post_id}/comments/{comment_id}/` - **GET, PUT, PATCH, DELETE**: получаем, редактируем или удаляем комментарий с идентификатором {comment_id} в посте с id=post_id.