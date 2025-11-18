"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paalai-revshare.pages.dev
Prompt: Create a function to calculate the effective APR and ETH reward share for staking $PAAL tokens based on user input for duration and amount.
Generated: DETERMINISTIC_558038340fd22c80
Batch ID: 20250612_152000
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
    A class to calculate the effective APR and ETH reward share for staking $PAAL tokens.
    """

    def __init__(self, base_apr, reward_per_staked_token):
        """
        Initialize the staking calculator with the base APR and the reward per staked token.

        :param base_apr: Base Annual Percentage Rate (APR) for staking in decimal form (e.g., 0.05 for 5%).
        :param reward_per_staked_token: Reward in ETH received per $PAAL staked token per year.
        """
        if base_apr < 0 or reward_per_staked_token < 0:
            raise ValueError("Base APR and reward per staked token must be non-negative.")

        self.base_apr = base_apr
        self.reward_per_staked_token = reward_per_staked_token

    def calculate_effective_apr(self, amount, duration_in_days):
        """
        Calculate the effective APR based on the amount staked and the duration.

        :param amount: The amount of $PAAL tokens being staked.
        :param duration_in_days: Duration of staking in days.
        :return: Effective APR for the given duration and amount.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        if duration_in_days <= 0:
            raise ValueError("Duration must be greater than zero.")

        annual_days = 365
        effective_apr = (self.base_apr * (duration_in_days / annual_days)) * amount
        return effective_apr

    def calculate_eth_reward_share(self, amount):
        """
        Calculate the ETH reward share based on the amount staked.

        :param amount: The amount of $PAAL tokens being staked.
        :return: Total ETH rewards for the given amount staked.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        eth_reward_share = self.reward_per_staked_token * amount
        return eth_reward_share

# Example usage:
if __name__ == "__main__":
    try:
        # Constants for the staking calculator
        BASE_APR = 0.05  # 5% APR
        REWARD_PER_STAKED_TOKEN = 0.01  # 0.01 ETH per token staked per year

        # Create an instance of StakingCalculator
        staking_calculator = StakingCalculator(BASE_APR, REWARD_PER_STAKED_TOKEN)

        # Define staking parameters
        amount_staked = 1000  # Amount of $PAAL Tokens
        staking_duration = 30  # Duration in days

        # Calculate effective APR and ETH reward share
        effective_apr = staking_calculator.calculate_effective_apr(amount_staked, staking_duration)
        eth_reward_share = staking_calculator.calculate_eth_reward_share(amount_staked)

        # Print results
        print(f"Effective APR for staking ${amount_staked} PAAL for {staking_duration} days: {effective_apr:.2f}")
        print(f"ETH reward share for staking ${amount_staked} PAAL: {eth_reward_share:.2f} ETH")
    
    except ValueError as e:
        print(f"Error: {e}")
```
