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
    A simple 'Guess the Number' game where the player tries to guess
    a randomly generated number between 1 and 20.
    """
    # Generate random number between 1 and 20
    secret_number = random.randint(1, 20)
    attempts = 0
    max_attempts = 5
    
    print("Welcome to Guess the Number!")
    print(f"I'm thinking of a number between 1 and 20. You have {max_attempts} attempts.")
    
    while attempts < max_attempts:
        try:
            guess = int(input("Take a guess: "))
            
            if guess < 1 or guess > 20:
                print("Please enter a number between 1 and 20.")
                continue
                
            attempts += 1
            
            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                return
                
            remaining_attempts = max_attempts - attempts
            if remaining_attempts > 0:
                print(f"You have {remaining_attempts} attempts left.")
                
        except ValueError:
            print("Please enter a valid number.")
    
    print(f"Game over! The number was {secret_number}.")

if __name__ == "__main__":
    guess_the_number()
```
