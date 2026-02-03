# Домашнее задание: Классы и инициализация
#
# ЗАДАНИЕ 1: Класс Book (Книга)
#
# Создайте класс Book со следующими требованиями:
# 1) В __init__ принимайте параметры: title (название), author (автор), pages (количество страниц)
# 2) Сохраните эти параметры как атрибуты объекта через self
# 3) Создайте метод get_info(), который возвращает строку: "'{title}' автор {author}, {pages} стр."
# 4) Создайте метод is_long(), который возвращает True, если страниц > 300, иначе False
# 5) Создайте 3 объекта книг и выведите информацию о каждой.


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def get_info(self):
        return f"'{self.title}' автор {self.author}, {self.pages} стр."
    def is_long (self):
        if self.pages > 300:
            return True
        else:
            return False


book1 = Book("Война и мир", "Толстой", 1225)
book2 = Book("Гранатовый браслет", "Куприн", 387)
book3 = Book("Сумерки", "Стефани Майер", 566)
print(book1.get_info())
print(book2.get_info())
print(book3.get_info())

# ЗАДАНИЕ 2: Класс BankAccount (Банковский счёт)
#
# Создайте класс BankAccount:
#
# 1) В __init__ принимайте: owner (владелец), balance (начальный баланс, по умолчанию 0)
# 2) Создайте метод deposit(amount) — пополнение счёта (увеличивает self.balance)
# 3) Создайте метод withdraw(amount) — снятие денег:
# 4) Если денег достаточно — уменьшает баланс и возвращает True
#    Если недостаточно — возвращает False и выводит "Недостаточно средств"
# 5) Создайте метод get_balance() — возвращает текущий баланс
# 6) Создайте счёт, пополните его, попробуйте снять деньги (достаточно и недостаточно), выведите баланс.


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self, amount):
        self.balance = self.balance - amount
        if self.balance > 0:
            self.balance = self.balance - amount
            return True
        else:
            return False, "Недостаточно средств"
    def get_balance(self):
        return self.balance

account = BankAccount( "Svetlana" ,100 )
result = account.deposit(100)
result1 = account.withdraw(100)
result2 = account.withdraw(300)
print(account.get_balance())
