# test-task-tree-menu
Создание на django древовидного меню
## Установка
1. Склонируйте репозиторий с помощью команды `git clone https://github.com/GudimArt/test-task-tree-menu.git`
2. Установите зависимости, используя команду `pip install -r requirements.txt` 
## Использование
1. Сгенерируйте секретный ключ(SECRET_KEY), и сохраните его в файле `.env'.
2. Сделайте следующие команды:
`python manage.py makemigrations`
`python manage.py migrate`
`python manage.py loaddata data.json`
3. Запустите сервер с помощью команды `python manage.py runserver`.
