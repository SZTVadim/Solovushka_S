"""
Тема: Функции и условные конструкции в Python
"""

# ЗАДАНИЕ 1: Функции и условия

# 1. Создайте функцию calculate_total(price, tax_percent):
#    - возвращает итоговую цену с налогом
#    - если налог > 20% или цена < 0, возвращает сообщение об ошибке

def calculate_total(price, tax_percent):
    if tax_percent > 20 or price < 0:
        return "Ошибка"
    itogo = price + (price * tax_percent / 100)
    return itogo

# 2. Создайте функцию get_level(points):
#    - points >= 100 → "Эксперт"
#    - points >= 50 → "Продвинутый"
#    - points >= 20 → "Начинающий"
#    - иначе → "Новичок"

def get_level(points):
    if points >= 100:
        print("Эксперт")
        if points >= 50:
            print("Продвинутый")
            if points >= 20:
                print("Начинающий")
            else:
                print("Новичок")

# ЗАДАНИЕ 2: Функции с условиями и match/case

# 1. Создайте функцию process_status(status) с match/case:
#    - "active" → "Статус активен"
#    - "inactive" → "Статус неактивен"
#    - "pending" → "Статус в ожидании"
#    - "blocked" → "Статус заблокирован"
#    - иначе → "Неизвестный статус"

def process_status(status):
    match status:
        case "active":
            print("Статус активен")
        case "inactive":
            print("Статус неактивен")
        case "pending":
            print("Статус в ожидании")
        case "blocked":
            print("Статус заблокирован")
        case _:
            print("Неизвестный статус")
