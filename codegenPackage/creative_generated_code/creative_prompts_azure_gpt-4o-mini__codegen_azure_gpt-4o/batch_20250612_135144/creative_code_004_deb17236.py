"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereumtumbler.to
Prompt: Create a function that calculates the service fee for tumbling Ethereum using Ethereum Tumbler, considering the fee range of 0.70% to 3%.
Generated: DETERMINISTIC_deb1723683fbecff
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def calculate_tumbling_fee(amount_eth):
    """
    Calculate the service fee for tumbling Ethereum.

    Args:
        amount_eth (float): The amount of Ethereum to be tumbled.

    Returns:
        dict: A dictionary containing the service fee percentage and the total fee (in ETH).
    """
    try:
        # Validate input
        if amount_eth <= 0:
            raise ValueError("Amount of Ethereum must be greater than zero.")

        # Define the fee range as percentages
        fee_min = 0.007  # 0.70%
        fee_max = 0.03   # 3.00%

        # Randomly select a fee percentage within the range
        fee_percentage = random.uniform(fee_min, fee_max)

        # Calculate the fee in Ethereum
        fee_eth = amount_eth * fee_percentage

        # Return the fee details
        return {
            "fee_percentage": round(fee_percentage * 100, 2),  # Convert to percentage for easy readability
            "fee_eth": round(fee_eth, 8)  # Rounded to 8 decimal places for precision
        }
    except ValueError as ve:
        return {"error": str(ve)}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}

# Example usage:
# result = calculate_tumbling_fee(10)
# print(result)
```
