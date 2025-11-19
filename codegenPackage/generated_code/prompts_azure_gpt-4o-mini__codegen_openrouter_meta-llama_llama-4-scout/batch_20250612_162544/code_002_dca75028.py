"""
Generated Code Metadata:
========================
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: How can I implement an API to manage product details, including instructions for use and care for items like "Xícaras" and "Pratos"?
Generated: DETERMINISTIC_dca75028523e8188
Batch ID: 20250612_162544
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
    title="Product Management API",
    description="API to manage product details",
    version="1.0.0"
)

class Product(BaseModel):
    id: int
    name: str
    description: str
    instructions_for_use: str
    care_instructions: str

class ProductManager:
    def __init__(self):
        self.products = {}

    def get_product(self, product_id: int):
        return self.products.get(product_id)

    def create_product(self, product: Product):
        if product.id in self.products:
            raise HTTPException(status_code=400, detail="Product already exists")
        self.products[product.id] = product
        return product

    def update_product(self, product_id: int, product: Product):
        if product_id not in self.products:
            raise HTTPException(status_code=404, detail="Product not found")
        self.products[product_id] = product
        return product

    def delete_product(self, product_id: int):
        if product_id not in self.products:
            raise HTTPException(status_code=404, detail="Product not found")
        del self.products[product_id]

product_manager = ProductManager()

# Create some sample products
sample_products = [
    Product(id=1, name="Xícaras", description="Coffee cups", instructions_for_use="Use for hot beverages", care_instructions="Wash with soap and water"),
    Product(id=2, name="Pratos", description="Plates", instructions_for_use="Use for serving food", care_instructions="Wash with soap and water")
]
for product in sample_products:
    product_manager.create_product(product)

@app.get("/products/")
async def read_products():
    return list(product_manager.products.values())

@app.get("/products/{product_id}")
async def read_product(product_id: int):
    product = product_manager.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/products/")
async def create_product(product: Product):
    return product_manager.create_product(product)

@app.put("/products/{product_id}")
async def update_product(product_id: int, product: Product):
    return product_manager.update_product(product_id, product)

@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    product_manager.delete_product(product_id)
    return {"message": "Product deleted successfully"}

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
# Run the application
# uvicorn app:app --host 0.0.0.0 --port 8000
```
