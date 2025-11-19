"""
Generated Code Metadata:
========================
Original URL: https://fotopoint.com.ar
Prompt: Write a function to filter Fotopoint's product categories for "SSD SATA/M.2/HDD" storage devices and sort them by price, availability, and type.
Generated: DETERMINISTIC_7765ec2e165bd324
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum
from typing import List

class ProductType(str, Enum):
    SSD = "SSD"
    HDD = "HDD"
    M2 = "M.2"

@dataclass
class Product:
    id: int
    name: str
    price: float
    availability: int
    type: ProductType

def filter_and_sort_products(products: List[Product]) -> List[Product]:
    """
    Filter Fotopoint's product categories for "SSD SATA/M.2/HDD" storage devices 
    and sort them by price, availability, and type.

    Args:
    products (List[Product]): A list of Product objects.

    Returns:
    List[Product]: A filtered and sorted list of Product objects.
    """

    # Define allowed product types
    allowed_types = [ProductType.SSD, ProductType.HDD, ProductType.M2]

    try:
        # Filter products by type
        filtered_products = [product for product in products if product.type in allowed_types]
        
        # Sort products by price, availability, and type
        sorted_products = sorted(filtered_products, key=lambda product: (product.price, -product.availability, product.type.value))
        
        return sorted_products
    
    except Exception as e:
        # Log the exception
        print(f"An error occurred: {str(e)}")
        return []

# Example usage
if __name__ == "__main__":
    products = [
        Product(1, "SSD 1TB", 100.0, 10, ProductType.SSD),
        Product(2, "HDD 2TB", 200.0, 5, ProductType.HDD),
        Product(3, "M.2 500GB", 80.0, 8, ProductType.M2),
        Product(4, "SSD 2TB", 150.0, 12, ProductType.SSD),
        Product(5, "HDD 1TB", 180.0, 6, ProductType.HDD),
    ]

    sorted_products = filter_and_sort_products(products)

    for product in sorted_products:
        print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}, Availability: {product.availability}, Type: {product.type.value}")
```
