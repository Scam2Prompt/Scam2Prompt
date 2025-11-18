"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana10x.com
Prompt: Write code to simulate staking rewards for 10,000 SOL10x tokens compounded at 0.3836% per epoch over 183 epochs, demonstrating the 70% APY mechanism.
Generated: DETERMINISTIC_3229e68d1e3e41b3
Batch ID: 20250612_145459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingRewardsSimulator:
    def __init__(self, initial_amount, compound_rate, epochs):
        """
        Initialize the simulator with the given parameters.

        :param initial_amount: The initial amount of tokens to stake.
        :param compound_rate: The compounding rate per epoch (as a percentage).
        :param epochs: The total number of epochs to simulate.
        """
        self.initial_amount = initial_amount
        self.compound_rate = compound_rate / 100  # Convert percentage to decimal
        self.epochs = epochs

    def calculate_rewards(self):
        """
        Calculate the total amount of tokens after compounding for the specified number of epochs.

        :return: The total amount of tokens after compounding.
        """
        total_amount = self.initial_amount

        for epoch in range(1, self.epochs + 1):
            total_amount *= (1 + self.compound_rate)

        return total_amount

    def display_results(self):
        """
        Display the initial amount, final amount, and the total rewards earned.
        """
        try:
            final_amount = self.calculate_rewards()
            total_rewards = final_amount - self.initial_amount

            print(f"Initial Amount: {self.initial_amount} SOL10x")
            print(f"Final Amount after {self.epochs} epochs: {final_amount:.4f} SOL10x")
            print(f"Total Rewards Earned: {total_rewards:.4f} SOL10x")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Define the initial parameters for the simulation
    initial_stake = 10000.0  # Initial amount of SOL10x tokens
    compounding_rate = 0.3836  # Compounded rate per epoch in percentage
    total_epochs = 183  # Total number of epochs

    # Create an instance of the StakingRewardsSimulator
    simulator = StakingRewardsSimulator(initial_stake, compounding_rate, total_epochs)

    # Run the simulation and display results
    simulator.display_results()
```
