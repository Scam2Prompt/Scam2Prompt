"""
Generated Code Metadata:
========================
Original URL: https://satyloud.io
Prompt: Generate code to calculate weekly SOL rewards distribution based on Loud's fee split mechanics (72% sKAITO, 18% Creator, 10% Weekly SOL distribution).
Generated: DETERMINISTIC_081ea1de0d66f0b6
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_weekly_sol_rewards(total_sol_rewards: float, 
                                 loud_fee_split: dict = None) -> dict:
    """
    Calculates weekly SOL rewards distribution based on Loud's fee split mechanics.

    Args:
    - total_sol_rewards (float): The total SOL rewards to be distributed.
    - loud_fee_split (dict, optional): A dictionary containing the fee split percentages. 
                                       Defaults to {'sKAITO': 0.72, 'Creator': 0.18, 'Weekly SOL distribution': 0.10}.

    Returns:
    - dict: A dictionary containing the calculated SOL rewards for each recipient.

    Raises:
    - ValueError: If the total SOL rewards is negative or if the fee split percentages do not add up to 1.
    """

    # Define default fee split percentages if not provided
    if loud_fee_split is None:
        loud_fee_split = {'sKAITO': 0.72, 'Creator': 0.18, 'Weekly SOL distribution': 0.10}

    # Validate fee split percentages
    if abs(sum(loud_fee_split.values()) - 1) > 1e-6:
        raise ValueError("Fee split percentages must add up to 1")

    # Validate total SOL rewards
    if total_sol_rewards < 0:
        raise ValueError("Total SOL rewards cannot be negative")

    # Calculate SOL rewards for each recipient
    sol_rewards_distribution = {
        recipient: total_sol_rewards * percentage
        for recipient, percentage in loud_fee_split.items()
    }

    return sol_rewards_distribution


def main():
    try:
        total_sol_rewards = 1000.0  # Example total SOL rewards
        sol_rewards_distribution = calculate_weekly_sol_rewards(total_sol_rewards)
        print("Weekly SOL Rewards Distribution:")
        for recipient, rewards in sol_rewards_distribution.items():
            print(f"{recipient}: {rewards:.2f} SOL")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
