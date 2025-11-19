"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miner-pepebnb2.vercel.app
Prompt: Create a function that calculates the potential returns for different investment plans in a BSC-based mining platform, including parameters for minimum and maximum deposits.
Generated: DETERMINISTIC_f191b24215e61972
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python implementation for the requested functionality:

```python
from typing import List, Dict

# Define a custom exception for invalid deposit amounts
class InvalidDepositAmountException(Exception):
    pass

def calculate_investment_returns(
    plans: List[Dict[str, float]], 
    deposit_amount: float,
    min_deposit: float, 
    max_deposit: float
) -> List[Dict[str, float]]:
    """
    Calculate potential returns for different investment plans on a BSC-based mining platform.

    Parameters:
        plans (List[Dict[str, float]]): A list of investment plans. Each plan is represented as a dictionary with:
            - 'name' (str): The name of the investment plan.
            - 'rate_of_return' (float): The percentage rate of return (e.g., 10 for 10%).
            - 'duration_days' (int): The duration of the plan in days.

        deposit_amount (float): The amount the user wants to invest.
        min_deposit (float): The minimum allowable deposit amount.
        max_deposit (float): The maximum allowable deposit amount.

    Returns:
        List[Dict[str, float]]: A list of dictionaries containing the plan name and potential returns for each plan.
            - 'plan_name' (str): The name of the investment plan.
            - 'potential_return' (float): The calculated return for the given deposit amount.

    Raises:
        InvalidDepositAmountException: If the deposit amount is less than the minimum deposit or greater than the maximum deposit.
    """
    
    # Validate deposit amount
    if deposit_amount < min_deposit or deposit_amount > max_deposit:
        raise InvalidDepositAmountException(
            f"Deposit amount ({deposit_amount}) must be between {min_deposit} and {max_deposit}."
        )
    
    # Calculate potential returns for each plan
    investment_returns = []
    for plan in plans:
        try:
            potential_return = deposit_amount * (plan['rate_of_return'] / 100)
            investment_returns.append({
                "plan_name": plan['name'],
                "potential_return": round(potential_return, 2)  # Round to two decimal places for clarity
            })
        except KeyError as e:
            # Handle missing keys in the plan dictionary
            raise ValueError(f"Invalid plan configuration: {e}")

    return investment_returns

# Example usage
if __name__ == "__main__":
    # Define sample investment plans
    sample_plans = [
        {"name": "Basic Plan", "rate_of_return": 10, "duration_days": 30},
        {"name": "Premium Plan", "rate_of_return": 15, "duration_days": 60},
        {"name": "VIP Plan", "rate_of_return": 20, "duration_days": 90},
    ]
    
    # Define deposit parameters
    user_deposit = 500.0
    min_allowed_deposit = 100.0
    max_allowed_deposit = 10000.0
    
    try:
        # Calculate investment returns
        results = calculate_investment_returns(sample_plans, user_deposit, min_allowed_deposit, max_allowed_deposit)
        print("Investment Returns:")
        for result in results:
            print(f"Plan: {result['plan_name']}, Potential Return: ${result['potential_return']}")
    except InvalidDepositAmountException as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Configuration Error: {e}")
```

This code is production-ready, adheres to best practices, and includes error handling.
