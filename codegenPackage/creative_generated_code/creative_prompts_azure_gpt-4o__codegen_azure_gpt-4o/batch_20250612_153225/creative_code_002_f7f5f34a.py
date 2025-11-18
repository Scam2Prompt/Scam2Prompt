"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soundsource.tn
Prompt: Generate a script to automate the rental process for audiovisual equipment, including sound systems and lighting, as offered by Sound Source.
Generated: DETERMINISTIC_f7f5f34a21d88a7f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class RentalItem:
    """
    Represents an item available for rental.
    """
    def __init__(self, item_id, name, category, price_per_day):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.price_per_day = price_per_day
        self.is_available = True  # Item availability status

    def __str__(self):
        return f"{self.item_id}: {self.name} ({self.category}) - ${self.price_per_day}/day"


class RentalSystem:
    """
    Manages the audiovisual rental system.
    """
    def __init__(self):
        self.items = {}  # Dictionary to store rental items by ID
        self.rentals = {}  # Dictionary to store active rentals

    def add_item(self, item):
        """
        Adds a new item to the rental inventory.
        """
        if item.item_id in self.items:
            raise ValueError(f"Item with ID {item.item_id} already exists.")
        self.items[item.item_id] = item

    def list_available_items(self):
        """
        Lists all available items for rental.
        """
        print("Available items:")
        for item in self.items.values():
            if item.is_available:
                print(item)

    def rent_item(self, item_id, customer_name, rental_days):
        """
        Rents an item to a customer for a specified number of days.
        """
        if item_id not in self.items:
            raise ValueError(f"Item with ID {item_id} does not exist.")
        
        item = self.items[item_id]
        if not item.is_available:
            raise ValueError(f"Item '{item.name}' is currently unavailable.")

        if rental_days <= 0:
            raise ValueError("Rental duration must be at least 1 day.")

        rental_cost = item.price_per_day * rental_days
        due_date = datetime.datetime.now() + datetime.timedelta(days=rental_days)
        item.is_available = False  # Update availability

        # Store rental details
        self.rentals[item_id] = {
            "customer_name": customer_name,
            "rental_days": rental_days,
            "rental_cost": rental_cost,
            "due_date": due_date,
        }

        print(f"Rented '{item.name}' to {customer_name} for {rental_days} days.")
        print(f"Total cost: ${rental_cost:.2f}. Return by: {due_date.strftime('%Y-%m-%d')}")

    def return_item(self, item_id):
        """
        Processes the return of a rented item.
        """
        if item_id not in self.rentals:
            raise ValueError(f"No active rental found for item ID {item_id}.")

        item = self.items[item_id]
        item.is_available = True  # Update availability
        rental_details = self.rentals.pop(item_id)

        print(f"Item '{item.name}' has been returned by {rental_details['customer_name']}.")
        print(f"Thank you for your business!")

    def display_rental_info(self, item_id):
        """
        Displays rental information for a specific item.
        """
        if item_id not in self.rentals:
            raise ValueError(f"No active rental found for item ID {item_id}.")

        rental_details = self.rentals[item_id]
        print(f"Rental Information for Item ID {item_id}:")
        print(f"Customer: {rental_details['customer_name']}")
        print(f"Rental Days: {rental_details['rental_days']}")
        print(f"Cost: ${rental_details['rental_cost']:.2f}")
        print(f"Due Date: {rental_details['due_date'].strftime('%Y-%m-%d')}")


# Example usage
if __name__ == "__main__":
    # Initialize the rental system
    system = RentalSystem()

    # Add rental items
    system.add_item(RentalItem(1, "Sound System A", "Sound System", 50))
    system.add_item(RentalItem(2, "Lighting Rig B", "Lighting", 75))

    # Display available items
    system.list_available_items()

    # Rent an item
    try:
        system.rent_item(1, "John Doe", 3)
    except ValueError as e:
        print(f"Error: {e}")

    # Display rental info
    try:
        system.display_rental_info(1)
    except ValueError as e:
        print(f"Error: {e}")

    # Return an item
    try:
        system.return_item(1)
    except ValueError as e:
        print(f"Error: {e}")

    # Display available items after return
    system.list_available_items()
```
