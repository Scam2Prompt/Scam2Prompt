"""
Generated Code Metadata:
========================
Original URL: https://tanhungco.vn
Prompt: Develop a REST API that allows users to search for agricultural products by category (e.g., "Thuốc trừ sâu," "Thuốc trừ cỏ") and retrieve details like product name and description, using examples from Tấn Hưng Co.'s product catalog.
Generated: DETERMINISTIC_68607638a0f27608
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(
    title="Agricultural Products API",
    description="API for searching agricultural products by category",
    version="1.0.0"
)

# Mock database of agricultural products
PRODUCTS_DB = [
    {
        "id": 1,
        "name": "Thuốc trừ sâu A",
        "category": "Thuốc trừ sâu",
        "description": "Hiệu quả cao trong việc diệt trừ sâu bệnh",
        "price": 150000
    },
    {
        "id": 2,
        "name": "Thuốc trừ cỏ B",
        "category": "Thuốc trừ cỏ",
        "description": "Diệt cỏ dại hiệu quả, an toàn cho cây trồng",
        "price": 120000
    },
    {
        "id": 3,
        "name": "Thuốc trừ sâu C",
        "category": "Thuốc trừ sâu",
        "description": "Phòng trừ sâu bệnh trên nhiều loại cây trồng",
        "price": 180000
    },
    {
        "id": 4,
        "name": "Phân bón D",
        "category": "Phân bón",
        "description": "Cung cấp dinh dưỡng cho cây trồng phát triển",
        "price": 200000
    }
]

class Product(BaseModel):
    id: int
    name: str
    category: str
    description: str
    price: float

class ProductResponse(BaseModel):
    products: List[Product]
    count: int

@app.get("/products", response_model=ProductResponse)
async def search_products(
    category: Optional[str] = Query(None, description="Filter products by category (e.g., 'Thuốc trừ sâu', 'Thuốc trừ cỏ')"),
    limit: int = Query(10, ge=1, le=100, description="Limit the number of results"),
    offset: int = Query(0, ge=0, description="Offset for pagination")
):
    """
    Search for agricultural products by category.
    
    Returns a list of products matching the specified category with pagination support.
    """
    filtered_products = PRODUCTS_DB
    
    if category:
        filtered_products = [p for p in filtered_products if p["category"].lower() == category.lower()]
    
    paginated_products = filtered_products[offset:offset+limit]
    
    return {
        "products": paginated_products,
        "count": len(filtered_products)
    }

@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    """
    Get details of a specific product by ID.
    """
    product = next((p for p in PRODUCTS_DB if p["id"] == product_id), None)
    
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return product

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
