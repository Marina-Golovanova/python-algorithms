a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

def is_triangle(a, b, c):
    if a + b <= c or b + c <= a or a + c <= b:
        return "Such triangle doesn't exist"
    elif (a == b == c):
        return "This is an equilateral triangle"
    elif (a == b or a == c or b == c):
        return "This is an isosceles triangle"
    else:
        return "Such triangle exists"

print(is_triangle(a, b, c))