"""
Generated Code Metadata:
========================
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Generate code for a search functionality in an e-commerce app that filters products by categories such as "Bolas," "Fardamentos Esportivos," and "Equipamento."
Generated: DETERMINISTIC_63be576762380cea
Batch ID: 20250612_151414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Optional
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

app = FastAPI()

# Mock database of products
products_db = [
    {"id": 1, "name": "Bola de Futebol", "category": "Bolas", "price": 99.90},
    {"id": 2, "name": "Bola de Basquete", "category": "Bolas", "price": 129.90},
    {"id": 3, "name": "Camisa de Time", "category": "Fardamentos Esportivos", "price": 199.90},
    {"id": 4, "name": "Short de Treino", "category": "Fardamentos Esportivos", "price": 89.90},
    {"id": 5, "name": "Tênis Esportivo", "category": "Equipamento", "price": 299.90},
    {"id": 6, "name": "Meião", "category": "Equipamento", "price": 39.90},
]

class Product(BaseModel):
    id: int
    name: str
    category: str
    price: float

@app.get("/products/", response_model=List[Product])
def search_products(
    category: Optional[str] = Query(None, description="Filter products by category"),
    name: Optional[str] = Query(None, description="Filter products by name"),
    min_price: Optional[float] = Query(None, description="Minimum price filter"),
    max_price: Optional[float] = Query(None, description="Maximum price filter")
):
    """
    Search and filter products by various criteria.
    Available categories: Bolas, Fardamentos Esportivos, Equipamento
    """
    filtered_products = products_db
    
    if category:
        filtered_products = [p for p in filtered_products if p["category"].lower() == category.lower()]
    
    if name:
        filtered_products = [p for p in filtered_products if name.lower() in p["name"].lower()]
    
    if min_price is not None:
        filtered_products = [p for p in filtered_products if p["price"] >= min_price]
    
    if max_price is not None:
        filtered_products = [p for p in filtered_products if p["price"] <= max_price]
    
    if not filtered_products:
        raise HTTPException(status_code=404, detail="No products found matching the criteria")
    
    return filtered_products

@app.get("/categories/", response_model=List[str])
def get_categories():
    """Get all available product categories"""
    categories = {p["category"] for p in products_db}
    return sorted(categories)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
