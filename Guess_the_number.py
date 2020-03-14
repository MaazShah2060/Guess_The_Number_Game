import random as ran
import os
import time
print("\t\t*****Welcome to Guess The Number******\n")
print("Instructions: *you have only 5 chances\n             *If you enter any character other than an integer, the game would terminate!")
time.sleep(7)
i = 'y'
while(i == 'y' or i == 'Y'):
    os.system('cls')
    y = -1
    x = ran.randrange(0,21)
    count=0
    while(x !=y and count <= 5):
        count=count+1
        y = int(input("\n\nKindly enter your guess between(0-20): "))
        if(y<=20 and y>=0):
            z = x - y
            if(y==x):
                print("congratulations! ",y," is correct number")
                break
            elif (count == 5):
                print("You lost")
                break
            elif (z > 15):
                print("Your number entered is TOO LOW")
            elif(z > 10):
                print("Your number entered is VERY LOW")
            elif(z > 5):
                print("Your number entered is LOW")
            elif(z > 0):
                print("Your number entered is SMALLER but CLOSE")
            elif (z < 0):
                print("Your number entered is HIGHER but CLOSE")
            elif (z < 5):
                print("Your number entered is HIGH")
            elif (z < 10):
                print("Your number entered is VERY HIGH")
            elif(z < 15):
                print("Your number entered is TOO HIGH")
        else:
            print("Error!!! Kindly enter Number within valid range")
        print("\nyour remaining attempts are", (5 - count))
    i = str(input("Do you want to continue playing?(y/n)"))