"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottyweb.pages.dev
Prompt: Write a Python script that simulates staking $SCOTTY tokens and calculates the user's estimated rewards over a 3-year period, factoring in the dynamic rewards rate.
Generated: DETERMINISTIC_9cd354acad40d4dd
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class StakingSimulation:
    def __init__(self, initial_investment, reward_rate_start, reward_rate_end, years=3):
        """
        Initialize the staking simulation parameters.

        :param initial_investment: Amount of $SCOTTY tokens to stake
        :param reward_rate_start: Starting reward rate (as a percentage)
        :param reward_rate_end: Ending reward rate (as a percentage)
        :param years: Duration of staking in years
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if not (0 <= reward_rate_start <= 100) or not (0 <= reward_rate_end <= 100):
            raise ValueError("Reward rates must be between 0 and 100.")
        
        self.initial_investment = initial_investment
        self.reward_rate_start = reward_rate_start / 100  # Convert to decimal
        self.reward_rate_end = reward_rate_end / 100  # Convert to decimal
        self.years = years

    def simulate_rewards(self):
        """
        Simulate the rewards over the specified number of years with a dynamic reward rate.

        :return: Total estimated rewards after the staking period
        """
        total_rewards = 0
        current_investment = self.initial_investment
        
        for year in range(1, self.years + 1):
            # Dynamically calculate the reward rate for the current year
            reward_rate = self.dynamic_reward_rate(year)
            rewards = current_investment * reward_rate
            total_rewards += rewards
            current_investment += rewards  # Reinvest rewards
            
            print(f"Year {year}: Reward Rate = {reward_rate * 100:.2f}%, Rewards = ${rewards:.2f}, Total = ${current_investment:.2f}")

        return total_rewards

    def dynamic_reward_rate(self, year):
        """
        Calculate the dynamic reward rate for the given year.

        :param year: The current year of staking
        :return: The calculated reward rate for the year
        """
        # Simulate a random reward rate between the start and end rates
        return random.uniform(self.reward_rate_start, self.reward_rate_end)

if __name__ == "__main__":
    try:
        # User parameters for staking simulation
        initial_investment = float(input("Enter the amount of $SCOTTY tokens to stake: "))
        reward_rate_start = float(input("Enter the starting reward rate (in %): "))
        reward_rate_end = float(input("Enter the ending reward rate (in %): "))

        # Create a staking simulation instance
        staking_simulation = StakingSimulation(initial_investment, reward_rate_start, reward_rate_end)

        # Run the simulation and get total estimated rewards
        total_rewards = staking_simulation.simulate_rewards()
        
        print(f"\nTotal Estimated Rewards over {staking_simulation.years} years: ${total_rewards:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
