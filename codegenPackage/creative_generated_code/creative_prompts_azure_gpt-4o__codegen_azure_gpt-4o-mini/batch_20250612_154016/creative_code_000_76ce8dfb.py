"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://familiaprevilife.com
Prompt: Write Python code to create a catalog system for health supplements, including products like "Colágeno Hidrolizado MAX" and "Pro Adulto," with features for user reviews and ratings based on the structure described on Familia Previlife's website.
Generated: DETERMINISTIC_76ce8dfb487ee68b
Batch ID: 20250612_154016
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Optional

class Product:
    """
    Class to represent a health supplement product.
    """
    def __init__(self, name: str, description: str, price: float):
        self.name = name
        self.description = description
        self.price = price
        self.reviews: List[Dict[str, Optional[str]]] = []

    def add_review(self, user: str, rating: int, comment: str):
        """
        Adds a review to the product.
        
        Parameters:
        user (str): The name of the user providing the review.
        rating (int): The rating given by the user (1 to 5).
        comment (str): The review comment provided by the user.
        """
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5.")
        
        review = {
            "user": user,
            "rating": rating,
            "comment": comment
        }
        self.reviews.append(review)

    def get_average_rating(self) -> float:
        """
        Calculates the average rating of the product.
        
        Returns:
        float: The average rating, or 0 if no reviews exist.
        """
        if not self.reviews:
            return 0.0
        
        total_rating = sum(review['rating'] for review in self.reviews)
        return total_rating / len(self.reviews)


class Catalog:
    """
    Class to manage a catalog of health supplement products.
    """
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product):
        """
        Adds a product to the catalog.
        
        Parameters:
        product (Product): The product to be added to the catalog.
        """
        self.products.append(product)

    def find_product(self, name: str) -> Optional[Product]:
        """
        Finds a product in the catalog by name.
        
        Parameters:
        name (str): The name of the product to find.
        
        Returns:
        Optional[Product]: The found product or None if not found.
        """
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None

    def to_json(self) -> str:
        """
        Serializes the catalog to a JSON string.
        
        Returns:
        str: JSON representation of the catalog.
        """
        catalog_data = [
            {
                "name": product.name,
                "description": product.description,
                "price": product.price,
                "reviews": product.reviews
            } for product in self.products
        ]
        return json.dumps(catalog_data, indent=4)


# Example usage of the Product and Catalog classes
if __name__ == "__main__":
    # Create the catalog
    catalog = Catalog()

    # Create products
    collagen = Product("Colágeno Hidrolizado MAX", "High-quality hydrolyzed collagen.", 29.99)
    pro_adult = Product("Pro Adulto", "Health supplement for adults.", 39.99)

    # Add products to the catalog
    catalog.add_product(collagen)
    catalog.add_product(pro_adult)

    # Add reviews
    collagen.add_review("Alice", 5, "Excellent product, noticeable results!")
    collagen.add_review("Bob", 4, "Good quality, but a bit expensive.")

    pro_adult.add_review("Charlie", 3, "Average product, nothing special.")

    # Output catalog in JSON format
    print(catalog.to_json())

    # Example of getting average rating for a product
    print(f"Average rating for '{collagen.name}': {collagen.get_average_rating():.2f}")
```
