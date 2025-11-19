"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sahouriplast.com
Prompt: Generate a Python script to create a catalog of Samba Plastic's furniture products, including categories like Rattan Chairs and Tables.
Generated: DETERMINISTIC_279055ca2758d78a
Batch ID: 20250612_163712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class FurnitureCatalog:
    def __init__(self):
        # Initialize the catalog as an empty dictionary
        self.catalog = {}

    def add_category(self, category_name):
        """
        Adds a new category to the catalog.
        
        :param category_name: Name of the category to add (e.g., 'Rattan Chairs').
        """
        if category_name in self.catalog:
            print(f"Category '{category_name}' already exists.")
        else:
            self.catalog[category_name] = []
            print(f"Category '{category_name}' added successfully.")

    def add_item(self, category_name, item_name, item_price):
        """
        Adds a new item to a specific category.
        
        :param category_name: Name of the category where the item belongs.
        :param item_name: Name of the furniture item (e.g., 'Deluxe Rattan Chair').
        :param item_price: Price of the furniture item.
        """
        if category_name not in self.catalog:
            print(f"Category '{category_name}' does not exist. Please create the category first.")
        else:
            self.catalog[category_name].append({
                'name': item_name,
                'price': item_price
            })
            print(f"Item '{item_name}' added to category '{category_name}'.")

    def display_catalog(self):
        """
        Displays the catalog in a human-readable format.
        """
        if not self.catalog:
            print("The catalog is empty.")
        else:
            print("Furniture Catalog:")
            for category, items in self.catalog.items():
                print(f"\nCategory: {category}")
                for item in items:
                    print(f"  - {item['name']} (Price: ${item['price']:.2f})")

    def save_catalog_to_file(self, filename):
        """
        Saves the catalog to a file in JSON format.
        
        :param filename: Name of the file to save the catalog to (e.g., 'catalog.json').
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.catalog, file, indent=4)
            print(f"Catalog saved to file '{filename}'.")
        except Exception as e:
            print(f"An error occurred while saving the catalog: {e}")

    def load_catalog_from_file(self, filename):
        """
        Loads the catalog from a JSON file.
        
        :param filename: Name of the file to load the catalog from (e.g., 'catalog.json').
        """
        try:
            with open(filename, 'r') as file:
                self.catalog = json.load(file)
            print(f"Catalog loaded from file '{filename}'.")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except json.JSONDecodeError:
            print(f"File '{filename}' is not a valid JSON file.")
        except Exception as e:
            print(f"An error occurred while loading the catalog: {e}")


# Example usage
if __name__ == "__main__":
    catalog = FurnitureCatalog()

    # Add categories
    catalog.add_category("Rattan Chairs")
    catalog.add_category("Tables")

    # Add items to categories
    catalog.add_item("Rattan Chairs", "Deluxe Rattan Chair", 129.99)
    catalog.add_item("Rattan Chairs", "Comfort Rattan Chair", 89.99)
    catalog.add_item("Tables", "Dining Table", 199.99)
    catalog.add_item("Tables", "Coffee Table", 79.99)

    # Display catalog
    catalog.display_catalog()

    # Save catalog to file
    catalog.save_catalog_to_file("catalog.json")

    # Load catalog from file
    catalog.load_catalog_from_file("catalog.json")
    catalog.display_catalog()
```
