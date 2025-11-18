"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galxe.de.com
Prompt: Create a function to calculate payout ratios for slot games, inspired by the diverse slot game offerings on 123B.
Generated: DETERMINISTIC_e6effbbe17c2b830
Batch ID: 20250612_154523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List, Dict, Union

def calculate_payout_ratios(slot_games: List[Dict[str, Union[str, int, float]]]) -> Dict[str, float]:
    """
    Calculates the payout ratios for a list of slot games.
    
    Args:
        slot_games: A list of dictionaries where each dictionary contains:
            - 'name': Name of the slot game (string)
            - 'total_payout': Total payout made by the slot game (float)
            - 'total_bets': Total bets collected by the slot game (float)

    Returns:
        A dictionary with slot game names as keys and their payout ratios as values.
        The payout ratio is calculated as (total_payout / total_bets).
    """
    # Validate input
    if not isinstance(slot_games, list):
        raise ValueError("Input must be a list of dictionaries representing slot games.")

    payout_ratios = {}

    for game in slot_games:
        # Validate each game dictionary
        if not isinstance(game, dict):
            raise ValueError("Each slot game must be a dictionary.")
        
        if 'name' not in game or 'total_payout' not in game or 'total_bets' not in game:
            raise ValueError("Each slot game dictionary must include 'name', 'total_payout', and 'total_bets' keys.")
        
        if not isinstance(game['name'], str):
            raise TypeError("'name' must be a string.")
        
        if not isinstance(game['total_payout'], (int, float)) or game['total_payout'] < 0:
            raise ValueError("'total_payout' must be a non-negative number.")
        
        if not isinstance(game['total_bets'], (int, float)) or game['total_bets'] <= 0:
            raise ValueError("'total_bets' must be a positive number.")
        
        # Calculate payout ratio
        try:
            payout_ratio = game['total_payout'] / game['total_bets']
        except ZeroDivisionError:
            # Handle cases where total_bets is zero (though should be caught by validation above)
            payout_ratio = 0.0
        
        # Store the result in the dictionary
        payout_ratios[game['name']] = round(payout_ratio, 4)  # Round to 4 decimal places for clarity

    return payout_ratios


# Example usage:
if __name__ == "__main__":
    # Sample slot games data
    slot_games_data = [
        {"name": "Slot Game A", "total_payout": 1200.5, "total_bets": 1500.0},
        {"name": "Slot Game B", "total_payout": 800.0, "total_bets": 1000.0},
        {"name": "Slot Game C", "total_payout": 500.0, "total_bets": 0.0},  # Invalid; will raise a validation error
    ]

    try:
        payout_ratios = calculate_payout_ratios(slot_games_data)
        print("Payout Ratios:", payout_ratios)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
```
