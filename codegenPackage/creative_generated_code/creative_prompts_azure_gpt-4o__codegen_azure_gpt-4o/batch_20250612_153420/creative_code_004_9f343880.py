"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magesdsdf.pages.dev
Prompt: Write a function to calculate rewards from Star Point staking in the Merlin ecosystem using the staking parameters provided on the MerlinSwap platform.
Generated: DETERMINISTIC_9f343880a6d528df
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import Dict, Union

# Define a custom exception for invalid staking parameters
class InvalidStakingParametersException(Exception):
    pass

def calculate_rewards(staked_amount: float, staking_duration: int, staking_parameters: Dict[str, Union[float, int]]) -> float:
    """
    Calculate rewards from Star Point staking in the Merlin ecosystem.

    Parameters:
    - staked_amount (float): The amount of Star Points staked.
    - staking_duration (int): The duration of staking in days.
    - staking_parameters (Dict[str, Union[float, int]]): A dictionary containing:
        * 'base_rate' (float): The base reward rate per day.
        * 'bonus_rate' (float): The bonus rate multiplier for long-term staking.
        * 'bonus_threshold_days' (int): The threshold in days for applying the bonus rate.

    Returns:
    - float: The calculated rewards for the staking period.

    Raises:
    - InvalidStakingParametersException: If the staking parameters are invalid.
    - ValueError: If staked_amount or staking_duration are invalid.
    """
    # Validate input
    if staked_amount <= 0 or staking_duration <= 0:
        raise ValueError("Staked amount and staking duration must be positive values.")
    
    if 'base_rate' not in staking_parameters or 'bonus_rate' not in staking_parameters or 'bonus_threshold_days' not in staking_parameters:
        raise InvalidStakingParametersException("Staking parameters must include 'base_rate', 'bonus_rate', and 'bonus_threshold_days'.")
    
    base_rate = staking_parameters['base_rate']
    bonus_rate = staking_parameters['bonus_rate']
    bonus_threshold_days = staking_parameters['bonus_threshold_days']

    if base_rate <= 0 or bonus_rate <= 0 or bonus_threshold_days < 0:
        raise InvalidStakingParametersException("Invalid values in staking parameters.")

    # Calculate rewards
    if staking_duration > bonus_threshold_days:
        # Apply bonus rate for long-term staking
        reward = staked_amount * base_rate * staking_duration * bonus_rate
    else:
        # Apply base rate for regular staking
        reward = staked_amount * base_rate * staking_duration

    return reward

# Example usage
if __name__ == "__main__":
    try:
        staking_parameters = {
            'base_rate': 0.01,          # 1% daily reward
            'bonus_rate': 1.5,         # 50% bonus for long-term staking
            'bonus_threshold_days': 30 # Bonus applies after 30 days
        }
        staked_amount = 1000          # Example: 1000 Star Points
        staking_duration = 45         # Example: Staking for 45 days

        rewards = calculate_rewards(staked_amount, staking_duration, staking_parameters)
        print(f"Calculated rewards: {rewards:.2f} Star Points")
    except (InvalidStakingParametersException, ValueError) as e:
        print(f"Error: {e}")
```
