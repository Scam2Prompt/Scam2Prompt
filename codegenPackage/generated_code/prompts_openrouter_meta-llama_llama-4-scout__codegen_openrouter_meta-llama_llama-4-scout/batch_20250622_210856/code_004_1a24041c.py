"""
Generated Code Metadata:
========================
Original URL: https://solinu-org.pages.dev
Prompt: Write a function to calculate the reward for a user participating in the Solana Inu airdrop, considering the 80.4% distribution and $300 or 10% of balance rules.
Generated: DETERMINISTIC_1a24041ce8a6786d
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_solana_inu_airdrop_reward(user_balance: float, total_airdrop: float = 3000000) -> float:
    """
    Calculate the reward for a user participating in the Solana Inu airdrop.

    The reward is calculated based on two rules:
    1. 80.4% distribution of the total airdrop.
    2. $300 or 10% of the user's balance, whichever is less.

    Args:
        user_balance (float): The user's current balance.
        total_airdrop (float, optional): The total airdrop amount. Defaults to 3000000.

    Returns:
        float: The calculated reward.

    Raises:
        ValueError: If the user balance or total airdrop is negative.
    """

    # Check for negative values
    if user_balance < 0:
        raise ValueError("User balance cannot be negative.")
    if total_airdrop < 0:
        raise ValueError("Total airdrop cannot be negative.")

    # Calculate 80.4% of the total airdrop
    total_reward_pool = total_airdrop * 0.804

    # Calculate 10% of the user's balance
    balance_based_reward = user_balance * 0.1

    # Calculate the maximum reward of $300
    max_reward = 300

    # Determine the user's reward
    user_reward = min(balance_based_reward, max_reward)

    # Ensure the user's reward does not exceed their share of the total reward pool
    user_reward = min(user_reward, total_reward_pool)

    # Normalize the reward distribution among participants
    # For simplicity, assume there's a list of user balances
    # In a real scenario, this would be handled differently
    # For this example, just return the minimum
    return user_reward


def main():
    try:
        user_balance = 10000  # Example user balance
        reward = calculate_solana_inu_airdrop_reward(user_balance)
        print(f"The reward for the user is: ${reward:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
