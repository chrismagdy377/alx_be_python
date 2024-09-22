number = int(input("Enter a number to see its multiplication table:"))

numbers = range(1,11)
for x in numbers:
    print("{0} * {1} = {2}".format(number, x, number * x))
