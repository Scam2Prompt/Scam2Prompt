"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-earthmetasite.web.app
Prompt: How can I implement a staking rewards calculator for the EarthMeta token ($EMT) in Python?
Generated: DETERMINISTIC_570109a112c64473
Batch ID: 20250612_155503
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingRewardsCalculator:
    """
    A class to calculate staking rewards for the EarthMeta token ($EMT).
    """

    def __init__(self, total_supply: float, total_staked: float, annual_apr: float):
        """
        Initializes the StakingRewardsCalculator with the necessary parameters.

        Parameters:
        total_supply: Total supply of the $EMT token.
        total_staked: Total amount of $EMT token currently staked.
        annual_apr: Annual percentage rate (APR) for staking rewards.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        if total_staked < 0:
            raise ValueError("Total staked cannot be negative.")
        if annual_apr < 0:
            raise ValueError("Annual APR cannot be negative.")

        self.total_supply = total_supply
        self.total_staked = total_staked
        self.annual_apr = annual_apr

    def calculate_rewards(self, staked_amount: float, duration_days: int) -> float:
        """
        Calculates the staking rewards for a given staked amount and duration.

        Parameters:
        staked_amount: Amount of $EMT being staked.
        duration_days: Duration in days for which the amount is staked.

        Returns:
        The rewards earned over the duration.
        """
        if staked_amount <= 0:
            raise ValueError("Staked amount must be greater than zero.")
        if duration_days <= 0:
            raise ValueError("Duration must be greater than zero.")

        # Calculate daily interest rate from APR
        daily_interest_rate = self.annual_apr / 365 / 100
        
        # Calculate rewards
        rewards = staked_amount * daily_interest_rate * duration_days
        
        return rewards

    def get_staking_percentage(self) -> float:
        """
        Returns the staking percentage of the total supply.

        Returns:
        The percentage of the total supply that is currently staked.
        """
        if self.total_supply == 0:
            raise ValueError("Total supply cannot be zero to calculate staking percentage.")
        
        return (self.total_staked / self.total_supply) * 100


if __name__ == "__main__":
    try:
        # Example parameters
        TOTAL_SUPPLY = 1_000_000_000  # 1 billion $EMT tokens
        TOTAL_STAKED = 250_000_000     # 250 million $EMT tokens staked
        ANNUAL_APR = 5.0               # 5% annual APR

        # Instantiate the calculator
        rewards_calculator = StakingRewardsCalculator(TOTAL_SUPPLY, TOTAL_STAKED, ANNUAL_APR)

        # Calculate rewards for a staked amount over a specified duration
        staked_amount = 1000.0  # Amount of $EMT staked
        duration_days = 30      # Duration in days

        rewards = rewards_calculator.calculate_rewards(staked_amount, duration_days)
        staking_percentage = rewards_calculator.get_staking_percentage()

        # Output results
        print(f"Staking Rewards for ${staked_amount} EMT over {duration_days} days: ${rewards:.2f}")
        print(f"Current Staking Percentage of Total Supply: {staking_percentage:.2f}%")

    except Exception as e:
        print(f"Error: {e}")
```
