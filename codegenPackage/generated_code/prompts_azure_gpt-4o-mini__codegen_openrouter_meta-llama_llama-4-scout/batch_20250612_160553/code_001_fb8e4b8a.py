"""
Generated Code Metadata:
========================
Original URL: https://logingalagames-io.blogspot.com
Prompt: How can I implement a filtering system for furniture products based on price and relevance, as seen on the Móveis Campo Largo site?
Generated: DETERMINISTIC_fb8e4b8a25b4a871
Batch ID: 20250612_160553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# furniture_filter.py

class FurnitureProduct:
    """Represents a furniture product with price and relevance attributes."""

    def __init__(self, name: str, price: float, relevance: int):
        """
        Initializes a FurnitureProduct instance.

        Args:
        - name (str): Product name.
        - price (float): Product price.
        - relevance (int): Product relevance score.
        """
        self.name = name
        self.price = price
        self.relevance = relevance

class FurnitureFilter:
    """Provides methods for filtering furniture products by price and relevance."""

    def __init__(self, products: list[FurnitureProduct]):
        """
        Initializes a FurnitureFilter instance.

        Args:
        - products (list[FurnitureProduct]): List of furniture products.
        """
        self.products = products

    def filter_by_price(self, min_price: float = 0, max_price: float = float('inf')) -> list[FurnitureProduct]:
        """
        Filters products by price range.

        Args:
        - min_price (float): Minimum price (inclusive). Defaults to 0.
        - max_price (float): Maximum price (inclusive). Defaults to infinity.

        Returns:
        - list[FurnitureProduct]: Filtered products.
        """
        return [product for product in self.products if min_price <= product.price <= max_price]

    def filter_by_relevance(self, min_relevance: int = 0) -> list[FurnitureProduct]:
        """
        Filters products by relevance score.

        Args:
        - min_relevance (int): Minimum relevance score (inclusive). Defaults to 0.

        Returns:
        - list[FurnitureProduct]: Filtered products.
        """
        return [product for product in self.products if product.relevance >= min_relevance]

    def filter_by_price_and_relevance(self, min_price: float = 0, max_price: float = float('inf'), min_relevance: int = 0) -> list[FurnitureProduct]:
        """
        Filters products by price range and relevance score.

        Args:
        - min_price (float): Minimum price (inclusive). Defaults to 0.
        - max_price (float): Maximum price (inclusive). Defaults to infinity.
        - min_relevance (int): Minimum relevance score (inclusive). Defaults to 0.

        Returns:
        - list[FurnitureProduct]: Filtered products.
        """
        return [product for product in self.products if min_price <= product.price <= max_price and product.relevance >= min_relevance]

def main():
    # Example usage:
    products = [
        FurnitureProduct("Chair", 100.0, 5),
        FurnitureProduct("Table", 500.0, 3),
        FurnitureProduct("Bed", 800.0, 4),
        FurnitureProduct("Sofa", 1200.0, 5),
    ]

    filter = FurnitureFilter(products)

    try:
        print("All products:")
        for product in products:
            print(f"{product.name}: ${product.price:.2f}, Relevance: {product.relevance}")

        print("\nFiltered by price ($100-$500):")
        filtered_products = filter.filter_by_price(100, 500)
        for product in filtered_products:
            print(f"{product.name}: ${product.price:.2f}, Relevance: {product.relevance}")

        print("\nFiltered by relevance (>= 4):")
        filtered_products = filter.filter_by_relevance(4)
        for product in filtered_products:
            print(f"{product.name}: ${product.price:.2f}, Relevance: {product.relevance}")

        print("\nFiltered by price and relevance ($100-$500, >= 4):")
        filtered_products = filter.filter_by_price_and_relevance(100, 500, 4)
        for product in filtered_products:
            print(f"{product.name}: ${product.price:.2f}, Relevance: {product.relevance}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
