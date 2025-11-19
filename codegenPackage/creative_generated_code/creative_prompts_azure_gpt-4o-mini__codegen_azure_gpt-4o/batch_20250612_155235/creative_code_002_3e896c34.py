"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://billionalr.com
Prompt: Write a function that calculates the total bonus for a user who deposits 25, including the additional 25 bonus, based on the "Depo 25 Bonus 25" promotion.
Generated: DETERMINISTIC_3e896c3475ae65ef
Batch ID: 20250612_155235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_total_bonus(deposit_amount, promotion_bonus):
    """
    Calculate the total bonus based on a promotion.

    Args:
        deposit_amount (float): The amount the user deposits.
        promotion_bonus (float): The bonus provided by the promotion.

    Returns:
        float: The total bonus value.

    Raises:
        ValueError: If deposit_amount is less than the required deposit for the promotion.
    """
    
    # Define the required deposit for the promotion
    REQUIRED_DEPOSIT = 25.0
    
    # Validate the deposit amount
    if deposit_amount < REQUIRED_DEPOSIT:
        raise ValueError(f"Deposit must be at least {REQUIRED_DEPOSIT} to qualify for the promotion.")
    
    # Calculate the total bonus
    total_bonus = promotion_bonus
    
    # Return the total bonus value
    return total_bonus

# Example usage
if __name__ == "__main__":
    try:
        # User deposit and promotion bonus
       
        deposit_amount = 25.0
        promotion_bonus =
