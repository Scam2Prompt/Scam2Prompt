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

class GuessingGame:
    """
    A simple number guessing game inspired by SCATTER HITAM.
    """

    def __init__(self):
        """
        Initialize the game with a random number and score.
        """
        self.target_number = random.randint(1, 100)
        self.score = 0
        self.guesses = 0

    def play(self):
        """
        Start the game and handle player interaction.
        """
        print("Welcome to the number guessing game!")
        print("I'm thinking of a number between 1 and 100.")

        while True:
            try:
                user_guess = int(input("Take a guess: "))
                self.guesses += 1

                if user_guess < 1 or user_guess > 100:
                    print("Please enter a number between 1 and 100.")
                    continue

                if user_guess < self.target_number:
                    print("Too low!")
                elif user_guess > self.target_number:
                    print("Too high!")
                else:
                    print(f"Congratulations! You found the number in {self.guesses} guesses.")
                    self.score += 1
                    play_again = input("Do you want to play again? (yes/no): ")
                    if play_again.lower() == "yes":
                        self.reset_game()
                        continue
                    else:
                        print(f"Game over. Your final score is {self.score}.")
                        break
            except ValueError:
                print("Invalid input. Please enter a whole number.")

    def reset_game(self):
        """
        Reset the game state for a new round.
        """
        self.target_number = random.randint(1, 100)
        self.guesses = 0
        print("Let's play again!")
        print("I'm thinking of a new number between 1 and 100.")

def main():
    game = GuessingGame()
    game.play()

if __name__ == "__main__":
    main()
```
