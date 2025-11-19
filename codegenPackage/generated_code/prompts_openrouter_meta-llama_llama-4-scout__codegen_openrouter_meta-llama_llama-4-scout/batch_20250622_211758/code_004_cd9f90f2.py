"""
Generated Code Metadata:
========================
Original URL: https://trattar.blogspot.com
Prompt: "Create a RESTful API endpoint to retrieve information about Trattar Madeiras' products, including eucalyptus and pine wood, and their respective treatment processes."
Generated: DETERMINISTIC_cd9f90f28962c56f
Batch ID: 20250622_211758
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

app = FastAPI(
    title="Trattar Madeiras API",
    description="Retrieve information about Trattar Madeiras' products",
    version="1.0.0"
)

class Product(BaseModel):
    """Product model"""
    id: int
    name: str
    type: str  # eucalyptus or pine
    treatment_process: str

# Mock data for demonstration purposes
products = [
    Product(id=1, name="Eucalyptus Wood", type="eucalyptus", treatment_process="Drying and Planing"),
    Product(id=2, name="Pine Wood", type="pine", treatment_process="Drying and Molding"),
    Product(id=3, name="Eucalyptus Treated Wood", type="eucalyptus", treatment_process="Drying, Planing, and Chemical Treatment")
]

@app.get("/products/", response_model=List[Product])
async def get_products():
    """Retrieve a list of all products"""
    return products

@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    """Retrieve a product by ID"""
    product = next((p for p in products if p.id == product_id), None)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.get("/products/type/{product_type}", response_model=List[Product])
async def get_products_by_type(product_type: str):
    """Retrieve products by type (eucalyptus or pine)"""
    product_type = product_type.lower()
    if product_type not in ["eucalyptus", "pine"]:
        raise HTTPException(status_code=400, detail="Invalid product type")
    return [p for p in products if p.type == product_type]

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Handle HTTP exceptions"""
    return exc

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
# or 
# python app.py
```
