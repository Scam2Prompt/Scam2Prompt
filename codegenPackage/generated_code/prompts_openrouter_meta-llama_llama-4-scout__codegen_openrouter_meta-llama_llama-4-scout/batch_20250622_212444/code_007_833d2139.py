"""
Generated Code Metadata:
========================
Original URL: https://cm-canada.ca
Prompt: "Create a RESTful API endpoint to retrieve product information for a specific category, such as 'Valves' or 'PEX F1960', from a construction supply company's database."
Generated: DETERMINISTIC_833d21393e272ebe
Batch ID: 20250622_212444
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
from typing import List

# Initialize FastAPI app
app = FastAPI(
    title="Construction Supply Company API",
    description="API for retrieving product information",
    version="1.0.0"
)

# Define product model
class Product(BaseModel):
    id: int
    name: str
    description: str
    category: str
    price: float

# Sample in-memory database (replace with actual database connection)
products_db = [
    Product(id=1, name="Ball Valve", description="A type of valve", category="Valves", price=10.99),
    Product(id=2, name="PEX F1960 Fitting", description="A type of PEX fitting", category="PEX F1960", price=5.99),
    Product(id=3, name="Gate Valve", description="A type of valve", category="Valves", price=15.99),
    Product(id=4, name="PEX F1960 Pipe", description="A type of PEX pipe", category="PEX F1960", price=7.99),
]

# Define endpoint to retrieve products by category
@app.get("/products/category/{category}", response_model=List[Product])
async def get_products_by_category(category: str):
    """
    Retrieve product information for a specific category.

    Args:
    category (str): The category of products to retrieve.

    Returns:
    List[Product]: A list of products in the specified category.

    Raises:
    HTTPException: If no products are found in the specified category.
    """
    try:
        # Filter products by category
        products = [product for product in products_db if product.category.lower() == category.lower()]
        
        # Raise exception if no products are found
        if not products:
            raise HTTPException(status_code=404, detail=f"No products found in category '{category}'")
        
        return products
    
    except Exception as e:
        # Handle unexpected errors
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Define endpoint to retrieve all products
@app.get("/products", response_model=List[Product])
async def get_all_products():
    """
    Retrieve all product information.

    Returns:
    List[Product]: A list of all products.
    """
    try:
        return products_db
    
    except Exception as e:
        # Handle unexpected errors
        raise HTTPException(status_code=500, detail="Internal Server Error")

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
