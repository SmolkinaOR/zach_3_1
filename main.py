# Импортируем необходимые модули

import requests
# Устанавливаем URL API-запроса
url = "https://fakestoreapi.com/products/categories"
# Выполняем GET-запрос и получаем ответ
response = requests.get(url)
# Извлекаем данные JSON из ответа
users = response.json()
# Флаг, указывающий, найдена ли категория
find = False
# Итерируемся по списку пользователей
for user in users:
    print(f'Категория : {user} ')
cat_v = input('Введите категорию товара, о которой хотите узнать: ')
for user in users:
    # Проверяем, совпадает категория с введенной
    if user == cat_v:
        # Если да, ставим флаг
        find = True
if find == True:
    # Устанавливаем URL API-запроса
    url1 = "https://fakestoreapi.com/products/category/"+cat_v
    response = requests.get(url1)
    # Извлекаем данные JSON из ответа
    prod1 = response.json()
    for prod2 in prod1:
        print(f'идентификатор: {prod2["id"]} титул: {prod2["title"]}')
        print(f'категория: {prod2["category"]} адрес картинки: {prod2["image"]}')
        print(f'описание: {prod2["description"]} ')
else:
    print(f'Нет такой категории')





