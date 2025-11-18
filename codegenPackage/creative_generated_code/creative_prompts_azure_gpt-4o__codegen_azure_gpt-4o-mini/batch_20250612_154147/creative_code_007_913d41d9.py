"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dimo-chains.pages.dev
Prompt: Create a script to calculate rewards for drivers based on miles traveled using the DIMO app and the $DIMO token.
Generated: DETERMINISTIC_913d41d9f01ce7d1
Batch ID: 20250612_154147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Set up logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DriverRewardCalculator:
    def __init__(self, reward_rate_per_mile):
        """
        Initialize the DriverRewardCalculator with a specified reward rate.

        :param reward_rate_per_mile: The amount of $DIMO tokens earned per mile.
        """
        if reward_rate_per_mile < 0:
            logging.error("Reward rate per mile must be a non-negative value.")
            raise ValueError("Reward rate per mile must be a non-negative value.")
        self.reward_rate_per_mile = reward_rate_per_mile

    def calculate_reward(self, miles_traveled):
        """
        Calculate the reward for a driver based on miles traveled.

        :param miles_traveled: The total miles traveled by the driver.
        :return: The total reward in $DIMO tokens.
        """
        if miles_traveled < 0:
            logging.error("Miles traveled must be a non-negative value.")
            raise ValueError("Miles traveled must be a non-negative value.")
        
        reward = miles_traveled * self.reward_rate_per_mile
        logging.info(f"Calculated reward: {reward} $DIMO for {miles_traveled} miles traveled.")
        return reward

    def to_json(self, miles_traveled):
        """
        Convert the reward information to a JSON format.

        :param miles_traveled: The total miles traveled by the driver.
        :return: JSON string containing the reward information.
        """
        reward = self.calculate_reward(miles_traveled)
        reward_info = {
            'miles_traveled': miles_traveled,
            'reward': reward
        }
        return json.dumps(reward_info)

def main():
    try:
        # Initialize the reward calculator with a specified reward rate ($DIMO tokens per mile)
        calculator = DriverRewardCalculator(reward_rate_per_mile=0.05)  # Example: 0.05 $DIMO per mile
        
        # Example miles traveled
        miles_traveled = 150  # Example: 150 miles

        # Calculate the reward and output the result in JSON format
        reward_json = calculator.to_json(miles_traveled)
        print(reward_json)

    except ValueError as e:
        logging.error(f"ValueError: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
