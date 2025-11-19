"""
Generated Code Metadata:
========================
Original URL: https://whales-market-8x5.pages.dev
Prompt: "How would you integrate Runes and WLs (whitelist) management into a digital asset marketplace, considering the features shown on Whales Market?"
Generated: DETERMINISTIC_690ab9c94926211a
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Digital Asset Marketplace: Runes and Whitelist (WL) Management Integration

This script provides a basic implementation for managing Runes and Whitelists (WLs) in a digital asset marketplace.
It includes functionality for adding/removing Runes, managing WLs, and verifying user access based on WL status.
"""

from typing import List, Dict, Optional


class Marketplace:
    def __init__(self):
        """
        Initialize the marketplace with empty Runes and Whitelist (WL) data structures.
        """
        self.runes: Dict[str, Dict] = {}  # Runes storage: {rune_id: {name, description, price}}
        self.whitelist: List[str] = []  # Whitelist storage: List of user IDs

    # Runes Management
    def add_rune(self, rune_id: str, name: str, description: str, price: float) -> None:
        """
        Add a new Rune to the marketplace.

        :param rune_id: Unique identifier for the Rune.
        :param name: Name of the Rune.
        :param description: Description of the Rune.
        :param price: Price of the Rune.
        """
        if rune_id in self.runes:
            raise ValueError(f"Rune with ID '{rune_id}' already exists.")
        self.runes[rune_id] = {
            "name": name,
            "description": description,
            "price": price
        }

    def remove_rune(self, rune_id: str) -> None:
        """
        Remove a Rune from the marketplace.

        :param rune_id: Unique identifier for the Rune to be removed.
        """
        if rune_id not in self.runes:
            raise ValueError(f"Rune with ID '{rune_id}' does not exist.")
        del self.runes[rune_id]

    def list_runes(self) -> List[Dict]:
        """
        List all Runes available in the marketplace.

        :return: List of Runes with their details.
        """
        return [{"id": rune_id, **details} for rune_id, details in self.runes.items()]

    # Whitelist Management
    def add_to_whitelist(self, user_id: str) -> None:
        """
        Add a user to the whitelist.

        :param user_id: Unique identifier for the user.
        """
        if user_id in self.whitelist:
            raise ValueError(f"User '{user_id}' is already whitelisted.")
        self.whitelist.append(user_id)

    def remove_from_whitelist(self, user_id: str) -> None:
        """
        Remove a user from the whitelist.

        :param user_id: Unique identifier for the user.
        """
        if user_id not in self.whitelist:
            raise ValueError(f"User '{user_id}' is not in the whitelist.")
        self.whitelist.remove(user_id)

    def is_whitelisted(self, user_id: str) -> bool:
        """
        Check if a user is whitelisted.

        :param user_id: Unique identifier for the user.
        :return: True if the user is whitelisted, False otherwise.
        """
        return user_id in self.whitelist

    # Marketplace Access
    def purchase_rune(self, user_id: str, rune_id: str) -> Optional[Dict]:
        """
        Allow a whitelisted user to purchase a Rune.

        :param user_id: Unique identifier for the user.
        :param rune_id: Unique identifier for the Rune.
        :return: Details of the purchased Rune if successful, None otherwise.
        """
        if not self.is_whitelisted(user_id):
            raise PermissionError(f"User '{user_id}' is not whitelisted and cannot purchase Runes.")
        if rune_id not in self.runes:
            raise ValueError(f"Rune with ID '{rune_id}' does not exist.")
        return self.runes[rune_id]


# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the marketplace
        marketplace = Marketplace()

        # Add Runes
        marketplace.add_rune("rune1", "Fire Rune", "A powerful fire-based rune.", 100.0)
        marketplace.add_rune("rune2", "Water Rune", "A calming water-based rune.", 80.0)

        # Add users to the whitelist
        marketplace.add_to_whitelist("user123")
        marketplace.add_to_whitelist("user456")

        # List available Runes
        print("Available Runes:", marketplace.list_runes())

        # Purchase a Rune
        purchased_rune = marketplace.purchase_rune("user123", "rune1")
        print("Purchased Rune:", purchased_rune)

        # Remove a Rune
        marketplace.remove_rune("rune2")

        # Remove a user from the whitelist
        marketplace.remove_from_whitelist("user456")

    except Exception as e:
        print(f"Error: {e}")
```
