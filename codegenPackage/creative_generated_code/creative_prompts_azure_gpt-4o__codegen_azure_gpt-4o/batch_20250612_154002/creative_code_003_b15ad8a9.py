"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcqex.com
Prompt: Write a function to calculate staking rewards for an Ethereum-based DeFi protocol using DCQEX tools.
Generated: DETERMINISTIC_b15ad8a954609935
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal
from decimal import Decimal, InvalidOperation


def calculate_staking_rewards(staked_amount, annual_percentage_rate, days_staked):
    """
    Calculate staking rewards for an Ethereum-based DeFi protocol.

    Args:
        staked_amount (float or str): The amount of ETH staked by the user. Should be positive.
        annual_percentage_rate (float or str): Annual percentage rate (APR) for staking. Should be positive.
        days_staked (int): Number of days the user has staked their ETH. Should be non-negative.

    Returns:
        dict: Contains the staking rewards in ETH and the total balance (initial stake + rewards).

    Raises:
        ValueError: If the input values are invalid (e.g., negative or non-numeric).
    """
    try:
        # Convert input values to Decimal for precise calculations
        staked_amount = Decimal(staked_amount)
        annual_percentage_rate = Decimal(annual_percentage_rate)
        days_staked = int(days_staked)

        # Validate inputs
        if staked_amount <= 0:
            raise ValueError("Staked amount must be positive.")
        if annual_percentage_rate <= 0:
            raise ValueError("Annual percentage rate (APR) must be positive.")
        if days_staked < 0:
            raise ValueError("Days staked must be non-negative.")

        # Calculate daily rate from APR
        daily_rate = annual_percentage_rate / Decimal(100) / Decimal(365)

        # Calculate rewards
        rewards = staked_amount * daily_rate * Decimal(days_staked)

        # Calculate total balance (staked amount + rewards)
        total_balance = staked_amount + rewards

        # Return the rewards and total balance
        return {
            "rewards": float(rewards),  # Convert back to float for readability
            "total_balance": float(total_balance)  # Convert back to float for readability
        }

    except (InvalidOperation, ValueError) as e:
        # Handle invalid input values
        raise ValueError(f"Invalid input: {e}")


# Example usage
if __name__ == "__main__":
    try:
        staked = "1.5"  # ETH
        apr = "10"  # APR as percentage
        days = 30  # Number of days staked

        result = calculate_staking_rewards(staked, apr, days)
        print(f"Staking Rewards: {result['rewards']} ETH")
        print(f"Total Balance: {result['total_balance']} ETH")
    except ValueError as e:
        print(f"Error: {e}")
```
