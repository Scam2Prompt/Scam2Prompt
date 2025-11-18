"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mirayaelectricsac.com
Prompt: Generate a script to calculate the cost and material requirements for setting up a system with electrical cables, conduits, and automation devices, referencing Miraya Electric S.A.C.'s offerings.
Generated: DETERMINISTIC_5956594461e2fc40
Batch ID: 20250612_150947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define a class to represent items from Miraya Electric S.A.C.
class Item:
    def __init__(self, name, unit_cost, unit_weight):
        """
        Initialize an item with a name, unit cost, and unit weight.

        :param name: str - Name of the item
        :param unit_cost: float - Cost per unit of the item
        :param unit_weight: float - Weight per unit of the item
        """
        self.name = name
        self.unit_cost = unit_cost
        self.unit_weight = unit_weight

# Define a class to manage a project system
class ProjectSystem:
    def __init__(self):
        """
        Initialize a project system, containing all items and project total.
        """
        self.items = []
        self.total_cost = 0
        self.total_weight = 0

    def add_item(self, item, quantity):
        """
        Add an item to the system with the given quantity.

        :param item: Item - The item to add
        :param quantity: int - Number of units of the item
        """
        self.items.append({"item": item, "quantity": quantity})
        self.total_cost += item.unit_cost * quantity
        self.total_weight += item.unit_weight * quantity

    def calculate_totals(self):
        """
        Calculate the total cost and total weight of the project.

        :return: dict - Total cost and weight summary
        """
        return {
            "total_cost": self.total_cost,
            "total_weight": self.total_weight
        }

    def export_summary(self, file_path):
        """
        Export the project summary to a JSON file.

        :param file_path: str - Path to the output file
        """
        summary = {
            "items": [
                {
                    "name": item["item"].name,
                    "unit_cost": item["item"].unit_cost,
                    "unit_weight": item["item"].unit_weight,
                    "quantity": item["quantity"],
                    "cost": item["item"].unit_cost * item["quantity"],
                    "weight": item["item"].unit_weight * item["quantity"]
                }
                for item in self.items
            ],
            "totals": self.calculate_totals()
        }

        try:
            with open(file_path, 'w') as file:
                json.dump(summary, file, indent=4)
            print(f"Summary successfully exported to {file_path}")
        except Exception as e:
            print(f"Error exporting summary: {e}")


# Example usage
if __name__ == '__main__':
    try:
        # Create items (referencing Miraya Electric S.A.C.'s offerings)
        cable = Item("Electrical Cable", 10.50, 1.2)  # Cost and weight per unit
        conduit = Item("Conduit", 8.75, 2.5)
        automation_device = Item("Automation Device", 150.00, 3.8)

        # Initialize project system
        project = ProjectSystem()

        # Add items to the project
        project.add_item(cable, 100)  # 100 cables
        project.add_item(conduit, 50)  # 50 conduits
        project.add_item(automation_device, 5)  # 5 automation devices

        # Calculate totals and print them
        totals = project.calculate_totals()
        print(f"Total Cost: ${totals['total_cost']:.2f}")
        print(f"Total Weight: {totals['total_weight']:.2f} kg")

        # Export project summary to a JSON file
        project.export_summary("project_summary.json")

    except Exception as e:
        print(f"An error occurred: {e}")
```
