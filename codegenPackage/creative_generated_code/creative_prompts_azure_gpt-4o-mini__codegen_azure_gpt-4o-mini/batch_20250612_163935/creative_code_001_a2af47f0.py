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
def calculate_jackpot_winnings(game_type: str, bet_amount: float) -> float:
    """
    Calculate potential jackpot winnings based on the type of togel game and the bet amount.

    Parameters:
    game_type (str): The type of togel game ('2D', '3D', '4D').
    bet_amount (float): The amount of money being bet.

    Returns:
    float: The potential winnings.

    Raises:
    ValueError: If an invalid game type is provided.
    ValueError: If the bet amount is not a positive number.
    """
    
    # Validate the bet amount
    if bet_amount <= 0:
        raise ValueError("Bet amount must be a positive number.")

    # Define payout multipliers for each game type
    payout_multipliers = {
        '2D': 70,  # Example payout multiplier for 2D
        '3D': 500, # Example payout multiplier for 3D
        '4D': 2500 # Example payout multiplier for 4D
    }

    # Check if the game type is valid
    if game_type not in payout_multipliers:
        raise ValueError("Invalid game type. Please choose '2D', '3D', or '4D'.")

    # Calculate potential winnings
    winnings = bet_amount * payout_multipliers[game_type]

    return winnings

# Example usage:
if __name__ == "__main__":
    try:
        game_type = '3D'  # Can be '2D', '3D', or '4D'
        bet_amount = 10.0  # Example bet amount
        winnings = calculate_jackpot_winnings(game_type, bet_amount)
        print(f"Potential winnings for {game_type} with a bet of {bet_amount} is: {winnings}")
    except ValueError as e:
        print(f"Error: {e}")
```
