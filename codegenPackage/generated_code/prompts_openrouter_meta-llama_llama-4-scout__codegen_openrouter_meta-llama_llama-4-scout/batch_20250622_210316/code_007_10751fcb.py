"""
Generated Code Metadata:
========================
Original URL: https://germanierpropiedades.com
Prompt: "Create a RESTful API endpoint to retrieve a list of properties for sale in La Cumbre, Córdoba, filtering by price range and property type."
Generated: DETERMINISTIC_10751fcb4c81c2f1
Batch ID: 20250622_210316
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
    title="Properties API",
    description="Retrieve a list of properties for sale in La Cumbre, Córdoba",
    version="1.0.0"
)

class Property(BaseModel):
    id: int
    price: float
    type: str
    location: str

class PropertyFilter(BaseModel):
    min_price: float | None = None
    max_price: float | None = None
    type: str | None = None

# Mock data for demonstration purposes
properties: List[Property] = [
    Property(id=1, price=500000.0, type="House", location="La Cumbre, Córdoba"),
    Property(id=2, price=300000.0, type="Apartment", location="La Cumbre, Córdoba"),
    Property(id=3, price=700000.0, type="House", location="La Cumbre, Córdoba"),
    Property(id=4, price=200000.0, type="Apartment", location="La Cumbre, Córdoba"),
]

@app.get("/properties/", response_model=List[Property])
async def read_properties(filter: PropertyFilter | None = None):
    """
    Retrieve a list of properties for sale in La Cumbre, Córdoba,
    filtering by price range and property type.

    :param filter: Filter criteria (price range and/or property type)
    :return: List of properties matching the filter criteria
    """
    try:
        filtered_properties = properties.copy()

        if filter:
            if filter.min_price:
                filtered_properties = [p for p in filtered_properties if p.price >= filter.min_price]
            if filter.max_price:
                filtered_properties = [p for p in filtered_properties if p.price <= filter.max_price]
            if filter.type:
                filtered_properties = [p for p in filtered_properties if p.type.lower() == filter.type.lower()]

        return filtered_properties

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# requirements.txt
fastapi
pydantic
uvicorn
```

```bash
# Run with: uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
