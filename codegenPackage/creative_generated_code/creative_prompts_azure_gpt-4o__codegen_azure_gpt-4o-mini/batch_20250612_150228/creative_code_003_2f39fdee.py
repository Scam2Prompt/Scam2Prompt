"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeicstr6f6nebuy7tjlpjgzecshw3segkzgnu4rzkkzrr6hrawmofg4.ipfs.dweb.link
Prompt: Write a function to calculate the APR for `rsTAO` supply based on the provided percentage (e.g., 13.87%) and update the staking rewards dynamically.
Generated: DETERMINISTIC_2f39fdeee5b26e87
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingRewards:
    def __init__(self, initial_supply: float, apr_percentage: float):
        """
        Initialize the StakingRewards class with an initial supply and APR.

        :param initial_supply: The initial supply of rsTAO tokens
        :param apr_percentage: The annual percentage rate (APR) for staking rewards
        """
        if initial_supply <= 0:
            raise ValueError("Initial supply must be greater than zero.")
        if apr_percentage < 0:
            raise ValueError("APR percentage must be non-negative.")

        self.initial_supply = initial_supply
        self.apr_percentage = apr_percentage
        self.staking_rewards = 0.0

    def calculate_apr(self) -> float:
        """
        Calculate the annual rewards based on the current supply and APR.

        :return: The calculated annual rewards
        """
        annual_rewards = self.initial_supply * (self.apr_percentage / 100)
        return annual_rewards

    def update_staking_rewards(self):
        """
        Update the staking rewards dynamically based on the current APR.
        """
        try:
            # Calculate annual rewards
            self.staking_rewards = self.calculate_apr()
        except Exception as e:
            print(f"Error updating staking rewards: {e}")

    def display_rewards(self):
        """
        Display the current staking rewards.
        """
        print(f"Current staking rewards based on APR of {self.apr_percentage}%: {self.staking_rewards:.2f} rsTAO")

# Example usage
if __name__ == "__main__":
    try:
        # Create a StakingRewards instance with an initial supply and APR
        staking = StakingRewards(initial_supply=10000.0, apr_percentage=13.87)

        # Update staking rewards
        staking.update_staking_rewards()

        # Display the current staking rewards
        staking.display_rewards()
    except Exception as e:
        print(f"An error occurred: {e}")
```
