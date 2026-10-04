import random

print("=======")
print("      ROCK PAPER SCISSORS")
print("==========")

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

for round_number in range(1, 6):
    print(f"\nRound {round_number} of 5")

    player = input("Choose rock, paper, or scissors: ").lower()
    computer = random.choice(choices)

    if player not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    print("Computer chose:", computer)

    if player == computer:
        print("It's a tie!")

    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        print("You win this round!")
        player_score += 1

    else:
        print("Computer wins this round!")
        computer_score += 1

print("\n================================")
print("           FINAL SCORE")
print("================================")

print("Your score:", player_score)
print("Computer score:", computer_score)

if player_score > computer_score:
    print(" Congratulations! You won the game!")
elif computer_score > player_score:
    print(" Computer won the game. Better luck next time!")
else:
    print(" The game is a tie!")
