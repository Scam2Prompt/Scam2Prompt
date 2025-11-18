"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jhwedfuhuifhw0928.xyz
Prompt: Write a script to calculate the total rewards earned per day based on the current APY and token balances provided by the Ethena platform.
Generated: DETERMINISTIC_ec7533052f48996b
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime, timedelta

class RewardCalculator:
    def __init__(self, apy: float, token_balances: dict):
        """
        Initialize the RewardCalculator with the annual percentage yield (APY)
        and a dictionary of token balances.

        :param apy: Annual Percentage Yield as a decimal (e.g., 0.05 for 5%)
        :param token_balances: Dictionary with token names as keys and their balances as values
        """
        self.apy = apy
        self.token_balances = token_balances

    def calculate_daily_rewards(self) -> dict:
        """
        Calculate the total rewards earned per day based on the current APY
        and token balances.

        :return: Dictionary with token names as keys and daily rewards earned as values
        """
        daily_rewards = {}

        # Calculate daily rate from APY
        daily_rate = self.apy / 365
        for token, balance in self.token_balances.items():
            # Calculate daily reward for each token
            daily_reward = balance * daily_rate
            
            # Store the result in the dictionary
            daily_rewards[token] = daily_reward

        return daily_rewards

def load_config(file_path: str) -> tuple:
    """
    Load the configuration file containing the APY and token balances.

    :param file_path: Path to the JSON configuration file
    :return: A tuple containing the APY and token balances
    """
    try:
        with open(file_path, 'r') as file:
            config = json.load(file)
            apy = config.get('apy', 0.0)
            token_balances = config.get('token_balances', {})
            return apy, token_balances
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise ValueError(f"Error loading configuration: {e}")

def main():
    """
    Main function to execute the reward calculation.
    """
    config_file_path = 'config.json'  # Path to the JSON configuration file

    try:
        # Load configuration
        apy, token_balances = load_config(config_file_path)

        # Initialize the reward calculator
        calculator = RewardCalculator(apy, token_balances)

        # Calculate daily rewards
        daily_rewards = calculator.calculate_daily_rewards()

        # Print the results
        print(f"Daily Rewards Calculation as of {datetime.now().strftime('%Y-%m-%d')}:")
        for token, reward in daily_rewards.items():
            print(f"{token}: {reward:.6f}")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```

**Note**: Ensure that you place a JSON configuration file named `config.json` in the same directory as this script. The JSON file should contain the APY and token balances in the following format:

```json
{
    "apy": 0.05,
    "token_balances": {
        "ETH": 10.0,
        "DAI": 2000.0
    }
}
```
