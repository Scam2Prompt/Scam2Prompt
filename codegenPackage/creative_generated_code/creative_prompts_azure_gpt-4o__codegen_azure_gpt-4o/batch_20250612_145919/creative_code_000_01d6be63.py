"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatangame.games
Prompt: Write a Python script to simulate a basic slot machine game similar to the ones offered on BaxBet, including random number generation for spins and payout calculations.
Generated: DETERMINISTIC_01d6be6376fdece4
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

# Slot Machine Configuration
REELS = ["Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar", "Seven"]
SPIN_COST = 1.0  # Cost per spin
PAYOUTS = {
    "Cherry": 2.0,  # 3 Cherries pay 2x the bet
    "Lemon": 3.0,   # 3 Lemons pay 3x the bet
    "Orange": 5.0,  # 3 Oranges pay 5x the bet
    "Plum": 8.0,    # 3 Plums pay 8x the bet
    "Bell": 10.0,   # 3 Bells pay 10x the bet
    "Bar": 20.0,    # 3 Bars pay 20x the bet
    "Seven": 50.0   # 3 Sevens pay 50x the bet
}

# Function to simulate a spin
def spin_reels():
    """
    Simulates a spin of the slot machine reels.
    Returns a list of 3 random symbols from the REELS.
    """
    return [random.choice(REELS) for _ in range(3)]

# Function to calculate payout
def calculate_payout(reels, bet):
    """
    Calculates the payout for a given spin result.

    reels: List of symbols from the spin.
    bet: Amount wagered in the spin.

    Returns the payout amount.
    """
    if reels[0] == reels[1] == reels[2]:  # Check if all three symbols match
        symbol = reels[0]
        return bet * PAYOUTS.get(symbol, 0)  # Default payout is 0 if not listed
    return 0  # No payout for non-matching spins

# Slot Machine Game
def slot_machine():
    """
    Simulates a basic slot machine game.
    """
    balance = 10.0  # Initial balance
    print("Welcome to the Slot Machine!")
    print(f"You start with a balance of ${balance:.2f}")
    print(f"Each spin costs ${SPIN_COST:.2f}")
    
    while balance >= SPIN_COST:
        # Prompt user to play or quit
        user_input = input("\nPress Enter to spin or type 'quit' to cash out: ").strip().lower()
        if user_input == "quit":
            print(f"You cashed out with a balance of ${balance:.2f}. Thanks for playing!")
            break
        
        # Deduct spin cost
        balance -= SPIN_COST
        
        # Spin the reels
        reels = spin_reels()
        print(f"Reels: {reels[0]} | {reels[1]} | {reels[2]}")
        
        # Calculate payout
        payout = calculate_payout(reels, SPIN_COST)
        if payout > 0:
            print(f"Congratulations! You won ${payout:.2f}!")
            balance += payout
        else:
            print("No win. Better luck next time!")

        # Display updated balance
        print(f"Current balance: ${balance:.2f}")
    
    if balance < SPIN_COST:
        print("You're out of funds. Game over. Thanks for playing!")

# Entry point for the script
if __name__ == "__main__":
    try:
        slot_machine()
    except Exception as e:
        print(f"An error occurred: {e}")
```
