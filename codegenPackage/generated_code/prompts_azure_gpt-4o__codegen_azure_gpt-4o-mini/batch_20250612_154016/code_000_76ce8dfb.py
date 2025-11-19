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
import json
from typing import List, Dict, Optional

class Product:
    """Class representing a health supplement product."""
    
    def __init__(self, name: str, description: str, price: float):
        self.name = name
        self.description = description
        self.price = price
        self.reviews: List[Dict[str, str]] = []  # List to store reviews

    def add_review(self, user: str, rating: int, comment: str):
        """Add a review to the product."""
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        self.reviews.append({
            "user": user,
            "rating": rating,
            "comment": comment
        })

    def get_average_rating(self) -> Optional[float]:
        """Calculate the average rating of the product."""
        if not self.reviews:
            return None
        total_rating = sum(review['rating'] for review in self.reviews)
        return total_rating / len(self.reviews)

    def to_dict(self) -> Dict:
        """Convert product details to a dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "average_rating": self.get_average_rating(),
            "reviews": self.reviews
        }

class Catalog:
    """Class representing a catalog of health supplements."""
    
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product):
        """Add a product to the catalog."""
        self.products.append(product)

    def find_product(self, name: str) -> Optional[Product]:
        """Find a product by name."""
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None

    def to_json(self) -> str:
        """Convert the catalog to a JSON string."""
        return json.dumps([product.to_dict() for product in self.products], indent=4)

def main():
    """Main function to demonstrate the catalog system."""
    catalog = Catalog()

    # Create products
    collagen = Product("Colágeno Hidrolizado MAX", "High-quality hydrolyzed collagen.", 29.99)
    pro_adulto = Product("Pro Adulto", "Supplement for adults with essential vitamins.", 34.99)

    # Add products to the catalog
    catalog.add_product(collagen)
    catalog.add_product(pro_adulto)

    # Add reviews
    try:
        collagen.add_review("Alice", 5, "Excellent product!")
        collagen.add_review("Bob", 4, "Very good, but a bit pricey.")
        pro_adulto.add_review("Charlie", 3, "It's okay, nothing special.")
    except ValueError as e:
        print(f"Error adding review: {e}")

    # Print catalog in JSON format
    print(catalog.to_json())

if __name__ == "__main__":
    main()
```
