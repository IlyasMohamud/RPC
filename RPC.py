import random
choices = ["rock", "paper", "scissors"]
score = 0

def computer():#computer chooses random int, that becomes one of the choices
    x = random.randint(0,2)
    choice =  choices[x]
    print("computer chose " + choice)
    return choice


def user():#takes user input for choice, if the choice is invalid the user has to go agian
    while True:
        x = input("Choose between either Rock, Paper or Scissors ")
        choice = x.lower()
        if choice in choices:
            print("you chose "+ choice)
            return choice
            
        
        print("Invalid input")

def checkWinner(user, comp):#very redundant try to make shorter, maybe make choices into numbers and check?
    if user == comp:
        print("It was a draw")
        return 0
    if user == "scissors" and comp == "paper":
         print("You won")
         return 1
    if user == "rock" and comp == "scissors":
        print("You won")
        return 1
    if user == "paper" and comp == "rock":
        print("You won")
        return 1

    else:
        print("You lost")
        return 0


def keepgoing():#checks if the user wants to continue or not
   while True:
        x = input("would you like to continue, yes or no ")
        answer = x.lower()
        if answer == "yes":
            "Starting game again"
            return False 
        if answer == "no":
            print("Thanks for playing")
            return True
        print("invalid input")




def RPC(): #main game function
    print("Welcome to Rock Paper Scissors\n")
    while True:
       
        checkWinner(user(), computer())
        answer = keepgoing()
        if answer:
            return ""

    





if __name__ == "__main__":
    RPC()

