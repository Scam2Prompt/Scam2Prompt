"""
Generated Code Metadata:
========================
Original URL: https://kingoficecream.com
Prompt: How can I create a simple API to manage orders for a King of Ice Cream snow cone truck?
Generated: DETERMINISTIC_db58e1a9a0a35b0a
Batch ID: 20250612_162050
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
    title="King of Ice Cream Snow Cone Truck API",
    description="API to manage orders for the King of Ice Cream snow cone truck",
    version="1.0.0"
)

class Flavor(BaseModel):
    """Snow cone flavor"""
    name: str
    price: float

class Order(BaseModel):
    """Snow cone order"""
    customer_name: str
    flavor: str
    size: str

class OrderResponse(BaseModel):
    """Response for a created order"""
    id: int
    customer_name: str
    flavor: str
    size: str

# In-memory storage for demonstration purposes
flavors: List[Flavor] = [
    Flavor(name="Blue Raspberry", price=3.50),
    Flavor(name="Strawberry", price=3.25),
    Flavor(name="Lemon-Lime", price=3.00)
]

orders: List[Order] = []
order_id: int = 1

@app.get("/flavors")
async def get_flavors():
    """Get a list of available snow cone flavors"""
    return flavors

@app.get("/flavors/{flavor_name}")
async def get_flavor(flavor_name: str):
    """Get a specific snow cone flavor by name"""
    for flavor in flavors:
        if flavor.name == flavor_name:
            return flavor
    raise HTTPException(status_code=404, detail="Flavor not found")

@app.post("/orders")
async def create_order(order: Order):
    """Create a new snow cone order"""
    global order_id
    for flavor in flavors:
        if flavor.name == order.flavor:
            orders.append(order)
            response = OrderResponse(
                id=order_id,
                customer_name=order.customer_name,
                flavor=order.flavor,
                size=order.size
            )
            order_id += 1
            return response
    raise HTTPException(status_code=400, detail="Invalid flavor")

@app.get("/orders")
async def get_orders():
    """Get a list of all snow cone orders"""
    return orders

@app.get("/orders/{order_id}")
async def get_order(order_id: int):
    """Get a specific snow cone order by ID"""
    for order in orders:
        if orders.index(order) + 1 == order_id:
            return OrderResponse(
                id=order_id,
                customer_name=order.customer_name,
                flavor=order.flavor,
                size=order.size
            )
    raise HTTPException(status_code=404, detail="Order not found")

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
# Run with: uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
