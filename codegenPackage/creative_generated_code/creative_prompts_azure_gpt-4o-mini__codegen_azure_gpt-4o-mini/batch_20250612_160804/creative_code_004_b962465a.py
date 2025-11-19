"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-e.pages.dev
Prompt: Generate a script that automates the staking process for DOGE20 tokens, including reward distribution over two years.
Generated: DETERMINISTIC_b962465af3b7f1a0
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from datetime import datetime, timedelta

class Doge20Staking:
    def __init__(self, initial_stake, reward_rate, staking_duration):
        """
        Initialize the staking contract with the initial stake, reward rate, and staking duration.
        
        :param initial_stake: The initial amount of DOGE20 tokens to stake.
        :param reward_rate: The annual reward rate (as a decimal, e.g., 0.05 for 5%).
        :param staking_duration: The total duration for staking in years.
        """
        self.initial_stake = initial_stake
        self.reward_rate = reward_rate
        self.staking_duration = staking_duration
        self.start_time = datetime.now()
        self.total_rewards = 0.0

    def calculate_rewards(self):
        """
        Calculate the total rewards earned over the staking duration.
        
        :return: Total rewards accumulated.
        """
        # Calculate total rewards using the formula: Rewards = Principal * Rate * Time
        total_years = self.staking_duration
        self.total_rewards = self.initial_stake * self.reward_rate * total_years
        return self.total_rewards

    def distribute_rewards(self):
        """
        Distribute rewards to the staker, simulating the reward distribution every quarter.
        """
        # Calculate the reward per quarter
        quarterly_reward = self.calculate_rewards() / (self.staking_duration * 4)
        
        for quarter in range(self.staking_duration * 4):
            # Simulate waiting time for reward distribution
            time.sleep(1)  # Replace with appropriate delay in production
            print(f"Quarter {quarter + 1}: Distributed {quarterly_reward:.2f} DOGE20 as rewards.")

    def staking_summary(self):
        """
        Print a summary of the staking process.
        """
        end_time = self.start_time + timedelta(days=365 * self.staking_duration)
        print(f"Staking Summary:")
        print(f"Initial Stake: {self.initial_stake} DOGE20")
        print(f"Total Rewards: {self.total_rewards:.2f} DOGE20")
        print(f"Staking Duration: {self.staking_duration} years")
        print(f"Staking Period: {self.start_time} to {end_time}")

def main():
    try:
        # User inputs
        initial_stake = float(input("Enter the initial DOGE20 stake amount: "))
        reward_rate = float(input("Enter the annual reward rate (e.g., 0.05 for 5%): "))
        staking_duration = int(input("Enter the staking duration in years: "))
        
        # Create staking instance
        doge20_staking = Doge20Staking(initial_stake, reward_rate, staking_duration)
        
        # Start the distribution process
        doge20_staking.distribute_rewards()
        
        # Display the summary of the staking process
        doge20_staking.staking_summary()
        
    except ValueError as e:
        print("Invalid input. Please enter numeric values for stake amount, reward rate, and duration.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
