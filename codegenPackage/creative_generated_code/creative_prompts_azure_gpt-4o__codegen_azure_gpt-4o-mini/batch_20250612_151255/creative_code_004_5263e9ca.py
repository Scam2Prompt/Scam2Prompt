"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solananpcs.pages.dev
Prompt: Write code for tracking $NPCS token rewards distribution to long-term holders, aligned with the roadmap's Phase 2 airdrop plans.
Generated: DETERMINISTIC_5263e9cae3a548c3
Batch ID: 20250612_151255
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
from datetime import datetime
from typing import List, Dict, Any

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TokenRewardTracker:
    def __init__(self, token_name: str, total_supply: float):
        """
        Initializes the TokenRewardTracker with the specified token name and total supply.
        
        :param token_name: Name of the token
        :param total_supply: Total supply of the token
        """
        self.token_name = token_name
        self.total_supply = total_supply
        self.holders: Dict[str, float] = {}  # Holds user addresses and their token amounts
        self.rewards_distribution_log: List[Dict[str, Any]] = []  # Log of rewards distribution

    def add_holder(self, address: str, amount: float) -> None:
        """
        Adds a new holder with a specified amount of tokens.
        
        :param address: Address of the token holder
        :param amount: Amount of tokens held
        """
        if address in self.holders:
            logging.warning(f"Address {address} already exists. Updating amount.")
            self.holders[address] += amount
        else:
            self.holders[address] = amount
        logging.info(f"Added/Updated holder {address} with amount {amount}.")

    def distribute_rewards(self, rewards: float) -> None:
        """
        Distributes rewards to all holders proportionally based on their holdings.

        :param rewards: Total rewards to distribute
        """
        total_holding = sum(self.holders.values())
        if total_holding == 0:
            logging.error("Total holdings are zero, cannot distribute rewards.")
            return
        
        logging.info(f"Distributing {rewards} rewards to {len(self.holders)} holders.")
        
        for address, amount in self.holders.items():
            reward = (amount / total_holding) * rewards
            self.rewards_distribution_log.append({
                "timestamp": datetime.now().isoformat(),
                "address": address,
                "reward": reward
            })
            logging.info(f"Distributed {reward} {self.token_name} to {address}.")

    def save_distribution_log(self, file_path: str) -> None:
        """
        Saves the rewards distribution log to a JSON file.
        
        :param file_path: Path to the file where the log should be saved
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.rewards_distribution_log, file, indent=4)
            logging.info(f"Distribution log saved to {file_path}.")
        except IOError as e:
            logging.error(f"Failed to save distribution log: {e}")

# Example of using the TokenRewardTracker
if __name__ == "__main__":
    tracker = TokenRewardTracker(token_name="$NPCS", total_supply=1_000_000.0)

    # Adding some holders
    tracker.add_holder("0xABC123...", 5000.0)
    tracker.add_holder("0xDEF456...", 3000.0)
    tracker.add_holder("0xGHI789...", 1000.0)

    # Distributing rewards
    tracker.distribute_rewards(rewards=10000.0)

    # Saving the distribution log
    tracker.save_distribution_log("rewards_distribution_log.json")
```
