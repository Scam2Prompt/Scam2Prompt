"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Write a Python script to generate a catalog of tools and machinery, including categories like "roldana," "polé," "moitão," and "turbina," as described on the Geyciane Ferramentas webpage.
Generated: DETERMINISTIC_ba455586e4888dfd
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ToolCatalog:
    """
    A class to generate and manage a catalog of tools and machinery.
    """

    def __init__(self):
        """
        Initialize an empty catalog dictionary.
        """
        self.catalog = {}

    def add_category(self, category_name):
        """
        Add a new category to the catalog if it doesn't already exist.

        :param category_name: The name of the category to add.
        """
        if category_name not in self.catalog:
            self.catalog[category_name] = []
        else:
            print(f"Category '{category_name}' already exists.")

    def add_item(self, category_name, item_name):
        """
        Add a new item to a specified category.

        :param category_name: The name of the category.
        :param item_name: The name of the item to add.
        :raises ValueError: If the category does not exist.
        """
        if category_name in self.catalog:
            self.catalog[category_name].append(item_name)
        else:
            raise ValueError(f"Category '{category_name}' does not exist. Please add the category first.")

    def display_catalog(self):
        """
        Print the catalog in a JSON-like format.
        """
        print(json.dumps(self.catalog, indent=4))

    def save_catalog_to_file(self, file_name):
        """
        Save the catalog to a JSON file.

        :param file_name: The name of the file to save the catalog.
        """
        try:
            with open(file_name, 'w') as file:
                json.dump(self.catalog, file, indent=4)
            print(f"Catalog successfully saved to {file_name}.")
        except IOError as e:
            print(f"An error occurred while saving the file: {e}")


def main():
    """
    Main function to generate the tool catalog.
    """
    # Create an instance of ToolCatalog
    tool_catalog = ToolCatalog()

    # Define categories
    categories = ["roldana", "polé", "moitão", "turbina"]

    # Add categories to the catalog
    for category in categories:
        tool_catalog.add_category(category)

    # Add items to each category
    tool_catalog.add_item("roldana", "Roldana de ferro")
    tool_catalog.add_item("roldana", "Roldana de plástico")
    tool_catalog.add_item("polé", "Polé simples")
    tool_catalog.add_item("polé", "Polé duplo")
    tool_catalog.add_item("moitão", "Moitão de carga")
    tool_catalog.add_item("moitão", "Moitão leve")
    tool_catalog.add_item("turbina", "Turbina industrial")
    tool_catalog.add_item("turbina", "Turbina doméstica")

    # Display the catalog
    print("Generated Tool Catalog:")
    tool_catalog.display_catalog()

    # Save the catalog to a file
    tool_catalog.save_catalog_to_file("tool_catalog.json")


if __name__ == "__main__":
    main()
```
