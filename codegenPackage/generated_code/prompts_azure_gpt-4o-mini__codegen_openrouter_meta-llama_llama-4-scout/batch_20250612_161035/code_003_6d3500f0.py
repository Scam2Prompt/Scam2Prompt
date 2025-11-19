"""
Generated Code Metadata:
========================
Original URL: https://nc8301x1.pages.dev
Prompt: Create a function to calculate the total Notcoin rewards distributed based on the given statistics from the Notcoin airdrop.
Generated: DETERMINISTIC_6d3500f07c6a0ad4
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_notcoin_rewards(
    total_users: int, 
    users_with_claimed_rewards: int, 
    average_reward_per_user: float, 
    unclaimed_rewards_percentage: float
) -> float:
    """
    Calculate the total Notcoin rewards distributed based on the given statistics from the Notcoin airdrop.

    Args:
    - total_users (int): The total number of users in the airdrop.
    - users_with_claimed_rewards (int): The number of users who have claimed their rewards.
    - average_reward_per_user (float): The average reward per user.
    - unclaimed_rewards_percentage (float): The percentage of unclaimed rewards.

    Returns:
    - float: The total Notcoin rewards distributed.

    Raises:
    - ValueError: If the input values are invalid.
    """

    # Validate input values
    if total_users < 0 or users_with_claimed_rewards < 0:
        raise ValueError("Total users and users with claimed rewards must be non-negative.")
    if average_reward_per_user < 0:
        raise ValueError("Average reward per user must be non-negative.")
    if unclaimed_rewards_percentage < 0 or unclaimed_rewards_percentage > 100:
        raise ValueError("Unclaimed rewards percentage must be between 0 and 100.")

    # Calculate the total rewards
    total_rewards = total_users * average_reward_per_user

    # Calculate the claimed rewards
    claimed_rewards = users_with_claimed_rewards * average_reward_per_user

    # Calculate the unclaimed rewards
    unclaimed_rewards = total_rewards * (unclaimed_rewards_percentage / 100)

    # Calculate the total rewards distributed
    total_rewards_distributed = total_rewards - unclaimed_rewards

    # Ensure the total rewards distributed is not negative
    total_rewards_distributed = max(0, total_rewards_distributed)

    return total_rewards_distributed


def main():
    try:
        total_users = 1000000
        users_with_claimed_rewards = 800000
        average_reward_per_user = 100.0
        unclaimed_rewards_percentage = 10.0

        total_rewards_distributed = calculate_notcoin_rewards(
            total_users, 
            users_with_claimed_rewards, 
            average_reward_per_user, 
            unclaimed_rewards_percentage
        )

        print(f"Total Notcoin rewards distributed: {total_rewards_distributed}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
