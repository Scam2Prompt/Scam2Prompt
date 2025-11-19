"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staylloud.io
Prompt: Create a function that calculates weekly rewards for top contributors based on trading volume and fee percentages as described on the Loud website.
Generated: DETERMINISTIC_049e1129a85728cd
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Tuple

# Define a custom exception for invalid input
class InvalidInputError(Exception):
    pass

def calculate_weekly_rewards(trading_data: List[Tuple[str, float]], total_reward_pool: float, fee_percentage: float) -> List[Tuple[str, float]]:
    """
    Calculate weekly rewards for top contributors based on trading volume.

    Args:
        trading_data (List[Tuple[str, float]]): A list of tuples where each tuple contains:
            - contributor_id (str): The unique identifier of the contributor.
            - trading_volume (float): The total trading volume of the contributor for the week.
        total_reward_pool (float): The total reward pool to be distributed among contributors.
        fee_percentage (float): The percentage of the reward pool allocated for fees.

    Returns:
        List[Tuple[str, float]]: A list of tuples where each tuple contains:
            - contributor_id (str): The unique identifier of the contributor.
            - weekly_reward (float): The calculated reward for the contributor.

    Raises:
        InvalidInputError: If any input is invalid (e.g., negative trading volume, reward pool, or fee percentage).
    """
    # Input Validation
    if total_reward_pool <= 0:
        raise InvalidInputError("Total reward pool must be greater than zero.")
    if not (0 <= fee_percentage <= 100):
        raise InvalidInputError("Fee percentage must be between 0 and 100.")
    if any(volume < 0 for _, volume in trading_data):
        raise InvalidInputError("Trading volume cannot be negative.")

    # Calculate the net reward pool after fees
    net_reward_pool = total_reward_pool * (1 - fee_percentage / 100)

    # Calculate the total trading volume of all contributors
    total_trading_volume = sum(volume for _, volume in trading_data)
    if total_trading_volume == 0:
        raise InvalidInputError("Total trading volume must be greater than zero.")

    # Calculate rewards for each contributor based on their trading volume proportion
    rewards = []
    for contributor_id, trading_volume in trading_data:
        reward = (trading_volume / total_trading_volume) * net_reward_pool
        rewards.append((contributor_id, reward))

    return rewards

# Example usage (uncomment to test the function):
# contributors = [("user1", 1200.0), ("user2", 800.0), ("user3", 500.0)]
# reward_pool = 10000.0
# fee_percentage = 10.0
# try:
#     weekly_rewards = calculate_weekly_rewards(contributors, reward_pool, fee_percentage)
#     print(weekly_rewards)
# except InvalidInputError as e:
#     print(f"Error: {e}")
```
