import random

def get_player_choice():
    while True:
        choice = input("Choose snake (s), water (w), or gun (g): ").lower()
        if choice in ["s", "w", "g"]:
            return choice
        else:
            print("Invalid choice. Try again.")

def get_computer_choice():
    return random.choice(["s", "w", "g"])

def determine_winner(player_choice, computer_choice):
    print(f"You chose: {player_choice} \nComputer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "s" and computer_choice == "w") or \
         (player_choice == "w" and computer_choice == "g") or \
         (player_choice == "g" and computer_choice == "s"):
        print("You win!")
    else:
        print("Computer wins!")

while True:
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    determine_winner(player_choice, computer_choice)

    play_again = input("Play again? (y/n): ").lower()
    if play_again != "y":
        break
