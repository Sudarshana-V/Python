import random
computer=random.randint(1,51)
user=int(input("Guess a number between 1 and 50: "))
while(computer!=user):
    if(user>computer):
        print("Too High! Try again.")
    else:
        print("Too low! Try again.")
    user=int(input("Guess a number between 1 and 50: "))
if(user==computer):
    print("Congratulations, you guessed the number!")

#OUTPUT
#Guess a number between 1 and 50: 32
#Too High! Try again.
#Guess a number between 1 and 50: 10
#Too High! Try again.
#Guess a number between 1 and 50: 5
#Too low! Try again.
#Guess a number between 1 and 50: 8
#Too low! Try again.
#Guess a number between 1 and 50: 9
#Congratulations, you guessed the number!
