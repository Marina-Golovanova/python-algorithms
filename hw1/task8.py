year = int(input("Enter year: "))

def is_leap_year(year):
    if (year % 4 != 0):
        return "It's not a leap year"

    elif (year % 100 != 0):
        return "It's a leap year"

    elif (year % 400 == 0):
        return "It's a leap year"
        
    else:
        return "It's not a leap year"

print(is_leap_year(year))