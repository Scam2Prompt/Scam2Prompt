"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scapemania-0x2eca5.pages.dev
Prompt: Develop a function that calculates the bonus percentage for referrals based on the purchase amount of $MANIA tokens, using the tiered bonus system (5% to 15%).
Generated: DETERMINISTIC_d871ecb64d080501
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_bonus_percentage(purchase_amount: float) -> float:
    """
    Calculate the bonus percentage for referrals based on the purchase amount of $MANIA tokens.
    
    Bonus Tiers:
    - $0 - $999.99: 5%
    - $1000 - $4999.99: 10%
    - $5000 and above: 15%

    Args:
        purchase_amount (float): The amount of $MANIA tokens purchased.

    Returns:
        float: The bonus percentage corresponding to the purchase amount.

    Raises:
        ValueError: If purchase_amount is negative.
    """
    
    # Validate the input
    if purchase_amount < 0:
        raise ValueError("Purchase amount cannot be negative.")

    # Determine the bonus percentage based on the purchase amount
    if purchase_amount < 1000:
        bonus_percentage = 0.05
    elif purchase_amount < 5000:
        bonus_percentage = 0.10
    else:
        bonus_percentage = 0.15

    return bonus_percentage

# Example usage:
if __name__ == "__main__":
    try:
        amount = float(input("Enter the purchase amount of $MANIA tokens: "))
        bonus = calculate_bonus_percentage(amount)
        print(f"The bonus percentage for a purchase of ${amount:.2f} is {bonus * 100:.2f}%.")
    except ValueError as e:
        print(f"Error: {e}")
```
