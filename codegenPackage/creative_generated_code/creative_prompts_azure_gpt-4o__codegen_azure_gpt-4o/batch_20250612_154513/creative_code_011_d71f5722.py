"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://locinews.com
Prompt: Write code to simulate a betting game for "Bầu Cua Bet88," incorporating the unique gameplay mechanics described on the website.
Generated: DETERMINISTIC_d71f5722c6de7836
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, well-documented implementation for simulating a simplified betting game based on "Bầu Cua Bet88."

```python
import random

# Game configuration constants
ANIMALS = ["Crab", "Fish", "Rooster", "Shrimp", "Gourd", "Deer"]
MIN_BET = 10   # Minimum bet amount
MAX_BET = 1000 # Maximum bet amount

# Function to validate user input
def get_valid_bet():
    while True:
        try:
            bet = int(input(f"Enter your bet amount (between {MIN_BET} and {MAX_BET}): "))
            if MIN_BET <= bet <= MAX_BET:
                return bet
            else:
                print(f"Invalid amount. Please enter a value between {MIN_BET} and {MAX_BET}.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Function to validate chosen animal
def get_valid_animal():
    while True:
        choice = input(f"Choose an animal to bet on ({', '.join(ANIMALS)}): ").capitalize()
        if choice in ANIMALS:
            return choice
        else:
            print(f"Invalid choice. Please select one of the following: {', '.join(ANIMALS)}.")

# Function to roll dice (generate random results)
def roll_dice():
    return [random.choice(ANIMALS) for _ in range(3)]

# Simulate the game
def play_game():
    print("Welcome to Bầu Cua Bet88!")
    
    # Step 1: Get user's bet amount
    bet_amount = get_valid_bet()
    
    # Step 2: Get user's chosen animal
    chosen_animal = get_valid_animal()
    
    # Step 3: Roll the dice
    print("\nRolling the dice...")
    rolled_animals = roll_dice()
    print(f"The dice rolled: {', '.join(rolled_animals)}")
    
    # Step 4: Calculate winnings
    winning_count = rolled_animals.count(chosen_animal)
    if winning_count > 0:
        winnings = bet_amount * winning_count
        print(f"Congratulations! Your chosen animal '{chosen_animal}' appeared {winning_count} time(s).")
        print(f"You win ${winnings}!")
    else:
        print(f"Sorry, your chosen animal '{chosen_animal}' did not appear. You lose ${bet_amount}.")
    
    # Step 5: Ask if user wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_game()
    else:
        print("Thank you for playing! Goodbye.")

# Entry point of the script
if __name__ == "__main__":
    play_game()
```

This Python code implements a simple betting game where users can choose animals, place bets, and win based on dice rolls. The code includes input validation, error handling, and adheres to production-ready principles.
