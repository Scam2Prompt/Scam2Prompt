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
class StakingCalculator:
    """
    A class to calculate staking rewards for WCT based on WalletConnect's fee and reward structure.
    """

    def __init__(self, staking_amount, annual_reward_rate, fee_percentage):
        """
        Initializes the staking calculator with the given parameters.

        :param staking_amount: The amount of WCT staked (in the base currency)
        :param annual_reward_rate: The annual reward rate (as a percentage)
        :param fee_percentage: The fee percentage applied to rewards (as a percentage)
        """
        if staking_amount < 0:
            raise ValueError("Staking amount must be non-negative.")
        if not (0 <= annual_reward_rate <= 100):
            raise ValueError("Annual reward rate must be between 0 and 100.")
        if not (0 <= fee_percentage <= 100):
            raise ValueError("Fee percentage must be between 0 and 100.")

        self.staking_amount = staking_amount
        self.annual_reward_rate = annual_reward_rate / 100  # Convert percentage to decimal
        self.fee_percentage = fee_percentage / 100  # Convert percentage to decimal

    def calculate_rewards(self, years):
        """
        Calculates the total rewards over a given number of years.

        :param years: The number of years to calculate rewards for
        :return: Total rewards after fees
        """
        if years < 0:
            raise ValueError("Number of years must be non-negative.")

        # Calculate the gross rewards before fees
        gross_rewards = self.staking_amount * self.annual_reward_rate * years
        # Calculate total fees on the gross rewards
        fee_amount = gross_rewards * self.fee_percentage
        # Calculate net rewards after fees
        net_rewards = gross_rewards - fee_amount

        return net_rewards

    def display_rewards(self, years):
        """
        Displays the calculated rewards in a formatted manner.

        :param years: The number of years to calculate rewards for
        """
        try:
            rewards = self.calculate_rewards(years)
            print(f"For {years} year(s) of staking {self.staking_amount} WCT:")
            print(f"Net rewards after fees: {rewards:.2f} WCT")
        except ValueError as e:
            print(f"Error calculating rewards: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the staking calculator
        staking_amount = 1000  # Example staking amount in WCT
        annual_reward_rate = 10  # Example annual reward rate in percentage
        fee_percentage = 2  # Example fee percentage in percentage
        
        calculator = StakingCalculator(staking_amount, annual_reward_rate, fee_percentage)

        # Display rewards for a 5-year staking period
        calculator.display_rewards(5)
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
