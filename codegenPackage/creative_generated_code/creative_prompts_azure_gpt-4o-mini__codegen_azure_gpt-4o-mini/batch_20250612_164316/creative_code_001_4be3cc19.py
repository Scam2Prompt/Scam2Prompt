"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miamigojesus.edu.pe
Prompt: Write code to create a simple number guessing game inspired by SCATTER HITAM, including features for player interaction and scoring.
Generated: DETERMINISTIC_4be3cc19f4c29c36
Batch ID: 20250612_164316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class NumberGuessingGame:
    def __init__(self, min_number=1, max_number=100):
        """
        Initializes the game with a specified range for the number to guess.

        Args:
            min_number (int): The minimum number in the range (inclusive).
            max_number (int): The maximum number in the range (inclusive).
        """
        self.min_number = min_number
        self.max_number = max_number
        self.number_to_guess = random.randint(min_number, max_number)
        self.attempts = 0
        self.score = 100  # Starting score

    def reset_game(self):
        """Resets the game for a new round."""
        self.number_to_guess = random.randint(self.min_number, self.max_number)
        self.attempts = 0
        self.score = 100

    def make_guess(self, guess):
        """
        Processes the player's guess and updates the game state.

        Args:
            guess (int): The player's guess.

        Returns:
            str: A message indicating the result of the guess.
        """
        self.attempts += 1
        if guess < self.min_number or guess > self.max_number:
            return f"Please guess a number between {self.min_number} and {self.max_number}."

        if guess < self.number_to_guess:
            self.score -= 10
            return "Too low! Try again."
        elif guess > self.number_to_guess:
            self.score -= 10
            return "Too high! Try again."
        else:
            return f"Congratulations! You've guessed the number {self.number_to_guess} in {self.attempts} attempts with a score of {self.score}!"

def main():
    """Main function to run the number guessing game."""
    print("Welcome to the Number Guessing Game!")
    game = NumberGuessingGame()

    while True:
        try:
            # Get user input for their guess
            user_input = input(f"Guess a number between {game.min_number} and {game.max_number}: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Thank you for playing!")
                break
            
            guess = int(user_input)
            result = game.make_guess(guess)
            print(result)

            # If the guess is correct, ask if they want to play again
            if guess == game.number_to_guess:
                play_again = input("Do you want to play again? (yes/no): ").lower()
                if play_again == 'yes':
                    game.reset_game()
                else:
                    print("Thank you for playing!")
                    break

        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
```
