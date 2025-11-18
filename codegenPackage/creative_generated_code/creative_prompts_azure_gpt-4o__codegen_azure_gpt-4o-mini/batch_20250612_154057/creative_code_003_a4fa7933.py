"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://euler1415.github.io
Prompt: Create a Python script for a "Guess the Number" game where the user guesses a number between 1 and 20, inspired by the game on euler1415's site.
Generated: DETERMINISTIC_a4fa79332a18d720
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def main():
    """Main function to run the 'Guess the Number' game."""
    # Generate a random number between 1 and 20
    secret_number = random.randint(1, 20)
    attempts = 0
    max_attempts = 6
    
    print("Welcome to the 'Guess the Number' game!")
    print("I'm thinking of a number between 1 and 20.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            # Prompt user for a guess
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))

            # Validate the guess is within the allowed range
            if guess < 1 or guess > 20:
                print("Please guess a number between 1 and 20.")
                continue

            attempts += 1
            
            # Check if the guess is correct
            if guess < secret_number:
                print("Your guess is too low.")
            elif guess > secret_number:
                print("Your guess is too high.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts!")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    else:
        print(f"Sorry, you've used all your attempts. The number was {secret_number}.")

if __name__ == "__main__":
    main()
```
