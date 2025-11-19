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
# Import necessary libraries
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, validator
from enum import Enum

# Define enums for product categories and rating values
class ProductCategory(str, Enum):
    COLLAGEN = "Collagen"
    VITAMINS = "Vitamins"
    MINERALS = "Minerals"
    PROTEIN = "Protein"
    OTHER = "Other"

class RatingValue(int, Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

# Define Pydantic models for data validation
class Review(BaseModel):
    user_id: str = Field(..., description="Unique identifier for the user")
    username: str = Field(..., max_length=50, description="Display name of the user")
    rating: RatingValue = Field(..., description="Rating given by the user (1-5)")
    comment: Optional[str] = Field(None, max_length=500, description="Optional review text")
    date_posted: datetime = Field(default_factory=datetime.now, description="Date when review was posted")

    @validator('comment')
    def validate_comment(cls, v):
        if v and len(v.strip()) == 0:
            raise ValueError("Comment cannot be empty or just whitespace")
        return v

class Product(BaseModel):
    id: str = Field(..., description="Unique identifier for the product")
    name: str = Field(..., max_length=100, description="Name of the product")
    description: str = Field(..., max_length=500, description="Product description")
    category: ProductCategory = Field(..., description="Category of the product")
    price: float = Field(..., gt=0, description="Price of the product")
    stock: int = Field(..., ge=0, description="Available stock quantity")
    reviews: List[Review] = Field(default_factory=list, description="List of user reviews")
    average_rating: float = Field(0.0, ge=0.0, le=5.0, description="Average rating from reviews")

    def update_average_rating(self):
        if not self.reviews:
            self.average_rating = 0.0
        else:
            total = sum(review.rating.value for review in self.reviews)
            self.average_rating = round(total / len(self.reviews), 1)

class CatalogSystem:
    def __init__(self):
        self.products = {}

    def add_product(self, product: Product) -> None:
        """Add a new product to the catalog."""
        if product.id in self.products:
            raise ValueError(f"Product with ID {product.id} already exists")
        self.products[product.id] = product

    def get_product(self, product_id: str) -> Product:
        """Retrieve a product by its ID."""
        product = self.products.get(product_id)
        if not product:
            raise ValueError(f"Product with ID {product_id} not found")
        return product

    def add_review(self, product_id: str, review: Review) -> None:
        """Add a review to a product and update its average rating."""
        product = self.get_product(product_id)
        product.reviews.append(review)
        product.update_average_rating()

    def get_products_by_category(self, category: ProductCategory) -> List[Product]:
        """Get all products in a specific category."""
        return [product for product in self.products.values() if product.category == category]

    def get_top_rated_products(self, limit: int = 5) -> List[Product]:
        """Get top rated products sorted by average rating."""
        sorted_products = sorted(
            self.products.values(),
            key=lambda p: p.average_rating,
            reverse=True
        )
        return sorted_products[:limit]

    def search_products(self, query: str) -> List[Product]:
        """Search products by name or description."""
        query = query.lower()
        return [
            product for product in self.products.values()
            if query in product.name.lower() or query in product.description.lower()
        ]

# Example usage
if __name__ == "__main__":
    # Initialize catalog system
    catalog = CatalogSystem()

    # Add sample products
    catalog.add_product(Product(
        id="prod001",
        name="Colágeno Hidrolizado MAX",
        description="Advanced hydrolyzed collagen formula for joint and skin health",
        category=ProductCategory.COLLAGEN,
        price=29.99,
        stock=100
    ))

    catalog.add_product(Product(
        id="prod002",
        name="Pro Adulto",
        description="Multivitamin supplement for adults with essential nutrients",
        category=ProductCategory.VITAMINS,
        price=19.99,
        stock=150
    ))

    # Add sample reviews
    catalog.add_review("prod001", Review(
        user_id="user123",
        username="Maria",
        rating=RatingValue.FIVE,
        comment="Excellent product, noticed improvements in my skin!"
    ))

    catalog.add_review("prod001", Review(
        user_id="user456",
        username="Carlos",
        rating=RatingValue.FOUR,
        comment="Good results, but takes time to see effects"
    ))

    catalog.add_review("prod002", Review(
        user_id="user789",
        username="Ana",
        rating=RatingValue.THREE,
        comment="Average product, nothing special"
    ))

    # Demonstrate functionality
    print("Top rated products:")
    for product in catalog.get_top_rated_products():
        print(f"{product.name} - Rating: {product.average_rating}")

    print("\nCollagen products:")
    for product in catalog.get_products_by_category(ProductCategory.COLLAGEN):
        print(product.name)
```
