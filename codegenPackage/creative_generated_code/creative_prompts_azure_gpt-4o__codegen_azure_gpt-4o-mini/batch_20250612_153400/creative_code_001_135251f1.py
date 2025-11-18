"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-poodlinu.pages.dev
Prompt: Generate code to calculate staking rewards for $POODL tokens based on the annual percentage rate (176%) and the total amount staked. Include functionality to display the rewards in real-time.
Generated: DETERMINISTIC_135251f15586e855
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class StakingRewardsCalculator:
    def __init__(self, annual_percentage_rate: float, total_staked: float):
        """
        Initializes the staking rewards calculator.
        
        :param annual_percentage_rate: The annual percentage rate for staking rewards (in percentage).
        :param total_staked: The total amount of tokens staked.
        """
        self.annual_percentage_rate = annual_percentage_rate / 100  # Convert to decimal
        self.total_staked = total_staked

    def calculate_rewards(self, time_period: float) -> float:
        """
        Calculate the staking rewards over a given time period.
        
        :param time_period: The time period for which rewards are calculated (in days).
        :return: The calculated rewards.
        """
        try:
            if time_period < 0:
                raise ValueError("Time period cannot be negative.")
                
            # Calculate daily rate
            daily_rate = self.annual_percentage_rate / 365
            # Calculate rewards
            rewards = self.total_staked * daily_rate * time_period
            return rewards
        
        except Exception as e:
            print(f"Error calculating rewards: {e}")
            return 0.0

    def display_rewards(self, refresh_interval: int = 5):
        """
        Continuously display the calculated rewards in real-time.

        :param refresh_interval: The interval (in seconds) to refresh the rewards display.
        """
        print("Real-time Staking Rewards Display (Press Ctrl+C to stop):")
        try:
            while True:
                # Assume we want to calculate rewards for a time period of 1 day
                rewards = self.calculate_rewards(1)  # 1 day
                print(f"Current Staking Rewards: {rewards:.2f} POODL tokens")
                
                time.sleep(refresh_interval)
        
        except KeyboardInterrupt:
            print("\nReal-time display stopped.")
        except Exception as e:
            print(f"Error during display: {e}")

if __name__ == "__main__":
    # Example usage
    annual_percentage_rate = 176  # Annual Percentage Rate for staking
    total_staked = 1000  # Total amount of $POODL tokens staked

    # Create a StakingRewardsCalculator instance
    rewards_calculator = StakingRewardsCalculator(annual_percentage_rate, total_staked)
    
    # Start displaying rewards in real-time
    rewards_calculator.display_rewards()
```
