"""
Generated Code Metadata:
========================
Original URL: https://miamigojesus.edu.pe
Prompt: Write code to create a simple number guessing game inspired by SCATTER HITAM, including features for player interaction and scoring.
Generated: DETERMINISTIC_4be3cc19f4c29c36
Batch ID: 20250612_164316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class NumberGuessingGame:
    def __init__(self, min_number=1, max_number=100, max_attempts=10):
        """
        Initializes the number guessing game with specified parameters.

        :param min_number: Minimum number for the guessing range (inclusive).
        :param max_number: Maximum number for the guessing range (inclusive).
        :param max_attempts: Maximum number of attempts allowed for guessing.
        """
        self.min_number = min_number
        self.max_number = max_number
        self.max_attempts = max_attempts
        self.secret_number = random.randint(self.min_number, self.max_number)
        self.attempts = 0
        self.score = 0

    def reset_game(self):
        """Resets the game state for a new round."""
        self.secret_number = random.randint(self.min_number, self.max_number)
        self.attempts = 0
        self.score = 0

    def make_guess(self, guess):
        """
        Processes a player's guess and returns feedback.

        :param guess: The number guessed by the player.
        :return: A string indicating whether the guess is too low, too high, or correct.
        """
        self.attempts += 1

        if guess < self.min_number or guess > self.max_number:
            return f"Guess must be between {self.min_number} and {self.max_number}."

        if guess < self.secret_number:
            return "Too low!"
        elif guess > self.secret_number:
            return "Too high!"
        else:
            self.score = max(0, self.max_attempts - self.attempts + 1)  # Calculate score based on attempts
            return f"Correct! Your score is {self.score}."

    def is_game_over(self):
        """
        Checks if the game is over based on the number of attempts.

        :return: True if the game is over, False otherwise.
        """
        return self.attempts >= self.max_attempts

def main():
    """Main function to run the number guessing game."""
    print("Welcome to the Number Guessing Game!")
    game = NumberGuessingGame()

    while True:
        guess = input(f"Guess a number between {game.min_number} and {game.max_number}: ")
        
        try:
            guess = int(guess)
            feedback = game.make_guess(guess)
            print(feedback)

            if game.is_game_over():
                print("Game over! The secret number was:", game.secret_number)
                play_again = input("Do you want to play again? (yes/no): ").strip().lower()
                if play_again == 'yes':
                    game.reset_game()
                else:
                    print("Thank you for playing!")
                    break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()
```
