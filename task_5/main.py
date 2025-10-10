#Имя автора - awerys
# Ввод данных от пользователя
user_input = input("Введите числа через пробел: ")
numbers = list(map(int, user_input.split()))

# Генератор списка для квадратов
squares = [num ** 2 for num in numbers]

# Подробный вывод
print("\nРезультаты:")
print("=" * 30)
for i, (original, squared) in enumerate(zip(numbers, squares), 1):
    print(f"{i}. {original}² = {squared}")
print("=" * 30)
print(f"Исходный список: {numbers}")
print(f"Список квадратов: {squares}")
