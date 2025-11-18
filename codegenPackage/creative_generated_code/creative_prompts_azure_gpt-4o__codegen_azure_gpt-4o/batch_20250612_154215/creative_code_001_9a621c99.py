"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aigentmigrateagixdapp.pages.dev
Prompt: Generate a script for tracking ETH rewards allocation and total staked amounts in the AIX ecosystem using the data provided in the migration dashboard.
Generated: DETERMINISTIC_9a621c995f1b5631
Batch ID: 20250612_154215
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
from typing import List, Dict

# Configure logging for error tracking and debugging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("eth_rewards_tracker.log"),
        logging.StreamHandler()
    ]
)

class ETHRewardsTracker:
    def __init__(self):
        """
        Initialize an instance of ETHRewardsTracker.
        """
        self.total_staked = 0.0  # Total ETH staked in the ecosystem
        self.rewards_allocation: Dict[str, float] = {}  # Rewards allocation per user

    def load_migration_data(self, filepath: str) -> List[Dict]:
        """
        Load migration data from the dashboard JSON file.
        
        Args:
        filepath (str): Path to the JSON file containing migration data.
        
        Returns:
        List[Dict]: List of migration records.
        """
        try:
            with open(filepath, 'r') as file:
                data = json.load(file)
            logging.info("Migration data loaded successfully.")
            return data
        except FileNotFoundError as e:
            logging.error(f"File not found: {filepath}")
            raise e
        except json.JSONDecodeError as e:
            logging.error("Failed to parse JSON file.")
            raise e

    def calculate_rewards(self, migration_data: List[Dict]):
        """
        Calculate rewards allocation and total staked amounts based on migration data.
        
        Args:
        migration_data (List[Dict]): List of migration records loaded from JSON file.
        """
        try:
            for record in migration_data:
                user_address = record.get("user_address")
                staked_amount = float(record.get("staked_amount", 0))
                reward_percentage = float(record.get("reward_percentage", 0))

                # Update total staked ETH
                self.total_staked += staked_amount

                # Calculate reward allocation
                reward_allocation = staked_amount * (reward_percentage / 100)

                # Store rewards allocation by user
                self.rewards_allocation[user_address] = self.rewards_allocation.get(user_address, 0) + reward_allocation

            logging.info("Rewards calculation completed successfully.")
        except KeyError as e:
            logging.error(f"Missing required key in migration data: {str(e)}")
            raise e
        except ValueError as e:
            logging.error(f"Invalid data format in migration data: {str(e)}")
            raise e

    def display_results(self):
        """
        Display the total staked amount and rewards allocation.
        """
        print("=== ETH Rewards Tracker ===")
        print(f"Total ETH Staked: {self.total_staked:.4f} ETH")
        print("Rewards Allocation:")
        for user, reward in self.rewards_allocation.items():
            print(f"User {user}: {reward:.4f} ETH")

    def save_results(self, filepath: str):
        """
        Save the rewards allocation and total staked amount to a JSON file.

        Args:
        filepath (str): Path to the output JSON file.
        """
        results = {
            "total_staked": self.total_staked,
            "rewards_allocation": self.rewards_allocation
        }
        try:
            with open(filepath, 'w') as file:
                json.dump(results, file, indent=4)
            logging.info("Results saved successfully.")
        except IOError as e:
            logging.error(f"Failed to write results to file: {filepath}")
            raise e

if __name__ == "__main__":
    # File paths for input and output data
    migration_data_file = "migration_dashboard.json"
    output_results_file = "eth_rewards_results.json"

    # Initialize the rewards tracker
    tracker = ETHRewardsTracker()

    try:
        # Load migration data
        migration_data = tracker.load_migration_data(migration_data_file)

        # Calculate rewards and total staked amounts
        tracker.calculate_rewards(migration_data)

        # Display the results
        tracker.display_results()

        # Save the results to a file
        tracker.save_results(output_results_file)
    except Exception as e:
        logging.error(f"An error occurred during execution: {str(e)}")
```

This Python script fulfills the requirements of the request, including error handling, clean code structure, and documentation via comments.
