"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-inqubeta-ai.pages.dev
Prompt: Generate code to calculate the rewards earned by staking QUBE tokens over a specified period, factoring in the reward pool allocation from the sell tax.
Generated: DETERMINISTIC_0b69add6bcb9fda9
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class QUBEStaking:
    def __init__(self, total_supply: float, sell_tax_rate: float, reward_pool_allocation: float):
        """
        Initialize the QUBEStaking instance.

        :param total_supply: Total supply of QUBE tokens.
        :param sell_tax_rate: Sell tax rate as a decimal (e.g., 0.05 for 5%).
        :param reward_pool_allocation: Amount allocated to the reward pool from the sell tax.
        """
        self.total_supply = total_supply
        self.sell_tax_rate = sell_tax_rate
        self.reward_pool_allocation = reward_pool_allocation

    def calculate_rewards(self, staked_amount: float, duration_days: int) -> float:
        """
        Calculate the rewards earned by staking QUBE tokens over a specified period.

        :param staked_amount: Amount of QUBE tokens staked.
        :param duration_days: Duration in days for which the tokens are staked.
        :return: The calculated rewards.
        :raises ValueError: If staked_amount or duration_days are invalid.
        """
        # Validate inputs
        if staked_amount <= 0:
            raise ValueError("Staked amount must be greater than zero.")
        if duration_days <= 0:
            raise ValueError("Duration must be greater than zero.")

        # Calculate total rewards from the sell tax
        total_rewards_pool = self.total_supply * self.sell_tax_rate * self.reward_pool_allocation
        
        # Calculate user rewards based on their stake proportion
        user_reward_ratio = staked_amount / self.total_supply
        user_rewards = total_rewards_pool * user_reward_ratio * (duration_days / 365)  # Annualized rewards

        return user_rewards


# Example usage
if __name__ == "__main__":
    try:
        total_supply = 1_000_000  # Total QUBE tokens
        sell_tax_rate = 0.05  # 5% sell tax
        reward_pool_allocation = 0.1  # 10% of the tax allocated to rewards

        # Create an instance of QUBEStaking
        staking = QUBEStaking(total_supply, sell_tax_rate, reward_pool_allocation)

        # Calculate rewards for staked tokens
        staked_amount = 10000  # Amount of QUBE tokens staked
        duration_days = 30  # Number of days staked

        rewards = staking.calculate_rewards(staked_amount, duration_days)
        print(f"Rewards earned by staking {staked_amount} QUBE tokens for {duration_days} days: {rewards:.2f} QUBE")
    
    except ValueError as e:
        print(f"Error: {e}")
```
