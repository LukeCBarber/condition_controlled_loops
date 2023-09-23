#Numbers to Sum

quantity = int(input("How many numbers would you like to add? "))

total = 0 # accumulator variable
i = 1 # keeps track of how many numbers entered

while i <= quantity:
    number = input("Enter number " + str(i) + ": ")
    total = total + int(number)
    i = i + 1

print("The sum is:", total)

