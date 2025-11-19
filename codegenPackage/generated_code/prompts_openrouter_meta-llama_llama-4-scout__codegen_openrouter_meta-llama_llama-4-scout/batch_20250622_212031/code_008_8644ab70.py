"""
Generated Code Metadata:
========================
Original URL: https://frigoterm.ro
Prompt: "Generate a list of REST API endpoints for managing orders and inventory for an e-commerce platform selling air conditioning systems like frigoterm.ro."
Generated: DETERMINISTIC_8644ab70db2de19e
Batch ID: 20250622_212031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="E-commerce Platform API for Air Conditioning Systems",
    description="API for managing orders and inventory",
    version="1.0.0",
)

# Define Pydantic models for request and response bodies
class AirConditioningSystem(BaseModel):
    id: int
    name: str
    price: float
    quantity: int

class Order(BaseModel):
    id: int
    customer_name: str
    air_conditioning_system_id: int
    quantity: int

# In-memory data store for demonstration purposes
air_conditioning_systems: List[AirConditioningSystem] = [
    AirConditioningSystem(id=1, name="AC System 1", price=1000.0, quantity=10),
    AirConditioningSystem(id=2, name="AC System 2", price=1200.0, quantity=5),
]

orders: List[Order] = []

# API Endpoints
@app.get("/air-conditioning-systems/", response_model=List[AirConditioningSystem])
def read_air_conditioning_systems():
    """Retrieve a list of all air conditioning systems"""
    return air_conditioning_systems

@app.get("/air-conditioning-systems/{system_id}", response_model=AirConditioningSystem)
def read_air_conditioning_system(system_id: int):
    """Retrieve a single air conditioning system by ID"""
    system = next((system for system in air_conditioning_systems if system.id == system_id), None)
    if system is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Air conditioning system not found")
    return system

@app.post("/air-conditioning-systems/", response_model=AirConditioningSystem, status_code=status.HTTP_201_CREATED)
def create_air_conditioning_system(new_system: AirConditioningSystem):
    """Create a new air conditioning system"""
    existing_system = next((system for system in air_conditioning_systems if system.id == new_system.id), None)
    if existing_system is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Air conditioning system with this ID already exists")
    air_conditioning_systems.append(new_system)
    return new_system

@app.put("/air-conditioning-systems/{system_id}", response_model=AirConditioningSystem)
def update_air_conditioning_system(system_id: int, updated_system: AirConditioningSystem):
    """Update an existing air conditioning system"""
    system = next((system for system in air_conditioning_systems if system.id == system_id), None)
    if system is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Air conditioning system not found")
    system.name = updated_system.name
    system.price = updated_system.price
    system.quantity = updated_system.quantity
    return system

@app.delete("/air-conditioning-systems/{system_id}")
def delete_air_conditioning_system(system_id: int):
    """Delete an air conditioning system"""
    global air_conditioning_systems
    air_conditioning_systems = [system for system in air_conditioning_systems if system.id != system_id]
    return {"message": f"Air conditioning system with ID {system_id} deleted"}

@app.get("/orders/", response_model=List[Order])
def read_orders():
    """Retrieve a list of all orders"""
    return orders

@app.get("/orders/{order_id}", response_model=Order)
def read_order(order_id: int):
    """Retrieve a single order by ID"""
    order = next((order for order in orders if order.id == order_id), None)
    if order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return order

@app.post("/orders/", response_model=Order, status_code=status.HTTP_201_CREATED)
def create_order(new_order: Order):
    """Create a new order"""
    existing_order = next((order for order in orders if order.id == new_order.id), None)
    if existing_order is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Order with this ID already exists")
    system = next((system for system in air_conditioning_systems if system.id == new_order.air_conditioning_system_id), None)
    if system is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Air conditioning system not found")
    if system.quantity < new_order.quantity:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Insufficient quantity in stock")
    system.quantity -= new_order.quantity
    orders.append(new_order)
    return new_order

@app.put("/orders/{order_id}", response_model=Order)
def update_order(order_id: int, updated_order: Order):
    """Update an existing order"""
    order = next((order for order in orders if order.id == order_id), None)
    if order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    order.customer_name = updated_order.customer_name
    order.air_conditioning_system_id = updated_order.air_conditioning_system_id
    order.quantity = updated_order.quantity
    return order

@app.delete("/orders/{order_id}")
def delete_order(order_id: int):
    """Delete an order"""
    global orders
    global air_conditioning_systems
    order = next((order for order in orders if order.id == order_id), None)
    if order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    system = next((system for system in air_conditioning_systems if system.id == order.air_conditioning_system_id), None)
    system.quantity += order.quantity
    orders = [o for o in orders if o.id != order_id]
    return {"message": f"Order with ID {order_id} deleted"}
```
