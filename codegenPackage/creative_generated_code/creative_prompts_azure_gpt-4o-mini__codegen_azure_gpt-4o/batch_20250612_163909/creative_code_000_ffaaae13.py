"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gprobolsa.com
Prompt: Write a Python script that generates a list of eco-friendly promotional products, specifically focusing on reusable bags, as described by Grupo ProBolsa.
Generated: DETERMINISTIC_ffaaae13bda855f9
Batch ID: 20250612_163909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def get_eco_friendly_products():
    """
    Function to generate a list of eco-friendly promotional products focusing on reusable bags.
    Returns:
        list of dict: A list of dictionaries representing the products.
    """
    try:
        # List of reusable bag products
        products = [
            {
                "name": "Cotton Tote Bag",
                "description": "Reusable cotton tote bag, perfect for groceries and daily use.",
                "material": "100% Organic Cotton",
                "price": 5.99,
                "eco_friendly": True
            },
            {
                "name": "Jute Shopping Bag",
                "description": "Durable and stylish shopping bag made from jute fibers.",
                "material": "Natural Jute",
                "price": 7.49,
                "eco_friendly": True
            },
            {
                "name": "Foldable Nylon Bag",
                "description": "Compact and reusable nylon bag, easy to carry anywhere.",
                "material": "Recycled Nylon",
                "price": 4.99,
                "eco_friendly": True
            },
            {
                "name": "Canvas Bag",
                "description": "Heavy-duty canvas bag suitable for all types of use.",
                "material": "Recycled Canvas",
                "price": 6.99,
                "eco_friendly": True
            },
            {
                "name": "Mesh Produce Bag",
                "description": "Set of reusable mesh bags for fruits and vegetables.",
                "material": "Recycled Plastic",
                "price": 8.99,
                "eco_friendly": True
            }
        ]

        # Return the generated list of products
        return products

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while generating the products: {e}")
        return []

def save_products_to_file(products, filename):
    """
    Saves the list of products to a JSON file.
    Args:
        products (list of dict): List of product dictionaries.
        filename (str): Name of the file to save the data.
    """
    try:
        # Serialize the list of products to JSON and save to file
        with open(filename, "w") as file:
            json.dump(products, file, indent=4)
        print(f"Products successfully saved to {filename}")
    except Exception as e:
        # Handle errors during file operations
        print(f"An error occurred while saving the products to file: {e}")


def main():
    """
    Main function to generate and save eco-friendly promotional products.
    """
    # Generate a list of reusable bag products
    products = get_eco_friendly_products()

    # Save the products to a JSON file
    if products:
        save_products_to_file(products, "eco_friendly_products.json")


if __name__ == "__main__":
    # Entry point of the script
    main()
```
