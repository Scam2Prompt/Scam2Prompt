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

class DimoRewardCalculator:
    """
    DimoRewardCalculator calculates rewards for drivers based on miles traveled
    using the DIMO app and the $DIMO token.
    """

    def __init__(self, reward_rate_per_mile):
        """
        Initializes the reward calculator with a reward rate per mile.

        :param reward_rate_per_mile: The reward rate in $DIMO tokens per mile.
        """
        if reward_rate_per_mile <= 0:
            raise ValueError("Reward rate per mile must be greater than 0.")
        self.reward_rate_per_mile = reward_rate_per_mile

    def calculate_rewards(self, miles):
        """
        Calculates the rewards in $DIMO tokens based on miles traveled.

        :param miles: Total miles traveled by the driver.
        :return: Rewards in $DIMO tokens.
        """
        if miles < 0:
            raise ValueError("Miles traveled cannot be negative.")
        return round(miles * self.reward_rate_per_mile, 2)

def load_driver_data(file_path):
    """
    Loads driver data from a JSON file.

    :param file_path: Path to the JSON file containing driver data.
    :return: A list of dictionaries containing driver data.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Error decoding JSON from file: {file_path}")

def save_rewards_to_file(file_path, rewards_data):
    """
    Saves the rewards data to a JSON file.

    :param file_path: Path to the JSON file to save the rewards data.
    :param rewards_data: A dictionary containing driver rewards data.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(rewards_data, file, indent=4)
    except IOError as e:
        raise IOError(f"Error saving rewards to file: {file_path}. {e}")

def main():
    """
    Main function of the script, calculates rewards for drivers based on miles traveled
    and saves the results to a file.
    """
    # Configuration
    driver_data_file = "drivers.json"
    rewards_output_file = "rewards.json"
    reward_rate_per_mile = 0.1  # $DIMO tokens per mile

    try:
        # Load driver data
        driver_data = load_driver_data(driver_data_file)

        # Initialize the reward calculator
        calculator = DimoRewardCalculator(reward_rate_per_mile)

        # Calculate rewards for each driver
        rewards = {}
        for driver in driver_data:
            driver_id = driver.get("id")
            miles = driver.get("miles_traveled")

            if driver_id is None or miles is None:
                print(f"Skipping invalid driver data: {driver}")
                continue

            try:
                rewards[driver_id] = {
                    "miles_traveled": miles,
                    "rewards_in_dimo": calculator.calculate_rewards(miles)
                }
            except ValueError as e:
                print(f"Error calculating rewards for driver {driver_id}: {e}")
        
        # Save rewards to file
        save_rewards_to_file(rewards_output_file, rewards)

        print("Rewards calculation completed successfully.")
        print(f"Rewards data saved to {rewards_output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
