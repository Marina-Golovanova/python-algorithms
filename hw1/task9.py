a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

def find_mid_number(a, b, c):
    if a > b > c or a < b < c:
        return b
    elif a > c > b or a < c < b:
        return c
    return a

print(find_mid_number(a, b, c))