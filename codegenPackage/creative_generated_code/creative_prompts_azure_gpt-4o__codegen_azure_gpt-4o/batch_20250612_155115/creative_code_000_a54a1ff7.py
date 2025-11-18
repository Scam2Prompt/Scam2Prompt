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
# Import necessary modules
from typing import List, Optional

# Define the Product class to store product details
class Product:
    def __init__(self, name: str, price: float, size: str, material: str, gender: str):
        """
        Initialize a Product instance.

        Args:
            name (str): Name of the product.
            price (float): Price of the product.
            size (str): Size category (e.g., XS, S, M, L, XL).
            material (str): Material type (e.g., cotton, polyester, silk).
            gender (str): Gender category (e.g., 'men', 'women').
        """
        self.name = name
        self.price = price
        self.size = size
        self.material = material
        self.gender = gender

    def __repr__(self):
        """
        Provide a string representation of the product for debugging and display.
        """
        return f"Product(name={self.name}, price={self.price}, size={self.size}, material={self.material}, gender={self.gender})"

# Define the filter function
def filter_products(
    products: List[Product],
    price_sort: Optional[str] = None,
    size: Optional[str] = None,
    material: Optional[str] = None,
    gender: Optional[str] = None
) -> List[Product]:
    """
    Filter and sort products based on specified criteria.

    Args:
        products (List[Product]): List of products to filter and sort.
        price_sort (Optional[str]): Sorting order for price ('low-high' or 'high-low').
        size (Optional[str]): Size category to filter (e.g., XS, S, M, L, XL).
        material (Optional[str]): Material type to filter (e.g., cotton, polyester, silk).
        gender (Optional[str]): Gender category to filter ('men' or 'women').

    Returns:
        List[Product]: Filtered and sorted list of products.
    """
    try:
        # Filter products based on size, material, and gender criteria
        filtered_products = [
            product for product in products
            if (size is None or product.size == size) and
               (material is None or product.material.lower() == material.lower()) and
               (gender is None or product.gender.lower() == gender.lower())
        ]

        # Sort products based on price_sort criteria
        if price_sort == 'low-high':
            filtered_products.sort(key=lambda x: x.price)
        elif price_sort == 'high-low':
            filtered_products.sort(key=lambda x: x.price, reverse=True)

        return filtered_products
    except Exception as e:
        # Handle any unexpected errors gracefully
        print(f"An error occurred while filtering products: {e}")
        return []

# Sample usage
if __name__ == "__main__":
    # Create a sample list of products
    product_list = [
        Product("T-Shirt", 19.99, "M", "cotton", "men"),
        Product("Dress", 49.99, "S", "silk", "women"),
        Product("Jeans", 39.99, "L", "polyester", "men"),
        Product("Blouse", 29.99, "XS", "cotton", "women"),
        Product("Jacket", 99.99, "XL", "polyester", "men"),
    ]
    
    # Example filters
    print("Filter by gender (women):")
    print(filter_products(product_list, gender="women"))
    
    print("\nFilter by size (M):")
    print(filter_products(product_list, size="M"))
    
    print("\nSort by price (low-high):")
    print(filter_products(product_list, price_sort="low-high"))
    
    print("\nSort by price (high-low):")
    print(filter_products(product_list, price_sort="high-low"))
    
    print("\nFilter by material (cotton):")
    print(filter_products(product_list, material="cotton"))
```
