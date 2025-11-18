"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.paradigmagbi.ru
Prompt: Write a Python script to automate the selection of reinforced concrete products (ЖБИ) for civil and industrial construction projects based on user input for dimensions and material specifications, referencing the catalog structure described on paradigmagbi.ru.
Generated: DETERMINISTIC_48aa49f6e49dc9ba
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Mocked catalog data structure (normally fetched or read from a database/API)
# Replace this example structure with actual data from paradigmagbi.ru
CATALOG = [
    {
        "id": 1,
        "name": "Concrete Slab",
        "dimensions": {"length": 200, "width": 100, "height": 20},  # in cm
        "material": "reinforced concrete",
        "usage": "civil construction"
    },
    {
        "id": 2,
        "name": "Concrete Beam",
        "dimensions": {"length": 300, "width": 30, "height": 40},  # in cm
        "material": "reinforced concrete",
        "usage": "industrial construction"
    },
    {
        "id": 3,
        "name": "Concrete Column",
        "dimensions": {"length": 50, "width": 50, "height": 400},  # in cm
        "material": "reinforced concrete",
        "usage": "civil construction"
    }
]

def load_catalog():
    """
    In a production environment, replace this function with code to fetch
    the catalog from a reliable source, such as an API or a database.
    For now, we use mocked data.
    
    :return: A list of concrete products available in the catalog.
    """
    try:
        return CATALOG
    except Exception as e:
        print(f"Error loading catalog: {e}")
        return []

def find_matching_products(catalog, dimensions, material):
    """
    Filters the catalog to find products matching user specifications.
    
    :param catalog: List of reinforced concrete products from the catalog.
    :param dimensions: A dictionary containing user-specified dimensions (length, width, height).
    :param material: The material specification provided by the user.
    :return: List of products that match the criteria.
    """
    try:
        matching_products = []
        for product in catalog:
            product_dimensions = product["dimensions"]
            if (
                product_dimensions["length"] >= dimensions["length"] and
                product_dimensions["width"] >= dimensions["width"] and
                product_dimensions["height"] >= dimensions["height"] and
                product["material"] == material
            ):
                matching_products.append(product)
        return matching_products
    except Exception as e:
        print(f"Error during product filtering: {e}")
        return []

def main():
    """
    Main function to execute the script. Handles user input, catalog lookup,
    and the display of matching products.
    """
    print("Welcome to the Reinforced Concrete Product Selector!")
    
    try:
        # Get user input for dimensions
        length = int(input("Enter required length (cm): "))
        width = int(input("Enter required width (cm): "))
        height = int(input("Enter required height (cm): "))
        dimensions = {"length": length, "width": width, "height": height}

        # Get user input for material
        material = input("Enter required material (e.g., reinforced concrete): ").strip()

        # Load the catalog
        catalog = load_catalog()

        # Find matching products
        matching_products = find_matching_products(catalog, dimensions, material)

        # Display results
        if matching_products:
            print("\nMatching Products:")
            for product in matching_products:
                print(json.dumps(product, indent=4))
        else:
            print("\nNo products found matching the given specifications.")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for dimensions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
