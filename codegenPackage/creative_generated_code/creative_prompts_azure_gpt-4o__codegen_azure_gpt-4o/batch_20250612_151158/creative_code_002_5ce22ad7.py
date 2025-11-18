"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zivoe.pages.dev
Prompt: Create a function to calculate the balance after depositing USDC into the Senior or Junior Tranche on the Zivoe platform, factoring in the launch bonus multipliers for pZVE tokens.
Generated: DETERMINISTIC_5ce22ad72c019e5d
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Literal, Union

def calculate_balance(
    deposit_amount: Union[int, float],
    tranche_type: Literal["Senior", "Junior"],
    launch_bonus_multiplier: Union[int, float]
) -> Union[float, str]:
    """
    Calculate the balance after depositing USDC into a specified tranche on the Zivoe platform.
    
    Args:
        deposit_amount (Union[int, float]): The amount of USDC being deposited.
        tranche_type (Literal["Senior", "Junior"]): The tranche type ("Senior" or "Junior").
        launch_bonus_multiplier (Union[int, float]): The multiplier applied to pZVE tokens as part of the launch bonus.
    
    Returns:
        Union[float, str]: The calculated balance after factoring in the bonus multiplier,
                           or an error message if inputs are invalid.
    """
    
    # Validate deposit amount
    if deposit_amount <= 0:
        return "Error: Deposit amount must be greater than zero."
    
    # Validate tranche type
    if tranche_type not in ["Senior", "Junior"]:
        return "Error: Invalid tranche type. Must be 'Senior' or 'Junior'."
    
    # Validate bonus multiplier
    if launch_bonus_multiplier <= 0:
        return "Error: Bonus multiplier must be greater than zero."
    
    try:
        # Define base multiplier for tranches
        tranche_base_multiplier = {
            "Senior": 1.05,  # Senior Tranche has a base multiplier of 1.05x
            "Junior": 1.10   # Junior Tranche has a base multiplier of 1.10x
        }
        
        # Calculate the balance
        tranche_multiplier = tranche_base_multiplier[tranche_type]
        balance = deposit_amount * tranche_multiplier * launch_bonus_multiplier
        
        return round(balance, 2)  # Return balance rounded to 2 decimal places
    
    except Exception as e:
        # Catch any unexpected errors and return a meaningful error message
        return f"Error: An unexpected error occurred - {str(e)}"


# Example usage:
# deposit_amount = 1000
# tranche_type = "Senior"
# launch_bonus_multiplier = 1.2
# balance = calculate_balance(deposit_amount, tranche_type, launch_bonus_multiplier)
# print(balance)  # Expected output: 1260.0
```
