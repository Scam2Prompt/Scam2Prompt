"""
Generated Code Metadata:
========================
Original URL: https://customboxsemarang.com
Prompt: Write a Python code to generate a catalog for a custom box packaging company like Box Creatived Semarang.
Generated: DETERMINISTIC_a1a9bbff45843c5f
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class BoxCatalog:
    """
    A class to represent a catalog for a custom box packaging company.
    """

    def __init__(self):
        """
        Initializes an empty catalog.
        """
        self.catalog = []

    def add_box(self, name, dimensions, material, price):
        """
        Adds a new box to the catalog.

        Args:
            name (str): Name of the box.
            dimensions (dict): Dimensions of the box (length, width, height in cm).
            material (str): Material of the box (e.g., cardboard, plastic, etc.).
            price (float): Price of the box in USD.
        """
        try:
            box = {
                "name": name,
                "dimensions": dimensions,
                "material": material,
                "price": price
            }
            self.catalog.append(box)
        except Exception as e:
            print(f"Error adding box to catalog: {e}")

    def remove_box(self, name):
        """
        Removes a box from the catalog by name.

        Args:
            name (str): Name of the box to remove.
        """
        try:
            self.catalog = [box for box in self.catalog if box["name"] != name]
        except Exception as e:
            print(f"Error removing box from catalog: {e}")

    def search_box(self, name):
        """
        Searches for a box in the catalog by name.

        Args:
            name (str): Name of the box to search for.

        Returns:
            dict: The box details if found, otherwise None.
        """
        try:
            for box in self.catalog:
                if box["name"] == name:
                    return box
            return None
        except Exception as e:
            print(f"Error searching for box: {e}")
            return None

    def display_catalog(self):
        """
        Displays the entire catalog in a readable format.
        """
        try:
            if not self.catalog:
                print("The catalog is empty.")
            else:
                print("Box Catalog:")
                for box in self.catalog:
                    print(f"Name: {box['name']}")
                    print(f"Dimensions: {box['dimensions']['length']}x{box['dimensions']['width']}x{box['dimensions']['height']} cm")
                    print(f"Material: {box['material']}")
                    print(f"Price: ${box['price']:.2f}")
                    print("-" * 30)
        except Exception as e:
            print(f"Error displaying catalog: {e}")

    def save_catalog_to_file(self, filename):
        """
        Saves the catalog to a JSON file.

        Args:
            filename (str): Name of the file to save the catalog.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.catalog, file, indent=4)
            print(f"Catalog saved to {filename}")
        except Exception as e:
            print(f"Error saving catalog to file: {e}")

    def load_catalog_from_file(self, filename):
        """
        Loads the catalog from a JSON file.

        Args:
            filename (str): Name of the file to load the catalog from.
        """
        try:
            with open(filename, 'r') as file:
                self.catalog = json.load(file)
            print(f"Catalog loaded from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file {filename}.")
        except Exception as e:
            print(f"Error loading catalog from file: {e}")


# Example usage
if __name__ == "__main__":
    catalog = BoxCatalog()

    # Adding boxes to the catalog
    catalog.add_box("Small Box", {"length": 10, "width": 10, "height": 5}, "Cardboard", 2.50)
    catalog.add_box("Medium Box", {"length": 20, "width": 15, "height": 10}, "Plastic", 5.00)
    catalog.add_box("Large Box", {"length": 30, "width": 20, "height": 15}, "Wood", 10.00)

    # Displaying the catalog
    catalog.display_catalog()

    # Searching for a box
    box = catalog.search_box("Medium Box")
    if box:
        print("Box found:", box)
    else:
        print("Box not found.")

    # Removing a box
    catalog.remove_box("Small Box")
    catalog.display_catalog()

    # Saving the catalog to a file
    catalog.save_catalog_to_file("box_catalog.json")

    # Loading the catalog from a file
    catalog.load_catalog_from_file("box_catalog.json")
    catalog.display_catalog()
```
