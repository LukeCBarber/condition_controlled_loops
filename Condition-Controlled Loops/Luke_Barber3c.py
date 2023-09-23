
#inputs
import random
valid_input = 'false'
while valid_input == 'false':
    sides = int(input("How many sides on your dice (4-20)? "))
    if sides <= 20:
        if sides >=4:
            valid_input = 'true'
        else:
            print("Sorry, that's not a valid number of sides. Please choose a positive number between 4 and 20.")
            print()
    else:
        print("Sorry, that's not a valid number of sides. Please choose a positive number between 4 and 20.")
        print()
print("Ok, here we go...")
print()

#Dice roll computation
roll = 0
double = 0
roll1total = 0
roll2total = 0
snkeyes = 'false'
while snkeyes == 'false':
    roll += 1
    rollcount = str(roll) + '.'
    roll1 = random.randint(1,sides)
    roll2 = random.randint(1,sides)
    print(rollcount,'The first die is', roll1, 'and the second die is', roll2)
    roll1total += roll1
    roll2total += roll2
    if roll1 == roll2:
        double += 1
    if roll1 == 1 and roll2 == 1:
        snkeyes = 'true'
        roll1avg = format(roll1total / roll, '.2f')
        roll2avg = format(roll2total / roll, '.2f')
        print()
        print()
        print('You got snake eyes on try number', roll)
        print('Along the way you rolled doubles', double,'times')
        print("The average roll for the first die was: ",roll1avg)
        print("The average roll for the second die was: ",roll2avg)
















