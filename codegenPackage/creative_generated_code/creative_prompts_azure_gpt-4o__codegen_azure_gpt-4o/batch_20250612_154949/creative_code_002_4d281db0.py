"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Recommend a library or tool for managing product categories such as "Equipamentos," "Suprimentos," and "Home Decor" in an e-commerce platform, referencing the ebrasilbrazz website structure.
Generated: DETERMINISTIC_4d281db0240b5535
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing FastAPI, a modern, fast (high-performance) web framework for Python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid

# Initialize the FastAPI application
app = FastAPI()

# Data model for a product category
class ProductCategory(BaseModel):
    id: str  # Unique identifier for each category
    name: str  # Name of the category
    description: Optional[str] = None  # Optional description for the category

# In-memory database for storing product categories
# In production, replace this with an actual database (like PostgreSQL, MySQL, MongoDB, etc.)
categories_db = []

# Endpoint to get all product categories
@app.get("/categories", response_model=List[ProductCategory])
def get_categories():
    """
    Retrieve all product categories.
    """
    return categories_db

# Endpoint to add a new product category
@app.post("/categories", response_model=ProductCategory)
def create_category(category: ProductCategory):
    """
    Add a new product category to the database.
    """
    # Check if a category with the same name already exists
    for existing_category in categories_db:
        if existing_category['name'].lower() == category.name.lower():
            raise HTTPException(status_code=400, detail="Category with this name already exists.")

    # Add a unique ID to the category
    category.id = str(uuid.uuid4())
    categories_db.append(category.dict())
    return category

# Endpoint to retrieve a category by its ID
@app.get("/categories/{category_id}", response_model=ProductCategory)
def get_category(category_id: str):
    """
    Retrieve a product category by its ID.
    """
    for category in categories_db:
        if category['id'] == category_id:
            return category
    raise HTTPException(status_code=404, detail="Category not found.")

# Endpoint to update an existing category
@app.put("/categories/{category_id}", response_model=ProductCategory)
def update_category(category_id: str, updated_category: ProductCategory):
    """
    Update the details of an existing product category.
    """
    for index, category in enumerate(categories_db):
        if category['id'] == category_id:
            # Ensure the updated category name is unique
            for existing_category in categories_db:
                if existing_category['name'].lower() == updated_category.name.lower() and existing_category['id'] != category_id:
                    raise HTTPException(status_code=400, detail="Category with this name already exists.")
            
            # Update the category
            updated_category.id = category_id  # Preserve the original ID
            categories_db[index] = updated_category.dict()
            return updated_category
    raise HTTPException(status_code=404, detail="Category not found.")

# Endpoint to delete a product category
@app.delete("/categories/{category_id}", response_model=dict)
def delete_category(category_id: str):
    """
    Delete a product category by its ID.
    """
    for index, category in enumerate(categories_db):
        if category['id'] == category_id:
            del categories_db[index]
            return {"message": "Category deleted successfully."}
    raise HTTPException(status_code=404, detail="Category not found.")

# Run this application using the command:
# uvicorn <filename_without_extension>:app --reload
# Example: uvicorn main:app --reload

# This code provides a REST API for managing product categories in an e-commerce platform.
# Use the endpoints to create, retrieve, update, and delete categories effectively.
```
