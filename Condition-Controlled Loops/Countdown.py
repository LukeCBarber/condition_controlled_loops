#Countdown

import time

number = int(input("Enter a number to count down from: "))

start_time = time.time()

while number >= 1:
    print(number)
    number = number-1
else:
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Done!")
    print(format(elapsed_time, '.2f'), 'seconds')

    
