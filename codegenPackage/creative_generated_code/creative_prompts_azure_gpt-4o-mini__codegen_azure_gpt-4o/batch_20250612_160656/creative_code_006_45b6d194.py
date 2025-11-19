"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seedify-cs6.pages.dev
Prompt: Create a function to calculate potential earnings from staking $SFUND on Seedify.
Generated: DETERMINISTIC_45b6d1940487c79f
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required modules
from typing import Union

def calculate_staking_earnings(initial_amount: Union[int, float], annual_percentage_yield: Union[int, float], staking_period_months: int) -> float:
    """
    Calculate potential earnings from staking SFUND.
    
    Parameters:
        initial_amount (int | float): The initial amount of SFUND staked.
        annual_percentage_yield (int | float): The annual percentage yield (APY) provided by Seedify.
        staking_period_months (int): The number of months the SFUND is staked for.
    
    Returns:
        float: The total earnings from staking SFUND.
    """
    try:
        # Input validation
        if initial_amount <= 0:
            raise ValueError("Initial amount must be greater than 0.")
        if annual_percentage_yield <= 0:
            raise ValueError("Annual percentage yield (APY) must be greater than 0.")
        if staking_period_months <= 0:
            raise ValueError("Staking period must be greater than 0.")
        
        # Convert APY to monthly yield (divide by 12)
        monthly_yield = annual_percentage_yield / 12 / 100
        
        # Compound earnings over the staking period
        total_amount = initial_amount * (1 + monthly_yield) ** staking_period_months
        
        # Calculate the earnings (total amount - initial amount)
        earnings = total_amount - initial_amount
        
        return round(earnings, 2)  # Return earnings rounded to 2 decimal places
    
    except ValueError as ve:
        # Handle value errors for invalid inputs
        print(f"ValueError: {ve}")
        return 0.0
    
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An error occurred: {e}")
        return 0.0

# Example usage:
# initial_amount = 1000 (SFUND)
# annual_percentage_yield = 12 (%) APY
# staking_period_months = 6
# print(calculate_staking_earnings(1000, 12, 6))
```
