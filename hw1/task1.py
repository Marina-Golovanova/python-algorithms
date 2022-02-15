def find_sum_and_mul_numbers(n: int):
    sum = 0
    mul = 1
    arr = [int(x) for x in str(n)]
    for el in arr:
        sum += el
        mul *= el
    return f"Сумма: {sum}, произведение: {mul}"

number = int(input("Введите трехзначное число: "))

print(find_sum_and_mul_numbers(number))