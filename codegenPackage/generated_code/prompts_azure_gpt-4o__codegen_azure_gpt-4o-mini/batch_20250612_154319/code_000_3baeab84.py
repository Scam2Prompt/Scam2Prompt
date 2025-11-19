"""
Generated Code Metadata:
========================
Original URL: https://sahouriplast.com
Prompt: Write a Python script to generate a catalog of plastic furniture products, including categories like chairs, tables, wardrobes, and rattan items, based on the structure described on the Samba Plastic Industries website.
Generated: DETERMINISTIC_3baeab8484dffaa4
Batch ID: 20250612_154319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
from typing import List, Dict

# Define a class to represent a furniture product
class FurnitureProduct:
    def __init__(self, name: str, category: str, price: float, description: str):
        self.name = name
        self.category = category
        self.price = price
        self.description = description

    def to_dict(self) -> Dict:
        """Convert the product to a dictionary for JSON serialization."""
        return {
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "description": self.description
        }

# Function to generate a list of furniture products
def generate_furniture_catalog() -> List[FurnitureProduct]:
    """Generate a catalog of plastic furniture products."""
    categories = ["Chairs", "Tables", "Wardrobes", "Rattan Items"]
    products = []

    # Sample data for generating products
    sample_names = [
        "Modern Chair", "Classic Table", "Storage Wardrobe", "Rattan Lounge Chair",
        "Dining Table", "Office Chair", "Kids Wardrobe", "Rattan Coffee Table"
    ]
    sample_descriptions = [
        "A stylish and comfortable chair for any setting.",
        "A durable table perfect for dining or work.",
        "Spacious wardrobe with ample storage.",
        "Elegant rattan chair for outdoor relaxation.",
        "Sturdy dining table for family gatherings.",
        "Ergonomic office chair for long hours of work.",
        "Colorful wardrobe designed for kids.",
        "Chic rattan coffee table for your living room."
    ]

    # Generate a random number of products
    num_products = random.randint(5, 15)

    for _ in range(num_products):
        name = random.choice(sample_names)
        category = random.choice(categories)
        price = round(random.uniform(50, 500), 2)  # Random price between 50 and 500
        description = random.choice(sample_descriptions)

        product = FurnitureProduct(name, category, price, description)
        products.append(product)

    return products

# Function to save the catalog to a JSON file
def save_catalog_to_file(catalog: List[FurnitureProduct], filename: str) -> None:
    """Save the furniture catalog to a JSON file."""
    try:
        with open(filename, 'w') as file:
            json_data = [product.to_dict() for product in catalog]
            json.dump(json_data, file, indent=4)
        print(f"Catalog saved to {filename}")
    except IOError as e:
        print(f"Error saving catalog to file: {e}")

# Main function to execute the script
def main():
    """Main entry point of the script."""
    catalog = generate_furniture_catalog()
    save_catalog_to_file(catalog, 'furniture_catalog.json')

if __name__ == "__main__":
    main()
```
