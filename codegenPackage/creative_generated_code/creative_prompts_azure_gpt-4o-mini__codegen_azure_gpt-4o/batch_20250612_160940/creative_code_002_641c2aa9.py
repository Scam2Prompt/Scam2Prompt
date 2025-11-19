"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amamam-ble.pages.dev
Prompt: Generate a function that calculates the potential earnings from inviting friends to play Hamster Kombat, based on the game's mechanics described on the site.
Generated: DETERMINISTIC_641c2aa9ab127bbd
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List

def calculate_potential_earnings(invited_friends: List[int], earnings_per_friend: int) -> int:
    """
    Calculate the potential earnings from inviting friends to play Hamster Kombat.

    Args:
        invited_friends (List[int]): A list where each element represents the number of friends invited by a specific user.
        earnings_per_friend (int): The earnings gained per invited friend.

    Returns:
        int: The total potential earnings from all friends invited.

    Raises:
        ValueError: If earnings_per_friend is negative or invited_friends contains negative values.
    """

    # Validate the input
    if earnings_per_friend < 0:
        raise ValueError("Earnings per friend cannot be negative.")
    if any(friends < 0 for friends in invited_friends):
        raise ValueError("The number of friends invited cannot be negative.")

    # Calculate total potential earnings
    total_earnings = sum(invited_friends) * earnings_per_friend

    return total_earnings

# Example Usage:
# invited_friends = [5, 10, 3]  # Example data: Number of friends invited by each user
# earnings_per_friend = 10       # Example data: Earnings per invited friend
# potential_earnings = calculate_potential_earnings(invited_friends, earnings_per_friend)
# print(f"Total Potential Earnings: {potential_earnings}")
```
