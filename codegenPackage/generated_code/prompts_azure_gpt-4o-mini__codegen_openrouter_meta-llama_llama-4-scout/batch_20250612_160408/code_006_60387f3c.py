"""
Generated Code Metadata:
========================
Original URL: https://frigoterm.ro
Prompt: Outline a code example for managing product recommendations for air conditioning units on an e-commerce platform.
Generated: DETERMINISTIC_60387f3c637b0f47
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_recommendations.py

class Product:
    """Represents an air conditioning unit product."""

    def __init__(self, product_id, name, price, category, rating):
        """
        Initializes a Product instance.

        Args:
            product_id (int): Unique product identifier.
            name (str): Product name.
            price (float): Product price.
            category (str): Product category (e.g., 'window', 'central').
            rating (float): Product rating (out of 5).
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.rating = rating


class ProductRecommender:
    """Manages product recommendations for air conditioning units."""

    def __init__(self):
        """Initializes a ProductRecommender instance."""
        self.products = {}

    def add_product(self, product):
        """
        Adds a product to the recommender.

        Args:
            product (Product): Product to add.

        Raises:
            ValueError: If a product with the same ID already exists.
        """
        if product.product_id in self.products:
            raise ValueError("Product with ID {} already exists".format(product.product_id))
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        """
        Removes a product from the recommender.

        Args:
            product_id (int): ID of the product to remove.

        Raises:
            KeyError: If the product does not exist.
        """
        if product_id not in self.products:
            raise KeyError("Product with ID {} does not exist".format(product_id))
        del self.products[product_id]

    def get_recommendations(self, category=None, min_rating=0, max_price=float('inf')):
        """
        Returns a list of recommended products.

        Args:
            category (str, optional): Category to filter by. Defaults to None.
            min_rating (float, optional): Minimum rating to filter by. Defaults to 0.
            max_price (float, optional): Maximum price to filter by. Defaults to infinity.

        Returns:
            list[Product]: List of recommended products.
        """
        recommended_products = [
            product for product in self.products.values()
            if (category is None or product.category == category)
            and product.rating >= min_rating
            and product.price <= max_price
        ]
        return sorted(recommended_products, key=lambda product: product.rating, reverse=True)


class RecommendationService:
    """Provides a service for generating product recommendations."""

    def __init__(self, recommender):
        """
        Initializes a RecommendationService instance.

        Args:
            recommender (ProductRecommender): Product recommender instance.
        """
        self.recommender = recommender

    def get_top_rated_products(self, category=None, num_products=5):
        """
        Returns a list of top-rated products.

        Args:
            category (str, optional): Category to filter by. Defaults to None.
            num_products (int, optional): Number of products to return. Defaults to 5.

        Returns:
            list[Product]: List of top-rated products.
        """
        recommended_products = self.recommender.get_recommendations(category=category)
        return recommended_products[:num_products]

    def get_products_by_price_range(self, min_price, max_price, category=None):
        """
        Returns a list of products within a price range.

        Args:
            min_price (float): Minimum price to filter by.
            max_price (float): Maximum price to filter by.
            category (str, optional): Category to filter by. Defaults to None.

        Returns:
            list[Product]: List of products within the price range.
        """
        recommended_products = self.recommender.get_recommendations(category=category, min_rating=0, max_price=max_price)
        return [product for product in recommended_products if product.price >= min_price]


def main():
    # Create products
    product1 = Product(1, "Window AC", 200.0, "window", 4.5)
    product2 = Product(2, "Central AC", 1000.0, "central", 4.8)
    product3 = Product(3, "Portable AC", 300.0, "portable", 4.2)

    # Create recommender and add products
    recommender = ProductRecommender()
    recommender.add_product(product1)
    recommender.add_product(product2)
    recommender.add_product(product3)

    # Create recommendation service
    recommendation_service = RecommendationService(recommender)

    # Get top-rated products
    top_rated_products = recommendation_service.get_top_rated_products()
    print("Top-rated products:")
    for product in top_rated_products:
        print(f"{product.name}: {product.rating}/5")

    # Get products by price range
    products_by_price_range = recommendation_service.get_products_by_price_range(100.0, 500.0)
    print("\nProducts by price range ($100-$500):")
    for product in products_by_price_range:
        print(f"{product.name}: ${product.price:.2f}")


if __name__ == "__main__":
    main()
```
