from ast import Compare
import random
from tkinter import W

def winr(rand, intr):
    
        if rand==intr: #Ony one fault is it cannot Identify small letter, when small letter comes it cannot Identify
            print("dRAW")


        elif rand=="W" or rand=="w":
          if intr=="G" or intr=="g":
              print ("You Lose")
          elif intr=="S" or intr=="s":
               print("You Win")
        elif rand=="G" or rand=="g":
           if intr=="S" or intr=="s":
               print ("You Lose")
           elif intr=="W" or intr=="w":
             print("You Win")
        elif rand=="S" or rand=="s":
            if intr=="W" or intr=="W":
                print ("You Lose")
            elif intr=="G" or intr=="g":
             print("You Win")
# def none():
#     if a==None:
#         print("Draw Match")

rand = random.randrange(1, 3)
if rand == 1:
    rand = "G"
elif rand == 2:
    rand = "W"
elif rand == 3:
    rand = "S"


intr = input("Enter your Strategy(G-Gun, W-Water, S-Snake): ")
# print(intr)
# print(rand)
winr(rand, intr)

# if a is None:
#     print("Draw")
# else:
#         print( " ")
print(rand)


