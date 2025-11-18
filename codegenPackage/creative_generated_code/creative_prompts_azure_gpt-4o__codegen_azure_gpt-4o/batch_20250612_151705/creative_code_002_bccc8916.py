"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lyvely-claim.pages.dev
Prompt: Generate code for setting up a tiered tipping system on a platform, inspired by Lyvely's "Grateful" feature, with customizable tip amounts.
Generated: DETERMINISTIC_bccc891688c4ba8f
Batch ID: 20250612_151705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# tipping_system.py

from typing import List, Dict


class TippingSystem:
    """
    A class to manage a tiered tipping system with customizable tip amounts.
    """

    def __init__(self):
        """
        Initializes the TippingSystem with default tiers.
        """
        self.tiers = [
            {"name": "Bronze", "amount": 5},  # Default tier with $5 tip
            {"name": "Silver", "amount": 10}, # Default tier with $10 tip
            {"name": "Gold", "amount": 20},  # Default tier with $20 tip
        ]

    def get_tiers(self) -> List[Dict[str, str]]:
        """
        Retrieves the list of tipping tiers.

        :return: A list of dictionaries representing the tiers.
        """
        return self.tiers

    def add_tier(self, name: str, amount: float) -> None:
        """
        Adds a new tier to the tipping system.

        :param name: The name of the tier (e.g., "Platinum").
        :param amount: The monetary value of the tier.
        :raises ValueError: If the amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Tip amount must be a positive number.")
        self.tiers.append({"name": name, "amount": amount})

    def remove_tier(self, name: str) -> None:
        """
        Removes a tier from the tipping system by name.

        :param name: The name of the tier to remove.
        :raises ValueError: If the tier name does not exist.
        """
        for tier in self.tiers:
            if tier["name"].lower() == name.lower():
                self.tiers.remove(tier)
                return
        raise ValueError(f"Tier '{name}' not found.")

    def update_tier(self, name: str, new_amount: float) -> None:
        """
        Updates the tip amount for an existing tier.

        :param name: The name of the tier to update.
        :param new_amount: The new monetary value for the tier.
        :raises ValueError: If the tier is not found or the new amount is not positive.
        """
        if new_amount <= 0:
            raise ValueError("Tip amount must be a positive number.")

        for tier in self.tiers:
            if tier["name"].lower() == name.lower():
                tier["amount"] = new_amount
                return
        raise ValueError(f"Tier '{name}' not found.")

    def get_tip_amount(self, name: str) -> float:
        """
        Retrieves the tip amount for a specific tier.

        :param name: The name of the tier to retrieve the amount from.
        :return: The monetary value of the tier.
        :raises ValueError: If the tier is not found.
        """
        for tier in self.tiers:
            if tier["name"].lower() == name.lower():
                return tier["amount"]
        raise ValueError(f"Tier '{name}' not found.")


if __name__ == "__main__":
    # Example usage of TippingSystem
    tipping_system = TippingSystem()

    try:
        print("Available Tiers:", tipping_system.get_tiers())

        # Add a new tier
        tipping_system.add_tier("Platinum", 50)
        print("Added Platinum Tier:", tipping_system.get_tiers())

        # Update an existing tier
        tipping_system.update_tier("Silver", 15)
        print("Updated Silver Tier:", tipping_system.get_tiers())

        # Get tip amount for a tier
        tip_amount = tipping_system.get_tip_amount("Gold")
        print("Gold Tier Tip Amount:", tip_amount)

        # Remove a tier
        tipping_system.remove_tier("Bronze")
        print("Removed Bronze Tier:", tipping_system.get_tiers())

    except ValueError as e:
        print(f"Error: {e}")
```
