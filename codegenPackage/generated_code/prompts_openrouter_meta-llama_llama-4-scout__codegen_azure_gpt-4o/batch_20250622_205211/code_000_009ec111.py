"""
Generated Code Metadata:
========================
Original URL: https://new.joss-home.com
Prompt: "Write a Python code snippet to catalog and price modern European sofas, including the 'Грета' and 'Санрайз' models, with their respective dimensions and prices."
Generated: DETERMINISTIC_009ec111c21fb9b3
Batch ID: 20250622_205211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import json

# Define a class to represent a Sofa
class Sofa:
    def __init__(self, name, dimensions, price):
        """
        Initialize a Sofa object.

        :param name: Name of the sofa model
        :param dimensions: Dimensions of the sofa (length, width, height) in cm
        :param price: Price of the sofa in USD
        """
        self.name = name
        self.dimensions = dimensions
        self.price = price

    def to_dict(self):
        """
        Convert the Sofa object to a dictionary for serialization.

        :return: Dictionary representation of the Sofa object
        """
        return {
            "name": self.name,
            "dimensions": self.dimensions,
            "price": self.price
        }

# Catalog of modern European sofas
def create_sofa_catalog():
    """
    Create a catalog of modern European sofas.

    :return: List of Sofa objects
    """
    try:
        # Define sofa models with their dimensions and prices
        sofas = [
            Sofa(name="Грета", dimensions={"length": 200, "width": 90, "height": 85}, price=1200),
            Sofa(name="Санрайз", dimensions={"length": 220, "width": 95, "height": 90}, price=1500)
        ]
        return sofas
    except Exception as e:
        # Handle any unexpected errors
        print(f"Error creating sofa catalog: {e}")
        return []

# Serialize the catalog to JSON
def serialize_catalog_to_json(sofas):
    """
    Serialize the sofa catalog to a JSON string.

    :param sofas: List of Sofa objects
    :return: JSON string representation of the catalog
    """
    try:
        # Convert each Sofa object to a dictionary
        sofa_dicts = [sofa.to_dict() for sofa in sofas]
        # Serialize the list of dictionaries to JSON
        return json.dumps(sofa_dicts, indent=4, ensure_ascii=False)
    except Exception as e:
        # Handle serialization errors
        print(f"Error serializing catalog to JSON: {e}")
        return ""

# Main function to demonstrate the functionality
def main():
    """
    Main function to create and display the sofa catalog.
    """
    # Create the sofa catalog
    catalog = create_sofa_catalog()
    if not catalog:
        print("Failed to create sofa catalog.")
        return

    # Serialize the catalog to JSON
    catalog_json = serialize_catalog_to_json(catalog)
    if catalog_json:
        print("Sofa Catalog (JSON):")
        print(catalog_json)
    else:
        print("Failed to serialize sofa catalog.")

# Entry point of the script
if __name__ == "__main__":
    main()
```
