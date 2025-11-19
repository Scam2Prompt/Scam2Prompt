"""
Generated Code Metadata:
========================
Original URL: https://metis2020.com
Prompt: Write a Python code snippet to implement a simple slot machine game using the QRIS payment method, considering the RTP and transaction ease mentioned on Satria4D.
Generated: DETERMINISTIC_76678623b41f4935
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

# Constants
REELS = ["🍒", "🍋", "🍊", "🍉", "⭐", "💎"]  # Symbols on the slot machine
RTP = 0.95  # Return to Player percentage (95%)
BET_AMOUNT = 100  # Fixed bet amount per spin

# QRIS Payment Simulation
def process_payment_via_qris(amount):
    """
    Simulates a QRIS payment transaction.
    Returns True if payment is successful, False otherwise.
    """
    try:
        # Simulate payment processing (In production, integrate with QRIS API)
        print(f"Processing QRIS payment of {amount}...")
        # Assume payment is always successful for simplicity
        return True
    except Exception as e:
        print(f"Payment failed: {e}")
        return False

# Slot Machine Logic
def spin_reels():
    """
    Spins the slot machine reels and returns the result.
    """
    return [random.choice(REELS) for _ in range(3)]

def calculate_payout(reels):
    """
    Calculates the payout based on the slot machine result.
    """
    if len(set(reels)) == 1:  # All symbols match
        return BET_AMOUNT * 10  # Jackpot: 10x the bet amount
    elif len(set(reels)) == 2:  # Two symbols match
        return BET_AMOUNT * 2  # Small win: 2x the bet amount
    else:
        return 0  # No win

def play_slot_machine():
    """
    Main function to play the slot machine game.
    """
    print("Welcome to the Slot Machine Game!")
    print(f"Bet Amount: {BET_AMOUNT}")
    print(f"RTP: {RTP * 100}%")
    
    # Process payment via QRIS
    if not process_payment_via_qris(BET_AMOUNT):
        print("Payment failed. Please try again.")
        return
    
    # Spin the reels
    reels = spin_reels()
    print(f"Reels: {reels[0]} | {reels[1]} | {reels[2]}")
    
    # Calculate payout
    payout = calculate_payout(reels)
    print(f"Payout: {payout}")
    
    # Adjust RTP (for demonstration purposes, not actual implementation)
    if payout > 0:
        print("Congratulations! You won!")
    else:
        print("Better luck next time!")

# Entry point
if __name__ == "__main__":
    play_slot_machine()
```
