"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-buck.pages.dev
Prompt: Create a program that calculates the rewards distributed by CoinBuck based on completed tasks, referrals, and engagement bonuses.
Generated: DETERMINISTIC_902f1610804ae416
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
CoinBuck Rewards Calculator

This program calculates the total rewards distributed by CoinBuck based on three components:
1. Completed tasks
2. Referrals
3. Engagement bonuses

Author: Expert Programmer
Date: YYYY-MM-DD
"""

def calculate_rewards(completed_tasks, referrals, engagement_bonus):
    """
    Calculate total rewards based on completed tasks, referrals, and engagement bonuses.

    Args:
        completed_tasks (list of tuples): Each tuple contains (task_name, reward_amount).
        referrals (int): Number of referrals made.
        engagement_bonus (float): Engagement bonus amount.

    Returns:
        float: Total rewards amount.
    """
    try:
        # Validate inputs
        if not isinstance(completed_tasks, list) or not all(isinstance(task, tuple) and len(task) == 2 for task in completed_tasks):
            raise ValueError("Invalid format for completed_tasks. Expected a list of tuples (task_name, reward_amount).")
        if not isinstance(referrals, int) or referrals < 0:
            raise ValueError("Invalid number of referrals. Expected a non-negative integer.")
        if not isinstance(engagement_bonus, (int, float)) or engagement_bonus < 0:
            raise ValueError("Invalid engagement bonus amount. Expected a non-negative number.")

        # Calculate rewards from completed tasks
        task_rewards = sum(task[1] for task in completed_tasks)

        # Calculate referral rewards (assuming $5 per referral)
        referral_rewards = referrals * 5

        # Total rewards
        total_rewards = task_rewards + referral_rewards + engagement_bonus
        return total_rewards

    except ValueError as ve:
        print(f"ValueError: {ve}")
        return 0
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0


def main():
    """
    Main function to demonstrate the CoinBuck Rewards Calculator.
    """
    print("Welcome to the CoinBuck Rewards Calculator!")

    try:
        # Sample input values
        completed_tasks = [("Task 1", 10), ("Task 2", 20), ("Task 3", 15)]
        referrals = 3
        engagement_bonus = 7.5

        # Calculate total rewards
        total_rewards = calculate_rewards(completed_tasks, referrals, engagement_bonus)

        # Display results
        print(f"Total Rewards Distributed: ${total_rewards:.2f}")

    except Exception as e:
        print(f"An error occurred during execution: {e}")


if __name__ == "__main__":
    # Entry point of the program
    main()
```
