# Number to Sum
# While-loop with break statement

total = 0

while True:
    number = input("Enter a number or 'done': ")
    if number == "done":
        break # exit loop
    else:
        total = total + int(number)

print("The sum is:", total)
