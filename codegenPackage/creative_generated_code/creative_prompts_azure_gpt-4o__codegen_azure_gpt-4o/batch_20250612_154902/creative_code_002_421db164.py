"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://levva.net
Prompt: Create a function to calculate yield optimization for $LVVA token staking on Levva, incorporating bonus percentages for lock-up periods of 1, 6, and 12 months.
Generated: DETERMINISTIC_421db164513ec6ee
Batch ID: 20250612_154902
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

# Define the function to calculate yield optimization
def calculate_yield_optimization(initial_stake: float, annual_percentage_yield: float, lockup_period_months: int) -> Union[float, str]:
    """
    Calculate yield optimization for $LVVA token staking based on lock-up periods.
    
    Args:
        initial_stake (float): The amount of tokens initially staked.
        annual_percentage_yield (float): The annual percentage yield as a percentage (e.g., 10 for 10% APY).
        lockup_period_months (int): The lock-up period in months (1, 6, or 12).
        
    Returns:
        Union[float, str]: The total yield after the lock-up period, including bonuses, or error message if inputs are invalid.
    """
    
    # Validate inputs
    if initial_stake <= 0:
        return "Error: Initial stake must be greater than 0."
    if annual_percentage_yield <= 0:
        return "Error: APY must be greater than 0."
    if lockup_period_months not in [1, 6, 12]:
        return "Error: Lock-up period must be 1, 6, or 12 months."
    
    # Define bonus percentages for lock-up periods
    bonus_percentage = {
        1: 2,   # 2% bonus for 1 month lock-up
        6: 10,  # 10% bonus for 6 months lock-up
        12: 25  # 25% bonus for 12 months lock-up
    }
    
    # Calculate the base yield (APY calculation assumes full-year staking)
    monthly_yield = (annual_percentage_yield / 100) / 12
    base_yield = initial_stake * monthly_yield * lockup_period_months
    
    # Apply the lock-up bonus
    bonus_multiplier = bonus_percentage[lockup_period_months] / 100
    total_yield = base_yield * (1 + bonus_multiplier)
    
    return total_yield

# Example usage:
# initial_stake = 1000 (tokens), APY = 15%, lock-up = 6 months
# total_yield = calculate_yield_optimization(1000, 15, 6)
# print(f"Total yield after 6 months: {total_yield:.2f} tokens")
```
