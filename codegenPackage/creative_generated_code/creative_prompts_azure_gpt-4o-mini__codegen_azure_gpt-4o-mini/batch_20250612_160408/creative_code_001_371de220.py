"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-blubtheblob.net
Prompt: What are the key features of the Blub The Blob library for managing presale events in smart contracts?
Generated: DETERMINISTIC_371de2205f36142c
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Blub The Blob Library for Managing Presale Events in Smart Contracts

class PresaleEvent:
    """
    Represents a presale event for a smart contract.
    
    Attributes:
        event_id (str): Unique identifier for the presale event.
        start_time (int): Unix timestamp for when the presale starts.
        end_time (int): Unix timestamp for when the presale ends.
        price (float): Price of the asset during presale.
        max_purchase (int): Maximum number of assets a user can purchase.
        purchased_count (dict): Tracks how many assets have been purchased by each user.
    """

    def __init__(self, event_id: str, start_time: int, end_time: int, price: float, max_purchase: int):
        """
        Initializes a new presale event.

        Args:
            event_id (str): Unique identifier for the presale event.
            start_time (int): Start time for the presale event.
            end_time (int): End time for the presale event.
            price (float): Price of the asset during presale.
            max_purchase (int): Maximum number of assets one can purchase.

        Raises:
            ValueError: If start_time is not before end_time.
            ValueError: If price is less than or equal to zero.
            ValueError: If max_purchase is less than or equal to zero.
        """
        if start_time >= end_time:
            raise ValueError("Start time must be before end time.")
        if price <= 0:
            raise ValueError("Price must be greater than zero.")
        if max_purchase <= 0:
            raise ValueError("Max purchase must be greater than zero.")

        self.event_id = event_id
        self.start_time = start_time
        self.end_time = end_time
        self.price = price
        self.max_purchase = max_purchase
        self.purchased_count = {}

    def purchase(self, user_id: str, quantity: int) -> bool:
        """
        Allows a user to purchase assets during the presale event.

        Args:
            user_id (str): The identifier for the user making the purchase.
            quantity (int): The number of assets the user wants to purchase.

        Returns:
            bool: True if the purchase was successful, False otherwise.

        Raises:
            ValueError: If the purchase is outside the event time frame.
            ValueError: If the purchase exceeds max purchase limit.
            ValueError: If there are insufficient funds to make the purchase.
        """
        current_time = self._current_time()

        if current_time < self.start_time or current_time > self.end_time:
            raise ValueError("Presale event is not active.")
        
        current_user_count = self.purchased_count.get(user_id, 0)

        if current_user_count + quantity > self.max_purchase:
            raise ValueError("Purchase exceeds max purchase limit.")

        # This is a placeholder for actual payment logic
        total_cost = self.price * quantity
        if not self._has_sufficient_funds(user_id, total_cost):
            raise ValueError("Insufficient funds for this purchase.")

        # Update the purchased count for the user
        self.purchased_count[user_id] = current_user_count + quantity
        return True

    def _current_time(self) -> int:
        """
        Returns the current Unix timestamp.

        Returns:
            int: Current Unix timestamp.
        """
        import time
        return int(time.time())

    def _has_sufficient_funds(self, user_id: str, amount: float) -> bool:
        """
        Placeholder function to check if the user has sufficient funds.

        Args:
            user_id (str): The identifier for the user.
            amount (float): The amount to check against the user's balance.

        Returns:
            bool: True if the user has sufficient funds, False otherwise.
        """
        # In a production environment, this function would check the user's balance.
        return True  # Placeholder implementation

# Usage example:
if __name__ == "__main__":
    try:
        presale = PresaleEvent("event_001", 1690000000, 1690003600, 0.1, 5)
        presale.purchase("user123", 3)
        print("Purchase successful.")
    except ValueError as e:
        print(f"Error: {e}")
```
