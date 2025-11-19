"""
Generated Code Metadata:
========================
Original URL: https://www.tntmytariff.com
Prompt: Write a Python script to simulate a simple slot machine game similar to those offered on SLOT777, with a focus on generating random outcomes for a 3-reel slot game.
Generated: DETERMINISTIC_c245c4e4db1e3593
Batch ID: 20250622_212338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

def spin_reels():
    """
    Simulates spinning the reels of a slot machine.
    Returns a list of three random symbols.
    """
    symbols = ['🍒', '🍋', '🍊', '⭐', '💎', '🔔', '🍇']
    return [random.choice(symbols) for _ in range(3)]

def calculate_payout(reels):
    """
    Calculates the payout based on the result of the reels.
    Returns the payout amount.
    """
    if len(set(reels)) == 1:  # All three symbols match
        return 100  # Jackpot payout
    elif len(set(reels)) == 2:  # Two symbols match
        return 10  # Small payout
    else:
        return 0  # No payout

def play_slot_machine():
    """
    Main function to simulate playing the slot machine.
    Handles user input and displays the results.
    """
    print("Welcome to the Slot Machine Game!")
    print("Press Enter to spin the reels or type 'quit' to exit.")
    
    while True:
        user_input = input("Your choice: ").strip().lower()
        if user_input == 'quit':
            print("Thank you for playing! Goodbye!")
            break
        
        # Spin the reels
        reels = spin_reels()
        print(f"Reels: {reels[0]} | {reels[1]} | {reels[2]}")
        
        # Calculate and display payout
        payout = calculate_payout(reels)
        if payout > 0:
            print(f"Congratulations! You won {payout} coins!")
        else:
            print("No payout this time. Better luck next spin!")
        print("-" * 30)

if __name__ == "__main__":
    try:
        play_slot_machine()
    except Exception as e:
        print(f"An error occurred: {e}")
```
