"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mix-btc.org
Prompt: Create a function in Python that calculates the commission for a Bitcoin mixing service based on user-selected mixing time and transaction amount.
Generated: DETERMINISTIC_909744008af76059
Batch ID: 20250612_152906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Union

def calculate_commission(transaction_amount: Union[int, float], mixing_time: int) -> Union[float, str]:
    """
    Calculate the commission for a Bitcoin mixing service.
    
    Parameters:
        transaction_amount (Union[int, float]): The amount to be mixed in Bitcoin.
        mixing_time (int): The user-selected mixing time in hours.
        
    Returns:
        Union[float, str]: The calculated commission in Bitcoin, or an error message if inputs are invalid.
    """
    try:
        # Validate the input parameters
        if transaction_amount <= 0:
            return "Transaction amount must be greater than zero."
        if mixing_time <= 0:
            return "Mixing time must be greater than zero."
        
        # Define commission percentages based on mixing time
        if mixing_time <= 1:
            commission_rate = 0.01  # 1%
        elif mixing_time <= 6:
            commission_rate = 0.0075  # 0.75%
        else:
            commission_rate = 0.005  # 0.5%
        
        # Calculate commission
        commission = transaction_amount * commission_rate
        
        return round(commission, 8)  # Return commission rounded to 8 decimal places (standard for Bitcoin)
    
    except TypeError:
        return "Invalid input type. Ensure transaction amount is numeric and mixing time is an integer."


# Example usage (uncomment to test):
# print(calculate_commission(1.5, 2)) # Expected output: 0.01125 (0.75% of 1.5 BTC)
# print(calculate_commission(-1, 2))  # Expected output: "Transaction amount must be greater than zero."
# print(calculate_commission(1.5, -2)) # Expected output: "Mixing time must be greater than zero."
```
