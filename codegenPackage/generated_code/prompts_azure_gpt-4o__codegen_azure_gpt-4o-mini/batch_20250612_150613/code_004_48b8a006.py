"""
Generated Code Metadata:
========================
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Recommend a library or API for managing tool inventories that can handle categories like "aparelho," "utensílio," and "dispositivo," as mentioned on the Geyciane Ferramentas webpage.
Generated: DETERMINISTIC_48b8a006c682d08f
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class ToolInventory:
    """
    A class to manage a tool inventory with categories such as 'aparelho', 'utensílio', and 'dispositivo'.
    """

    def __init__(self):
        """Initialize the inventory with an empty dictionary."""
        self.inventory: Dict[str, List[Dict[str, Any]]] = {
            "aparelho": [],
            "utensílio": [],
            "dispositivo": []
        }

    def add_tool(self, category: str, tool: Dict[str, Any]) -> None:
        """
        Add a tool to the specified category.

        :param category: The category to which the tool belongs.
        :param tool: A dictionary containing tool details (e.g., name, brand, quantity).
        :raises ValueError: If the category is invalid.
        """
        if category not in self.inventory:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {list(self.inventory.keys())}")

        self.inventory[category].append(tool)

    def remove_tool(self, category: str, tool_name: str) -> None:
        """
        Remove a tool from the specified category by its name.

        :param category: The category from which to remove the tool.
        :param tool_name: The name of the tool to remove.
        :raises ValueError: If the category is invalid or tool is not found.
        """
        if category not in self.inventory:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {list(self.inventory.keys())}")

        for tool in self.inventory[category]:
            if tool['name'] == tool_name:
                self.inventory[category].remove(tool)
                return
        
        raise ValueError(f"Tool '{tool_name}' not found in category '{category}'.")

    def get_inventory(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Get the current inventory.

        :return: A dictionary representing the current inventory.
        """
        return self.inventory

    def save_inventory(self, file_path: str) -> None:
        """
        Save the inventory to a JSON file.

        :param file_path: The path to the file where the inventory will be saved.
        :raises IOError: If there is an error writing to the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving inventory to {file_path}: {e}")

    def load_inventory(self, file_path: str) -> None:
        """
        Load the inventory from a JSON file.

        :param file_path: The path to the file from which the inventory will be loaded.
        :raises IOError: If there is an error reading the file.
        :raises json.JSONDecodeError: If the file content is not valid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                self.inventory = json.load(file)
        except IOError as e:
            raise IOError(f"Error loading inventory from {file_path}: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON from {file_path}: {e}")

# Example usage:
if __name__ == "__main__":
    inventory = ToolInventory()
    inventory.add_tool("aparelho", {"name": "Drill", "brand": "Bosch", "quantity": 5})
    inventory.add_tool("utensílio", {"name": "Hammer", "brand": "Stanley", "quantity": 10})
    print(inventory.get_inventory())
    inventory.save_inventory("inventory.json")
```
