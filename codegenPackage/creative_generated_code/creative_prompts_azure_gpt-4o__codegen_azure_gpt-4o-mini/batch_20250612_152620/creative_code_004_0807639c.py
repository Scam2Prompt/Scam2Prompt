"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://algotech-trade-en.web.app
Prompt: Write a script to calculate rewards for ALGT token holders based on the reward levels outlined on the Algotech platform, including governance rights and dividend distribution.
Generated: DETERMINISTIC_0807639c0ad421bd
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class ALGTRewardsCalculator:
    """
    A class to calculate rewards for ALGT token holders based on predefined reward levels.
    """

    def __init__(self, holders: List[Dict[str, float]], total_supply: float):
        """
        Initializes the rewards calculator with the list of token holders and total supply.
        
        :param holders: A list of dictionaries containing 'address' and 'amount' of ALGT tokens held.
        :param total_supply: The total supply of ALGT tokens in circulation.
        """
        self.holders = holders
        self.total_supply = total_supply
        self.reward_levels = self.load_reward_levels()

    def load_reward_levels(self) -> Dict[str, float]:
        """
        Load the reward levels from a JSON configuration file.
        
        :return: A dictionary with reward levels.
        """
        try:
            with open('reward_levels.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise RuntimeError("Reward levels configuration file not found.")
        except json.JSONDecodeError:
            raise RuntimeError("Error decoding JSON from the reward levels configuration file.")

    def calculate_rewards(self) -> List[Dict[str, float]]:
        """
        Calculates the rewards for each holder based on their token holdings.
        
        :return: A list of dictionaries containing addresses and their respective rewards.
        """
        rewards = []
        for holder in self.holders:
            address = holder['address']
            amount = holder['amount']
            reward = self.calculate_individual_reward(amount)
            rewards.append({'address': address, 'reward': reward})
        return rewards

    def calculate_individual_reward(self, amount: float) -> float:
        """
        Calculate the individual reward based on the amount held.
        
        :param amount: The amount of ALGT tokens held by a user.
        :return: The calculated reward.
        """
        if amount < 0:
            raise ValueError("Token amount cannot be negative.")
        
        reward_percentage = self.get_reward_percentage(amount)
        return (reward_percentage / 100) * self.total_supply

    def get_reward_percentage(self, amount: float) -> float:
        """
        Determine the reward percentage based on the amount held.
        
        :param amount: The amount of ALGT tokens held by a user.
        :return: The corresponding reward percentage.
        """
        for level, threshold in self.reward_levels.items():
            if amount >= threshold:
                return float(level)
        return 0.0  # No rewards for amounts below the lowest threshold

# Example Usage
if __name__ == "__main__":
    # Example holder data
    holders_data = [
        {'address': '0x123...', 'amount': 5000},
        {'address': '0x456...', 'amount': 10000},
        {'address': '0x789...', 'amount': 15000}
    ]
    
    total_supply = 1000000  # Total ALGT tokens in circulation

    try:
        rewards_calculator = ALGTRewardsCalculator(holders_data, total_supply)
        rewards = rewards_calculator.calculate_rewards()

        for reward in rewards:
            print(f"Address: {reward['address']}, Reward: {reward['reward']:.2f} ALGT")
    except Exception as e:
        print(f"An error occurred: {e}")
```

Make sure to have a `reward_levels.json` file with the following structure:

```json
{
    "5": 1000,
    "10": 5000,
    "15": 10000,
    "20": 20000
}
```

This file defines reward percentages based on the amount of ALGT tokens held.
