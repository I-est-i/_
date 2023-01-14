# Сделано в Visual Studio Code для вк
import requests    # В консоли нужно ввести pip install requests
import json         # Не надо, оно уже есть
import random        # Не надо, оно уже есть
import vk             # В консоли нужно ввести pip install requests

def write_json_status(data):
    with open('group.json', 'w', encoding='utf-8') as file: 
        json.dump(data, file, indent=2, ensure_ascii=False) 

def random_Id():                     # Это генератор рандомных чисел 
    return random.randint(0, 10000) 

APP_ID = 1 # Что-то своё             Необходимо!
USER_LOGIN = 1 # Что-то своё         Логин от аккаунта
USER_PASSWORD = 1 # Что-то своё     Пароль от аккаунта
token = 1 # Что-то своё                 Токен нужно брать из вк



session = vk.AuthSession(app_id=APP_ID, user_login=USER_LOGIN, user_password=USER_PASSWORD, scope='messages', access_token=token)         # Обьединение всего к сессии
vkapi = vk.API(session)         # Подключение самого вк API и привязка его к сессии


MESSAGE = 'Привет, отправил это сообщение через VK API'         # Само сообщение

g = vkapi.messages.send(user_id=Что-то своё, random_id=random_id(), message=MESSAGE)         #User_id это тот, кому вы отправляете сообщение
write_json_status(g)