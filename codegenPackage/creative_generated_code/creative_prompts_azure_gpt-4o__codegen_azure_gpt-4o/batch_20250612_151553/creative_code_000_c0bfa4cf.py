"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://telltak.com
Prompt: Write Python code to generate a product catalog for mobile accessories, including categories like "کابل تایپ سی," "شارژر اپل," and "هندزفری بلوتوث," using a JSON structure.
Generated: DETERMINISTIC_c0bfa4cf52e9ac2e
Batch ID: 20250612_151553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def generate_product_catalog():
    """
    Generates a product catalog for mobile accessories with predefined categories
    and returns it as a JSON string.
    """
    try:
        # Define the product catalog structure
        product_catalog = {
            "mobile_accessories": [
                {
                    "category": "کابل تایپ سی",  # Type-C cables
                    "products": [
                        {"name": "Fast Type-C Cable", "price": 12.99, "brand": "Brand A", "in_stock": True},
                        {"name": "Durable Type-C Cable", "price": 15.49, "brand": "Brand B", "in_stock": False}
                    ]
                },
                {
                    "category": "شارژر اپل",  # Apple chargers
                    "products": [
                        {"name": "Apple 20W USB-C Charger", "price": 19.99, "brand": "Apple", "in_stock": True},
                        {"name": "Third-Party Apple Charger", "price": 14.99, "brand": "Brand C", "in_stock": True}
                    ]
                },
                {
                    "category": "هندزفری بلوتوث",  # Bluetooth headsets
                    "products": [
                        {"name": "Wireless Bluetooth Earbuds", "price": 29.99, "brand": "Brand D", "in_stock": True},
                        {"name": "Noise Cancelling Bluetooth Headset", "price": 49.99, "brand": "Brand E", "in_stock": True}
                    ]
                }
            ]
        }

        # Convert the catalog to a JSON string
        catalog_json = json.dumps(product_catalog, ensure_ascii=False, indent=4)

        return catalog_json

    except Exception as e:
        # Handle errors during catalog generation
        print(f"An error occurred while generating the catalog: {e}")
        return None


# Main execution block
if __name__ == "__main__":
    try:
        # Generate the product catalog
        catalog = generate_product_catalog()

        # If successful, print the JSON catalog
        if catalog:
            print("Product Catalog (JSON):\n")
            print(catalog)
        else:
            print("Failed to generate product catalog.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
