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

def guess_the_number():
    """
    A simple "Guess the Number" game where the user guesses a number between 1 and 20.
    The game provides feedback and runs until the user guesses correctly or chooses to exit.
    """
    # Generate a random number between 1 and 20
    target_number = random.randint(1, 20)
    attempts = 0  # Track the number of attempts
    
    print("Welcome to the 'Guess the Number' game!")
    print("I have selected a number between 1 and 20. Try to guess it!")
    print("Type 'exit' to quit the game at any time.")
    
    while True:
        try:
            user_input = input("Enter your guess (1-20): ").strip()
            
            # Check if the user wants to exit the game
            if user_input.lower() == 'exit':
                print("Thanks for playing! Goodbye!")
                break
            
            # Validate the user input
            guess = int(user_input)
            if guess < 1 or guess > 20:
                print("Please enter a valid number between 1 and 20.")
                continue
            
            # Increment the attempt counter
            attempts += 1
            
            # Compare the guess with the target number
            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        
        except ValueError:
            # Handle invalid input (non-integers)
            print("Invalid input! Please enter a number between 1 and 20.")
        except Exception as e:
            # Handle unexpected errors gracefully
            print(f"An error occurred: {e}")
            print("Please try again.")

# Run the game if the script is executed directly
if __name__ == "__main__":
    guess_the_number()
```
