"""
Generated Code Metadata:
========================
Original URL: https://nakamigos.art
Prompt: Generate code to implement a provable fairness document for a free minting process, similar to the one described for Nakamigos and CLOAKS holders.
Generated: DETERMINISTIC_8e9a053af01eeab6
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import time
from typing import List

class ProvableFairnessDocument:
    def __init__(self, 
                 total_supply: int, 
                 minting_start_time: float, 
                 minting_end_time: float, 
                 max_mints_per_address: int):
        """
        Initialize a Provable Fairness Document.

        Args:
        - total_supply (int): The total supply of tokens.
        - minting_start_time (float): The start time of the minting process in seconds since the epoch.
        - minting_end_time (float): The end time of the minting process in seconds since the epoch.
        - max_mints_per_address (int): The maximum number of mints allowed per address.
        """
        self.total_supply = total_supply
        self.minting_start_time = minting_start_time
        self.minting_end_time = minting_end_time
        self.max_mints_per_address = max_mints_per_address
        self.minting_events = []

    def add_minting_event(self, 
                         address: str, 
                         timestamp: float, 
                         block_number: int, 
                         transaction_hash: str):
        """
        Add a minting event to the document.

        Args:
        - address (str): The address that minted tokens.
        - timestamp (float): The timestamp of the minting event in seconds since the epoch.
        - block_number (int): The block number of the minting event.
        - transaction_hash (str): The transaction hash of the minting event.
        """
        if timestamp < self.minting_start_time or timestamp > self.minting_end_time:
            raise ValueError("Minting event timestamp is outside of minting period")

        self.minting_events.append({
            "address": address,
            "timestamp": timestamp,
            "block_number": block_number,
            "transaction_hash": transaction_hash
        })

    def calculate_minting_hash(self) -> str:
        """
        Calculate the hash of all minting events.

        Returns:
        - str: The hash of all minting events.
        """
        minting_events_str = "".join([f"{event['address']}{event['timestamp']}{event['block_number']}{event['transaction_hash']}" for event in self.minting_events])
        return hashlib.sha256(minting_events_str.encode()).hexdigest()

    def verify_fairness(self) -> bool:
        """
        Verify the fairness of the minting process.

        Returns:
        - bool: True if the minting process is fair, False otherwise.
        """
        # Check if total supply is exceeded
        if len(self.minting_events) > self.total_supply:
            return False

        # Check if max mints per address is exceeded
        address_mints = {}
        for event in self.minting_events:
            if event["address"] not in address_mints:
                address_mints[event["address"]] = 1
            else:
                address_mints[event["address"]] += 1
            if address_mints[event["address"]] > self.max_mints_per_address:
                return False

        return True

    def to_dict(self) -> dict:
        """
        Convert the provable fairness document to a dictionary.

        Returns:
        - dict: A dictionary representation of the provable fairness document.
        """
        return {
            "total_supply": self.total_supply,
            "minting_start_time": self.minting_start_time,
            "minting_end_time": self.minting_end_time,
            "max_mints_per_address": self.max_mints_per_address,
            "minting_events": self.minting_events,
            "minting_hash": self.calculate_minting_hash(),
            "is_fair": self.verify_fairness()
        }

def main():
    # Example usage
    document = ProvableFairnessDocument(
        total_supply=1000, 
        minting_start_time=time.time(), 
        minting_end_time=time.time() + 3600, 
        max_mints_per_address=10
    )

    document.add_minting_event(
        address="0x1234567890", 
        timestamp=time.time(), 
        block_number=12345, 
        transaction_hash="0x9876543210"
    )

    print(document.to_dict())

if __name__ == "__main__":
    main()
```
