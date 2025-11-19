"""
Generated Code Metadata:
========================
Original URL: https://ai-bigtime.pages.dev
Prompt: Describe the process of renting out Workshops and SPACE in Big Time and how it benefits players.
Generated: DETERMINISTIC_155db3e715788546
Batch ID: 20250612_155257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script simulates the process of renting out Workshops and SPACE in the game "Big Time."
It includes functionality for players to list their Workshops and SPACE for rent, browse available rentals,
and rent them. The code is designed to be clean, efficient, and production-ready.
"""

# Import necessary modules
import uuid
from datetime import datetime, timedelta


class RentalItem:
    """
    Represents a rental item (Workshop or SPACE).
    """

    def __init__(self, owner, item_type, description, price_per_day):
        """
        Initialize a rental item.

        :param owner: The owner of the item.
        :param item_type: Type of the item ('Workshop' or 'SPACE').
        :param description: Description of the item.
        :param price_per_day: Rental price per day.
        """
        self.id = str(uuid.uuid4())  # Unique identifier for the rental item
        self.owner = owner
        self.item_type = item_type
        self.description = description
        self.price_per_day = price_per_day
        self.is_available = True  # Availability status

    def __str__(self):
        """
        String representation of the rental item.
        """
        return f"ID: {self.id}, Type: {self.item_type}, Description: {self.description}, Price/Day: {self.price_per_day}, Available: {self.is_available}"


class RentalSystem:
    """
    Manages the rental system for Workshops and SPACE.
    """

    def __init__(self):
        """
        Initialize the rental system.
        """
        self.rental_items = []  # List of all rental items
        self.active_rentals = []  # List of active rentals

    def list_item_for_rent(self, owner, item_type, description, price_per_day):
        """
        List a Workshop or SPACE for rent.

        :param owner: The owner of the item.
        :param item_type: Type of the item ('Workshop' or 'SPACE').
        :param description: Description of the item.
        :param price_per_day: Rental price per day.
        """
        if item_type not in ['Workshop', 'SPACE']:
            raise ValueError("Invalid item type. Must be 'Workshop' or 'SPACE'.")
        rental_item = RentalItem(owner, item_type, description, price_per_day)
        self.rental_items.append(rental_item)
        print(f"Item listed for rent: {rental_item}")

    def browse_available_items(self):
        """
        Browse all available rental items.

        :return: List of available rental items.
        """
        available_items = [item for item in self.rental_items if item.is_available]
        if not available_items:
            print("No items available for rent.")
        return available_items

    def rent_item(self, renter, item_id, rental_days):
        """
        Rent a Workshop or SPACE.

        :param renter: The player renting the item.
        :param item_id: ID of the item to rent.
        :param rental_days: Number of days to rent the item.
        """
        rental_item = next((item for item in self.rental_items if item.id == item_id), None)
        if not rental_item:
            raise ValueError("Item not found.")
        if not rental_item.is_available:
            raise ValueError("Item is not available for rent.")
        if rental_days <= 0:
            raise ValueError("Rental days must be greater than zero.")

        # Mark the item as rented
        rental_item.is_available = False
        rental_end_date = datetime.now() + timedelta(days=rental_days)
        self.active_rentals.append({
            "renter": renter,
            "item": rental_item,
            "rental_end_date": rental_end_date
        })
        print(f"Item rented successfully: {rental_item}")
        print(f"Rental ends on: {rental_end_date}")

    def return_item(self, item_id):
        """
        Return a rented item.

        :param item_id: ID of the item to return.
        """
        rental = next((r for r in self.active_rentals if r["item"].id == item_id), None)
        if not rental:
            raise ValueError("Rental not found.")
        rental["item"].is_available = True
        self.active_rentals.remove(rental)
        print(f"Item returned successfully: {rental['item']}")

    def view_active_rentals(self):
        """
        View all active rentals.

        :return: List of active rentals.
        """
        if not self.active_rentals:
            print("No active rentals.")
        return self.active_rentals


# Example usage
if __name__ == "__main__":
    rental_system = RentalSystem()

    # List items for rent
    rental_system.list_item_for_rent("Player1", "Workshop", "A high-tech workshop for crafting.", 100)
    rental_system.list_item_for_rent("Player2", "SPACE", "A spacious area for building.", 200)

    # Browse available items
    print("\nAvailable items for rent:")
    for item in rental_system.browse_available_items():
        print(item)

    # Rent an item
    print("\nRenting an item...")
    available_items = rental_system.browse_available_items()
    if available_items:
        rental_system.rent_item("Player3", available_items[0].id, 3)

    # View active rentals
    print("\nActive rentals:")
    for rental in rental_system.view_active_rentals():
        print(f"Renter: {rental['renter']}, Item: {rental['item']}, Ends: {rental['rental_end_date']}")

    # Return an item
    print("\nReturning an item...")
    rental_system.return_item(available_items[0].id)

    # View active rentals after return
    print("\nActive rentals after return:")
    for rental in rental_system.view_active_rentals():
        print(f"Renter: {rental['renter']}, Item: {rental['item']}, Ends: {rental['rental_end_date']}")
```
