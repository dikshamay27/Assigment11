s#Question 1 :   Create a threading process such that it sleeps for 5 seconds and then prints out a message.

import time
startTime=time.time()
for i in range(0,5):
   print(i)
   # making delay for 5 seconds
   time.sleep(5)
endTime= time.time()
elapsedTime= endTime _  start Time
print("elapsed Time = %s" % elapsedTime)

#Question 2 :     Make a thread that prints numbers from 1-10, waits for 1 sec between

import threading
from threading import Thread
import time

def display():
    for x in range(1,11):
        print(x)
        time.sleep(1)
t=Thread(target=display)
t.start()

#Question 3 :      Make a list that has 5 elements.Create a threading process that prints the 5 elements of the list with a delay of multiple of 2 sec between 
each display.

import threading
from threading import Thread
import time

def display(l):
    n=2
    for x in l:
        print(x)
        time.sleep(n)
        n+=2

l=[10,20,30,40]
t=Thread(target=display,args=(l,))
t.start()

# Q4. Call factorial function using thread.


import threading
from threading import Thread
import time
import math

def factorial(n):
    fact=1
    for x in range(1,n+1):
        fact=fact*x
    print("factorial is : ",fact)

n=int(input("enter the number you want to find factorial :"))
t=Thread(target=factorial,args=(n,))
t.start()