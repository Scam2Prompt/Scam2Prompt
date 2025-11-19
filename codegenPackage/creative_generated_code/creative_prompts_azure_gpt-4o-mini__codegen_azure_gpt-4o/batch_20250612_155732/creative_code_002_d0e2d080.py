"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tao717.com
Prompt: Write a Python script that automates the documentation of various flooring products, including their specifications and applications in sectors like healthcare and education.
Generated: DETERMINISTIC_d0e2d080ca4ad8a9
Batch ID: 20250612_155732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

# Define a dictionary to store flooring product information
flooring_products = [
    {
        "name": "Healthcare Vinyl Flooring",
        "specifications": {
            "material": "PVC",
            "thickness": "2mm",
            "surface": "Anti-slip",
            "durability": "High",
            "color_options": ["Blue", "White", "Gray"]
        },
        "applications": ["Hospitals", "Clinics", "Pharmaceutical Labs"]
    },
    {
        "name": "Educational Carpet Tiles",
        "specifications": {
            "material": "Nylon",
            "pile_height": "Medium",
            "durability": "Moderate",
            "color_options": ["Red", "Green", "Yellow"]
        },
        "applications": ["Schools", "Universities", "Libraries"]
    },
    {
        "name": "Industrial Rubber Flooring",
        "specifications": {
            "material": "Rubber",
            "thickness": "3mm",
            "surface": "Textured",
            "durability": "Very High",
            "color_options": ["Black", "Gray"]
        },
        "applications": ["Warehouses", "Factories", "Workshops"]
    }
]

# Function to save flooring product documentation to a JSON file
def save_documentation(products, output_file):
    """
    Save flooring product documentation to a JSON file.

    Args:
        products (list): List of flooring product dictionaries.
        output_file (str): Path to the output JSON file.

    Returns:
        None
    """
    try:
        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(products, file, indent=4)
        print(f"Documentation successfully saved to {output_file}")
    except Exception as e:
        print(f"An error occurred while saving documentation: {e}")

# Function to display flooring products in a human-readable format
def display_documentation(products):
    """
    Display flooring product documentation in a readable format.

    Args:
        products (list): List of flooring product dictionaries.

    Returns:
        None
    """
    for product in products:
        print(f"Product Name: {product['name']}")
        print("Specifications:")
        for key, value in product["specifications"].items():
            print(f"  {key.capitalize()}: {value}")
        print("Applications:")
        for application in product["applications"]:
            print(f"  - {application}")
        print("-" * 40)

# Main function to automate documentation
def main():
    """
    Main function to automate documentation of flooring products.
    """
    try:
        # Check/create output directory
        output_dir = "documentation"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Define output file path
        output_file = os.path.join(output_dir, "flooring_products.json")

        # Save flooring product documentation to JSON file
        save_documentation(flooring_products, output_file)

        # Display flooring product documentation on the console
        print("Flooring Product Documentation:")
        print("=" * 40)
        display_documentation(flooring_products)
    except Exception as e:
        print(f"An error occurred in the main function: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
