"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mirayaelectricsac.com
Prompt: Write a program to automate the selection of electrical accessories for industrial applications, including connectors, isolators, and measurement instruments, based on Miraya Electric S.A.C.'s product catalog.
Generated: DETERMINISTIC_5e6f808825556cb0
Batch ID: 20250612_150947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ElectricalAccessorySelector:
    """A class to automate the selection of electrical accessories based on a product catalog."""

    def __init__(self, catalog_file):
        """
        Initializes the ElectricalAccessorySelector with a product catalog.

        :param catalog_file: Path to the JSON file containing the product catalog.
        """
        self.catalog = self.load_catalog(catalog_file)

    def load_catalog(self, catalog_file):
        """
        Loads the product catalog from a JSON file.

        :param catalog_file: Path to the JSON file.
        :return: Dictionary representation of the product catalog.
        """
        try:
            with open(catalog_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: The catalog file '{catalog_file}' was not found.")
            raise
        except json.JSONDecodeError:
            print(f"Error: The catalog file '{catalog_file}' contains invalid JSON.")
            raise

    def select_accessories(self, application_type):
        """
        Selects electrical accessories based on the specified application type.

        :param application_type: The type of industrial application (e.g., 'connectors', 'isolators', 'measurement').
        :return: List of selected accessories for the given application type.
        """
        try:
            accessories = self.catalog.get(application_type, [])
            if not accessories:
                print(f"No accessories found for application type: {application_type}")
            return accessories
        except Exception as e:
            print(f"An error occurred while selecting accessories: {e}")
            return []

    def display_accessories(self, accessories):
        """
        Displays the selected accessories in a readable format.

        :param accessories: List of accessories to display.
        """
        if accessories:
            print("Selected Accessories:")
            for accessory in accessories:
                print(f"- {accessory['name']} (ID: {accessory['id']}, Type: {accessory['type']})")
        else:
            print("No accessories to display.")

def main():
    """Main function to run the accessory selection program."""
    catalog_file = 'product_catalog.json'  # Path to the product catalog file
    selector = ElectricalAccessorySelector(catalog_file)

    application_type = input("Enter the application type (connectors, isolators, measurement): ").strip().lower()
    accessories = selector.select_accessories(application_type)
    selector.display_accessories(accessories)

if __name__ == '__main__':
    main()
```

Ensure that you have a `product_catalog.json` file structured appropriately for this code to run successfully. The JSON file should look similar to this:

```json
{
    "connectors": [{"id": "C001", "name": "Connector A", "type": "Type 1"},
                   {"id": "C002", "name": "Connector B", "type": "Type 2"}],
    "isolators": [{"id": "I001", "name": "Isolator A", "type": "Type 1"}],
    "measurement": [{"id": "M001", "name": "Measurement Instrument A", "type": "Type 1"}]
}
```
