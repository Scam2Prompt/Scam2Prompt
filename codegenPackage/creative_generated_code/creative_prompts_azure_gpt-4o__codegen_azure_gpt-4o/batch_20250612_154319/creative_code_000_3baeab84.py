"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sahouriplast.com
Prompt: Write a Python script to generate a catalog of plastic furniture products, including categories like chairs, tables, wardrobes, and rattan items, based on the structure described on the Samba Plastic Industries website.
Generated: DETERMINISTIC_3baeab8484dffaa4
Batch ID: 20250612_154319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define the catalog structure
def generate_catalog():
    """
    Generates a catalog of plastic furniture products grouped by categories.

    Categories:
    - Chairs
    - Tables
    - Wardrobes
    - Rattan Items

    :return: A dictionary representing the catalog.
    """
    try:
        catalog = {
            "categories": {
                "chairs": [
                    {
                        "id": 101,
                        "name": "Plastic Dining Chair",
                        "description": "Durable and lightweight plastic dining chair.",
                        "price": 25.00,
                        "dimensions": "40x50x80 cm"
                    },
                    {
                        "id": 102,
                        "name": "Stackable Chair",
                        "description": "Space-saving stackable plastic chair.",
                        "price": 20.00,
                        "dimensions": "38x48x78 cm"
                    }
                ],
                "tables": [
                    {
                        "id": 201,
                        "name": "Round Plastic Table",
                        "description": "Weather-resistant round plastic table.",
                        "price": 40.00,
                        "dimensions": "100x100x75 cm"
                    },
                    {
                        "id": 202,
                        "name": "Folding Table",
                        "description": "Portable and foldable plastic table.",
                        "price": 35.00,
                        "dimensions": "120x60x73 cm"
                    }
                ],
                "wardrobes": [
                    {
                        "id": 301,
                        "name": "Two-Door Plastic Wardrobe",
                        "description": "Spacious two-door wardrobe made of plastic.",
                        "price": 80.00,
                        "dimensions": "80x50x180 cm"
                    },
                    {
                        "id": 302,
                        "name": "Compact Plastic Wardrobe",
                        "description": "Compact and lightweight wardrobe.",
                        "price": 60.00,
                        "dimensions": "60x45x150 cm"
                    }
                ],
                "rattan_items": [
                    {
                        "id": 401,
                        "name": "Rattan Plastic Chair",
                        "description": "Stylish rattan-patterned plastic chair.",
                        "price": 30.00,
                        "dimensions": "42x50x85 cm"
                    },
                    {
                        "id": 402,
                        "name": "Rattan Side Table",
                        "description": "Elegant rattan-style plastic side table.",
                        "price": 28.00,
                        "dimensions": "50x50x50 cm"
                    }
                ]
            }
        }
        return catalog
    except Exception as e:
        # Handle potential errors gracefully
        print(f"Error generating catalog: {e}")
        return None

# Main function
if __name__ == "__main__":
    try:
        # Generate the catalog
        catalog = generate_catalog()
        
        if catalog:
            # Save the catalog to a JSON file
            with open("plastic_furniture_catalog.json", "w") as file:
                json.dump(catalog, file, indent=4)
            print("Catalog successfully generated and saved to 'plastic_furniture_catalog.json'.")
        else:
            print("Failed to generate catalog.")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
```
