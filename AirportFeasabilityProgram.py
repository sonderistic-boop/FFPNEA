import time
import sys
import re

global verification1

def setup():
    global verification1
    verification1 = False


def mainmenu():
    global verification1
    while verification1 == False:
        verification1 = False
        try:
            option1 = int(input("1) Enter airport details \n2) Enter flight details \n3)Enter price plan and calculate profit \n4) Clear data \n5) Quit\n"))
        except ValueError:
            print("Invalid Input")
        if (option1 > 5) and (option1 < 1):
            print("Invalid Input")
        else:
            verification1 = True
            print(option1)
            return int(option1)
        


setup()
mainmenu()

    



        
if mainmenu() == 1:
    print("YOOOO")

print("\n-::Flight Feasability Program::-\n")

        

        
