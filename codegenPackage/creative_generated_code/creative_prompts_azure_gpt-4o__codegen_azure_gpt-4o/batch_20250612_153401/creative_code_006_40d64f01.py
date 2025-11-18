"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gemcaster.vercel.app
Prompt: Create a function to calculate the total Zora fees in ETH for collecting multiple casts on Gemcaster.
Generated: DETERMINISTIC_40d64f01c2444136
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List, Union

def calculate_zora_fees(cast_prices_eth: List[Union[int, float]], zora_fee_percentage: float = 0.025) -> float:
    """
    Calculate the total Zora fees in ETH for collecting multiple casts.

    Parameters:
        cast_prices_eth (List[Union[int, float]]): A list of cast prices in ETH.
        zora_fee_percentage (float): The fee percentage charged by Zora. Default is 2.5% (0.025).

    Returns:
        float: The total Zora fees in ETH.
    """
    
    # Validate inputs
    if not cast_prices_eth:
        raise ValueError("The cast_prices_eth list cannot be empty.")
    
    if not isinstance(zora_fee_percentage, (int, float)) or zora_fee_percentage < 0:
        raise ValueError("Invalid zora_fee_percentage. It must be a non-negative number.")
    
    # Calculate total fee by applying the Zora fee percentage to each cast price
    total_zora_fees = sum(price * zora_fee_percentage for price in cast_prices_eth)
    
    return total_zora_fees

# Example usage:
# cast_prices_eth = [0.1, 0.2, 0.5]  # Cast prices in ETH
# total_fees = calculate_zora_fees(cast_prices_eth)
# print(f"Total Zora fees in ETH: {total_fees}")
```
