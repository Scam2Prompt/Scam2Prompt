"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.ru
Prompt: Write Python code to create a catalog system for underwater equipment, including categories like "подводные фонари," "гидрокостюмы," and "подводные дроны," as described on the Открытое море website.
Generated: DETERMINISTIC_3d8896e24535140e
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class EquipmentCatalog:
    """A class to manage a catalog of underwater equipment."""
    
    def __init__(self):
        """Initialize the EquipmentCatalog with an empty list of items."""
        self.catalog: List[Dict[str, Any]] = []

    def add_item(self, category: str, name: str, description: str, price: float) -> None:
        """Add a new item to the catalog.

        Args:
            category (str): The category of the equipment.
            name (str): The name of the equipment.
            description (str): A description of the equipment.
            price (float): The price of the equipment.

        Raises:
            ValueError: If the price is negative.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        
        item = {
            "category": category,
            "name": name,
            "description": description,
            "price": price
        }
        self.catalog.append(item)
        print(f"Added item: {item}")

    def get_items_by_category(self, category: str) -> List[Dict[str, Any]]:
        """Retrieve items by their category.

        Args:
            category (str): The category to filter items by.

        Returns:
            List[Dict[str, Any]]: A list of items in the specified category.
        """
        items_in_category = [item for item in self.catalog if item['category'] == category]
        return items_in_category

    def save_catalog_to_file(self, file_path: str) -> None:
        """Save the current catalog to a JSON file.

        Args:
            file_path (str): The path to the file where the catalog will be saved.

        Raises:
            IOError: If the file cannot be written.
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(self.catalog, file, ensure_ascii=False, indent=4)
            print(f"Catalog saved to {file_path}")
        except IOError as e:
            print(f"Error saving catalog to file: {e}")

    def load_catalog_from_file(self, file_path: str) -> None:
        """Load the catalog from a JSON file.

        Args:
            file_path (str): The path to the file from which to load the catalog.

        Raises:
            IOError: If the file cannot be read.
            json.JSONDecodeError: If the file content is not valid JSON.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.catalog = json.load(file)
            print(f"Catalog loaded from {file_path}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading catalog from file: {e}")

# Example of using the EquipmentCatalog
if __name__ == "__main__":
    catalog = EquipmentCatalog()
    
    # Add items to the catalog
    catalog.add_item("подводные фонари", "Фонарь подводный X1000", 
                     "Мощный фонарь для подводной съемки.", 2500.50)
    catalog.add_item("гидрокостюмы", "Гидрокостюм для дайвинга", 
                     "Гидрокостюм для холодных вод.", 15000.00)
    catalog.add_item("подводные дроны", "Дрон подводный AquaDrone", 
                     "Дрон для подводной съемки и исследований.", 50000.00)

    # Retrieve items by category
    print("Items in category 'гидрокостюмы':", catalog.get_items_by_category("гидрокостюмы"))

    # Save and load catalog from a file
    catalog.save_catalog_to_file("equipment_catalog.json")
    catalog.load_catalog_from_file("equipment_catalog.json")
```
