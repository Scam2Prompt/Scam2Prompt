"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://todaythegames.com
Prompt: Write a Python script to simulate a virtual slot machine game similar to the "Super Wheel" described on todaythegames.com, including random spin outcomes and a leaderboard system.
Generated: DETERMINISTIC_a70409418d325653
Batch ID: 20250612_145203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json

# Constants
WHEEL_OPTIONS = ["Cherry", "Bell", "Seven", "Diamond", "Bar"]
PAYOUTS = {
    "Cherry": 10,
    "Bell": 20,
    "Seven": 50,
    "Diamond": 100,
    "Bar": 200
}
DEFAULT_CREDITS = 100

# File to store leaderboard data
LEADERBOARD_FILE = "leaderboard.json"

def spin_wheel():
    """
    Simulates spinning the wheel and returns the random outcome.
    """
    return random.choice(WHEEL_OPTIONS)

def calculate_payout(outcome, bet):
    """
    Calculates the payout based on the spin outcome and bet amount.
    """
    return PAYOUTS.get(outcome, 0) * bet

def load_leaderboard():
    """
    Loads the leaderboard from a file. Creates an empty leaderboard if the file doesn't exist.
    """
    try:
        with open(LEADERBOARD_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_leaderboard(leaderboard):
    """
    Saves the leaderboard to a file.
    """
    with open(LEADERBOARD_FILE, "w") as file:
        json.dump(leaderboard, file, indent=4)

def display_leaderboard(leaderboard):
    """
    Displays the leaderboard in a formatted manner.
    """
    print("\n--- Leaderboard ---")
    sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    for rank, (player, score) in enumerate(sorted_leaderboard, start=1):
        print(f"{rank}. {player}: {score} credits")
    print("--------------------\n")

def main():
    """
    Main function to simulate the slot machine game.
    """
    print("Welcome to the Virtual Slot Machine!")
    print("Spin the wheel and test your luck.")
    
    # Initialize leaderboard
    leaderboard = load_leaderboard()

    # Get player name
    player_name = input("Enter your name: ").strip()
    if not player_name:
        print("Invalid name. Exiting...")
        return

    # Initialize player credits
    player_credits = DEFAULT_CREDITS
    print(f"Hello, {player_name}! You start with {player_credits} credits.")
    
    while player_credits > 0:
        # Display current credits
        print(f"\nYour current credits: {player_credits}")
        
        # Get bet amount
        try:
            bet = int(input("Enter your bet amount (0 to quit): "))
            if bet == 0:
                print("Thanks for playing!")
                break
            if bet < 0 or bet > player_credits:
                print("Invalid bet amount. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
        
        # Spin the wheel
        outcome = spin_wheel()
        print(f"Wheel landed on: {outcome}")
        
        # Calculate winnings
        winnings = calculate_payout(outcome, bet)
        player_credits += winnings - bet
        print(f"You {'won' if winnings > 0 else 'lost'} {abs(winnings - bet)} credits.")
        
    # Update leaderboard
    leaderboard[player_name] = max(leaderboard.get(player_name, 0), player_credits)
    save_leaderboard(leaderboard)
    
    # Display final results
    print(f"\nGame over! Final credits: {player_credits}")
    display_leaderboard(leaderboard)

if __name__ == "__main__":
    main()
```
