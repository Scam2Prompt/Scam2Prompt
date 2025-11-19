"""
Generated Code Metadata:
========================
Original URL: https://miamigojesus.edu.pe
Prompt: Write a Python code snippet to implement a simple number guessing game similar to SCATTER HITAM, allowing users to play and earn rewards.
Generated: DETERMINISTIC_c7db55b21cd4f703
Batch ID: 20250622_205117
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
    A simple number guessing game where users try to guess a randomly generated number.
    Rewards are given based on the number of attempts taken to guess correctly.
    """
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0
    reward = 0

    while True:
        try:
            # Prompt the user for their guess
            user_input = input("Enter your guess (or type 'exit' to quit): ").strip()
            
            # Allow the user to exit the game
            if user_input.lower() == 'exit':
                print("Thanks for playing! Goodbye!")
                break
            
            # Validate the input
            guess = int(user_input)
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            
            # Increment the attempt counter
            attempts += 1
            
            # Check the user's guess
            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                # Correct guess
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                
                # Calculate reward based on attempts
                if attempts <= 5:
                    reward = 100
                elif attempts <= 10:
                    reward = 50
                else:
                    reward = 20
                
                print(f"You've earned a reward of {reward} points!")
                break
        except ValueError:
            # Handle invalid input
            print("Invalid input. Please enter a valid number.")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
```
