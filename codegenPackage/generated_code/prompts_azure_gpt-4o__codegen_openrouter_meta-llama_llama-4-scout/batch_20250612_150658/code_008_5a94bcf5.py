"""
Generated Code Metadata:
========================
Original URL: https://tonroll.cc
Prompt: Write code to implement a subscription system where traders earn bonuses based on the number of users copying their trades, as outlined in Earnie's app features.
Generated: DETERMINISTIC_5a94bcf532757935
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# subscription_system.py

from typing import Dict
from datetime import datetime, timedelta

class Trader:
    """Represents a trader with a unique ID and a list of copiers."""

    def __init__(self, trader_id: int):
        """
        Initializes a Trader object.

        Args:
        trader_id (int): Unique ID of the trader.
        """
        self.trader_id = trader_id
        self.copiers = []
        self.bonus_history = []

    def add_copier(self, copier_id: int):
        """
        Adds a copier to the trader's list of copiers.

        Args:
        copier_id (int): Unique ID of the copier.
        """
        self.copiers.append(copier_id)

    def remove_copier(self, copier_id: int):
        """
        Removes a copier from the trader's list of copiers.

        Args:
        copier_id (int): Unique ID of the copier.
        """
        if copier_id in self.copiers:
            self.copiers.remove(copier_id)

    def calculate_bonus(self, num_copiers: int) -> float:
        """
        Calculates the bonus based on the number of copiers.

        Args:
        num_copiers (int): Number of copiers.

        Returns:
        float: The calculated bonus.
        """
        # Bonus structure: 10% for 1-10 copiers, 20% for 11-50 copiers, 30% for 51+ copiers
        if num_copiers <= 10:
            return 0.10
        elif num_copiers <= 50:
            return 0.20
        else:
            return 0.30

    def update_bonus_history(self, bonus: float):
        """
        Updates the trader's bonus history.

        Args:
        bonus (float): The bonus to add to the history.
        """
        self.bonus_history.append({"date": datetime.now(), "bonus": bonus})


class SubscriptionSystem:
    """Manages traders and their copiers, and calculates bonuses."""

    def __init__(self):
        """
        Initializes a SubscriptionSystem object.
        """
        self.traders: Dict[int, Trader] = {}

    def add_trader(self, trader_id: int):
        """
        Adds a trader to the system.

        Args:
        trader_id (int): Unique ID of the trader.
        """
        if trader_id not in self.traders:
            self.traders[trader_id] = Trader(trader_id)

    def remove_trader(self, trader_id: int):
        """
        Removes a trader from the system.

        Args:
        trader_id (int): Unique ID of the trader.
        """
        if trader_id in self.traders:
            del self.traders[trader_id]

    def add_copier(self, trader_id: int, copier_id: int):
        """
        Adds a copier to a trader.

        Args:
        trader_id (int): Unique ID of the trader.
        copier_id (int): Unique ID of the copier.
        """
        if trader_id in self.traders:
            self.traders[trader_id].add_copier(copier_id)

    def remove_copier(self, trader_id: int, copier_id: int):
        """
        Removes a copier from a trader.

        Args:
        trader_id (int): Unique ID of the trader.
        copier_id (int): Unique ID of the copier.
        """
        if trader_id in self.traders:
            self.traders[trader_id].remove_copier(copier_id)

    def calculate_trader_bonus(self, trader_id: int) -> float:
        """
        Calculates the bonus for a trader based on their copiers.

        Args:
        trader_id (int): Unique ID of the trader.

        Returns:
        float: The calculated bonus.
        """
        if trader_id in self.traders:
            num_copiers = len(self.traders[trader_id].copiers)
            bonus = self.traders[trader_id].calculate_bonus(num_copiers)
            self.traders[trader_id].update_bonus_history(bonus)
            return bonus
        else:
            raise ValueError("Trader not found")

    def get_trader_bonus_history(self, trader_id: int) -> list:
        """
        Gets the bonus history for a trader.

        Args:
        trader_id (int): Unique ID of the trader.

        Returns:
        list: The bonus history for the trader.
        """
        if trader_id in self.traders:
            return self.traders[trader_id].bonus_history
        else:
            raise ValueError("Trader not found")


def main():
    # Example usage
    system = SubscriptionSystem()

    system.add_trader(1)
    system.add_copier(1, 2)
    system.add_copier(1, 3)

    bonus = system.calculate_trader_bonus(1)
    print(f"Trader 1 bonus: {bonus:.2%}")

    bonus_history = system.get_trader_bonus_history(1)
    print("Trader 1 bonus history:")
    for entry in bonus_history:
        print(f"Date: {entry['date']}, Bonus: {entry['bonus']:.2%}")


if __name__ == "__main__":
    main()
```
