#Random Number guessing Game(Project-2)
import random

def number_guessing_game():
    """
    This function implements a number guessing game where the player tries to guess a randomly generated number.
    """
    lower_bound = 1  # Set the lower limit for the random number
    upper_bound = 100  # Set the upper limit for the random number
    secret_number = random.randint(lower_bound, upper_bound)  # Generate the secret number

    guesses = 0  # Initialize the guess counter

    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")

    while True:
        try:
            guess = int(input("Enter your guess: "))  # Get the player's guess
            guesses += 1  # Increment the guess counter

            if guess < secret_number:
                print("Higher number please.")
            elif guess > secret_number:
                print("Lower number please.")
            else:
                print(f"Congratulations! You guessed the number in {guesses} guesses!")
                break  # Exit the loop when the number is guessed correctly

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    number_guessing_game()  # Start the game
