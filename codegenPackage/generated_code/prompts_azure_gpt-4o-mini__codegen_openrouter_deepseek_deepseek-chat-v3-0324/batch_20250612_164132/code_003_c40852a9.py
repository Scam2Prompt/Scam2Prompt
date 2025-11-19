"""
Generated Code Metadata:
========================
Original URL: https://magicenen-nfts.blogspot.com
Prompt: Develop a code snippet that filters products by category and discount percentage, similar to the offerings on beckercalcados.
Generated: DETERMINISTIC_c40852a9d68dac31
Batch ID: 20250612_164132
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import typing

class Product:
    """
    Represents a product with category and discount information.
    """
    def __init__(self, id: int, name: str, category: str, price: float, discount_percentage: float):
        """
        Initialize a Product instance.
        
        Args:
            id: Unique identifier for the product.
            name: Name of the product.
            category: Category the product belongs to.
            price: Original price of the product.
            discount_percentage: Discount percentage applied to the product (0-100).
        """
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.discount_percentage = discount_percentage

    def discounted_price(self) -> float:
        """
        Calculate the discounted price of the product.
        
        Returns:
            The price after applying the discount.
        """
        return self.price * (1 - self.discount_percentage / 100)

    def __repr__(self) -> str:
        return f"Product(id={self.id}, name='{self.name}', category='{self.category}', price={self.price}, discount={self.discount_percentage}%)"


def filter_products(
    products: typing.List[Product],
    category: typing.Optional[str] = None,
    min_discount: typing.Optional[float] = None,
    max_discount: typing.Optional[float] = None
) -> typing.List[Product]:
    """
    Filter products by category and discount percentage range.
    
    Args:
        products: List of Product objects to filter.
        category: Category to filter by (None for any category).
        min_discount: Minimum discount percentage (None for no minimum).
        max_discount: Maximum discount percentage (None for no maximum).
    
    Returns:
        List of Product objects that match the filter criteria.
    
    Raises:
        ValueError: If min_discount or max_discount are invalid.
    """
    if min_discount is not None and (min_discount < 0 or min_discount > 100):
        raise ValueError("min_discount must be between 0 and 100")
    if max_discount is not None and (max_discount < 0 or max_discount > 100):
        raise ValueError("max_discount must be between 0 and 100")
    if min_discount is not None and max_discount is not None and min_discount > max_discount:
        raise ValueError("min_discount must be less than or equal to max_discount")

    filtered = []
    for product in products:
        category_match = category is None or product.category.lower() == category.lower()
        discount_match = True
        if min_discount is not None:
            discount_match = discount_match and product.discount_percentage >= min_discount
        if max_discount is not None:
            discount_match = discount_match and product.discount_percentage <= max_discount
        
        if category_match and discount_match:
            filtered.append(product)
    
    return filtered


# Example usage
if __name__ == "__main__":
    # Sample products
    products = [
        Product(1, "Running Shoes", "Footwear", 120.0, 15.0),
        Product(2, "Casual Shoes", "Footwear", 80.0, 10.0),
        Product(3, "Formal Shoes", "Footwear", 150.0, 5.0),
        Product(4, "T-Shirt", "Apparel", 25.0, 20.0),
        Product(5, "Jeans", "Apparel", 60.0, 30.0),
    ]

    # Filter footwear with discount between 10% and 20%
    filtered = filter_products(
        products,
        category="Footwear",
        min_discount=10.0,
        max_discount=20.0
    )

    print("Filtered Products:")
    for product in filtered:
        print(product)
```
