num = int(input('введите число: '))  # ввод числа пользователем


def fib(var):  # объявление новой функции
    if var <= 1:
        return var   # обработка базового случая
    else:
        return fib(var - 1) + fib(var - 2)  # формула Фибоначчи


for n in range(num):  # цикл до введенного числа
    print(fib(n))
