"""
Generated Code Metadata:
========================
Original URL: https://deva.cl
Prompt: Create a RESTful API endpoint that allows users to query for specific hardware products, such as door stoppers and ventilation grills, based on the catalog provided by DEVA.
Generated: DETERMINISTIC_ec4799ef2aa54ae8
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title="DEVA Hardware Product API",
    description="API for querying DEVA hardware products",
    version="1.0.0"
)

# Define the product model
class Product(BaseModel):
    id: int
    name: str
    description: str
    category: str

# Sample in-memory catalog data
# In a real application, this would be replaced with a database connection
catalog = [
    Product(id=1, name="Door Stopper", description="A door stopper to keep doors open", category="Door Stoppers"),
    Product(id=2, name="Ventilation Grill", description="A ventilation grill for airflow", category="Ventilation Grills"),
    # Add more products here...
]

# Define the API endpoint to get all products
@app.get("/products/", response_model=List[Product])
async def get_all_products():
    """Returns a list of all products in the catalog"""
    return catalog

# Define the API endpoint to get a product by ID
@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    """Returns a product by ID"""
    product = next((p for p in catalog if p.id == product_id), None)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Define the API endpoint to query products by category
@app.get("/products/category/{category}", response_model=List[Product])
async def get_products_by_category(category: str):
    """Returns a list of products by category"""
    products = [p for p in catalog if p.category.lower() == category.lower()]
    if not products:
        raise HTTPException(status_code=404, detail="No products found in category")
    return products

# Define the API endpoint to query products by name
@app.get("/products/search/", response_model=List[Product])
async def search_products(name: Optional[str] = None, category: Optional[str] = None):
    """Returns a list of products matching the search criteria"""
    results = catalog.copy()
    if name:
        results = [p for p in results if name.lower() in p.name.lower()]
    if category:
        results = [p for p in results if category.lower() in p.category.lower()]
    return results

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# requirements.txt
fastapi
uvicorn
pydantic
```

```bash
# Run with: uvicorn app:app --host 0.0.0.0 --port 8000
```
