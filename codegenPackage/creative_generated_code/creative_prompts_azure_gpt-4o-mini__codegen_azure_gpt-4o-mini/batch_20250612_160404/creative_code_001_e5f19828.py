"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xchangelite.com
Prompt: Write a Python function to calculate potential winnings from a no deposit bonus in a casino, similar to the examples provided on Xchange Elite.
Generated: DETERMINISTIC_e5f1982801c2bbf0
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_potential_winnings(bonus_amount: float, wagering_requirements: int, payout_percentage: float) -> float:
    """
    Calculate the potential winnings from a no deposit bonus in a casino.

    Parameters:
    bonus_amount (float): The amount of the no deposit bonus.
    wagering_requirements (int): The multiplier for the wagering requirements (e.g., 20 means wager 20x bonus).
    payout_percentage (float): The percentage of the total wagered amount that can be won (in decimal form, e.g., 0.8 for 80%).

    Returns:
    float: The potential winnings calculated from the bonus.
    
    Raises:
    ValueError: If any input parameter is invalid (negative values or zero).
    """
    
    # Validate inputs
    if bonus_amount <= 0:
        raise ValueError("Bonus amount must be greater than zero.")
    if wagering_requirements <= 0:
        raise ValueError("Wagering requirements must be greater than zero.")
    if not (0 <= payout_percentage <= 1):
        raise ValueError("Payout percentage must be between 0 and 1.")

    # Calculate total amount that needs to be wagered
    total_wagered = bonus_amount * wagering_requirements
    
    # Calculate potential winnings
    potential_winnings = total_wagered * payout_percentage
    
    return potential_winnings

# Example usage (uncomment to test):
# try:
#     winnings = calculate_potential_winnings(100, 20, 0.8)
#     print(f"Potential Winnings: ${winnings:.2f}")
# except ValueError as e:
#     print(f"Error: {e}")
```
