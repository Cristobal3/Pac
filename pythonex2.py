import random
'''
#Step 1
print('I am thinking of a number between 1 and 10.')
while True:
    num = int(input('What\'s the number? ' ))
    if num == 5:
        print('Yes! You won!')
        break
    else:
        print('Nope, try again.')

#Step 2
print('I am thinking of a number between 1 and 10.')
while True:
    num = int(input('What\'s the number? ' ))
    if num == 5:
        print('Yes! You won!')
        break
    elif num > 5:
        print(num,' is too high.')
    else:
        print(num,' is too low.')

#Step 3
randnum = random.randint(1,10)
print('I am thinking of a number between 1 and 10.')
while True:
    num = int(input('What\'s the number? ' ))
    if num == randnum:
        print('Yes! You won!')
        break
    elif num > randnum:
        print(num,' is too high.')
    else:
        print(num,' is too low.')
'''
#Step 4
while True:
    randnum = random.randint(1,10)
    print('I am thinking of a number between 1 and 10.')
    tries = 5
    while True:
        print('You have ',tries,' tries left.')
        num = int(input('What\'s the number? ' ))
        tries -=1
        if tries > 0:
            if num == randnum:
                print('Yes! You won!')
                break
            elif num > randnum:
                print(num,' is too high.')
            else:
                print(num,' is too low.')
        else:
            print('You ran out of guesses!')
            break
    answer = input('Do you want ot play again (Y or N)? ')
    if answer=='Y':
        r=4
    else:
        print('Bye!')
        break   
        
