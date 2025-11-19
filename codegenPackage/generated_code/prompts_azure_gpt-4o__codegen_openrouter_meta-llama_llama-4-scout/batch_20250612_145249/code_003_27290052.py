"""
Generated Code Metadata:
========================
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Write a script to sort products by criteria such as "Maior preço" or "Melhor Avaliados," as described on the "asacanelbrazzz" website.
Generated: DETERMINISTIC_27290052379b7d89
Batch ID: 20250612_145249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_sorter.py

class Product:
    """Represents a product with price and rating."""

    def __init__(self, name, price, rating):
        """
        Initializes a Product.

        Args:
            name (str): Product name.
            price (float): Product price.
            rating (float): Product rating.
        """
        self.name = name
        self.price = price
        self.rating = rating

    def __repr__(self):
        return f"Product('{self.name}', {self.price}, {self.rating})"


class ProductSorter:
    """Sorts products by different criteria."""

    def __init__(self, products):
        """
        Initializes a ProductSorter.

        Args:
            products (list[Product]): List of products to sort.
        """
        self.products = products

    def sort_by_price_desc(self):
        """
        Sorts products by price in descending order.

        Returns:
            list[Product]: Sorted list of products.
        """
        return sorted(self.products, key=lambda x: x.price, reverse=True)

    def sort_by_rating_desc(self):
        """
        Sorts products by rating in descending order.

        Returns:
            list[Product]: Sorted list of products.
        """
        return sorted(self.products, key=lambda x: x.rating, reverse=True)


def main():
    try:
        # Example products
        products = [
            Product("Product A", 100.0, 4.5),
            Product("Product B", 50.0, 4.8),
            Product("Product C", 200.0, 4.2),
        ]

        sorter = ProductSorter(products)

        print("Produtos por Maior Preço:")
        for product in sorter.sort_by_price_desc():
            print(f"{product.name}: R${product.price:.2f}")

        print("\nProdutos por Melhor Avaliados:")
        for product in sorter.sort_by_rating_desc():
            print(f"{product.name}: {product.rating:.2f} estrelas")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
