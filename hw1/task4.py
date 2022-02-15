from random import randint, uniform

def gen():
    start_number = int(input("Введите нижнее целое число: "))
    end_number = int(input("Введите верхнее целое число: "))
    number = randint(start_number , end_number)

    start_float = int(input("Введите нижнее вещественное число: "))
    end_float = int(input("Введите верхнее вещественное число: "))
    float_number = uniform(start_float, end_float)

    start_symbol = input("Введите первый символ: ")
    end_symbol = input("Введите второй символ: ")
    symbol = chr(randint(ord(start_symbol), ord(end_symbol)))
    return f"Случайное целое число: {number}. Случайное вещественное число: {float_number}. Случайный символ: {symbol}"

print(gen())