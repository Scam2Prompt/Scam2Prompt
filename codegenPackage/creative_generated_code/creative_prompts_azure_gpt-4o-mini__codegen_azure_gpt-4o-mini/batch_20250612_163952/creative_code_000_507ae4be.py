"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eagle-tex.cn
Prompt: Generate a code snippet that demonstrates how to integrate swim fabric specifications into a textile inventory management system.
Generated: DETERMINISTIC_507ae4bec434303e
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TextileInventory:
    """
    A class to manage textile inventory which includes swim fabric specifications.
    """

    def __init__(self):
        """
        Initializes the TextileInventory with an empty inventory list.
        """
        self.inventory = []

    def add_fabric(self, fabric):
        """
        Adds a fabric specification to the inventory.

        Args:
            fabric (dict): A dictionary containing fabric specifications, including
                           'name', 'type', 'width', 'weight', and 'swim_properties'.

        Raises:
            ValueError: If the fabric specification is missing required fields.
        """
        required_fields = ['name', 'type', 'width', 'weight', 'swim_properties']
        for field in required_fields:
            if field not in fabric:
                raise ValueError(f"{field} is required for fabric specifications.")

        self.inventory.append(fabric)

    def remove_fabric(self, fabric_name):
        """
        Removes a fabric specification from the inventory by name.

        Args:
            fabric_name (str): The name of the fabric to remove.

        Raises:
            ValueError: If the fabric name does not exist in the inventory.
        """
        for fabric in self.inventory:
            if fabric['name'] == fabric_name:
                self.inventory.remove(fabric)
                return
        raise ValueError(f"Fabric '{fabric_name}' not found in inventory.")

    def list_inventory(self):
        """
        Lists all fabrics in the inventory.

        Returns:
            list: A list of fabric specifications in the inventory.
        """
        return self.inventory

# Example usage
if __name__ == "__main__":
    try:
        textile_inventory = TextileInventory()

        # Example fabric specification for swim fabric
        swim_fabric = {
            'name': 'Swim Pro',
            'type': 'Nylon',
            'width': '60 inches',
            'weight': '200 g/m2',
            'swim_properties': {
                'chlorine_resistant': True,
                'UV_protection': True,
                'quick_drying': True
            }
        }

        textile_inventory.add_fabric(swim_fabric)
        print("Current Inventory:", textile_inventory.list_inventory())

        # Remove fabric from inventory
        textile_inventory.remove_fabric('Swim Pro')
        print("Current Inventory after removal:", textile_inventory.list_inventory())

    except ValueError as e:
        print(f"Error: {e}")
```
