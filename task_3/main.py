#Имя автора - awerys
# Запрашиваем число у пользователя с проверкой
while True:
        a = int(input("Введите число a: "))
        b = int(input("Введите число b: "))
        if b > a:
            break
# Инициализируем переменную для суммы
total = 0
# Используем цикл for для подсчета суммы
print(f"Вычисляем сумму чисел от {a} до {b}:")
for i in range(b, a + b):
    total += i
    if a < b:
        print(f"{i} + ", end="")
    else:
        print(f"{i} = {total}")

print(f"Сумма всех чисел от {a} до {b} равна: {total}")
