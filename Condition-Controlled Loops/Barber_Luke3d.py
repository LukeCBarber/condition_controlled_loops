#input
print("STICK GAME")
print()
valid_input = 'false'

while valid_input == 'false':
    sticks = int(input('How many sticks to start with (10-100)? '))
    if sticks >= 10:
        if sticks <= 100:
            valid_input = 'true'
            print("Great, let's play . . .")
        else:
            print("Sorry, that's too many sticks. Try again.")
            print()
    else:
        print("Sorry, that's too many sticks. Try again.")
        print()
turn = 1
while sticks > 0:
    valid_input = 'false'
    while valid_input == 'false':
        print()
        print("Turn:", turn)
        print("There are", sticks,"sticks on the table.")
        take = int(input("How many sticks do you want to take (1, 2 or 3)? "))
        if take == 1 or take == 2 or take == 3:
            sticks = sticks - take
            if turn == 1:
                turn += 1
            else:
                turn -= 1
            valid_input = 'true'
            print()
        else:
            print("Sorry, that's not a valid number.")
            print()

print()
print("There are no sticks left on the table. Game over.")
print("Player", turn,"wins!")

    
