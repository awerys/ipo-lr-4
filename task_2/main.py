#Имя автора - awerys
# Исходный список
strings = ["hello", "world", "python"]
# Генератор списка, который повторяет каждую строку 3 раза
result = [string for string in strings for _ in range(3)]
print(result)
# Вывод: ['hello', 'hello', 'hello', 'world', 'world', 'world', 'python', 'python', 'python']
