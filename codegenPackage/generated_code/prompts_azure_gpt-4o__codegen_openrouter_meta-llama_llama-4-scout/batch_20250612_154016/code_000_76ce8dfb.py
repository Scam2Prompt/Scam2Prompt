"""
Generated Code Metadata:
========================
Original URL: https://familiaprevilife.com
Prompt: Write Python code to create a catalog system for health supplements, including products like "Colágeno Hidrolizado MAX" and "Pro Adulto," with features for user reviews and ratings based on the structure described on Familia Previlife's website.
Generated: DETERMINISTIC_76ce8dfb487ee68b
Batch ID: 20250612_154016
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# catalog_system.py

class Product:
    """Represents a health supplement product."""

    def __init__(self, id, name, description):
        """
        Initializes a Product instance.

        Args:
            id (int): Unique product identifier.
            name (str): Product name.
            description (str): Product description.
        """
        self.id = id
        self.name = name
        self.description = description
        self.reviews = []

    def add_review(self, review):
        """Adds a review to the product."""
        self.reviews.append(review)

    def get_average_rating(self):
        """Calculates the average rating of the product."""
        if not self.reviews:
            return 0.0
        return sum(review.rating for review in self.reviews) / len(self.reviews)


class Review:
    """Represents a user review for a product."""

    def __init__(self, id, user_name, rating, comment):
        """
        Initializes a Review instance.

        Args:
            id (int): Unique review identifier.
            user_name (str): Name of the user who wrote the review.
            rating (int): Rating given by the user (1-5).
            comment (str): Review comment.
        """
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")
        self.id = id
        self.user_name = user_name
        self.rating = rating
        self.comment = comment


class Catalog:
    """Represents a catalog of health supplement products."""

    def __init__(self):
        """Initializes an empty catalog."""
        self.products = {}

    def add_product(self, product):
        """Adds a product to the catalog."""
        self.products[product.id] = product

    def get_product(self, id):
        """Retrieves a product from the catalog by ID."""
        return self.products.get(id)

    def list_products(self):
        """Lists all products in the catalog."""
        return list(self.products.values())


def main():
    # Create a catalog
    catalog = Catalog()

    # Create products
    product1 = Product(1, "Colágeno Hidrolizado MAX", "Description for Colágeno Hidrolizado MAX")
    product2 = Product(2, "Pro Adulto", "Description for Pro Adulto")

    # Add products to the catalog
    catalog.add_product(product1)
    catalog.add_product(product2)

    # Create reviews
    review1 = Review(1, "John Doe", 5, "Excellent product!")
    review2 = Review(2, "Jane Doe", 4, "Good product, but not perfect.")

    # Add reviews to products
    product1.add_review(review1)
    product2.add_review(review2)

    # List products and their average ratings
    for product in catalog.list_products():
        print(f"Product: {product.name}")
        print(f"Description: {product.description}")
        print(f"Average Rating: {product.get_average_rating():.2f}")
        for review in product.reviews:
            print(f"  - {review.user_name}: {review.rating}/5 - {review.comment}")
        print()


if __name__ == "__main__":
    main()
```
