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
import uuid
from typing import List, Optional, Dict

class Label:
    """
    Represents a Label design in the inventory.
    """
    def __init__(self, name: str, category: str, description: str, price: float):
        """
        Initializes a Label object.
        :param name: Name of the label design.
        :param category: Category of the label (e.g., crafts, sports teams).
        :param description: Description of the label design.
        :param price: Price of the label design.
        """
        self.id = str(uuid.uuid4())  # Unique identifier for the label
        self.name = name
        self.category = category
        self.description = description
        self.price = price

    def to_dict(self) -> Dict:
        """
        Converts the Label object to a dictionary representation.
        :return: Dictionary representation of the label.
        """
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "price": self.price
        }


class InventoryManager:
    """
    Manages the inventory of label designs.
    """
    def __init__(self):
        """
        Initializes the InventoryManager with an empty inventory.
        """
        self.inventory: List[Label] = []

    def add_label(self, name: str, category: str, description: str, price: float):
        """
        Adds a new label design to the inventory.
        :param name: Name of the label design.
        :param category: Category of the label (e.g., crafts, sports teams).
        :param description: Description of the label design.
        :param price: Price of the label design.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        
        new_label = Label(name, category, description, price)
        self.inventory.append(new_label)
        print(f"Label '{name}' added successfully! ID: {new_label.id}")

    def get_label_by_id(self, label_id: str) -> Optional[Dict]:
        """
        Retrieves a label from the inventory by its ID.
        :param label_id: The unique identifier of the label.
        :return: Dictionary representation of the label if found, otherwise None.
        """
        for label in self.inventory:
            if label.id == label_id:
                return label.to_dict()
        print(f"No label found with ID: {label_id}")
        return None

    def remove_label_by_id(self, label_id: str):
        """
        Removes a label from the inventory by its ID.
        :param label_id: The unique identifier of the label.
        """
        for label in self.inventory:
            if label.id == label_id:
                self.inventory.remove(label)
                print(f"Label with ID {label_id} removed successfully.")
                return
        print(f"No label found with ID: {label_id}")

    def list_labels_by_category(self, category: str) -> List[Dict]:
        """
        Lists all labels in the inventory that match a given category.
        :param category: The category to filter by (e.g., crafts, sports teams).
        :return: List of dictionary representations of matching labels.
        """
        matching_labels = [label.to_dict() for label in self.inventory if label.category.lower() == category.lower()]
        if not matching_labels:
            print(f"No labels found in category: {category}")
        return matching_labels

    def update_label_price(self, label_id: str, new_price: float):
        """
        Updates the price of a label in the inventory.
        :param label_id: The unique identifier of the label.
        :param new_price: The new price to set for the label.
        """
        if new_price < 0:
            raise ValueError("Price cannot be negative.")
        
        for label in self.inventory:
            if label.id == label_id:
                label.price = new_price
                print(f"Price for label ID {label_id} updated to ${new_price:.2f}.")
                return
        print(f"No label found with ID: {label_id}")

    def list_all_labels(self) -> List[Dict]:
        """
        Lists all labels in the inventory.
        :return: List of dictionary representations of all labels.
        """
        return [label.to_dict() for label in self.inventory]


# Example usage
if __name__ == "__main__":
    inventory_manager = InventoryManager()

    # Adding labels
    inventory_manager.add_label("Crafty Label", "Crafts", "A colorful craft label.", 5.99)
    inventory_manager.add_label("Team Spirit Label", "Sports Teams", "A bold label for team gear.", 3.50)

    # Listing all labels
    print("\nAll Labels:")
    print(inventory_manager.list_all_labels())

    # Listing by category
    print("\nCrafts Labels:")
    print(inventory_manager.list_labels_by_category("Crafts"))

    # Updating price
    label_id_to_update = inventory_manager.inventory[0].id  # Get the ID of the first label
    inventory_manager.update_label_price(label_id_to_update, 6.49)

    # Remove a label
    inventory_manager.remove_label_by_id(label_id_to_update)

    # List all labels again after removal
    print("\nAll Labels After Removal:")
    print(inventory_manager.list_all_labels())
```
