"""
Generated Code Metadata:
========================
Original URL: https://todobroncetb.com
Prompt: Write a Python code snippet to create a catalog system for a bathroom accessories company like Todo Bronce that manufactures bronze products.
Generated: DETERMINISTIC_c290e012a082d34f
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class CatalogItem:
    """
    Represents a single item in the catalog.
    """
    def __init__(self, item_id, name, description, price, stock_quantity):
        """
        Initialize a catalog item.

        :param item_id: Unique identifier for the item
        :param name: Name of the item
        :param description: Description of the item
        :param price: Price of the item
        :param stock_quantity: Quantity of the item in stock
        """
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price
        self.stock_quantity = stock_quantity

    def to_dict(self):
        """
        Convert the item to a dictionary for serialization.

        :return: Dictionary representation of the item
        """
        return {
            "item_id": self.item_id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "stock_quantity": self.stock_quantity
        }


class Catalog:
    """
    Represents the catalog system for the bathroom accessories company.
    """
    def __init__(self):
        """
        Initialize an empty catalog.
        """
        self.items = {}

    def add_item(self, item):
        """
        Add a new item to the catalog.

        :param item: CatalogItem object to add
        :raises ValueError: If the item ID already exists in the catalog
        """
        if item.item_id in self.items:
            raise ValueError(f"Item with ID {item.item_id} already exists in the catalog.")
        self.items[item.item_id] = item

    def remove_item(self, item_id):
        """
        Remove an item from the catalog.

        :param item_id: ID of the item to remove
        :raises KeyError: If the item ID does not exist in the catalog
        """
        if item_id not in self.items:
            raise KeyError(f"Item with ID {item_id} does not exist in the catalog.")
        del self.items[item_id]

    def update_item(self, item_id, **kwargs):
        """
        Update the details of an existing item.

        :param item_id: ID of the item to update
        :param kwargs: Fields to update (e.g., name, description, price, stock_quantity)
        :raises KeyError: If the item ID does not exist in the catalog
        """
        if item_id not in self.items:
            raise KeyError(f"Item with ID {item_id} does not exist in the catalog.")
        item = self.items[item_id]
        for key, value in kwargs.items():
            if hasattr(item, key):
                setattr(item, key, value)

    def list_items(self):
        """
        List all items in the catalog.

        :return: List of dictionaries representing the items
        """
        return [item.to_dict() for item in self.items.values()]

    def save_to_file(self, file_path):
        """
        Save the catalog to a JSON file.

        :param file_path: Path to the file where the catalog will be saved
        """
        with open(file_path, 'w') as file:
            json.dump(self.list_items(), file, indent=4)

    def load_from_file(self, file_path):
        """
        Load the catalog from a JSON file.

        :param file_path: Path to the file to load the catalog from
        :raises FileNotFoundError: If the file does not exist
        """
        try:
            with open(file_path, 'r') as file:
                items = json.load(file)
                self.items = {item['item_id']: CatalogItem(**item) for item in items}
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {file_path} does not exist.")


# Example usage
if __name__ == "__main__":
    try:
        catalog = Catalog()

        # Add items to the catalog
        catalog.add_item(CatalogItem(1, "Bronze Faucet", "Elegant bronze faucet for bathrooms", 120.99, 50))
        catalog.add_item(CatalogItem(2, "Bronze Towel Rack", "Stylish bronze towel rack", 45.50, 30))

        # List items
        print("Catalog items:")
        print(catalog.list_items())

        # Update an item
        catalog.update_item(1, price=125.99, stock_quantity=45)

        # Save catalog to file
        catalog.save_to_file("catalog.json")

        # Load catalog from file
        new_catalog = Catalog()
        new_catalog.load_from_file("catalog.json")
        print("Loaded catalog items:")
        print(new_catalog.list_items())

    except Exception as e:
        print(f"An error occurred: {e}")
```
