
terms = int(input("How many Fibonacci numbers do you want? "))

first = 0
second = 1

print("Fibonacci Sequence:")

for i in range(terms):
    print(first, end=" ")

    next_number = first + second
    first = second
    second = next_number
