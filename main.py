storage = []

user_integer = int(input('Insert an integer: '))

while user_integer != 0:
    storage.append(user_integer)
    user_integer = int(input('Insert an integer: '))

storage.sort(reverse=True)

for numbers in storage:
    print(numbers)