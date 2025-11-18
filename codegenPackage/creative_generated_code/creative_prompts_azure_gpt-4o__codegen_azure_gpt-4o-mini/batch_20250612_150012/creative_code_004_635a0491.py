"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yfyuyyufy.pages.dev
Prompt: Write a script to calculate the rewards for EarthNode operators based on network transaction volume, using the tokenomics model described in the World Mobile Token documentation.
Generated: DETERMINISTIC_635a0491c5623325
Batch ID: 20250612_150012
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

# Set up logging for better tracing of the execution
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EarthNodeRewardCalculator:
    def __init__(self, transaction_volume: float, reward_rate: float):
        """
        Initializes the reward calculator with transaction volume and reward rate.

        :param transaction_volume: The total volume of transactions on the network.
        :param reward_rate: The rate at which rewards are calculated per transaction volume.
        """
        self.transaction_volume = transaction_volume
        self.reward_rate = reward_rate

    def calculate_rewards(self) -> float:
        """
        Calculates the rewards for EarthNode operators based on transaction volume.

        :return: Total rewards earned.
        """
        if self.transaction_volume < 0:
            logging.error("Transaction volume cannot be negative.")
            raise ValueError("Transaction volume cannot be negative.")
        
        if self.reward_rate < 0:
            logging.error("Reward rate cannot be negative.")
            raise ValueError("Reward rate cannot be negative.")
        
        rewards = self.transaction_volume * self.reward_rate
        logging.info(f"Calculated rewards: {rewards}")
        return rewards

def load_config(file_path: str) -> dict:
    """
    Loads configuration from a JSON file.

    :param file_path: The path to the configuration file.
    :return: Configuration data as a dictionary.
    """
    try:
        with open(file_path, 'r') as config_file:
            config = json.load(config_file)
            logging.info("Configuration loaded successfully.")
            return config
    except FileNotFoundError:
        logging.error(f"Configuration file not found: {file_path}")
        raise
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from the configuration file: {file_path}")
        raise

def main():
    """
    Main function to execute the reward calculation process.
    """
    try:
        # Load configuration
        config = load_config('config.json')
        
        transaction_volume = config.get('transaction_volume', 0.0)
        reward_rate = config.get('reward_rate', 0.0)

        # Create a reward calculator instance
        calculator = EarthNodeRewardCalculator(transaction_volume, reward_rate)

        # Calculate and print the rewards
        rewards = calculator.calculate_rewards()
        print(f"Total rewards for EarthNode operators: {rewards:.2f}")

    except Exception as e:
        logging.critical(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

**Note**: Ensure you have a `config.json` file with the following structure in the same directory:

```json
{
    "transaction_volume": 10000.0,
    "reward_rate": 0.05
}
```
