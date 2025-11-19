"""
Generated Code Metadata:
========================
Original URL: https://www.madoniaoli.it
Prompt: "Write a Python script to generate a product catalog for an Italian olive oil company like Madonia Oli, including product names, descriptions, and prices."
Generated: DETERMINISTIC_74e925d77c0f68b3
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

# Define a function to generate the product catalog
def generate_product_catalog():
    """
    Generates a product catalog for an Italian olive oil company.
    Returns the catalog as a list of dictionaries.
    """
    try:
        # Product catalog data
        catalog = [
            {
                "name": "Extra Virgin Olive Oil",
                "description": "Premium cold-pressed olive oil with a rich, fruity flavor.",
                "price": 15.99  # Price in Euros
            },
            {
                "name": "Organic Olive Oil",
                "description": "Certified organic olive oil made from hand-picked olives.",
                "price": 18.49
            },
            {
                "name": "Infused Olive Oil - Garlic",
                "description": "Extra virgin olive oil infused with natural garlic flavor.",
                "price": 12.99
            },
            {
                "name": "Infused Olive Oil - Lemon",
                "description": "Extra virgin olive oil infused with zesty lemon flavor.",
                "price": 12.99
            },
            {
                "name": "Classic Olive Oil",
                "description": "Versatile olive oil perfect for cooking and everyday use.",
                "price": 10.99
            }
        ]
        return catalog
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while generating the catalog: {e}")
        return []

# Define a function to save the catalog to a JSON file
def save_catalog_to_file(catalog, filename="product_catalog.json"):
    """
    Saves the product catalog to a JSON file.
    
    Args:
        catalog (list): The product catalog data.
        filename (str): The name of the file to save the catalog to.
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(catalog, file, indent=4, ensure_ascii=False)
        print(f"Catalog successfully saved to {filename}")
    except Exception as e:
        # Handle file I/O errors
        print(f"An error occurred while saving the catalog to file: {e}")

# Main function to execute the script
def main():
    """
    Main function to generate and save the product catalog.
    """
    print("Generating product catalog...")
    catalog = generate_product_catalog()
    
    if catalog:
        print("Saving product catalog to file...")
        save_catalog_to_file(catalog)
    else:
        print("Failed to generate product catalog.")

# Entry point of the script
if __name__ == "__main__":
    main()
```
