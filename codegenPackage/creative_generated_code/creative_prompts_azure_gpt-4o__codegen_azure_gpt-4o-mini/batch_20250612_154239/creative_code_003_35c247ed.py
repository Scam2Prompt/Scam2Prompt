"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimedsonic.pages.dev
Prompt: Write a script to handle staking operations for blockchain guilds, incorporating features similar to those described in Guildhall's "Staking" section.
Generated: DETERMINISTIC_35c247ed2e364528
Batch ID: 20250612_154239
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
from typing import Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class StakingOperation:
    def __init__(self, ledger_file: str):
        self.ledger_file = ledger_file
        self.stakers = self.load_ledger()

    def load_ledger(self) -> Dict[str, Any]:
        """Load the staking ledger from a JSON file."""
        try:
            with open(self.ledger_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            logging.warning("Ledger file not found. Initializing a new ledger.")
            return {}
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from the ledger file.")
            return {}

    def save_ledger(self):
        """Save the staking ledger to a JSON file."""
        with open(self.ledger_file, 'w') as file:
            json.dump(self.stakers, file, indent=4)
            logging.info("Ledger saved successfully.")

    def stake(self, user_id: str, amount: float) -> None:
        """Handle staking operation for a user."""
        if amount <= 0:
            logging.error("Invalid stake amount: must be greater than zero.")
            raise ValueError("Stake amount must be greater than zero.")
        
        if user_id not in self.stakers:
            self.stakers[user_id] = {'staked_amount': 0.0}
        
        self.stakers[user_id]['staked_amount'] += amount
        logging.info(f"User {user_id} has staked {amount}. Total staked: {self.stakers[user_id]['staked_amount']}.")
        self.save_ledger()

    def unstake(self, user_id: str, amount: float) -> None:
        """Handle unstaking operation for a user."""
        if user_id not in self.stakers:
            logging.error(f"User {user_id} does not have a staking record.")
            raise ValueError("User does not have a staking record.")
        
        if amount <= 0:
            logging.error("Invalid unstake amount: must be greater than zero.")
            raise ValueError("Unstake amount must be greater than zero.")
        
        if self.stakers[user_id]['staked_amount'] < amount:
            logging.error("Insufficient staked amount for the unstake operation.")
            raise ValueError("Insufficient staked amount.")
        
        self.stakers[user_id]['staked_amount'] -= amount
        logging.info(f"User {user_id} has unstaked {amount}. Total staked: {self.stakers[user_id]['staked_amount']}.")
        self.save_ledger()

    def get_staked_amount(self, user_id: str) -> float:
        """Retrieve the total staked amount for a user."""
        return self.stakers.get(user_id, {'staked_amount': 0.0})['staked_amount']

def main():
    """Main function to demonstrate staking operations."""
    ledger_file = 'staking_ledger.json'
    staking = StakingOperation(ledger_file)

    # Example operations
    try:
        staking.stake("user1", 50.0)
        staking.unstake("user1", 20.0)
        total_staked = staking.get_staked_amount("user1")
        logging.info(f"Total staked amount for user1: {total_staked}")
    except ValueError as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
