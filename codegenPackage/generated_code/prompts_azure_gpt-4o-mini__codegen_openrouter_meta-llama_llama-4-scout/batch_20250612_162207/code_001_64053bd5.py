"""
Generated Code Metadata:
========================
Original URL: https://egld.pages.dev
Prompt: Write a Python script to calculate EGLD staking rewards based on the formula provided by MultiversX.
Generated: DETERMINISTIC_64053bd550638dd6
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
EGLD Staking Rewards Calculator

Calculates EGLD staking rewards based on the formula provided by MultiversX.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_staking_rewards(
    total_staked: float, 
    total_rewards: float, 
    user_stake: float, 
    activation_height: int, 
    current_height: int
) -> float:
    """
    Calculates EGLD staking rewards.

    Args:
    - total_staked (float): Total EGLD staked.
    - total_rewards (float): Total rewards to be distributed.
    - user_stake (float): User's EGLD stake.
    - activation_height (int): Activation height of the stake.
    - current_height (int): Current block height.

    Returns:
    - float: Calculated staking rewards.
    """

    # Check for division by zero errors
    if total_staked == 0:
        raise ValueError("Total staked cannot be zero")

    # Calculate the number of epochs
    epochs = max(0, current_height - activation_height)

    # MultiversX staking rewards formula
    # Assuming the formula is: rewards = (user_stake / total_staked) * total_rewards * (epochs / epochs_total)
    # For simplicity, epochs_total is considered 1 for the given period
    rewards = (user_stake / total_staked) * total_rewards * (epochs / 3600)  # Assuming 3600 epochs in a period

    return rewards


def main():
    try:
        # Example usage
        total_staked = 1000000  # Total EGLD staked
        total_rewards = 10000  # Total rewards to be distributed
        user_stake = 1000  # User's EGLD stake
        activation_height = 1000  # Activation height of the stake
        current_height = 3600  # Current block height

        rewards = calculate_staking_rewards(
            total_staked, 
            total_rewards, 
            user_stake, 
            activation_height, 
            current_height
        )

        print(f"Calculated staking rewards: {rewards} EGLD")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
