s = input("give a positive integer and I'll tell you if it's a prime number: ")
number = int(s)
# print(number)
for n in range(2, number):
    y = number % n
    # print(n)
    # print(y)
    if y == 0:
        print(number, 'is not a prime number')
        break

else:
    print(number, 'is a prime number')
    # print(type(y))
