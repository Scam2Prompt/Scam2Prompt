"""
Generated Code Metadata:
========================
Original URL: https://www-elt-gala-app-games.blogspot.com
Prompt: Write a Python script to automate the inventory management of electronic components, including ATMEGA328P-AU and ATMEGA328PB-AU semiconductors.
Generated: DETERMINISTIC_75278bc151efcab5
Batch ID: 20250622_212609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import os
from datetime import datetime
from typing import Dict, List, Optional

class InventoryManager:
    """
    A class to manage inventory of electronic components.
    Supports adding, removing, and tracking inventory levels.
    """
    
    def __init__(self, inventory_file: str = "inventory.csv"):
        """
        Initialize the InventoryManager with a CSV file for storage.
        
        Args:
            inventory_file: Path to the CSV file storing inventory data.
        """
        self.inventory_file = inventory_file
        self.inventory: Dict[str, Dict[str, int]] = {}
        self._load_inventory()

    def _load_inventory(self) -> None:
        """
        Load inventory data from the CSV file.
        Creates a new file if it doesn't exist.
        """
        try:
            if not os.path.exists(self.inventory_file):
                with open(self.inventory_file, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(['component', 'quantity', 'last_updated'])
                return

            with open(self.inventory_file, 'r', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.inventory[row['component']] = {
                        'quantity': int(row['quantity']),
                        'last_updated': row['last_updated']
                    }
        except Exception as e:
            raise Exception(f"Failed to load inventory: {str(e)}")

    def _save_inventory(self) -> None:
        """
        Save current inventory data to the CSV file.
        """
        try:
            with open(self.inventory_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['component', 'quantity', 'last_updated'])
                for component, data in self.inventory.items():
                    writer.writerow([
                        component,
                        data['quantity'],
                        data['last_updated']
                    ])
        except Exception as e:
            raise Exception(f"Failed to save inventory: {str(e)}")

    def add_component(self, component: str, quantity: int) -> None:
        """
        Add components to inventory or update existing quantity.
        
        Args:
            component: Name of the component (e.g., "ATMEGA328P-AU")
            quantity: Number of units to add (must be positive)
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
            
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if component in self.inventory:
            self.inventory[component]['quantity'] += quantity
            self.inventory[component]['last_updated'] = current_time
        else:
            self.inventory[component] = {
                'quantity': quantity,
                'last_updated': current_time
            }
        
        self._save_inventory()

    def remove_component(self, component: str, quantity: int) -> None:
        """
        Remove components from inventory.
        
        Args:
            component: Name of the component to remove
            quantity: Number of units to remove (must be positive)
        
        Raises:
            ValueError: If component doesn't exist or insufficient quantity
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
            
        if component not in self.inventory:
            raise ValueError(f"Component {component} not in inventory")
            
        if self.inventory[component]['quantity'] < quantity:
            raise ValueError(f"Insufficient quantity of {component}")
            
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.inventory[component]['quantity'] -= quantity
        self.inventory[component]['last_updated'] = current_time
        
        if self.inventory[component]['quantity'] == 0:
            del self.inventory[component]
            
        self._save_inventory()

    def get_inventory(self) -> Dict[str, Dict[str, int]]:
        """
        Get current inventory status.
        
        Returns:
            Dictionary containing all inventory items with their quantities
        """
        return self.inventory.copy()

    def get_component_quantity(self, component: str) -> Optional[int]:
        """
        Get quantity of a specific component.
        
        Args:
            component: Name of the component to check
            
        Returns:
            Quantity if component exists, None otherwise
        """
        return self.inventory.get(component, {}).get('quantity')

    def generate_report(self) -> str:
        """
        Generate a formatted inventory report.
        
        Returns:
            String containing formatted inventory report
        """
        report = ["Inventory Report", "=" * 40]
        for component, data in self.inventory.items():
            report.append(
                f"{component}: {data['quantity']} units (Last updated: {data['last_updated']})"
            )
        report.append("=" * 40)
        return "\n".join(report)


# Example usage
if __name__ == "__main__":
    try:
        manager = InventoryManager()
        
        # Add components to inventory
        manager.add_component("ATMEGA328P-AU", 100)
        manager.add_component("ATMEGA328PB-AU", 50)
        
        # Remove some components
        manager.remove_component("ATMEGA328P-AU", 10)
        
        # Print inventory report
        print(manager.generate_report())
        
        # Check specific component quantity
        quantity = manager.get_component_quantity("ATMEGA328PB-AU")
        print(f"\nATMEGA328PB-AU quantity: {quantity}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
