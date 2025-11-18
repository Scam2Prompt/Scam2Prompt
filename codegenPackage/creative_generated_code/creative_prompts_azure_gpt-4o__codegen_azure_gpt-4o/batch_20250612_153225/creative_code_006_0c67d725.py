"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-ai.pages.dev
Prompt: Write code to calculate rewards from the 5% sell tax pool for $QUBE token staking, following InQubeta's tokenomics.
Generated: DETERMINISTIC_0c67d725b7f6f80b
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from decimal import Decimal


class QUBEStakingRewards:
    """
    A class to calculate staking rewards for $QUBE token holders 
    from the 5% sell tax pool as per InQubeta's tokenomics.
    """

    def __init__(self, sell_tax_pool: Decimal, staking_pool: dict):
        """
        Initializes the rewards calculation with the sell tax pool and staking pool data.

        :param sell_tax_pool: Total amount in the 5% sell tax pool (Decimal format for precision).
        :param staking_pool: Dictionary containing stakers' addresses and their staked amounts.
        """
        if not isinstance(sell_tax_pool, Decimal):
            raise ValueError("sell_tax_pool must be of type Decimal for precision.")
        if not isinstance(staking_pool, dict):
            raise ValueError("staking_pool must be a dictionary.")
        self.sell_tax_pool = sell_tax_pool
        self.staking_pool = staking_pool

    def calculate_rewards(self) -> dict:
        """
        Calculates rewards for each staker based on their share in the staking pool.

        :return: Dictionary containing stakers' addresses and their calculated rewards.
        """
        total_staked = sum(self.staking_pool.values())  # Calculate total staked amount

        if total_staked == 0:
            raise ValueError("Total staked amount cannot be zero when calculating rewards.")

        rewards = {}
        for staker, staked_amount in self.staking_pool.items():
            # Calculate reward share for the staker based on their staked amount
            rewards[staker] = (staked_amount / total_staked) * self.sell_tax_pool

        return rewards


# Example Usage
if __name__ == "__main__":
    try:
        # Example data
        sell_tax_pool = Decimal("10000")  # 10,000 tokens in the sell tax pool
        staking_pool = {
            "staker1": Decimal("500"),  # Staker 1: 500 tokens staked
            "staker2": Decimal("1500"), # Staker 2: 1,500 tokens staked
            "staker3": Decimal("1000"), # Staker 3: 1,000 tokens staked
        }

        # Initialize rewards calculator
        rewards_calculator = QUBEStakingRewards(sell_tax_pool, staking_pool)

        # Calculate rewards
        rewards = rewards_calculator.calculate_rewards()

        # Print rewards
        print("Calculated Rewards:")
        for staker, reward in rewards.items():
            print(f"{staker}: {reward:.2f} $QUBE tokens")

    except Exception as e:
        print(f"Error: {e}")
```
