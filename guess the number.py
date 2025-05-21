import random
import string
Gamenumber=random.randint(1,100)

while True:
    Usernumber=input("Enter number to guess")
    if (Usernumber=="Q"):
        print("You Quit Successfully","The game number is ",Gamenumber)
        break
    Usernumber=int(Usernumber)
    if(Usernumber==Gamenumber):
        print("__YouWon__ guessed successfully")
    elif(Usernumber<Gamenumber):
        print("Gussed number is too small")
    else:
        print("Gussed number is too large")
    
print("__GAMEOVER__")