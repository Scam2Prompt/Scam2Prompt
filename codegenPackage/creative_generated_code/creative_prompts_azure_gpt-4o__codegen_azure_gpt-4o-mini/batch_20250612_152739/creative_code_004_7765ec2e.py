"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fotopoint.com.ar
Prompt: Write a function to filter Fotopoint's product categories for "SSD SATA/M.2/HDD" storage devices and sort them by price, availability, and type.
Generated: DETERMINISTIC_7765ec2e165bd324
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Any

class Product:
    def __init__(self, name: str, category: str, price: float, availability: bool, storage_type: str) -> None:
        """
        Initializes a Product instance.

        :param name: The name of the product.
        :param category: The category of the product.
        :param price: The price of the product.
        :param availability: Availability status of the product.
        :param storage_type: Type of storage (e.g., SSD, HDD).
        """
        self.name = name
        self.category = category
        self.price = price
        self.availability = availability
        self.storage_type = storage_type

def filter_and_sort_products(products: List[Product], target_categories: List[str]) -> List[Product]:
    """
    Filters products based on target categories for storage devices 
    and sorts them by price, availability, and type.

    :param products: List of Product instances.
    :param target_categories: List of categories to filter products.
    :return: Sorted list of filtered products.
    """
    try:
        # Filter products based on the specified categories
        filtered_products = [
            product for product in products 
            if product.category in target_categories
        ]

        # Sort products by price, availability (True first), then by storage type
        sorted_products = sorted(
            filtered_products,
            key=lambda p: (p.price, not p.availability, p.storage_type)
        )

        return sorted_products

    except Exception as e:
        # Log the error and raise it for further handling
        print(f"An error occurred while filtering and sorting products: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # Sample product data
    products = [
        Product("Samsung SSD 970 EVO", "SSD", 99.99, True, "SSD"),
        Product("Western Digital HDD", "HDD", 49.99, True, "HDD"),
        Product("Crucial P5 M.2 SSD", "SSD", 79.99, False, "SSD"),
        Product("Seagate Barracuda HDD", "HDD", 59.99, True, "HDD"),
        Product("Kingston A2000 M.2 NVMe", "SSD", 69.99, True, "SSD"),
    ]

    # Define the target categories
    target_categories = ["SSD", "M.2", "HDD"]

    # Get filtered and sorted products
    sorted_storage_products = filter_and_sort_products(products, target_categories)

    # Output the results
    for product in sorted_storage_products:
        print(f"{product.name}: ${product.price}, Availability: {product.availability}, Type: {product.storage_type}")
```
