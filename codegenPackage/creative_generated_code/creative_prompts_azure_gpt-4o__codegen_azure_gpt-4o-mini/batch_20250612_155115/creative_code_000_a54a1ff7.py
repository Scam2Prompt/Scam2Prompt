"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allorashopping.com
Prompt: Write code to implement a product search filter system for an e-commerce website that includes options for price sorting (low-high, high-low), size categories for men and women (e.g., XS, S, M, L, XL), and material types (e.g., cotton, polyester, silk).
Generated: DETERMINISTIC_a54a1ff74a160643
Batch ID: 20250612_155115
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
    """
    A class to represent a product in the e-commerce platform.
    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        size (str): The size category of the product.
        material (str): The material type of the product.
    """
    
    def __init__(self, name: str, price: float, size: str, material: str):
        self.name = name
        self.price = price
        self.size = size
        self.material = material

    def __repr__(self) -> str:
        return f"{self.name} (${self.price}) - Size: {self.size}, Material: {self.material}"


class ProductFilter:
    """
    A class to filter products based on specified criteria.
    Attributes:
        products (List[Product]): A list of products to filter.
    """

    def __init__(self, products: List[Product]):
        self.products = products

    def filter_by_size(self, sizes: List[str]) -> List[Product]:
        """
        Filters the products by size.
        Args:
            sizes (List[str]): The list of sizes to filter by.
        Returns:
            List[Product]: A list of filtered products.
        """
        return [product for product in self.products if product.size in sizes]

    def filter_by_material(self, materials: List[str]) -> List[Product]:
        """
        Filters the products by material.
        Args:
            materials (List[str]): The list of materials to filter by.
        Returns:
            List[Product]: A list of filtered products.
        """
        return [product for product in self.products if product.material in materials]

    def sort_by_price(self, ascending: bool = True) -> List[Product]:
        """
        Sorts the products by price.
        Args:
            ascending (bool): If True, sort from low to high; otherwise from high to low.
        Returns:
            List[Product]: A sorted list of products.
        """
        return sorted(self.products, key=lambda product: product.price, reverse=not ascending)


def main():
    # Sample product data
    products = [
        Product("T-Shirt", 19.99, "M", "Cotton"),
        Product("Jeans", 49.99, "L", "Denim"),
        Product("Silk Scarf", 29.99, "One Size", "Silk"),
        Product("Athletic Shorts", 24.99, "S", "Polyester"),
        Product("Dress Shirt", 39.99, "XL", "Cotton"),
    ]

    # Initialize the product filter with the sample data
    product_filter = ProductFilter(products)

    # Example filter usage
    try:
        # Filter by size
        filtered_by_size = product_filter.filter_by_size(["M", "S"])
        print("Filtered by size (M, S):", filtered_by_size)

        # Filter by material
        filtered_by_material = product_filter.filter_by_material(["Cotton", "Silk"])
        print("Filtered by material (Cotton, Silk):", filtered_by_material)

        # Sort by price (low to high)
        sorted_by_price_low_high = product_filter.sort_by_price(ascending=True)
        print("Sorted by price (low to high):", sorted_by_price_low_high)

        # Sort by price (high to low)
        sorted_by_price_high_low = product_filter.sort_by_price(ascending=False)
        print("Sorted by price (high to low):", sorted_by_price_high_low)

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
