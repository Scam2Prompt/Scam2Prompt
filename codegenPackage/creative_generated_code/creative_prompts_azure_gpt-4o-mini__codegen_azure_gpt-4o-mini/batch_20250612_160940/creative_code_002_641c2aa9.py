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
def calculate_potential_earnings(invites: int, earnings_per_friend: float, bonus_multiplier: float = 1.0) -> float:
    """
    Calculate the potential earnings from inviting friends to play Hamster Kombat.

    Args:
        invites (int): The number of friends invited to play.
        earnings_per_friend (float): The amount earned per invited friend.
        bonus_multiplier (float): An optional multiplier for additional earnings (default is 1.0).

    Returns:
        float: The total potential earnings from the invitations.

    Raises:
        ValueError: If the number of invites is negative or earnings per friend is negative.
    """
    # Validate inputs
    if invites < 0:
        raise ValueError("The number of invites cannot be negative.")
    if earnings_per_friend < 0:
        raise ValueError("Earnings per friend cannot be negative.")

    # Calculate total earnings
    total_earnings = invites * earnings_per_friend * bonus_multiplier
    return total_earnings


# Example usage
if __name__ == "__main__":
    try:
        total = calculate_potential_earnings(invites=5, earnings_per_friend=10.0, bonus_multiplier=1.5)
        print(f"Total potential earnings: ${total:.2f}")
    except ValueError as e:
        print(f"Error calculating earnings: {e}")
```
