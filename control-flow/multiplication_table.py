number = int(input("Enter a number to see its multiplication table:"))

for x in range(1,11):
    print("{0} * {1} = {2}".format(number, x, number * x))
