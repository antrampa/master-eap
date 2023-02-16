number = int(input("give a integer and I'll tell you if it's a first number: "))
# print(number)
raw_list = [n for n in range(1, number+1)]
# print(raw_list)
list = [n for n in range(2, number+1) if (number % n == 0)]
# print(list)
# print(len(list))
# print(list[0])
if (len(list) == 1 and list[0] == number):
    print("the number {0} is a prime number".format(number))
else:
    print("The number {0} is not a prime number".format(number))
