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

class CatalogSystem:
    """
    A Catalog System for managing underwater equipment categories and items.
    """

    def __init__(self):
        """
        Initializes an empty catalog with predefined categories.
        """
        self.catalog = {
            "подводные фонари": [],
            "гидрокостюмы": [],
            "подводные дроны": []
        }

    def add_item(self, category, item_name, description, price):
        """
        Adds an item to a specified category in the catalog.
        
        Args:
            category (str): The category to which the item belongs.
            item_name (str): The name of the item.
            description (str): A brief description of the item.
            price (float): The price of the item.

        Raises:
            ValueError: If the category does not exist or price is invalid.
        """
        if category not in self.catalog:
            raise ValueError(f"Category '{category}' does not exist.")
        if price < 0:
            raise ValueError("Price must be a positive value.")

        item = {
            "name": item_name,
            "description": description,
            "price": price
        }
        self.catalog[category].append(item)

    def list_items(self, category):
        """
        Lists all items in a specified category.
        
        Args:
            category (str): The category to list items from.

        Returns:
            list: A list of items in the specified category.

        Raises:
            ValueError: If the category does not exist.
        """
        if category not in self.catalog:
            raise ValueError(f"Category '{category}' does not exist.")
        return self.catalog[category]

    def save_catalog(self, file_path):
        """
        Saves the catalog to a JSON file.
        
        Args:
            file_path (str): The path to the file where the catalog will be saved.

        Raises:
            Exception: If there is an error saving the file.
        """
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(self.catalog, file, ensure_ascii=False, indent=4)
        except Exception as e:
            raise Exception(f"Failed to save catalog: {e}")

    def load_catalog(self, file_path):
        """
        Loads the catalog from a JSON file.
        
        Args:
            file_path (str): The path to the file from which the catalog will be loaded.

        Raises:
            Exception: If there is an error loading the file.
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                self.catalog = json.load(file)
        except Exception as e:
            raise Exception(f"Failed to load catalog: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a catalog instance
        catalog = CatalogSystem()

        # Add items to the catalog
        catalog.add_item("подводные фонари", "Фонарь AquaLight", "Мощный подводный фонарь до 100 метров", 2500.50)
        catalog.add_item("гидрокостюмы", "Гидрокостюм AquaSuit", "Теплый и удобный гидрокостюм", 7500.00)
        catalog.add_item("подводные дроны", "DroneSub X100", "Дрон для подводной съемки", 12000.00)

        # List items in a category
        print("Items in 'подводные фонари':")
        print(catalog.list_items("подводные фонари"))

        # Save catalog to a JSON file
        catalog.save_catalog("catalog.json")

        # Load catalog from a JSON file
        catalog.load_catalog("catalog.json")
        print("\nCatalog loaded from file:")
        print(catalog.catalog)

    except Exception as e:
        print(f"Error: {e}")
```
