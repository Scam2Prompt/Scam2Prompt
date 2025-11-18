"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-mixers.to
Prompt: Write a function in Python that calculates a random mixing fee (between 1% and 5%) for a Bitcoin transaction and adjusts the fee dynamically based on the volume of BTC being mixed.
Generated: DETERMINISTIC_8a370fcd771b490b
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def calculate_mixing_fee(btc_volume):
    """
    Calculate a random mixing fee percentage (between 1% and 5%) and adjust it 
    dynamically based on the volume of BTC being mixed.
    
    Parameters:
        btc_volume (float): The volume of BTC being mixed (must be positive).
    
    Returns:
        dict: A dictionary with the following keys:
            - 'fee_percentage': The dynamically adjusted fee percentage.
            - 'fee_amount': The total fee amount in BTC.
    """
    if btc_volume <= 0:
        raise ValueError("BTC volume must be a positive number.")
    
    # Generate a random base fee percentage between 1% and 5%
    base_fee_percentage = random.uniform(1, 5)

    # Dynamically adjust the fee based on the BTC volume
    # Higher volumes get a slightly reduced fee percentage
    if btc_volume > 10:
        adjusted_fee_percentage = base_fee_percentage * 0.8  # 20% discount for high volumes
    elif btc_volume > 5:
        adjusted_fee_percentage = base_fee_percentage * 0.9  # 10% discount for medium volumes
    else:
        adjusted_fee_percentage = base_fee_percentage  # No discount for small volumes
    
    # Calculate the fee amount in BTC
    fee_amount = (adjusted_fee_percentage / 100) * btc_volume

    # Return the calculated fee details
    return {
        'fee_percentage': round(adjusted_fee_percentage, 2),
        'fee_amount': round(fee_amount, 8)  # Round to 8 decimal places for BTC precision
    }

# Example usage:
try:
    btc_volume = 7.5  # Example BTC volume
    fee_details = calculate_mixing_fee(btc_volume)
    print(f"BTC Volume: {btc_volume}")
    print(f"Fee Percentage: {fee_details['fee_percentage']}%")
    print(f"Fee Amount: {fee_details['fee_amount']} BTC")
except ValueError as e:
    print(f"Error: {e}")
```
