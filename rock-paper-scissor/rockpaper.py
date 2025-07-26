import random

options = ("rock", "paper", "scissors")
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice rock, paper, or scissors(r,p,s) : ")
 
    print(f"player :{player}")
    print(f"computer :{computer}")

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
        print("You win!")

    else:
        print("You lose!")

    
    if not input("Do you want to play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")