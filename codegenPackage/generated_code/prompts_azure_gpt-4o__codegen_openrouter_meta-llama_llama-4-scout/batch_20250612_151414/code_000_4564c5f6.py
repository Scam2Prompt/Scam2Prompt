"""
Generated Code Metadata:
========================
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Write Python code to create an e-commerce API for managing sports equipment categories like "Beach Vôlei," "Basquete," and "Rugby," including features for adding, updating, and deleting items.
Generated: DETERMINISTIC_4564c5f68ec57bb4
Batch ID: 20250612_151414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e-commerce_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Sports Equipment E-commerce API",
    description="API for managing sports equipment categories",
    version="1.0.0"
)

# Define a data model for sports equipment categories
class Category(BaseModel):
    id: int
    name: str

# In-memory data store for demonstration purposes
# Replace with a database in a production environment
categories: List[Category] = [
    Category(id=1, name="Beach Vôlei"),
    Category(id=2, name="Basquete"),
    Category(id=3, name="Rugby")
]

# GET all categories
@app.get("/categories/", response_model=List[Category])
def read_categories():
    """Retrieve a list of all sports equipment categories"""
    return categories

# GET category by ID
@app.get("/categories/{category_id}", response_model=Category)
def read_category(category_id: int):
    """Retrieve a sports equipment category by ID"""
    for category in categories:
        if category.id == category_id:
            return category
    raise HTTPException(status_code=404, detail="Category not found")

# POST create new category
@app.post("/categories/", response_model=Category)
def create_category(category: Category):
    """Create a new sports equipment category"""
    # Check for duplicate category IDs
    for existing_category in categories:
        if existing_category.id == category.id:
            raise HTTPException(status_code=400, detail="Category ID already exists")
    categories.append(category)
    return category

# PUT update existing category
@app.put("/categories/{category_id}", response_model=Category)
def update_category(category_id: int, category: Category):
    """Update an existing sports equipment category"""
    for existing_category in categories:
        if existing_category.id == category_id:
            existing_category.name = category.name
            return existing_category
    raise HTTPException(status_code=404, detail="Category not found")

# DELETE category by ID
@app.delete("/categories/{category_id}")
def delete_category(category_id: int):
    """Delete a sports equipment category by ID"""
    for i, category in enumerate(categories):
        if category.id == category_id:
            del categories[i]
            return {"message": f"Category {category_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Category not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
