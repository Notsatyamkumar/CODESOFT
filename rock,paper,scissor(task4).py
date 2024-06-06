import random

def game():
    choices = ["rock", "paper", "scissors"]
    score_user = 0
    score_computer = 0

    while True:
        print("\nRock-Paper-Scissors Game")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit Game")

        user_choice = input("Enter your choice (1/2/3) or 4 to quit: ")

        if user_choice == "4":
            print("\nFinal Score - You: {}, Computer: {}".format(score_user, score_computer))
            break

        if user_choice not in ["1", "2", "3"]:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        user_choice = choices[int(user_choice) - 1]

        computer_choice = random.choice(choices)

        print("\nYou chose: {}".format(user_choice))
        print("Computer chose: {}".format(computer_choice))

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
            score_user += 1
        else:
            print("Computer wins!")
            score_computer += 1

        print("Score - You: {}, Computer: {}".format(score_user, score_computer))

if __name__ == "__main__":
    game()