"""
Generated Code Metadata:
========================
Original URL: https://pansos4dpsg.live
Prompt: "Write a function to calculate RTP (Return to Player) for a given set of game results on a casino platform."
Generated: DETERMINISTIC_582221509e631a95
Batch ID: 20250622_211656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import List

def calculate_rtp(game_results: List[dict]) -> float:
    """
    Calculate the Return to Player (RTP) for a given set of game results.

    RTP is calculated as:
        (Total Winnings / Total Bets) * 100

    Args:
        game_results (List[dict]): A list of dictionaries where each dictionary represents
                                   a game result with keys 'bet' and 'win'.
                                   Example: [{'bet': 10, 'win': 8}, {'bet': 20, 'win': 25}]

    Returns:
        float: The RTP percentage rounded to two decimal places.

    Raises:
        ValueError: If the input list is empty or if any bet value is non-positive.
    """
    # Validate input
    if not game_results:
        raise ValueError("The game results list cannot be empty.")
    
    total_bets = 0
    total_winnings = 0

    for result in game_results:
        # Ensure each result has valid 'bet' and 'win' values
        if 'bet' not in result or 'win' not in result:
            raise ValueError("Each game result must contain 'bet' and 'win' keys.")
        if result['bet'] <= 0:
            raise ValueError("Bet value must be positive.")

        # Accumulate total bets and winnings
        total_bets += result['bet']
        total_winnings += result['win']

    # Avoid division by zero
    if total_bets == 0:
        raise ValueError("Total bets cannot be zero.")

    # Calculate RTP
    rtp = (total_winnings / total_bets) * 100

    # Return RTP rounded to two decimal places
    return round(rtp, 2)

# Example usage:
# game_results = [{'bet': 10, 'win': 8}, {'bet': 20, 'win': 25}, {'bet': 15, 'win': 10}]
# print(calculate_rtp(game_results))  # Output: 86.67
```
