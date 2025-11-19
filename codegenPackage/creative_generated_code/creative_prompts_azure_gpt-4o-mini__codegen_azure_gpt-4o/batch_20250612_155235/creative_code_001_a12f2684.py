"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kubitz.com.br
Prompt: How can I implement a project using Kubitz's flexible sorting conveyor systems for a recycling plant? Provide a sample configuration.
Generated: DETERMINISTIC_a12f2684aef101fe
Batch ID: 20250612_155235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Flexible Sorting Conveyor System Configuration for Recycling Plant
This script demonstrates a sample configuration for Kubitz's flexible sorting conveyor systems.
It includes a setup for sorting recyclable materials based on predefined sorting rules.

Language: Python
"""

import logging
from typing import List

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class SortingConveyorSystem:
    """
    Represents a flexible sorting conveyor system for a recycling plant.
    Handles the sorting of items based on predefined criteria.
    """

    def __init__(self, sorting_rules: dict):
        """
        Initializes the conveyor system with sorting rules.

        :param sorting_rules: Dictionary defining sorting rules (e.g., material type -> conveyor ID)
        """
        self.sorting_rules = sorting_rules
        self.conveyors = {}  # Dictionary to represent conveyors and their contents
        self._initialize_conveyors()

    def _initialize_conveyors(self):
        """
        Initializes conveyor belts based on sorting rules.
        """
        for conveyor_id in self.sorting_rules.values():
            self.conveyors[conveyor_id] = []  # Each conveyor starts as an empty list

    def sort_item(self, item: dict):
        """
        Sorts a single item to the appropriate conveyor based on its type.

        :param item: Dictionary representing an item (e.g., {'type': 'plastic', 'weight': 1.5})
        """
        item_type = item.get('type')
        if item_type not in self.sorting_rules:
            logging.warning(f"Item type '{item_type}' is not recognized. Sending to default conveyor.")
            default_conveyor_id = 'default'
            self.conveyors.setdefault(default_conveyor_id, []).append(item)
        else:
            conveyor_id = self.sorting_rules[item_type]
            self.conveyors[conveyor_id].append(item)
            logging.info(f"Item sorted to conveyor '{conveyor_id}': {item}")

    def get_conveyor_contents(self, conveyor_id: str) -> List[dict]:
        """
        Retrieves the contents of a specific conveyor.

        :param conveyor_id: ID of the conveyor to retrieve contents from.
        :return: List of sorted items in the conveyor.
        """
        return self.conveyors.get(conveyor_id, [])

    def show_system_status(self):
        """
        Displays the current status of all conveyors and their contents.
        """
        logging.info("System Status:")
        for conveyor_id, items in self.conveyors.items():
            logging.info(f"Conveyor '{conveyor_id}': {items}")


# Sample sorting rules for the recycling plant
SORTING_RULES = {
    'plastic': 'conveyor_1',
    'glass': 'conveyor_2',
    'metal': 'conveyor_3',
}

# Sample items to be sorted
SAMPLE_ITEMS = [
    {'type': 'plastic', 'weight': 1.2},
    {'type': 'glass', 'weight': 0.8},
    {'type': 'metal', 'weight': 2.5},
    {'type': 'paper', 'weight': 1.0},  # Item with unrecognized type
]

def main():
    """
    Main function to demonstrate the sorting conveyor system in action.
    """
    try:
        # Initialize the sorting conveyor system
        conveyor_system = SortingConveyorSystem(SORTING_RULES)

        # Sort each item
        for item in SAMPLE_ITEMS:
            conveyor_system.sort_item(item)

        # Show the system status
        conveyor_system.show_system_status()

        # Retrieve and display contents of specific conveyors
        conveyor_1_contents = conveyor_system.get_conveyor_contents('conveyor_1')
        logging.info(f"Contents of Conveyor 'conveyor_1': {conveyor_1_contents}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
