#Имя автора - awerys
# Запрашиваем число у пользователя с проверкой
while True:
    try:
        n = int(input("Введите положительное число n: "))
        if n > 0:
            break
        else:
            print("Число должно быть положительным!")
    except ValueError:
        print("Пожалуйста, введите целое число!")
# Инициализируем переменную для суммы
total = 0
# Используем цикл for для подсчета суммы
print(f"Вычисляем сумму чисел от 1 до {n}:")
for i in range(1, n + 1):
    total += i
    if i < n:
        print(f"{i} + ", end="")
    else:
        print(f"{i} = {total}")

print(f"Сумма всех чисел от 1 до {n} равна: {total}")
