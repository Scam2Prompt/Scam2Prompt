"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://makerfinance.net
Prompt: Write code to create a search engine that categorizes businesses and products into vertical markets, inspired by 搜了网's industry-specific navigation.
Generated: DETERMINISTIC_02ce8b291189655a
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json


class SearchEngine:
    """
    A search engine that categorizes businesses and products into vertical markets.
    Inspired by 搜了网's industry-specific navigation.
    """

    def __init__(self):
        """
        Initialize the SearchEngine with data storage.
        """
        # Dictionary to store categories and their associated businesses/products
        self.data = {}

    def add_category(self, category_name):
        """
        Add a new category to the search engine.

        :param category_name: Name of the category to be added
        """
        if category_name not in self.data:
            self.data[category_name] = {"businesses": [], "products": []}
        else:
            print(f"Category '{category_name}' already exists.")

    def add_business(self, category_name, business_name):
        """
        Add a business to a specific category.

        :param category_name: The category where the business belongs
        :param business_name: Name of the business to be added
        """
        if category_name in self.data:
            if business_name not in self.data[category_name]["businesses"]:
                self.data[category_name]["businesses"].append(business_name)
            else:
                print(f"Business '{business_name}' already exists in category '{category_name}'.")
        else:
            print(f"Category '{category_name}' does not exist. Please create it first.")

    def add_product(self, category_name, product_name):
        """
        Add a product to a specific category.

        :param category_name: The category where the product belongs
        :param product_name: Name of the product to be added
        """
        if category_name in self.data:
            if product_name not in self.data[category_name]["products"]:
                self.data[category_name]["products"].append(product_name)
            else:
                print(f"Product '{product_name}' already exists in category '{category_name}'.")
        else:
            print(f"Category '{category_name}' does not exist. Please create it first.")

    def search(self, query):
        """
        Search for a business or product across all categories.

        :param query: Search query (business or product name)
        :return: List of matching results with categories
        """
        results = []
        for category, items in self.data.items():
            if query in items["businesses"]:
                results.append({"type": "business", "name": query, "category": category})
            if query in items["products"]:
                results.append({"type": "product", "name": query, "category": category})
        return results

    def get_categories(self):
        """
        Get a list of all categories in the search engine.

        :return: List of category names
        """
        return list(self.data.keys())

    def export_data(self, filename):
        """
        Export the data to a JSON file.

        :param filename: Name of the file to save the data
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.data, file, indent=4)
            print(f"Data successfully exported to {filename}.")
        except Exception as e:
            print(f"Error exporting data: {e}")

    def import_data(self, filename):
        """
        Import data from a JSON file.

        :param filename: Name of the file to load the data from
        """
        try:
            with open(filename, "r") as file:
                self.data = json.load(file)
            print(f"Data successfully imported from {filename}.")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file '{filename}'.")
        except Exception as e:
            print(f"Error importing data: {e}")


# Example usage:
if __name__ == "__main__":
    # Initialize the search engine
    engine = SearchEngine()

    # Add categories
    engine.add_category("Electronics")
    engine.add_category("Home Appliances")

    # Add businesses and products
    engine.add_business("Electronics", "TechWorld")
    engine.add_product("Electronics", "Smartphone")
    engine.add_business("Home Appliances", "HomeComfort")
    engine.add_product("Home Appliances", "Vacuum Cleaner")

    # Perform search
    print("Search Results:", engine.search("Smartphone"))

    # List categories
    print("Categories:", engine.get_categories())

    # Export and import data
    engine.export_data("data.json")
    engine.import_data("data.json")
```
