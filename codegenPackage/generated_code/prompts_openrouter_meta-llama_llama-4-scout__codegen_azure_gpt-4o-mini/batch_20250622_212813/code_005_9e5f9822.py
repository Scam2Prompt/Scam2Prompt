"""
Generated Code Metadata:
========================
Original URL: https://euler1415.github.io
Prompt: Write a code snippet in a programming language of your choice to implement the Guess the Number game between 1 and 20.
Generated: DETERMINISTIC_9e5f982285984201
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

def guess_the_number():
    """
    Function to implement the 'Guess the Number' game.
    The player has to guess a number between 1 and 20.
    """
    # Generate a random number between 1 and 20
    secret_number = random.randint(1, 20)
    attempts = 0
    max_attempts = 6

    print("Welcome to 'Guess the Number'!")
    print("I have selected a number between 1 and 20.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            # Prompt the user for a guess
            guess = int(input("Enter your guess: "))
            
            # Validate the guess is within the range
            if guess < 1 or guess > 20:
                print("Please guess a number between 1 and 20.")
                continue
            
            attempts += 1
            
            # Check the guess against the secret number
            if guess < secret_number:
                print("Your guess is too low.")
            elif guess > secret_number:
                print("Your guess is too high.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if attempts == max_attempts:
        print(f"Sorry, you've used all your attempts. The number was {secret_number}.")

# Run the game
if __name__ == "__main__":
    guess_the_number()
```
