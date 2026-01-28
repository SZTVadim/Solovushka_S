# ЗАДАЧА 1: Система учета сотрудников

employees = {
    "Иван": {"возраст": 30, "отдел": "IT", "зарплата": 80000},
    "Мария": {"возраст": 25, "отдел": "HR", "зарплата": 60000},
    "Петр": {"возраст": 35, "отдел": "ITR", "зарплата": 90000},
    "Анна": {"возраст": 28, "отдел": "Маркетинг", "зарплата": 70000}
}

# 1. Добавьте нового сотрудника "Анна"
# 2 Создайте список всех имен сотрудников
# 3. Найдите среднюю зарплату всех сотрудников
# 4. Создайте множество всех отделов
# 5. Удалите сотрудника "Петр" и сохраните его данные
# 6. Создайте словарь, где ключ - отдел, а значение - список имен сотрудников

vce = list(employees.keys())
salary = sum(employee["зарплата"] for employee in employees.values())
salary2 = salary / len(employees)
all_departments = {employee["отдел"] for employee in employees.values()}
print(all_departments)
petr = employees.pop("Петр")

department_to_names = {}  # Списала из чата, не могу понять эту тему
for name, info in employees.items():
    department = info["отдел"]
    if department not in department_to_names:
        department_to_names[department] = []
    department_to_names[department].append(name)

print("Способ 1 - Базовый:")
for dept, names in department_to_names.items():
    print(f"{dept}: {names}")
