"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://securespend.io
Prompt: Write a function that calculates the potential jackpot winnings based on the type of togel game (2D, 3D, 4D) and the bet amount.
Generated: DETERMINISTIC_a2af47f0465b8728
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_jackpot(game_type, bet_amount):
    """
    Calculates the potential jackpot winnings for a given togel game type and bet amount.

    Parameters:
        game_type (str): Type of togel game ("2D", "3D", "4D").
        bet_amount (float): Amount of money bet by the player.

    Returns:
        float: Potential jackpot winnings.
    Raises:
        ValueError: If an invalid game type is provided or bet amount is negative.
    """
    # Define multipliers for each game type
    jackpot_multipliers = {
        "2D": 100,  # Example: For 2D, winnings = bet_amount * 100
        "3D": 1000, # Example: For 3D, winnings = bet_amount * 1000
        "4D": 10000 # Example: For 4D, winnings = bet_amount * 10000
    }
    
    # Validate input
    if game_type not in jackpot_multipliers:
        raise ValueError(f"Invalid game type '{game_type}'. Valid game types are: {', '.join(jackpot_multipliers.keys())}")
    
    if bet_amount < 0:
        raise ValueError("Bet amount cannot be negative.")

    # Calculate the jackpot winnings
    multiplier = jackpot_multipliers[game_type]
    jackpot = bet_amount * multiplier

    return jackpot


# Example usage:
try:
    game_type = "3D"
    bet_amount = 50
    winnings = calculate_jackpot(game_type, bet_amount)
    print(f"Potential winnings for {game_type} with a bet of {bet_amount} is: {winnings}")
except ValueError as e:
    print(f"Error: {e}")
```
