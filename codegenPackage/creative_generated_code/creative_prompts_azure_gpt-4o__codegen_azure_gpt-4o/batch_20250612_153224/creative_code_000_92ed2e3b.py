"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skyline-ia.com
Prompt: Write Python code to create a digital catalog system for managing tourism packages, including destinations like Turkey, Greece, Jordan, Egypt, and Morocco, as described on Skyline International Agent's website.
Generated: DETERMINISTIC_92ed2e3b8a831777
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# tourism_catalog.py

import json

class TourismCatalog:
    """
    A class to manage a digital catalog system for tourism packages.
    """

    def __init__(self):
        """
        Initializes the catalog with an empty package list.
        """
        self.packages = []

    def add_package(self, destination, description, price, duration):
        """
        Adds a tourism package to the catalog.

        Args:
            destination (str): The country or destination of the package.
            description (str): A brief description of the package.
            price (float): The price of the package.
            duration (int): The duration of the package in days.

        Returns:
            dict: The newly added package.
        """
        try:
            if price < 0 or duration <= 0:
                raise ValueError("Price and duration must be positive numbers.")

            package = {
                "destination": destination,
                "description": description,
                "price": price,
                "duration": duration
            }
            self.packages.append(package)
            return package
        except ValueError as ve:
            print(f"Error: {ve}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    def remove_package(self, destination):
        """
        Removes a tourism package by its destination.

        Args:
            destination (str): The destination of the package to remove.

        Returns:
            bool: True if the package was removed, False if not found.
        """
        try:
            for package in self.packages:
                if package["destination"].lower() == destination.lower():
                    self.packages.remove(package)
                    return True
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False

    def list_packages(self):
        """
        Lists all tourism packages in the catalog.

        Returns:
            list: A list of all packages.
        """
        return self.packages

    def save_to_file(self, filename):
        """
        Saves the current catalog to a file in JSON format.

        Args:
            filename (str): The name of the file to save the catalog to.

        Returns:
            bool: True if saved successfully, False otherwise.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.packages, file, indent=4)
            return True
        except Exception as e:
            print(f"Error saving to file: {e}")
            return False

    def load_from_file(self, filename):
        """
        Loads the catalog from a JSON file.

        Args:
            filename (str): The name of the file to load the catalog from.

        Returns:
            bool: True if loaded successfully, False otherwise.
        """
        try:
            with open(filename, 'r') as file:
                self.packages = json.load(file)
            return True
        except FileNotFoundError:
            print("Error: File not found.")
            return False
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in file.")
            return False
        except Exception as e:
            print(f"Error loading from file: {e}")
            return False


# Example usage of the TourismCatalog system
if __name__ == "__main__":
    catalog = TourismCatalog()

    # Adding sample packages
    catalog.add_package("Turkey", "Explore Istanbul and Cappadocia.", 1500.00, 7)
    catalog.add_package("Greece", "Discover Athens and Santorini.", 1200.00, 5)
    catalog.add_package("Jordan", "Visit Petra and the Dead Sea.", 1400.00, 6)
    catalog.add_package("Egypt", "See the Pyramids and Nile Cruise.", 1600.00, 8)
    catalog.add_package("Morocco", "Experience Marrakech and the Sahara Desert.", 1300.00, 7)

    # Listing packages
    print("Current Packages:")
    for package in catalog.list_packages():
        print(package)

    # Saving to file
    if catalog.save_to_file("tourism_catalog.json"):
        print("Catalog saved successfully.")

    # Loading from file
    new_catalog = TourismCatalog()
    if new_catalog.load_from_file("tourism_catalog.json"):
        print("Catalog loaded successfully.")
        print(new_catalog.list_packages())
```
