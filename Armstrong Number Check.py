
number = int(input("Enter a number: "))

temp = number
sum_of_digits = 0
digits = len(str(number))

while temp > 0:
    digit = temp % 10
    sum_of_digits += digit ** digits
    temp //= 10

if sum_of_digits == number:
    print(number, "is an Armstrong Number")
else:
    print(number, "is not an Armstrong Number")
