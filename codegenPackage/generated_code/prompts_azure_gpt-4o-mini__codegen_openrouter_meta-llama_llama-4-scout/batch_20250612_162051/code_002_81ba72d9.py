"""
Generated Code Metadata:
========================
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Create an API endpoint that retrieves a list of approved disinfectant products used for cleaning poultry buildings, including their environmental impact information.
Generated: DETERMINISTIC_81ba72d9c77a5995
Batch ID: 20250612_162051
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
    title="Disinfectant Products API",
    description="API endpoint to retrieve a list of approved disinfectant products used for cleaning poultry buildings",
    version="1.0.0"
)

# Define a model for DisinfectantProduct
class DisinfectantProduct(BaseModel):
    id: int
    name: str
    environmental_impact: dict

# In-memory data store for demonstration purposes
# Replace with a database connection in production
disinfectant_products = [
    DisinfectantProduct(id=1, name="Product A", environmental_impact={"carbon_footprint": 10, "water_usage": 5}),
    DisinfectantProduct(id=2, name="Product B", environmental_impact={"carbon_footprint": 8, "water_usage": 6}),
    DisinfectantProduct(id=3, name="Product C", environmental_impact={"carbon_footprint": 12, "water_usage": 4})
]

# API endpoint to retrieve a list of approved disinfectant products
@app.get("/disinfectant-products/", response_model=List[DisinfectantProduct])
async def read_disinfectant_products():
    try:
        # Return the list of disinfectant products
        return disinfectant_products
    except Exception as e:
        # Handle any unexpected errors
        raise HTTPException(status_code=500, detail="Internal Server Error")

# API endpoint to retrieve a disinfectant product by ID
@app.get("/disinfectant-products/{product_id}", response_model=DisinfectantProduct)
async def read_disinfectant_product(product_id: int):
    try:
        # Find the product by ID
        product = next((product for product in disinfectant_products if product.id == product_id), None)
        if product is None:
            # Raise a 404 error if the product is not found
            raise HTTPException(status_code=404, detail="Product not found")
        return product
    except Exception as e:
        # Handle any unexpected errors
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
# Run the application
# uvicorn app:app --host 0.0.0.0 --port 8000
```
