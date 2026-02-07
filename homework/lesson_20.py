# Домашнее задание: requests
#
# Адрес сваггера https://petstore.swagger.io/#
#
# Для ДЗ использовать клиента pet (группа запросов pet)
#
#
# Выполнить запрос Post
# Выполнить запрос Get
# Выполнить запрос Put
# Выполнить запрос Delete

import requests
response = requests.post( "https://petstore.swagger.io/v2/pet"),
headers = {"accept": "application/json", "Content-Type": "application/json"},
data_for_post = {
  "id": 9223372036854776000,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
response = requests.post("https://petstore.swagger.io/v2/pet", headers=headers, json=data_for_post)
print(f"{response.status_code}, успешно создан")
print(response.json())