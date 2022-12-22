# Variable Flipper (ex. input a=6 b=9, return a=9 b=6)
a = input("Type your first number here  ")
b = input("Type your second number here  ")

a, b = b, a

print(a)
print(b)