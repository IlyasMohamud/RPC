import random
choices = ["Rock", "Paper", "Scissors"]

def computer():
    x = random.randint(1,3)
    choice =  choices[x]
    return choice


print (computer())