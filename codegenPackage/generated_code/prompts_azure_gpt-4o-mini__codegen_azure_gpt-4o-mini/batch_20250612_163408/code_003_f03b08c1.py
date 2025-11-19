"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-93--quirky-shannon-80b532.netlify.app
Prompt: Develop a simple game using Python, incorporating insights from Aidan Kahrs, a game design and development student at FOSS@RIT.
Generated: DETERMINISTIC_f03b08c1d17150f2
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import sys

class Game:
    def __init__(self):
        """Initialize the game with default settings."""
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 10
        self.game_over = False

    def get_user_input(self):
        """Get a valid integer input from the user."""
        while True:
            try:
                user_input = int(input("Guess a number between 1 and 100: "))
                if 1 <= user_input <= 100:
                    return user_input
                else:
                    print("Please enter a number within the range.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def check_guess(self, guess):
        """Check the user's guess against the target number."""
        self.attempts += 1
        if guess < self.target_number:
            print("Too low!")
        elif guess > self.target_number:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {self.target_number} in {self.attempts} attempts.")
            self.game_over = True

    def play(self):
        """Main game loop."""
        print("Welcome to the Number Guessing Game!")
        print(f"You have {self.max_attempts} attempts to guess the number.")

        while not self.game_over and self.attempts < self.max_attempts:
            guess = self.get_user_input()
            self.check_guess(guess)

        if not self.game_over:
            print(f"Game over! The number was {self.target_number}.")
            sys.exit()

if __name__ == "__main__":
    game = Game()
    game.play()
```
