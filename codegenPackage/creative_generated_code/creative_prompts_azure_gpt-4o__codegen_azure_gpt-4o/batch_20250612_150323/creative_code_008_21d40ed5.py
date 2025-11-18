"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect.network
Prompt: Generate code to calculate staking rewards for WCT based on WalletConnect's fee and reward structure.
Generated: DETERMINISTIC_21d40ed51ddaa376
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# staking_rewards_calculator.py

class StakingRewardsCalculator:
    """
    A class to calculate staking rewards for WCT (WalletConnect Token).
    """

    def __init__(self, staking_amount, staking_period, annual_reward_rate, fee_rate):
        """
        Initialize the StakingRewardsCalculator.

        :param staking_amount: The amount staked (float).
        :param staking_period: The staking period in days (int).
        :param annual_reward_rate: The annual reward rate (float, as a percentage).
        :param fee_rate: The fee rate deducted by WalletConnect (float, as a percentage).
        """
        self.staking_amount = staking_amount
        self.staking_period = staking_period
        self.annual_reward_rate = annual_reward_rate / 100  # Convert percentage to decimal
        self.fee_rate = fee_rate / 100  # Convert percentage to decimal

    def calculate_rewards(self):
        """
        Calculate the rewards and fees for staking.

        :return: A dictionary with gross rewards, fees, and net rewards.
        """
        try:
            # Calculate the rewards before fees (gross rewards)
            # Formula: (staking_amount * annual_reward_rate * staking_period) / 365
            gross_rewards = (self.staking_amount * self.annual_reward_rate * self.staking_period) / 365

            # Calculate the WalletConnect fee
            fees = gross_rewards * self.fee_rate

            # Calculate the net rewards (after fees)
            net_rewards = gross_rewards - fees

            # Return the results
            return {
                "gross_rewards": round(gross_rewards, 2),
                "fees": round(fees, 2),
                "net_rewards": round(net_rewards, 2)
            }
        except Exception as e:
            raise ValueError(f"An error occurred while calculating rewards: {str(e)}")


# Example usage
if __name__ == "__main__":
    # Example inputs
    staking_amount = 1000.0  # Amount staked in WCT
    staking_period = 30  # Staking period in days
    annual_reward_rate = 10.0  # Annual reward rate (in %)
    fee_rate = 2.0  # WalletConnect fee rate (in %)

    # Create an instance of the calculator
    calculator = StakingRewardsCalculator(staking_amount, staking_period, annual_reward_rate, fee_rate)

    # Calculate the rewards
    try:
        rewards = calculator.calculate_rewards()
        print("Staking Rewards Calculation:")
        print(f"Gross Rewards: {rewards['gross_rewards']} WCT")
        print(f"Fees: {rewards['fees']} WCT")
        print(f"Net Rewards: {rewards['net_rewards']} WCT")
    except ValueError as error:
        print(f"Error: {error}")
```
