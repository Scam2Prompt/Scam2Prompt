"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uni-token.com
Prompt: Create a custom solution for the traceability of collectible items, incorporating the features described on Unitoken's website.
Generated: DETERMINISTIC_aeb9bdf11400aff1
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import hashlib
from datetime import datetime

class CollectibleItem:
    """
    A class to represent a collectible item with traceability features.
    """

    def __init__(self, item_id, name, description, owner):
        """
        Initialize a new collectible item.

        :param item_id: Unique identifier for the item.
        :param name: Name of the collectible item.
        :param description: Description of the collectible item.
        :param owner: Current owner of the collectible item.
        """
        self.item_id = item_id
        self.name = name
        self.description = description
        self.owner = owner
        self.history = []
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        
        # Log the creation of the item in history
        self._log_history(f"Item created by {self.owner}.")

    def _log_history(self, action):
        """
        Logs actions taken on the collectible item.

        :param action: The action to log.
        """
        timestamp = datetime.now()
        self.history.append({"action": action, "timestamp": timestamp.isoformat()})
        self.updated_at = timestamp

    def transfer_ownership(self, new_owner):
        """
        Transfers ownership of the collectible item to a new owner.

        :param new_owner: The new owner's name.
        :raises ValueError: If new_owner is the same as the current owner.
        """
        if new_owner == self.owner:
            raise ValueError("New owner must be different from the current owner.")
        
        # Log the ownership transfer
        self._log_history(f"Ownership transferred from {self.owner} to {new_owner}.")
        self.owner = new_owner

    def get_item_info(self):
        """
        Returns the information of the collectible item.

        :return: Dictionary containing the item information.
        """
        return {
            "item_id": self.item_id,
            "name": self.name,
            "description": self.description,
            "owner": self.owner,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "history": self.history
        }

    def to_json(self):
        """
        Serializes the collectible item to a JSON string.

        :return: JSON representation of the collectible item.
        """
        return json.dumps(self.get_item_info(), indent=4)

def generate_item_id(name, owner):
    """
    Generates a unique ID for a collectible item based on its name and owner.

    :param name: Name of the item.
    :param owner: Owner of the item.
    :return: Unique item ID.
    """
    unique_string = f"{name}-{owner}-{datetime.now().isoformat()}"
    return hashlib.sha256(unique_string.encode()).hexdigest()

# Example usage:
if __name__ == "__main__":
    try:
        item_id = generate_item_id("Rare Coin", "Alice")
        collectible = CollectibleItem(item_id, "Rare Coin", "A rare collectible coin.", "Alice")
        
        # Transfer ownership
        collectible.transfer_ownership("Bob")
        
        # Print item information
        print(collectible.to_json())
    except Exception as e:
        print(f"An error occurred: {e}")
```
