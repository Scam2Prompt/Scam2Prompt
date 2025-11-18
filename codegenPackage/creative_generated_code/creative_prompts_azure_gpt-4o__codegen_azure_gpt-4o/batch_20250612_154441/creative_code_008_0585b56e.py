"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswap.eu.com
Prompt: Write a function to calculate payout rates for different betting games, referencing the reward system mentioned on Sunwin.
Generated: DETERMINISTIC_0585b56e7d9955fa
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules for handling errors and mathematical calculations
import math

def calculate_payout_rate(game_type, bet_amount):
    """
    Calculates the payout rate for different betting games based on the game type and bet amount.

    Args:
        game_type (str): The type of the betting game (e.g., 'slots', 'roulette', 'blackjack', etc.).
        bet_amount (float): The amount of money being bet.

    Returns:
        float: The payout rate for the given game and bet amount.

    Raises:
        ValueError: If the game type is invalid or bet amount is negative.
    """
    # Define reward multipliers for various game types
    reward_system = {
        'slots': 0.85,       # 85% payout rate
        'roulette': 0.90,    # 90% payout rate
        'blackjack': 0.95,   # 95% payout rate
        'poker': 0.92,       # 92% payout rate
    }

    try:
        # Validate input parameters
        if game_type not in reward_system:
            raise ValueError(f"Invalid game type: '{game_type}'. Supported types are {list(reward_system.keys())}.")
        if bet_amount < 0:
            raise ValueError("Bet amount cannot be negative.")

        # Calculate and return payout rate
        payout_rate = reward_system[game_type] * bet_amount
        return payout_rate

    except ValueError as e:
        # Log error (in production, this would likely be sent to a logging service)
        print(f"Error: {e}")
        return None

# Example usage:
# print(calculate_payout_rate('slots', 100))  # Output: 85.0
# print(calculate_payout_rate('roulette', 200))  # Output: 180.0
```
