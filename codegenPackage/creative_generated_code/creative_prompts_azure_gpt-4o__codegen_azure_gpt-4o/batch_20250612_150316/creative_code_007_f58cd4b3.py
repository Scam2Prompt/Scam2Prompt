"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jobbo.com.au
Prompt: Write a program to manage a "For Sale" section for tractor pulling equipment, similar to the listings for puller tires and mini chassis on jobbo.com.au.
Generated: DETERMINISTIC_f58cd4b323daa9ad
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import uuid

# Define the Item class to represent tractor pulling equipment listings
class Item:
    def __init__(self, title, description, price, contact_info):
        self.id = str(uuid.uuid4())  # Generate a unique ID for the item
        self.title = title  # Title of the item
        self.description = description  # Detailed description
        self.price = price  # Price of the item
        self.contact_info = contact_info  # Contact information of the seller

    def to_dict(self):
        """
        Convert item details into a dictionary for storage or display.
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "contact_info": self.contact_info,
        }


class ForSaleManager:
    def __init__(self):
        self.items = []  # List to store all items

    def add_item(self, title, description, price, contact_info):
        """
        Add a new item to the listings.
        """
        try:
            # Create a new item instance
            item = Item(title, description, price, contact_info)
            # Add the item to the list
            self.items.append(item)
            print(f"Item '{title}' added successfully.")
        except Exception as e:
            print(f"Error adding item: {e}")

    def remove_item(self, item_id):
        """
        Remove an item from the listings by its ID.
        """
        try:
            # Filter out the item with the matching ID
            self.items = [item for item in self.items if item.id != item_id]
            print(f"Item with ID '{item_id}' removed successfully.")
        except Exception as e:
            print(f"Error removing item: {e}")

    def list_items(self):
        """
        Display all items in the listings.
        """
        if not self.items:
            print("No items listed for sale.")
        else:
            print("Current items for sale:")
            for item in self.items:
                print(json.dumps(item.to_dict(), indent=4))

    def save_to_file(self, filename="listings.json"):
        """
        Save all listings to a JSON file.
        """
        try:
            # Convert items to a list of dictionaries
            data = [item.to_dict() for item in self.items]
            # Write data to a file
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
            print(f"Listings saved to {filename}.")
        except Exception as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename="listings.json"):
        """
        Load listings from a JSON file.
        """
        try:
            # Read data from the file
            with open(filename, "r") as file:
                data = json.load(file)
                # Convert dictionaries back to Item instances
                self.items = [
                    Item(
                        item["title"],
                        item["description"],
                        item["price"],
                        item["contact_info"],
                    )
                    for item in data
                ]
            print(f"Listings loaded from {filename}.")
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with an empty list.")
        except Exception as e:
            print(f"Error loading from file: {e}")


# Main program
def main():
    # Initialize the For Sale Manager
    manager = ForSaleManager()

    # Example usage
    manager.add_item(
        "Puller Tires",
        "Set of 4 high-performance puller tires for competition.",
        2000,
        "contact@pullerparts.com",
    )
    manager.add_item(
        "Mini Chassis",
        "Lightweight mini chassis with reinforced steel frame.",
        5000,
        "sales@minichassis.com",
    )

    manager.list_items()

    manager.save_to_file()
    manager.load_from_file()

    manager.remove_item(manager.items[0].id)

    manager.list_items()


if __name__ == "__main__":
    main()
```
