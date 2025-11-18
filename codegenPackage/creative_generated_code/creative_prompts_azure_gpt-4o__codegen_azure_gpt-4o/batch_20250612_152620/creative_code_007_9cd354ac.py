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
import sys

class StakingSimulation:
    """
    A class to simulate staking $SCOTTY tokens and calculate estimated rewards 
    over a specified period factoring in a dynamic rewards rate.
    """
    def __init__(self, initial_tokens, annual_rewards_rate, dynamic_rate_change):
        """
        Initialize the StakingSimulation instance.

        Parameters:
            initial_tokens (float): Number of $SCOTTY tokens staked initially.
            annual_rewards_rate (float): Initial annual rewards rate (percentage).
            dynamic_rate_change (float): Annual percentage change in rewards rate.
        """
        self.initial_tokens = initial_tokens
        self.annual_rewards_rate = annual_rewards_rate / 100  # Convert to decimal
        self.dynamic_rate_change = dynamic_rate_change / 100  # Convert to decimal

    def calculate_rewards(self, years=3):
        """
        Calculate estimated rewards over a specified period.

        Parameters:
            years (int): Number of years to simulate (default is 3).

        Returns:
            dict: A dictionary containing year-by-year rewards and final total.
        """
        staked_tokens = self.initial_tokens
        rewards_summary = {}
        current_rate = self.annual_rewards_rate

        for year in range(1, years + 1):
            # Calculate rewards for the current year
            annual_reward = staked_tokens * current_rate
            staked_tokens += annual_reward  # Compound staking rewards
            rewards_summary[year] = {
                "Reward": round(annual_reward, 2),
                "Total Tokens": round(staked_tokens, 2),
                "Annual Rate": round(current_rate * 100, 2)  # Convert rate back to percentage
            }

            # Adjust the rate dynamically for next year
            current_rate = max(current_rate + self.dynamic_rate_change, 0)  # Ensure rate doesn't go negative

        return rewards_summary

def main():
    """Main function to run the staking simulation."""
    try:
        # User inputs for simulation
        print("Welcome to the $SCOTTY Token Staking Simulator!")
        initial_tokens = float(input("Enter the number of $SCOTTY tokens you want to stake: "))
        annual_rewards_rate = float(input("Enter the initial annual rewards rate (percentage): "))
        dynamic_rate_change = float(input("Enter the annual rate change percentage (positive or negative): "))

        # Create simulation instance
        staking_simulation = StakingSimulation(initial_tokens, annual_rewards_rate, dynamic_rate_change)

        # Run simulation for 3 years
        rewards = staking_simulation.calculate_rewards(years=3)

        # Display results
        print("\nStaking Simulation Results (3 years):")
        for year, data in rewards.items():
            print(f"Year {year}:")
            print(f"  Reward Earned: {data['Reward']} $SCOTTY")
            print(f"  Total Tokens: {data['Total Tokens']} $SCOTTY")
            print(f"  Annual Rate: {data['Annual Rate']}%")
    except ValueError as e:
        print(f"Error: Invalid input. Please enter numeric values. ({e})")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
