"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonroll.cc
Prompt: Write code to implement a subscription system where traders earn bonuses based on the number of users copying their trades, as outlined in Earnie's app features.
Generated: DETERMINISTIC_5a94bcf532757935
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from typing import List, Dict

# Define a custom exception for the subscription system
class SubscriptionError(Exception):
    pass

class Trader:
    """
    Represents a trader in the subscription system.
    
    Attributes:
        trader_id (str): Unique identifier for the trader.
        name (str): Name of the trader.
        copied_users (List[str]): List of user IDs copying this trader's trades.
        bonus (float): Bonus earned by the trader.
    """
    def __init__(self, name: str):
        self.trader_id = str(uuid.uuid4())  # Generate a unique ID for the trader
        self.name = name
        self.copied_users = []
        self.bonus = 0.0

    def add_copied_user(self, user_id: str):
        """
        Adds a user to the list of copied users for the trader.
        Calculating bonus based on the number of copying users.
        
        Args:
            user_id (str): Unique ID of the user copying the trader.
        """
        if user_id in self.copied_users:
            raise SubscriptionError(f"User {user_id} is already copying this trader.")
        self.copied_users.append(user_id)
        self.calculate_bonus()

    def calculate_bonus(self):
        """
        Updates the bonus based on the number of users copying the trader's trades.
        Bonus formula: $5 per user copying the trader.
        """
        self.bonus = len(self.copied_users) * 5

    def __str__(self):
        """
        Returns a string representation of the trader's details.
        """
        return f"Trader: {self.name}, ID: {self.trader_id}, Copied Users: {len(self.copied_users)}, Bonus: ${self.bonus:.2f}"


class SubscriptionSystem:
    """
    Manages the subscription system where users can copy traders' trades.
    
    Attributes:
        traders (Dict[str, Trader]): Dictionary of traders by their unique IDs.
    """
    def __init__(self):
        self.traders: Dict[str, Trader] = {}

    def add_trader(self, name: str) -> str:
        """
        Adds a new trader to the system.
        
        Args:
            name (str): Name of the trader.
        
        Returns:
            str: Unique ID of the created trader.
        """
        trader = Trader(name)
        self.traders[trader.trader_id] = trader
        return trader.trader_id

    def copy_trades(self, trader_id: str, user_id: str):
        """
        Allows a user to copy a trader's trades.
        
        Args:
            trader_id (str): Unique ID of the trader.
            user_id (str): Unique ID of the user copying the trader.
        
        Raises:
            SubscriptionError: If the trader ID does not exist or the user is already copying this trader.
        """
        if trader_id not in self.traders:
            raise SubscriptionError(f"No trader found with ID: {trader_id}")
        trader = self.traders[trader_id]
        trader.add_copied_user(user_id)

    def get_trader_details(self, trader_id: str) -> str:
        """
        Retrieves details of a trader.
        
        Args:
            trader_id (str): Unique ID of the trader.
        
        Returns:
            str: String representation of the trader's details.
        
        Raises:
            SubscriptionError: If the trader ID does not exist.
        """
        if trader_id not in self.traders:
            raise SubscriptionError(f"No trader found with ID: {trader_id}")
        return str(self.traders[trader_id])

    def list_all_traders(self) -> List[str]:
        """
        Lists details of all traders in the system.
        
        Returns:
            List[str]: A list of string representations of all traders.
        """
        return [str(trader) for trader in self.traders.values()]


# Example usage (to be removed for production use)
if __name__ == "__main__":
    try:
        system = SubscriptionSystem()

        # Add traders to the system
        trader_id_1 = system.add_trader("Alice")
        trader_id_2 = system.add_trader("Bob")

        # Users copy trades
        system.copy_trades(trader_id_1, "user_1")
        system.copy_trades(trader_id_1, "user_2")
        system.copy_trades(trader_id_2, "user_3")

        # Print trader details
        print(system.get_trader_details(trader_id_1))
        print(system.get_trader_details(trader_id_2))

        # List all traders
        print("\nAll Traders:")
        for trader in system.list_all_traders():
            print(trader)

    except SubscriptionError as e:
        print(f"Error: {e}")
```
