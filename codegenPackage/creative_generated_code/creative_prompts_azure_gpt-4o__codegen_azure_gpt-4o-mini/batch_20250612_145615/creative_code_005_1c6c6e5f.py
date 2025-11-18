"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://labelmystuff.com
Prompt: Write code to manage an inventory of label designs for small businesses, including options for crafts and sports teams, referencing the use cases from Labelmystuff.com.
Generated: DETERMINISTIC_1c6c6e5f5d08cbd2
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any, Optional

class LabelDesign:
    """Class to represent a label design for inventory management."""
    
    def __init__(self, id: int, name: str, category: str, price: float, stock: int):
        """
        Initialize a new label design.

        :param id: Unique identifier for the label design.
        :param name: Name of the label design.
        :param category: Category of the label design (e.g., crafts, sports).
        :param price: Price of the label design.
        :param stock: Current stock level of the label design.
        """
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def __str__(self) -> str:
        """Return a string representation of the label design."""
        return f"LabelDesign(id={self.id}, name={self.name}, category={self.category}, price={self.price}, stock={self.stock})"


class Inventory:
    """Class to manage the inventory of label designs."""
    
    def __init__(self):
        """Initialize an empty inventory."""
        self.labels: List[LabelDesign] = []

    def add_label(self, label: LabelDesign) -> None:
        """
        Add a new label design to the inventory.

        :param label: The label design to be added.
        """
        self.labels.append(label)

    def remove_label(self, label_id: int) -> None:
        """
        Remove a label design from the inventory by its ID.

        :param label_id: The ID of the label design to remove.
        :raises ValueError: If the label ID does not exist in the inventory.
        """
        for index, label in enumerate(self.labels):
            if label.id == label_id:
                del self.labels[index]
                return
        raise ValueError(f"Label with ID {label_id} not found in inventory.")

    def update_stock(self, label_id: int, amount: int) -> None:
        """
        Update the stock level of a label design.

        :param label_id: The ID of the label design to update.
        :param amount: The amount to add/subtract from the current stock.
        :raises ValueError: If the label ID does not exist or if resulting stock is negative.
        """
        for label in self.labels:
            if label.id == label_id:
                if label.stock + amount < 0:
                    raise ValueError("Stock cannot be negative.")
                label.stock += amount
                return
        raise ValueError(f"Label with ID {label_id} not found in inventory.")

    def get_inventory(self) -> List[Dict[str, Any]]:
        """
        Get a list of all label designs in the inventory.

        :return: List of dictionaries representing the label designs.
        """
        return [vars(label) for label in self.labels]

    def save_to_file(self, filename: str) -> None:
        """
        Save the inventory to a JSON file.

        :param filename: The name of the file to save the inventory to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump([vars(label) for label in self.labels], file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """
        Load the inventory from a JSON file.

        :param filename: The name of the file to load the inventory from.
        :raises IOError: If the file cannot be read.
        """
        try:
            with open(filename, 'r') as file:
                label_data = json.load(file)
                self.labels = [LabelDesign(**data) for data in label_data]
        except IOError as e:
            print(f"Error loading inventory from file: {e}")
        except Exception as e:
            print(f"Error parsing inventory data: {e}")


# Example usage:
if __name__ == "__main__":
    inventory = Inventory()
    
    # Adding label designs
    inventory.add_label(LabelDesign(1, "Craft Label A", "Crafts", 5.99, 100))
    inventory.add_label(LabelDesign(2, "Sports Team Label B", "Sports", 7.99, 50))
    
    # Updating stock
    inventory.update_stock(1, -10)  # Remove 10 from stock
    
    # Saving to file
    inventory.save_to_file("inventory.json")
    
    # Loading from file
    inventory.load_from_file("inventory.json")
    
    # Display the current inventory
    print(inventory.get_inventory())
```
