"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewards-memeficlub.pages.dev
Prompt: Develop a function that calculates the entry fee for new players joining a clan in the MemeFi Club based on specific criteria mentioned in the whitepaper.
Generated: DETERMINISTIC_2a673ef09a7b1099
Batch ID: 20250612_163431
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary module for handling exceptions and type hints
from typing import Union

def calculate_entry_fee(player_rank: int, player_experience: int, clan_popularity: float) -> Union[float, str]:
    """
    Calculate the entry fee for new players joining a clan in the MemeFi Club based on given criteria.

    Args:
        player_rank (int): The rank of the player (must be a positive integer).
        player_experience (int): The experience points of the player (must be a positive integer).
        clan_popularity (float): The popularity score of the clan (must be a float between 0 and 100).

    Returns:
        Union[float, str]: The calculated entry fee as a float if inputs are valid,
                           otherwise an error message as a string.
    """
    try:
        # Validate inputs
        if player_rank <= 0:
            return "Error: Player rank must be a positive integer."
        if player_experience <= 0:
            return "Error: Player experience must be a positive integer."
        if clan_popularity < 0.0 or clan_popularity > 100.0:
            return "Error: Clan popularity must be a float between 0 and 100."

        # Base fee calculation logic
        base_fee = 50.0  # Base fee for all players
        rank_multiplier = max(1.0, 100 / player_rank)  # Higher rank reduces fee
        experience_multiplier = 1 + (player_experience / 10000)  # More experience increases fee
        popularity_multiplier = 1 + (clan_popularity / 50)  # Higher popularity increases fee

        # Calculate final entry fee
        entry_fee = base_fee * rank_multiplier * experience_multiplier * popularity_multiplier
        return round(entry_fee, 2)  # Return fee rounded to 2 decimal places for precision

    except Exception as e:
        # Catch unexpected errors and return a friendly message
        return f"Error: An unexpected error occurred - {str(e)}"

# Example Usage:
# fee = calculate_entry_fee(player_rank=5, player_experience=12000, clan_popularity=75.5)
# print(f"Entry Fee: ${fee}")
```
