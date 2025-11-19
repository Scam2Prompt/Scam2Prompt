"""
Generated Code Metadata:
========================
Original URL: https://amamam-ble.pages.dev
Prompt: Generate a function that calculates the potential earnings from inviting friends to play Hamster Kombat, based on the game's mechanics described on the site.
Generated: DETERMINISTIC_641c2aa9ab127bbd
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_potential_earnings(invites: int, earnings_per_invite: float, bonus_threshold: int, bonus_amount: float) -> float:
    """
    Calculate the potential earnings from inviting friends to play Hamster Kombat.

    Parameters:
    invites (int): The number of friends invited to play.
    earnings_per_invite (float): The amount earned for each friend invited.
    bonus_threshold (int): The number of invites required to qualify for a bonus.
    bonus_amount (float): The bonus amount earned if the threshold is met.

    Returns:
    float: The total potential earnings from invites.
    
    Raises:
    ValueError: If any of the input parameters are negative or if invites is not an integer.
    """
    
    # Input validation
    if not isinstance(invites, int) or invites < 0:
        raise ValueError("Invites must be a non-negative integer.")
    if earnings_per_invite < 0:
        raise ValueError("Earnings per invite must be a non-negative float.")
    if bonus_threshold < 0:
        raise ValueError("Bonus threshold must be a non-negative integer.")
    if bonus_amount < 0:
        raise ValueError("Bonus amount must be a non-negative float.")

    # Calculate base earnings from invites
    total_earnings = invites * earnings_per_invite

    # Check if the bonus applies
    if invites >= bonus_threshold:
        total_earnings += bonus_amount

    return total_earnings

# Example usage
if __name__ == "__main__":
    try:
        invites = 10
        earnings_per_invite = 5.0
        bonus_threshold = 5
        bonus_amount = 20.0
        
        potential_earnings = calculate_potential_earnings(invites, earnings_per_invite, bonus_threshold, bonus_amount)
        print(f"Potential earnings from inviting {invites} friends: ${potential_earnings:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
