#use of Random Module in Python

from random import *                                # importing every property of random module

dice1 = [1, 2, 3, 4, 5, 6]
dice2 = [1, 2, 3, 4, 5, 6]

play = input("Do you wish to play?")

while play == "yes":
    x1 = sample(dice1, 1)
    y1 = sample(dice2, 1)
    x2 = sample(dice1, 1)
    y2 = sample(dice2, 1)

    print("For player 1: ")
    print(x1, ", ", y1)
    print("For player 2: ")
    print(x2, ", ", y2)
    play = input("Do you wish to play?")
    
else:
    print("Thankyou!")
