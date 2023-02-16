
number = [1, 2, 3, 4]
fruits = ['apple', 'banana', 'orange', 'ananas']

# a
comb1 = [(n, f) for n in number for f in fruits]
print(comb1)

# b
comb2 = [(n2, f2) for n2 in number if n2 % 2 != 0 for f2 in fruits]
print(comb2)

# c
comb3 = [(n3, f3) for n3 in number if n3 %
         2 != 0 for f3 in fruits if f3[0] == 'a']
print(comb3)
