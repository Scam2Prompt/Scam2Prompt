"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miamigojesus.edu.pe
Prompt: Write code to create a simple number guessing game inspired by SCATTER HITAM, including features for player interaction and scoring.
Generated: DETERMINISTIC_4be3cc19f4c29c36
Batch ID: 20250612_164316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def number_guessing_game():
    """
    A simple number guessing game where the player tries to guess a random number 
    within a specified range. The game includes scoring and player interaction.
    """
    print("Welcome to the Number Guessing Game!")
    print("Inspired by SCATTER HITAM")
    
    # Game configuration
    min_number = 1
    max_number = 100
    max_attempts = 10
    
    # Initialize the random number to guess
    target_number = random.randint(min_number, max_number)
    
    # Initialize player score and attempts
    player_score = 0
    attempts = 0
    
    print(f"\nGuess the number between {min_number} and {max_number}.")
    print(f"You have a maximum of {max_attempts} attempts. Good luck!\n")
    
    while attempts < max_attempts:
        try:
            # Increment attempts
            attempts += 1
            
            # Prompt player for a guess
            guess = int(input(f"Attempt {attempts}/{max_attempts}: Enter your guess: "))
            
            # Validate the guess range
            if guess < min_number or guess > max_number:
                print(f"Invalid input! Please enter a number between {min_number} and {max_number}.")
                continue
            
            # Check the guess against the target number
            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {target_number} correctly.")
                # Calculate score based on remaining attempts
                player_score = (max_attempts - attempts + 1) * 10
                break
        
        # Handle non-numeric input
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    # End of game feedback
    if attempts >= max_attempts and guess != target_number:
        print(f"\nGame Over! The correct number was {target_number}.")
    else:
        print(f"\nYour score: {player_score}")
    
    print("\nThank you for playing the Number Guessing Game!")

# Main entry point for the program
if __name__ == "__main__":
    try:
        number_guessing_game()
    except Exception as e:
        # Catch unexpected errors
        print(f"An error occurred: {e}")
```
