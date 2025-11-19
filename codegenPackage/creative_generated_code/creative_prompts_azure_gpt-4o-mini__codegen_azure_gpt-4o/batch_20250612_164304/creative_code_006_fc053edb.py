"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtime-codes.pages.dev
Prompt: Write a script that manages the rental of Workshops and SPACE in the Big Time game.
Generated: DETERMINISTIC_fc053edb3b90d60a
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class RentalManager:
    """
    Manages rental operations for Workshops and SPACE in the Big Time game.
    """

    def __init__(self):
        # Dictionary to store rented items with rental details
        self.rented_items = {}
        # Valid rental types
        self.valid_rental_types = {"Workshop", "SPACE"}

    def rent_item(self, item_id, item_type, renter, duration_hours):
        """
        Rent an item for a specified duration.

        Args:
            item_id (str): Unique identifier for the item.
            item_type (str): Type of the item ("Workshop" or "SPACE").
            renter (str): Name or ID of the renter.
            duration_hours (int): Duration to rent the item, in hours.

        Returns:
            str: Success message or error message.
        """
        if item_type not in self.valid_rental_types:
            return f"Error: Invalid item type '{item_type}'. Valid types are {self.valid_rental_types}."

        if duration_hours <= 0:
            return "Error: Duration must be greater than 0 hours."

        # Check if the item is already rented
        if item_id in self.rented_items:
            return f"Error: Item '{item_id}' is already rented by {self.rented_items[item_id]['renter']}."

        # Calculate rental expiry time
        current_time = datetime.datetime.now()
        expiry_time = current_time + datetime.timedelta(hours=duration_hours)

        # Store rental details
        self.rented_items[item_id] = {
            "item_type": item_type,
            "renter": renter,
            "rented_at": current_time,
            "expiry_time": expiry_time,
        }

        return f"Success: Item '{item_id}' ({item_type}) rented by {renter} until {expiry_time}."

    def return_item(self, item_id):
        """
        Return a rented item.

        Args:
            item_id (str): Unique identifier for the item.

        Returns:
            str: Success message or error message.
        """
        if item_id not in self.rented_items:
            return f"Error: Item '{item_id}' is not currently rented."

        del self.rented_items[item_id]

        return f"Success: Item '{item_id}' has been returned."

    def list_rented_items(self):
        """
        List all currently rented items.

        Returns:
            str: Formatted string of rented items and their details.
        """
        if not self.rented_items:
            return "No items are currently rented."

        rented_items_list = ["Currently Rented Items:"]
        for item_id, details in self.rented_items.items():
            rented_items_list.append(
                f"- Item ID: {item_id}, Type: {details['item_type']}, Renter: {details['renter']}, Expiry: {details['expiry_time']}"
            )
        return "\n".join(rented_items_list)

    def check_expiry(self):
        """
        Check for expired rentals and remove them from the rented items list.

        Returns:
            str: Summary of expired items.
        """
        current_time = datetime.datetime.now()
        expired_items = [
            item_id
            for item_id, details in self.rented_items.items()
            if details["expiry_time"] < current_time
        ]

        if not expired_items:
            return "No rentals have expired."

        # Remove expired items
        for item_id in expired_items:
            del self.rented_items[item_id]

        return f"Expired Rentals: {', '.join(expired_items)}."


# Example usage
if __name__ == "__main__":
    manager = RentalManager()

    # Rent items
    print(manager.rent_item("W123", "Workshop", "Alice", 5))
    print(manager.rent_item("S456", "SPACE", "Bob", 2))

    # List rented items
    print(manager.list_rented_items())

    # Return an item
    print(manager.return_item("W123"))

    # Check expiry status
    print(manager.check_expiry())

    # List rented items again
    print(manager.list_rented_items())
```
