var1 = "Hello World"

print(var1)

a = 5
b = 3

c = a + b

print(c)

c = a - b

print(c)

c = a * b

print(c)

c = a / b

print(c)

try:
    user_number = int(input("Please pick a number between one and ten \n"))
except ValueError:
    print("You did not pick a number")

if user_number < 1 or user_number > 10:
    print("You selected a number outside of the requested parameters")
else:
    print("You selected " + str(user_number))
