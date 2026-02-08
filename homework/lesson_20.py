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


# POST

url_post = "https://petstore.swagger.io/v2/pet"

headers_post = {"accept": "application/json", "Content-Type": "application/json"}

data_post = {
  "id": 669,
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

response_post = requests.post(url_post, json=data_post, headers=headers_post)

print(f" Успешно создан  Status code : {response_post.status_code}")
print(f" Тело ответа POST: {response_post.json()}")


# GET

url_get = "https://petstore.swagger.io/v2/pet/669"

headers_get = {"accept": "application/json"}
response_get = requests.get(url_get, headers=headers_get)
print(f"Успешно получен  Status code : {response_get.status_code}")
print(f" Тело ответа GET: {response_get.json()}")


# PUT


url_put = "https://petstore.swagger.io/v2/pet"

headers_put = {"accept": "application/json", "Content-Type": "application/json"}

data_put = {
  "id": 669,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie DOG",
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

response_put = requests.put(url_put, json=data_put, headers=headers_put)

print(f" Успешно обновлен  Status code : {response_put.status_code}")
print(f" Тело ответа PUT: {response_put.json()}")


# DELETE


url_delete = "https://petstore.swagger.io/v2/pet/669"

headers_delete = {"accept": "application/json"}
response_delete = requests.delete(url_delete, headers=headers_delete)
print(f"Успешно удален  Status code : {response_delete.status_code}")
print(f" Тело ответа DELETE: {response_delete.json()}")
