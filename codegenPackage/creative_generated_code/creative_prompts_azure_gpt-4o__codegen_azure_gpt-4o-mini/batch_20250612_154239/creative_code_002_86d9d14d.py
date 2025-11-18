"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimmints-4.vercel.app
Prompt: Create a function to calculate proportional gETH rewards based on Ethereum gas expenditure, following the gETH token architecture described on the webpage.
Generated: DETERMINISTIC_86d9d14db92b89d5
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal
from web3 import Web3

# Setting up the precision for decimal calculations
decimal.getcontext().prec = 18

class GETHRewardsCalculator:
    def __init__(self, gas_price: decimal.Decimal, gas_used: int, total_gas_expenditure: decimal.Decimal, total_rewards: decimal.Decimal):
        """
        Initialize the GETHRewardsCalculator with necessary parameters.
        
        :param gas_price: The gas price in gwei (as a decimal)
        :param gas_used: Total gas used by the transaction
        :param total_gas_expenditure: Total gas expenditure for calculations
        :param total_rewards: Total available gETH rewards for distribution
        """
        self.gas_price = gas_price
        self.gas_used = gas_used
        self.total_gas_expenditure = total_gas_expenditure
        self.total_rewards = total_rewards

    def calculate_rewards(self) -> decimal.Decimal:
        """
        Calculate the proportional gETH rewards based on gas expenditure.
        
        :return: The calculated gETH rewards for the user's transaction
        """
        try:
            # Ensure gas_used is a positive integer
            if self.gas_used <= 0:
                raise ValueError("Gas used must be a positive integer.")

            # Ensure total_gas_expenditure is positive and not zero
            if self.total_gas_expenditure <= 0:
                raise ValueError("Total gas expenditure must be a positive decimal value.")

            # Calculate the total cost of gas for the transaction in gwei
            transaction_gas_cost = self.gas_price * self.gas_used

            # Calculate the proportional rewards
            proportional_rewards = (transaction_gas_cost / self.total_gas_expenditure) * self.total_rewards

            # Ensure rewards are not negative
            return max(proportional_rewards, decimal.Decimal(0))
        
        except Exception as e:
            print(f"An error occurred while calculating rewards: {e}")
            return decimal.Decimal(0)

# Example usage:
if __name__ == "__main__":
    # Set gas price and usage
    gas_price = decimal.Decimal('100')  # gwei
    gas_used = 21000  # typical gas for a simple ETH transfer
    total_gas_expenditure = decimal.Decimal('1000000')  # total gas expenditure in gwei
    total_rewards = decimal.Decimal('50')  # total available gETH rewards

    # Create an instance of the rewards calculator
    rewards_calculator = GETHRewardsCalculator(gas_price, gas_used, total_gas_expenditure, total_rewards)

    # Calculate the rewards
    rewards = rewards_calculator.calculate_rewards()
    print(f"Calculated gETH rewards: {rewards} gETH")
```
