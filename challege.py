import math
import time
max = int(input("Tot welk getal wil je priemgetallen zoeken\n: "))
count = 1

while True:
    check = True
    for x in range(2, int(math.sqrt(count) + 1)):
        if count % x == 0: 
            check = False
            break
    if check == True:
        print (count)
    
    if count == max:
        break
    else:
        count += 1
    time.speed = 10