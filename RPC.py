import random
choices = ["rock", "paper", "scissors"]

def computer():
    x = random.randint(1,3)
    choice =  choices[x]
    return choice


def user():
    while True:
        x = input("Choose between either Rock, Paper or Scissors ")
        choice = x.lower()
        if choice in choices:
            return choice
        
        print("Invalid input")

def checkWinner(user, comp):#very redundant try to make shorter, maybe make choices into numbers and check?
    if user == comp:
        print("It was a draw")
        return 0
    if user == "scissors" & comp == "paper":
         print("You won")
         return 1
    if user == "rock" & comp == "scissors":
        print("You won")
        return 1
    if user == "paper" & comp == "rock":
        print("You won")
        return 1

    else:
        print("You lost")
        return 0



def RPC(): 
    print("Welcome to Rock Paper Scissors\n")
    





if __name__ == "__main__":

    RPC()

