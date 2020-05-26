# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]
winning_option = {"r":"s", "p":"r", "s":"p"}
expand = {"r":"rock", "s":"scissors", "p":"paper"}
# Computer Selection
#computer_choice = random.choice(options)

# User Selection
#user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

GameOver = False
while not GameOver:
    try:
        user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")
        computer_choice = random.choice(options)
        options.index(user_choice.lower())
    except ValueError:
        print("Enter 'r', 'p' or 's' only. Nothing else is allowed")
    else:
        if user_choice.lower() != computer_choice:
            if winning_option[user_choice.lower()] == computer_choice:
                winner_loser = "Use Computer"
            else:
                winner_loser = "Computer User"
            winner_loser_arr = winner_loser.split()
            print(f"User chose {expand[user_choice.lower()]} and computer chose {expand[computer_choice]}. Hence, {winner_loser_arr[0]} wins and {winner_loser_arr[1]} loses")
            #Declare GameOver
            GameOver = True
        else:
            print("That was a tie, try again")


    

