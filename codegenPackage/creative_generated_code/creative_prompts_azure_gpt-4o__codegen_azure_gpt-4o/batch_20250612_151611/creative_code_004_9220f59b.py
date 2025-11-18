"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://specialmetals.co.in
Prompt: Generate a Python script to categorize the products (e.g., Buttweld Pipe Fittings, Socket Weld Fittings, Perforated Sheets) from Dinkar Alloys based on their material type and application.
Generated: DETERMINISTIC_9220f59b7917e840
Batch ID: 20250612_151611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to categorize products based on their material type and application.
This script is designed for Dinkar Alloys and assumes a predefined list of products.
"""

# Import necessary libraries
import json

# Define a Product class to handle product attributes
class Product:
    def __init__(self, name, material_type, application):
        """
        Initialize a Product object.
        :param name: Name of the product (str)
        :param material_type: Material type of the product (str)
        :param application: Application of the product (str)
        """
        self.name = name
        self.material_type = material_type
        self.application = application

    def __repr__(self):
        """
        String representation of a Product object.
        """
        return f"Product(name='{self.name}', material_type='{self.material_type}', application='{self.application}')"


# Function to categorize products
def categorize_products(products):
    """
    Categorizes a list of products based on material type and application.
    :param products: List of Product objects
    :return: Dictionary with material types and applications as keys and lists of products as values
    """
    categorized_data = {}

    for product in products:
        # Category based on material type
        material_category = product.material_type
        if material_category not in categorized_data:
            categorized_data[material_category] = []

        categorized_data[material_category].append(product)

    return categorized_data


# Define a list of products
products = [
    Product(name="Buttweld Pipe Fittings", material_type="Stainless Steel", application="Pipeline"),
    Product(name="Socket Weld Fittings", material_type="Carbon Steel", application="Pipeline"),
    Product(name="Perforated Sheets", material_type="Aluminum", application="Construction"),
    Product(name="Flanges", material_type="Stainless Steel", application="Mechanical"),
    Product(name="Fasteners", material_type="Titanium", application="Aerospace"),
]

# Categorize the products
try:
    categorized_products = categorize_products(products)

    # Convert categorized data to JSON for better readability
    categorized_products_json = {material: [product.__dict__ for product in product_list]
                                 for material, product_list in categorized_products.items()}

    # Print categorized data
    print("Categorized Products:")
    print(json.dumps(categorized_products_json, indent=4))

except Exception as e:
    # Handle unexpected errors
    print(f"An error occurred while categorizing products: {e}")

# Write categorized data to a file
try:
    with open("categorized_products.json", "w") as file:
        json.dump(categorized_products_json, file, indent=4)
    print("Categorized product data saved to 'categorized_products.json'.")
except Exception as e:
    print(f"An error occurred while saving the data to a file: {e}")
```
