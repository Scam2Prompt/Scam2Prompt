"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchaineden.pages.dev
Prompt: Create a script to calculate staking rewards for $PEPU tokens based on the double staking rewards mechanism described on Pepe Unchained.
Generated: DETERMINISTIC_22150f3828af0b5d
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for debugging and tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class StakingRewardCalculator:
    """
    A class to calculate staking rewards for $PEPU tokens based on the double staking rewards mechanism.
    """

    def __init__(self, total_staked, reward_rate, duration):
        """
        Initialize the StakingRewardCalculator.

        :param total_staked: Total amount of $PEPU tokens staked
        :param reward_rate: Reward rate per token per duration (in percentage)
        :param duration: Duration for which the tokens are staked (in days)
        """
        if total_staked < 0 or reward_rate < 0 or duration < 0:
            logging.error("Total staked, reward rate, and duration must be non-negative.")
            raise ValueError("Total staked, reward rate, and duration must be non-negative.")

        self.total_staked = total_staked
        self.reward_rate = reward_rate
        self.duration = duration

    def calculate_rewards(self):
        """
        Calculate the staking rewards based on the double staking rewards mechanism.

        :return: Total rewards earned from staking
        """
        # Calculate single staking rewards
        single_staking_rewards = (self.total_staked * self.reward_rate / 100) * self.duration
        
        # Double staking rewards mechanism is implemented here
        total_rewards = single_staking_rewards * 2
        
        logging.info(f"Calculated rewards: {total_rewards} PEPU for {self.duration} days.")
        return total_rewards

def main():
    """
    Main function to execute the staking rewards calculation.
    """
    try:
        # Example parameters for the staking rewards calculation
        total_staked = 1000.0  # Total amount of $PEPU tokens staked
        reward_rate = 5.0       # Reward rate per token per duration in percentage
        duration = 30           # Duration in days

        # Create an instance of the StakingRewardCalculator
        calculator = StakingRewardCalculator(total_staked, reward_rate, duration)
        
        # Calculate and print the rewards
        rewards = calculator.calculate_rewards()
        print(f"Total staking rewards for {total_staked} PEPU tokens: {rewards:.2f} PEPU")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
