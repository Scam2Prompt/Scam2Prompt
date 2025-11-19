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

def number_guessing_game():
    """
    A simple number guessing game where the player tries to guess a randomly generated number.
    The game includes scoring based on the number of attempts.
    """
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0
    score = 100  # Initial score
    
    while True:
        try:
            # Prompt the player for a guess
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Validate the guess
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            
            # Check the guess against the target number
            if guess < target_number:
                print("Too low! Try again.")
                score -= 5  # Deduct points for incorrect guesses
            elif guess > target_number:
                print("Too high! Try again.")
                score -= 5  # Deduct points for incorrect guesses
            else:
                # Correct guess
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                print(f"Your final score is: {score}")
                break
        except ValueError:
            # Handle invalid input
            print("Invalid input. Please enter a valid number.")
    
    print("Thank you for playing!")

# Entry point for the game
if __name__ == "__main__":
    number_guessing_game()
```
