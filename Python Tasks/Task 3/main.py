# Sukurkite funkciją "addDigits", kuri priims sveiką skaičių nuo 10 iki 999 ir grąžins jo skaitmenų sumą. 

# Pvz.
# Jeigu duota 34, funckiją turėtų grąžinti 7.
# Jeigu duota 999, funckija turėtų grąžinti 27.


def addDigits(number):
    digits_sum = 0
    while number > 0:
        digits_sum += number % 10
        number //= 10
    return digits_sum


number = int(input("Enter a number between 10 and 999: "))
if 10 <= number <= 999:
    digits_sum = addDigits(number)
    print(f"The sum of digits in {number} is {digits_sum}")
else:
    print("Invalid input. Number should be between 10 and 999")

