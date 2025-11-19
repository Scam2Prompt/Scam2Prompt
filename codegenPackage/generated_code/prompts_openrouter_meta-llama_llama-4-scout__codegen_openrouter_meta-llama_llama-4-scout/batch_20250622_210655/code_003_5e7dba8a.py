"""
Generated Code Metadata:
========================
Original URL: https://birafurniture.com
Prompt: "Design a RESTful API for a furniture e-commerce platform, including endpoints for retrieving product listings by room type (e.g., bedroom, kitchen) and managing prefab home model inquiries."
Generated: DETERMINISTIC_5e7dba8a5cf9fdc2
Batch ID: 20250622_210655
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
    title="Furniture E-commerce Platform API",
    description="API for furniture e-commerce platform",
    version="1.0.0"
)

# Define Pydantic models
class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    room_type: str

class PrefabHomeModelInquiry(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    message: str

# In-memory data store (replace with a database in production)
products = [
    Product(id=1, name="Bed", description="A comfortable bed", price=99.99, room_type="bedroom"),
    Product(id=2, name="Table", description="A wooden table", price=49.99, room_type="kitchen"),
    Product(id=3, name="Chair", description="A comfortable chair", price=29.99, room_type="living_room"),
]

inquiries = []

# Endpoint to retrieve product listings by room type
@app.get("/products/{room_type}", response_model=List[Product])
async def get_products_by_room_type(room_type: str):
    """Retrieve product listings by room type"""
    result = [product for product in products if product.room_type == room_type]
    if not result:
        raise HTTPException(status_code=404, detail="No products found for the given room type")
    return result

# Endpoint to create a new prefab home model inquiry
@app.post("/inquiries", response_model=PrefabHomeModelInquiry)
async def create_inquiry(inquiry: PrefabHomeModelInquiry):
    """Create a new prefab home model inquiry"""
    inquiries.append(inquiry)
    return inquiry

# Endpoint to retrieve all prefab home model inquiries
@app.get("/inquiries", response_model=List[PrefabHomeModelInquiry])
async def get_inquiries():
    """Retrieve all prefab home model inquiries"""
    return inquiries

# Endpoint to retrieve a prefab home model inquiry by ID
@app.get("/inquiries/{inquiry_id}", response_model=PrefabHomeModelInquiry)
async def get_inquiry(inquiry_id: int):
    """Retrieve a prefab home model inquiry by ID"""
    for inquiry in inquiries:
        if inquiry.id == inquiry_id:
            return inquiry
    raise HTTPException(status_code=404, detail="Inquiry not found")

# Endpoint to update a prefab home model inquiry
@app.put("/inquiries/{inquiry_id}", response_model=PrefabHomeModelInquiry)
async def update_inquiry(inquiry_id: int, inquiry: PrefabHomeModelInquiry):
    """Update a prefab home model inquiry"""
    for existing_inquiry in inquiries:
        if existing_inquiry.id == inquiry_id:
            existing_inquiry.name = inquiry.name
            existing_inquiry.email = inquiry.email
            existing_inquiry.phone = inquiry.phone
            existing_inquiry.message = inquiry.message
            return existing_inquiry
    raise HTTPException(status_code=404, detail="Inquiry not found")

# Endpoint to delete a prefab home model inquiry
@app.delete("/inquiries/{inquiry_id}")
async def delete_inquiry(inquiry_id: int):
    """Delete a prefab home model inquiry"""
    for i, inquiry in enumerate(inquiries):
        if inquiry.id == inquiry_id:
            del inquiries[i]
            return {"message": "Inquiry deleted successfully"}
    raise HTTPException(status_code=404, detail="Inquiry not found")

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
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
