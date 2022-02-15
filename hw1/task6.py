n = int(input("Введите номер буквы в алфавите: "))

def find_ord_letter(n):
    return chr(n + 64)

print(find_ord_letter(n))