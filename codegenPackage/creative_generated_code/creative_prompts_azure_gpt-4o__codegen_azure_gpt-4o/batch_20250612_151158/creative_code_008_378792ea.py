"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stader.pages.dev
Prompt: Write a Python script to simulate staking ETH on the Stader platform and calculate the rewards earned over a specified period, factoring in auto-compounding.
Generated: DETERMINISTIC_378792ea2fb59df7
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import math

class ETHStakingSimulator:
    """
    Simulates ETH staking on the Stader platform with auto-compounding rewards.
    """

    def __init__(self, initial_stake, annual_reward_rate, compounding_frequency):
        """
        Initializes the simulator with staking details.
        
        Args:
            initial_stake (float): Initial amount of ETH staked.
            annual_reward_rate (float): Annual reward rate in percentage (e.g., 5.0 for 5%).
            compounding_frequency (int): Number of times rewards are compounded per year.
        """
        self.initial_stake = initial_stake
        self.annual_reward_rate = annual_reward_rate
        self.compounding_frequency = compounding_frequency

    def calculate_rewards(self, days):
        """
        Calculates the staking rewards over a specified period with auto-compounding.

        Args:
            days (int): Number of days to simulate staking.

        Returns:
            float: Total ETH after staking for the specified period (including rewards).
        """
        # Convert annual rate to fractional rate
        rate_per_period = (self.annual_reward_rate / 100) / self.compounding_frequency

        # Calculate total periods based on the number of days
        total_periods = (days / 365) * self.compounding_frequency

        # Apply compound interest formula
        final_amount = self.initial_stake * (1 + rate_per_period) ** total_periods

        return final_amount

def main():
    """
    Main function to simulate ETH staking and calculate rewards.
    """
    try:
        # Input: Initial stake amount, annual reward rate, and number of days
        initial_stake = float(input("Enter the initial amount of ETH to stake: "))
        annual_reward_rate = float(input("Enter the annual reward rate (in %): "))
        compounding_frequency = int(input("Enter the compounding frequency (e.g., 12 for monthly): "))
        days = int(input("Enter the number of days for staking simulation: "))

        # Validate inputs
        if initial_stake <= 0 or annual_reward_rate <= 0 or compounding_frequency <= 0 or days <= 0:
            raise ValueError("All inputs must be positive numbers.")

        # Create simulator instance
        simulator = ETHStakingSimulator(initial_stake, annual_reward_rate, compounding_frequency)

        # Calculate rewards
        final_amount = simulator.calculate_rewards(days)
        rewards = final_amount - initial_stake

        # Display results
        print(f"\nInitial Stake: {initial_stake:.4f} ETH")
        print(f"Annual Reward Rate: {annual_reward_rate:.2f}%")
        print(f"Compounding Frequency: {compounding_frequency} times per year")
        print(f"Days Staked: {days}")
        print(f"Final Amount (including rewards): {final_amount:.4f} ETH")
        print(f"Total Rewards Earned: {rewards:.4f} ETH")
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
