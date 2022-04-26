import random
import math
#Taking Input from User
lower=int(input("Enter Lower Limit: ")) 
upper=int(input("Enter Upper Limit: "))
#genrate Random Number in Between
#the Lower and the upper
x=random.randint(lower,upper)
print("\n\t You've only",round(math.log(upper-lower+1, 2)),"chance to guess the integer !\n ")

#Intializing the number of guesses.
count=0

#for calculating of minimum number of
#guesses depends upon range

while count <math.log(upper-lower + 1 , 2):
    count +=1
    #taking guessing number as input
    guess=int(input("Guess a Number: -"))
    
    #Condition testing :

    if x==guess:
        print("Congratulation You didi it in", count, "try")
        #once guessed , Loop will break
    elif x>guess:
        print("Your guessed is to small !")
    elif x< guess:
        print("You Guessed too high !")
#If Guessing number is more than required guesses
#show this output
if count >=math.log(upper-lower+1,2):
    print("\nThe Number id %d" %x)
    print("\t Better Luck Next time !")

     
