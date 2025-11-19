"""
Generated Code Metadata:
========================
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Develop a product recommendation API for an e-commerce platform that specializes in sports categories like "Beach Vôlei," "Rugby," and "Ginástica Rítmica."
Generated: DETERMINISTIC_bcea1e18f138a747
Batch ID: 20250612_151414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_recommendation_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Product Recommendation API",
    description="API for recommending products in sports categories",
    version="1.0.0"
)

# Define a data model for products
class Product(BaseModel):
    id: int
    name: str
    category: str
    price: float
    rating: float

# Define a data model for recommendations
class Recommendation(BaseModel):
    product_id: int
    score: float

# In-memory product database (replace with a real database in production)
products = [
    Product(id=1, name="Beach Vôlei Ball", category="Beach Vôlei", price=25.99, rating=4.5),
    Product(id=2, name="Rugby Ball", category="Rugby", price=30.99, rating=4.7),
    Product(id=3, name="Ginástica Rítmica Ribbon", category="Ginástica Rítmica", price=19.99, rating=4.3),
    Product(id=4, name="Beach Vôlei Net", category="Beach Vôlei", price=99.99, rating=4.8),
    Product(id=5, name="Rugby Jersey", category="Rugby", price=49.99, rating=4.6),
]

# Define a function to generate recommendations
def generate_recommendations(category: str, num_recommendations: int = 3) -> List[Recommendation]:
    category_products = [product for product in products if product.category == category]
    if not category_products:
        return []

    # Simple recommendation logic: recommend products with highest ratings
    recommended_products = sorted(category_products, key=lambda product: product.rating, reverse=True)[:num_recommendations]
    return [Recommendation(product_id=product.id, score=product.rating) for product in recommended_products]

# Define API endpoints
@app.get("/categories/")
async def get_categories():
    """Returns a list of unique categories"""
    categories = list(set(product.category for product in products))
    return {"categories": categories}

@app.get("/products/")
async def get_products(category: str | None = None):
    """Returns a list of products, filtered by category if specified"""
    if category:
        return [product for product in products if product.category == category]
    return products

@app.get("/recommendations/")
async def get_recommendations(category: str, num_recommendations: int = 3):
    """Returns a list of product recommendations for a given category"""
    recommendations = generate_recommendations(category, num_recommendations)
    if not recommendations:
        raise HTTPException(status_code=404, detail="No recommendations found for this category")
    return recommendations

@app.get("/products/{product_id}")
async def get_product(product_id: int):
    """Returns a product by ID"""
    product = next((product for product in products if product.id == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
