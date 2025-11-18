"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeic2ctv7vwt47e6rhckifdcdc2wzxyddiqrge5yfp43c2nk2co6d2u.ipfs.dweb.link
Prompt: Create a Python script to track Bedrock ecosystem partner rewards (e.g., Diamonds, Pendle, Arbitrum) and calculate total yield.
Generated: DETERMINISTIC_6268415fe19d8705
Batch ID: 20250612_150228
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
from typing import Dict, List

# Configure logging for easy debugging and tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RewardTracker:
    def __init__(self):
        # Initialize the rewards dictionary to store rewards for each partner
        self.rewards: Dict[str, float] = {}

    def add_reward(self, partner: str, amount: float):
        """Add a reward amount for a specific partner.
        
        Args:
            partner (str): The name of the partner.
            amount (float): The amount of reward to add.
        """
        if amount < 0:
            logging.error("Attempted to add a negative reward amount for partner: %s", partner)
            raise ValueError("Reward amount must be non-negative.")
        
        # Add or update the partner's total reward
        self.rewards[partner] = self.rewards.get(partner, 0) + amount
        logging.info("Added %.2f to %s. Total now: %.2f", amount, partner, self.rewards[partner])

    def calculate_total_yield(self) -> float:
        """Calculate the total yield from all partner rewards.
        
        Returns:
            float: The total yield.
        """
        total_yield = sum(self.rewards.values())
        logging.info("Calculated total yield: %.2f", total_yield)
        return total_yield

    def load_rewards_from_file(self, file_path: str):
        """Load rewards from a JSON file.
        
        Args:
            file_path (str): The path to the JSON file containing rewards.
        """
        try:
            with open(file_path, 'r') as file:
                self.rewards = json.load(file)
                logging.info("Loaded rewards from %s", file_path)
        except FileNotFoundError:
            logging.error("File not found: %s", file_path)
            raise
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from the file: %s", file_path)
            raise

    def save_rewards_to_file(self, file_path: str):
        """Save current rewards to a JSON file.
        
        Args:
            file_path (str): The path to the JSON file to save.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.rewards, file, indent=4)
                logging.info("Saved rewards to %s", file_path)
        except IOError as e:
            logging.error("I/O error occurred while saving rewards: %s", e)
            raise

if __name__ == "__main__":
    # Example usage of the RewardTracker
    tracker = RewardTracker()
    
    # Adding some rewards
    tracker.add_reward('Diamonds', 100.0)
    tracker.add_reward('Pendle', 150.5)
    tracker.add_reward('Arbitrum', 200.75)

    # Calculating total yield
    total_yield = tracker.calculate_total_yield()
    print(f"Total Yield: {total_yield:.2f}")

    # Save to file and load from file example
    tracker.save_rewards_to_file('rewards.json')
    tracker.load_rewards_from_file('rewards.json')
```
