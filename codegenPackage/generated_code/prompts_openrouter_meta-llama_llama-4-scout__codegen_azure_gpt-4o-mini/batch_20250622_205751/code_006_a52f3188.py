"""
Generated Code Metadata:
========================
Original URL: https://bafkreibeiglm45azw6myhsirtwvfq6qpbsfqnnjq2sf32tpnfhjutzndmu.ipfs.dweb.link
Prompt: Design a staking strategy for AEVO tokens, taking into account the 17.81% APR and the end of Epoch 10, and provide a code example to implement this strategy.
Generated: DETERMINISTIC_a52f3188636faaf0
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class StakingStrategy:
    def __init__(self, initial_investment, apr, epochs):
        """
        Initialize the staking strategy.

        :param initial_investment: The amount of AEVO tokens to stake.
        :param apr: Annual Percentage Rate (APR) for staking.
        :param epochs: The number of epochs to stake for.
        """
        self.initial_investment = initial_investment
        self.apr = apr / 100  # Convert percentage to decimal
        self.epochs = epochs
        self.epoch_duration = 14  # Assuming each epoch lasts 14 days

    def calculate_staking_rewards(self):
        """
        Calculate the total rewards earned after the specified number of epochs.

        :return: Total amount of AEVO tokens after staking.
        """
        try:
            # Calculate the total days for the epochs
            total_days = self.epochs * self.epoch_duration
            
            # Calculate the total rewards using the formula for compound interest
            total_amount = self.initial_investment * (1 + self.apr / 365) ** total_days
            
            return total_amount
        except Exception as e:
            print(f"Error calculating staking rewards: {e}")
            return None

    def display_results(self):
        """
        Display the results of the staking strategy.
        """
        total_amount = self.calculate_staking_rewards()
        if total_amount is not None:
            print(f"Initial Investment: {self.initial_investment} AEVO")
            print(f"Total Amount after {self.epochs} epochs: {total_amount:.2f} AEVO")
            print(f"Total Rewards Earned: {total_amount - self.initial_investment:.2f} AEVO")
        else:
            print("Could not display results due to an error in calculation.")

if __name__ == "__main__":
    # Example usage of the StakingStrategy class
    try:
        initial_investment = 1000  # Example initial investment in AEVO tokens
        apr = 17.81  # Annual Percentage Rate
        epochs = 10  # Number of epochs to stake

        staking_strategy = StakingStrategy(initial_investment, apr, epochs)
        staking_strategy.display_results()
    except Exception as e:
        print(f"An error occurred: {e}")
```
