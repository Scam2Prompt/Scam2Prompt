"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimmints-4.vercel.app
Prompt: Create a function to calculate proportional gETH rewards based on Ethereum gas expenditure, following the gETH token architecture described on the webpage.
Generated: DETERMINISTIC_86d9d14db92b89d5
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Module: geth_rewards_calculator

This module provides a function to calculate proportional gETH rewards based on Ethereum gas expenditure.
The gETH token architecture assumes rewards are distributed proportional to the gas spent by users.
"""

def calculate_geth_rewards(user_gas_expenditure, total_gas_expenditure, total_rewards_pool):
    """
    Calculate proportional gETH rewards based on Ethereum gas expenditure.

    Parameters:
        user_gas_expenditure (float): The amount of Ethereum gas spent by the user.
        total_gas_expenditure (float): The total Ethereum gas expenditure in the system.
        total_rewards_pool (float): The total gETH rewards pool to be distributed.

    Returns:
        float: The calculated gETH rewards for the user.

    Raises:
        ValueError: If any of the inputs are negative or total_gas_expenditure is zero.
    """
    # Validate input parameters
    if user_gas_expenditure < 0:
        raise ValueError("User gas expenditure cannot be negative.")
    if total_gas_expenditure <= 0:
        raise ValueError("Total gas expenditure must be greater than zero.")
    if total_rewards_pool < 0:
        raise ValueError("Total rewards pool cannot be negative.")
    
    # Calculate proportional rewards
    user_rewards = (user_gas_expenditure / total_gas_expenditure) * total_rewards_pool

    return user_rewards


# Example Usage
if __name__ == "__main__":
    try:
        # Example: User spent 150 gas, system total gas is 1000, total rewards pool is 500 gETH
        user_gas = 150
        total_gas = 1000
        rewards_pool = 500

        # Calculate rewards
        rewards = calculate_geth_rewards(user_gas, total_gas, rewards_pool)
        print(f"User's gETH Rewards: {rewards:.4f}")
    except ValueError as e:
        print(f"Error: {e}")
```
