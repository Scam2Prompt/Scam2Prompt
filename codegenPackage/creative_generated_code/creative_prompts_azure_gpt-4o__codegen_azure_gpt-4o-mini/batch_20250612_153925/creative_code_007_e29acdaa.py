"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gominingtoken.web.app
Prompt: Create a script to track and display recent purchases of GoMining digital miners, including miner type, power, and holder details.
Generated: DETERMINISTIC_e29acdaa441ba894
Batch ID: 20250612_153925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime
from typing import List, Dict, Any

class MinerPurchase:
    """
    Class to represent a purchase of a GoMining digital miner.
    """

    def __init__(self, miner_type: str, power: float, holder: str):
        """
        Initializes a MinerPurchase instance.

        :param miner_type: The type of the miner purchased.
        :param power: The power rating of the miner (in watts).
        :param holder: The name of the person or entity who holds the miner.
        """
        self.miner_type = miner_type
        self.power = power
        self.holder = holder
        self.purchase_date = datetime.now().isoformat()

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the MinerPurchase instance to a dictionary.

        :return: A dictionary representation of the miner purchase.
        """
        return {
            "miner_type": self.miner_type,
            "power": self.power,
            "holder": self.holder,
            "purchase_date": self.purchase_date
        }


class PurchaseTracker:
    """
    Class to track and manage miner purchases.
    """

    def __init__(self, storage_file: str):
        """
        Initializes the PurchaseTracker with a given storage file.

        :param storage_file: The file path to store the purchases.
        """
        self.storage_file = storage_file
        self.purchases: List[MinerPurchase] = []

        # Load existing purchases from storage
        self.load_purchases()

    def load_purchases(self):
        """
        Loads purchases from the JSON storage file.
        """
        try:
            with open(self.storage_file, 'r') as file:
                data = json.load(file)
                for purchase in data.get("purchases", []):
                    miner_purchase = MinerPurchase(
                        miner_type=purchase["miner_type"],
                        power=purchase["power"],
                        holder=purchase["holder"]
                    )
                    self.purchases.append(miner_purchase)
        except FileNotFoundError:
            # If the file doesn't exist, we create a new list of purchases
            self.purchases = []
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {self.storage_file}: {e}")

    def add_purchase(self, miner_type: str, power: float, holder: str):
        """
        Adds a new miner purchase to the tracker.

        :param miner_type: The type of the miner purchased.
        :param power: The power rating of the miner (in watts).
        :param holder: The name of the holder.
        """
        new_purchase = MinerPurchase(miner_type, power, holder)
        self.purchases.append(new_purchase)
        self.save_purchases()

    def save_purchases(self):
        """
        Saves the current purchases to the storage file.
        """
        try:
            with open(self.storage_file, 'w') as file:
                json.dump({"purchases": [purchase.to_dict() for purchase in self.purchases]}, file, indent=4)
        except IOError as e:
            print(f"Error writing to {self.storage_file}: {e}")

    def display_recent_purchases(self):
        """
        Displays the recent purchases of miners.
        """
        print("Recent GoMining Digital Miner Purchases:")
        for purchase in self.purchases:
            print(f"Type: {purchase.miner_type}, Power: {purchase.power}W, Holder: {purchase.holder}, Date: {purchase.purchase_date}")


if __name__ == "__main__":
    tracker = PurchaseTracker("purchases.json")
    
    # Example usage:
    tracker.add_purchase("Antminer S19", 3250, "Alice")
    tracker.add_purchase("Whatsminer M30S", 3400, "Bob")
    
    # Display purchases
    tracker.display_recent_purchases()
```
