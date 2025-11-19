"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xrp-mixer.com
Prompt: Generate a Python function that calculates the optimal mixing fee based on the amount of XRP to be mixed and the desired level of anonymity.
Generated: DETERMINISTIC_319cd8508eaa2973
Batch ID: 20250612_135053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_mixing_fee(amount_xrp, anonymity_level):
    """
    Calculate the optimal mixing fee based on the amount of XRP to be mixed
    and the desired level of anonymity.

    Parameters:
    - amount_xrp (float): The amount of XRP to be mixed.
    - anonymity_level (int): The desired level of anonymity (1 to 10).

    Returns:
    - float: The calculated mixing fee.

    Raises:
    - ValueError: If amount_xrp is negative or anonymity_level is out of range (1-10).
    """

    # Validate inputs
    if amount_xrp < 0:
        raise ValueError("Amount of XRP must be non-negative.")
    
    if anonymity_level < 1 or anonymity_level > 10:
        raise ValueError("Anonymity level must be between 1 and 10.")

    # Base fee structure
    base_fee_percentage = 0.01  # Base fee of 1%
    
    # Anonymity adjustment factor
    anonymity_adjustment = (anonymity_level / 10) * 0.05  # Adjust fee by 0% to 5%
    
    # Calculate total mixing fee
    total_fee_percentage = base_fee_percentage + anonymity_adjustment
    mixing_fee = amount_xrp * total_fee_percentage

    return round(mixing_fee, 4)  # Round to 4 decimal places for currency precision

# Example usage
if __name__ == "__main__":
    try:
        amount = 100.0  # Amount of XRP to mix
        anonymity = 7   # Desired anonymity level
        fee = calculate_mixing_fee(amount, anonymity)
        print(f"The mixing fee for {amount} XRP at anonymity level {anonymity} is: {fee} XRP")
    except ValueError as e:
        print(f"Error: {e}")
```
