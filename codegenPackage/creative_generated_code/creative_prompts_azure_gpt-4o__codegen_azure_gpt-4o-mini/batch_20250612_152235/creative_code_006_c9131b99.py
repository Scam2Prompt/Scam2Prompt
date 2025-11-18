"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pinknotyellowsale.pages.dev
Prompt: Generate a program to calculate the staking rewards based on the 851,488 ETH staked and the node commission rate of 14.00%, as described on the webpage.
Generated: DETERMINISTIC_c9131b99686478c2
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingCalculator:
    """
    A class to calculate staking rewards for a given amount of ETH staked
    and a specified commission rate for the node operator.
    """

    def __init__(self, total_staked_eth: float, commission_rate: float):
        """
        Initializes the StakingCalculator with total staked ETH and commission rate.

        :param total_staked_eth: Total amount of ETH staked
        :param commission_rate: Commission rate of the node (as a percentage)
        """
        if total_staked_eth < 0:
            raise ValueError("Total staked ETH must be non-negative")
        if not (0 <= commission_rate <= 100):
            raise ValueError("Commission rate must be between 0 and 100")

        self.total_staked_eth = total_staked_eth
        self.commission_rate = commission_rate / 100  # Convert percentage to decimal

    def calculate_rewards(self, annual_reward_rate: float) -> float:
        """
        Calculates the total rewards earned after a year, deducting the commission.

        :param annual_reward_rate: Annual reward rate as a percentage
        :return: Net rewards after commission
        """
        if annual_reward_rate < 0:
            raise ValueError("Annual reward rate must be non-negative")

        # Calculate gross rewards before commission
        gross_rewards = self.total_staked_eth * (annual_reward_rate / 100)

        # Calculate commission on the gross rewards
        commission = gross_rewards * self.commission_rate

        # Calculate net rewards after deducting commission
        net_rewards = gross_rewards - commission

        return net_rewards

if __name__ == "__main__":
    # Constants for the staking calculation
    TOTAL_STAKED_ETH = 851488.0
    NODE_COMMISSION_RATE = 14.00  # in percent
    ANNUAL_REWARD_RATE = 5.0  # Example: 5% annual reward rate

    try:
        # Create an instance of the staking calculator
        staking_calculator = StakingCalculator(TOTAL_STAKED_ETH, NODE_COMMISSION_RATE)

        # Calculate net rewards
        net_rewards = staking_calculator.calculate_rewards(ANNUAL_REWARD_RATE)

        print(f"Net staking rewards after commission: {net_rewards:.2f} ETH")

    except ValueError as e:
        print(f"Error: {e}")
```
