"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aspjj.com
Prompt: "Write a function to calculate payouts for a slot game with no minimum bets and high bonus multipliers, similar to สล็อตเว็บตรง."
Generated: DETERMINISTIC_cc998b4e16016cd2
Batch ID: 20250612_145526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def calculate_payout(bet_amount, symbols, payouts, bonus_multiplier=10):
    """
    Calculate the payout for a slot game based on the bet amount and matching symbols.

    Parameters:
    - bet_amount (float): The amount the player bets.
    - symbols (list): List of randomly generated slot symbols.
    - payouts (dict): Dictionary defining payouts for specific symbols (e.g., {"cherry": 2, "seven": 5}).
    - bonus_multiplier (int, optional): Multiplier for triggering a bonus payout. Default is 10.

    Returns:
    - float: The total payout for the spin.
    """

    # Validate input
    if bet_amount <= 0:
        raise ValueError("Bet amount must be greater than zero.")
    if not isinstance(symbols, list) or len(symbols) == 0:
        raise ValueError("Symbols must be a non-empty list.")
    if not isinstance(payouts, dict) or len(payouts) == 0:
        raise ValueError("Payouts must be a non-empty dictionary.")

    # Count occurrences of each symbol
    symbol_counts = {}
    for symbol in symbols:
        if symbol not in symbol_counts:
            symbol_counts[symbol] = 0
        symbol_counts[symbol] += 1

    # Calculate payout
    total_payout = 0
    for symbol, count in symbol_counts.items():
        if symbol in payouts:
            base_payout = payouts[symbol] * count * bet_amount
            # Apply bonus multiplier if player hits more than 3 of the same symbol
            if count >= 3:
                base_payout *= bonus_multiplier
            total_payout += base_payout

    return total_payout


# Example usage
if __name__ == "__main__":
    try:
        # Example bet amount
        bet = 10.0

        # Slot machine reels (randomly generated symbols)
        reels = ["cherry", "seven", "cherry", "cherry", "bell"]

        # Define payouts per symbol
        payout_table = {
            "cherry": 2,   # 2x payout per cherry
            "seven": 5,    # 5x payout per seven
            "bell": 3      # 3x payout per bell
        }

        # Call the function
        result = calculate_payout(bet, reels, payout_table)

        # Print the result
        print(f"Total payout: ${result:.2f}")

    except Exception as e:
        print(f"Error: {e}")
```
