"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdwin.lat
Prompt: Generate a script that calculates potential rewards based on participation in the USDT Reward Program.
Generated: DETERMINISTIC_58f9d64ad42133a0
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class USDTRewardProgram:
    def __init__(self, base_reward_rate, participation_amount):
        """
        Initializes the USDTRewardProgram class.

        :param base_reward_rate: The base rate of rewards per USDT participated.
        :param participation_amount: The amount of USDT the user participates with.
        """
        self.base_reward_rate = base_reward_rate
        self.participation_amount = participation_amount

    def calculate_rewards(self):
        """
        Calculates the total rewards based on participation.

        :return: Total rewards earned.
        """
        try:
            if self.participation_amount < 0:
                raise ValueError("Participation amount must be non-negative.")

            total_rewards = self.base_reward_rate * self.participation_amount
            return total_rewards

        except Exception as e:
            logging.error(f"Error calculating rewards: {e}")
            return 0

def main():
    """
    Main function to run the reward calculation.
    """
    # Example configuration
    base_reward_rate = 0.05  # Reward rate per USDT
    participation_amount = 1000  # USDT participated

    # Initialize the reward program
    reward_program = USDTRewardProgram(base_reward_rate, participation_amount)

    # Calculate and display the rewards
    total_rewards = reward_program.calculate_rewards()
    logging.info(f"Total rewards earned: {total_rewards} USDT")

if __name__ == "__main__":
    main()
```
