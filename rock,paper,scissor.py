import random
list1=['rock','paper','scissor']
computer=random.choice(list1)
user=str(input("Choose rock,paper, or scissor: "))
print("You chose ",user," and computer chose ",computer)
if(user==computer):
    print("It's a tie!")
elif(user=='rock' and computer=='scissor'):
    print("You win!")
elif(user=='rock' and computer=='paper'):
    print("Computer wins!")
elif(user=='scissor' and computer=='rock'):
    print("Computer wins!")
elif(user=='scissor' and computer=='paper'):
    print("You win!")
elif(user=='paper' and computer=='rock'):
    print("You win!")
elif(user=='paper' and computer=='scissor'):
    print("Computer wins!")
