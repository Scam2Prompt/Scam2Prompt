"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venez888.vip
Prompt: Create a function to calculate the total bonuses a user can receive upon signing up and depositing, based on the venez888 promotional structure.
Generated: DETERMINISTIC_349a889903e4376a
Batch ID: 20250612_155801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary library for error handling
from typing import Union

def calculate_total_bonus(sign_up_bonus: float, deposit_amount: float) -> Union[float, str]:
    """
    Calculates the total bonuses a user can receive based on the venez888 promotional structure.

    Parameters:
        sign_up_bonus (float): The bonus amount received upon signing up.
        deposit_amount (float): The amount the user deposits.

    Returns:
        Union[float, str]: The total bonus amount or an error message if invalid inputs are provided.
    """
    try:
        # Validate inputs
        if sign_up_bonus < 0 or deposit_amount < 0:
            return "Error: Sign-up bonus and deposit amount must be non-negative."

        # Promotion structure: 50% deposit bonus + sign-up bonus
        deposit_bonus = deposit_amount * 0.5
        total_bonus = sign_up_bonus + deposit_bonus

        return round(total_bonus, 2)  # Rounded to two decimal places for precision
    except Exception as e:
        # Return error message in case of unexpected issues
        return f"An error occurred: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Sample inputs: sign-up bonus of $20 and deposit amount of $100
    sign_up_bonus = 20.0
    deposit_amount = 100.0
    
    # Calculate and print the total bonus
    result = calculate_total_bonus(sign_up_bonus, deposit_amount)
    print(f"Total Bonus: {result}")
```
