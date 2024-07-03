"""
содержание ответа json по корзинам:
идент корзины 
идентификатор пользователя
дата создания карзины
продукты:
    идентификатор продукта - название можно взять название в продуктах, но лень.
    колличество в заказе
"""

# Импортируем необходимые модули

import requests
# Устанавливаем URL API-запроса
url = "https://fakestoreapi.com/carts"
# Выполняем GET-запрос и получаем ответ
response = requests.get(url)
# Извлекаем данные JSON из ответа
p_carts = response.json()
# Флаг, указывающий, найдена ли категория

# Итерируемся по карзинкам
for p_carts1 in p_carts:
    print(f'корзина : {p_carts1} ')
print('------------')
url2 = "https://fakestoreapi.com/users"
response = requests.get(url2)
# Извлекаем данные JSON из ответа
p_users = response.json()
for p_user in p_users:
    find = False
    print(f'идентификатор пользователя: {p_user["id"]}')
    print(f'Имя: {p_user["name"]["firstname"]} Фамилия: {p_user["name"]["lastname"]}')
    for p_carts2 in p_carts:
        if p_user["id"] == p_carts2["userId"]:
            find = True
            print(f'корзина : {p_carts2} ')
    if find == False:
        print('корзина пуста')
    print('------------')



