

import random

flag = True
while flag:
    num = input('Type your nuber for an upper nuber: ')

    if num.isdigit():
        print("Let's Play! ")
        num = int(num)
        flag = False

    else:
        print('Invalid number!')

secret = random.randint(1,num)

guess = None
count = 1

while guess != secret:
    guess = input('Please enter your nuber form 1 to ' + str(num) + ': ')

    if guess.isdigit():
        guess = int(guess)

    if guess == secret:
        print('You won!')
       

    else:
        print('Try again')
        count += 1