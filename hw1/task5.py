a = input("Введите первую букву: ")
b = input("Введите вторую букву: ")

def find_dif_between_letters(a, b):
    ord_first_letter = ord(a.lower()) - 96
    ord_second_letter = ord(b.lower()) - 96
    if (ord_first_letter < ord_second_letter):
        number_letters_between = ord_second_letter - ord_first_letter - 1
    else:
        number_letters_between = ord_first_letter - ord_second_letter - 1
    return f"Порядок первой буквы в алфавите: {ord_first_letter}. Порядок второй буквы в алфавите: {ord_second_letter}. Между ними {number_letters_between} букв"

print(find_dif_between_letters(a, b))