"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-en.web.app
Prompt: Develop a Python script to calculate the rewards pool distribution for $QUBE token staking, based on the 5% sell tax described in InQubeta's tokenomics.
Generated: DETERMINISTIC_419109d16e3ce6f9
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RewardsPool:
    def __init__(self, total_staked: float, sell_tax_rate: float = 0.05):
        """
        Initialize the RewardsPool with total staked amount and sell tax rate.

        :param total_staked: The total amount of QUBE tokens staked.
        :param sell_tax_rate: The rate at which tokens are taxed on sell transactions.
        """
        self.total_staked = total_staked
        self.sell_tax_rate = sell_tax_rate
        self.rewards_pool = 0.0

    def calculate_rewards_pool(self, total_sales: float) -> float:
        """
        Calculate the rewards pool based on total sales.

        :param total_sales: The total amount of QUBE tokens sold.
        :return: The amount added to the rewards pool from the sales.
        :raises ValueError: If total_sales is negative.
        """
        if total_sales < 0:
            raise ValueError("Total sales cannot be negative.")
        
        # Calculate the rewards pool contribution from sales
        contribution = total_sales * self.sell_tax_rate
        self.rewards_pool += contribution
        return self.rewards_pool

    def distribute_rewards(self) -> dict:
        """
        Distribute rewards to stakers based on their stake.

        :return: A dictionary with the stake and the corresponding reward for each staker.
        :raises ValueError: If total_staked is zero or less.
        """
        if self.total_staked <= 0:
            raise ValueError("Total staked must be greater than zero to distribute rewards.")

        # Example staker data
        stakers = {
            'staker1': 1000,
            'staker2': 5000,
            'staker3': 2500,
        }

        # Calculate total stake
        total_stake_amount = sum(stakers.values())
        
        # Calculate rewards distribution
        rewards_distribution = {}
        for staker, stake in stakers.items():
            rewards_distribution[staker] = (stake / total_stake_amount) * self.rewards_pool
        
        return rewards_distribution

if __name__ == "__main__":
    try:
        # Initialize the rewards pool with some total staked amount
        rewards_pool = RewardsPool(total_staked=10000)

        # Simulate total sales to calculate rewards pool
        total_sales = 20000  # Example total sales
        rewards_pool.calculate_rewards_pool(total_sales)

        # Distribute rewards to stakers
        rewards = rewards_pool.distribute_rewards()
        print("Rewards distribution:", rewards)

    except ValueError as e:
        print(f"Error: {e}")
```
