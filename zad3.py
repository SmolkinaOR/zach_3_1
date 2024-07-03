

import requests

# Ваш персональный access_token для доступа к API VK
access_token = 'vk1.a.WNjw_8RvXD-OW2JsIeguVccRa3sJ5qrOThHqF-IEgVuFSPAWOPL3OeHL4yHWahThsV1TbDKcbuvjxn7cZ_HcU8lJ-R3ek07BQ060dHYh5_FpGiBLEvrGylfDS5_LOzhY0lllSX_T2hyj2cFZ6gqt_uAvMoC8TQPkzddnflN90D9aVlVbFLJCi3gU5DOZ-Bhq'

# Запрашиваем у пользователя идентификатор или ник VK
user_input = input("Введите идентификатор или ник VK: ")

# Формируем URL для запроса
url = "https://api.vk.com/method/users.get"

# Параметры запроса и их значения
params = {
    # Идентификатор или ник VK пользователя
    "user_ids": user_input,
    # Список полей, которые необходимо получить
    "fields": "counters",
    # Ваш access_token
    "access_token": access_token,
    # Версия API
    "v": "5.131"
}

# Отправляем GET-запрос
response = requests.get(url, params=params)

# Получаем ответ в формате JSON
user_info = response.json()["response"][0]

# Выводим информацию о пользователе в читабельном виде
print("Имя:", user_info["first_name"])
print("Фамилия:", user_info["last_name"])
print("всего друзей:", user_info["counters"]['friends'])
