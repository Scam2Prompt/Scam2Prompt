"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-93--quirky-shannon-80b532.netlify.app
Prompt: Develop a simple game using Python, incorporating insights from Aidan Kahrs, a game design and development student at FOSS@RIT.
Generated: DETERMINISTIC_f03b08c1d17150f2
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import sys

class Game:
    def __init__(self):
        """Initialize the game with default settings."""
        self.target_number = random.randint(1, 100)  # Target number between 1 and 100
        self.guesses = 0  # Counter for the number of guesses

    def get_guess(self):
        """Prompt the player for a guess and return the validated input."""
        while True:
            try:
                guess = int(input("Enter your guess (1-100): "))
                if 1 <= guess <= 100:
                    return guess
                else:
                    print("Please enter a number between 1 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def check_guess(self, guess):
        """Check the player's guess against the target number and give feedback."""
        self.guesses += 1
        if guess < self.target_number:
            print("Too low!")
        elif guess > self.target_number:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {self.target_number} in {self.guesses} attempts.")
            return True  # Return True if the guess is correct
        return False  # Return False if the guess is incorrect

    def play(self):
        """Main game loop to play the guessing game."""
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")

        while True:
            guess = self.get_guess()
            if self.check_guess(guess):
                break  # Exit the loop if the guess is correct

        self.ask_to_play_again()

    def ask_to_play_again(self):
        """Prompt the player to play again or exit the game."""
        while True:
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again in ['yes', 'y']:
                self.__init__()  # Reset the game
                self.play()
            elif play_again in ['no', 'n']:
                print("Thanks for playing!")
                sys.exit(0)  # Exit the game
            else:
                print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    game = Game()
    game.play()
```
