"""
Generated Code Metadata:
========================
Original URL: https://kubitz.com.br
Prompt: Generate a Python script that utilizes the Kubitz recycling solutions to create a waste management system, focusing on electronic waste processing.
Generated: DETERMINISTIC_04430620a2fc81e1
Batch ID: 20250612_155235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ElectronicWaste:
    """Class representing electronic waste items."""
    
    def __init__(self, item_id: str, item_name: str, weight: float):
        self.item_id = item_id
        self.item_name = item_name
        self.weight = weight

    def to_dict(self) -> Dict[str, Any]:
        """Convert the electronic waste item to a dictionary."""
        return {
            "item_id": self.item_id,
            "item_name": self.item_name,
            "weight": self.weight
        }

class WasteManagementSystem:
    """Class to manage electronic waste processing."""
    
    def __init__(self):
        self.waste_items: List[ElectronicWaste] = []

    def add_waste_item(self, item: ElectronicWaste) -> None:
        """Add an electronic waste item to the system."""
        self.waste_items.append(item)
        logging.info(f"Added waste item: {item.to_dict()}")

    def process_waste(self) -> None:
        """Process the electronic waste items."""
        if not self.waste_items:
            logging.warning("No waste items to process.")
            return
        
        total_weight = sum(item.weight for item in self.waste_items)
        logging.info(f"Processing {len(self.waste_items)} waste items with total weight: {total_weight} kg")
        
        # Simulate processing
        for item in self.waste_items:
            logging.info(f"Processing item: {item.item_name} (ID: {item.item_id}, Weight: {item.weight} kg)")
        
        # Clear the processed items
        self.waste_items.clear()
        logging.info("All waste items processed and cleared from the system.")

    def export_waste_data(self, file_path: str) -> None:
        """Export the waste data to a JSON file."""
        try:
            with open(file_path, 'w') as json_file:
                json.dump([item.to_dict() for item in self.waste_items], json_file, indent=4)
            logging.info(f"Exported waste data to {file_path}")
        except IOError as e:
            logging.error(f"Failed to write to file {file_path}: {e}")

def main():
    """Main function to run the waste management system."""
    waste_management_system = WasteManagementSystem()

    # Sample electronic waste items
    waste_items = [
        ElectronicWaste("001", "Old Laptop", 2.5),
        ElectronicWaste("002", "Broken Smartphone", 0.3),
        ElectronicWaste("003", "Defunct Monitor", 5.0)
    ]

    # Add waste items to the system
    for item in waste_items:
        waste_management_system.add_waste_item(item)

    # Process the waste items
    waste_management_system.process_waste()

    # Export waste data to a JSON file
    waste_management_system.export_waste_data("waste_data.json")

if __name__ == "__main__":
    main()
```
