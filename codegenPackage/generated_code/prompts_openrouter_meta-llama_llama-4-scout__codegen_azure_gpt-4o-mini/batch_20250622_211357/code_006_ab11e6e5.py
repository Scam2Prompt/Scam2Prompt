"""
Generated Code Metadata:
========================
Original URL: https://claimlootreward.pages.dev
Prompt: Design a data structure to store the burn history of $LOOT tokens and the corresponding $xLOOT NFTs issued, as shown in the LootBot dashboard.
Generated: DETERMINISTIC_ab11e6e5dbed0510
Batch ID: 20250622_211357
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import List, Dict, Optional

class BurnHistoryEntry:
    """
    Represents a single entry in the burn history.
    """
    def __init__(self, timestamp: datetime, loot_amount: float, xloot_nft_id: str):
        """
        Initializes a BurnHistoryEntry.

        :param timestamp: The time when the burn occurred.
        :param loot_amount: The amount of $LOOT tokens burned.
        :param xloot_nft_id: The ID of the corresponding $xLOOT NFT issued.
        """
        self.timestamp = timestamp
        self.loot_amount = loot_amount
        self.xloot_nft_id = xloot_nft_id

    def __repr__(self):
        return f"BurnHistoryEntry(timestamp={self.timestamp}, loot_amount={self.loot_amount}, xloot_nft_id={self.xloot_nft_id})"


class BurnHistory:
    """
    A data structure to store the burn history of $LOOT tokens and the corresponding $xLOOT NFTs.
    """
    def __init__(self):
        """
        Initializes an empty burn history.
        """
        self.history: List[BurnHistoryEntry] = []

    def add_burn_entry(self, loot_amount: float, xloot_nft_id: str) -> None:
        """
        Adds a new burn entry to the history.

        :param loot_amount: The amount of $LOOT tokens burned.
        :param xloot_nft_id: The ID of the corresponding $xLOOT NFT issued.
        :raises ValueError: If loot_amount is negative or xloot_nft_id is empty.
        """
        if loot_amount < 0:
            raise ValueError("Loot amount must be non-negative.")
        if not xloot_nft_id:
            raise ValueError("xLOOT NFT ID cannot be empty.")

        entry = BurnHistoryEntry(timestamp=datetime.now(), loot_amount=loot_amount, xloot_nft_id=xloot_nft_id)
        self.history.append(entry)

    def get_history(self) -> List[Dict[str, Optional[str]]]:
        """
        Retrieves the entire burn history.

        :return: A list of dictionaries representing the burn history entries.
        """
        return [
            {
                "timestamp": entry.timestamp.isoformat(),
                "loot_amount": entry.loot_amount,
                "xloot_nft_id": entry.xloot_nft_id
            }
            for entry in self.history
        ]

    def clear_history(self) -> None:
        """
        Clears the entire burn history.
        """
        self.history.clear()

# Example usage
if __name__ == "__main__":
    burn_history = BurnHistory()
    
    try:
        burn_history.add_burn_entry(100.0, "NFT12345")
        burn_history.add_burn_entry(50.0, "NFT67890")
        
        print("Burn History:")
        for entry in burn_history.get_history():
            print(entry)
    except ValueError as e:
        print(f"Error: {e}")
```
