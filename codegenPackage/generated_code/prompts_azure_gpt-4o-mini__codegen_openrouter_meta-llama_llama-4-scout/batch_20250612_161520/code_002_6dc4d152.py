"""
Generated Code Metadata:
========================
Original URL: https://rawcakesandcandy.ro
Prompt: Create an API endpoint for an online bakery that allows users to customize their vegan cake orders, including size, flavor, and decorations, inspired by the offerings of Raw Cakes And Candy SRL.
Generated: DETERMINISTIC_6dc4d1528d0c306e
Batch ID: 20250612_161520
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
from typing import List, Optional
from enum import Enum

app = FastAPI(
    title="Vegan Cake Customization API",
    description="API for customizing vegan cake orders",
    version="1.0.0"
)

class CakeSize(str, Enum):
    """Available cake sizes"""
    small = "small"
    medium = "medium"
    large = "large"

class CakeFlavor(str, Enum):
    """Available cake flavors"""
    chocolate = "chocolate"
    vanilla = "vanilla"
    strawberry = "strawberry"

class Decoration(BaseModel):
    """Decoration model"""
    name: str
    description: Optional[str] = None

class CakeOrder(BaseModel):
    """Cake order model"""
    size: CakeSize
    flavor: CakeFlavor
    decorations: List[Decoration]

# In-memory storage for demonstration purposes
# Replace with a database in a production environment
cake_orders = []

@app.post("/orders/")
async def create_cake_order(order: CakeOrder):
    """
    Create a new cake order.

    :param order: Cake order details
    :return: Created cake order
    """
    try:
        # Validate order
        if not isinstance(order.size, CakeSize):
            raise HTTPException(status_code=400, detail="Invalid cake size")
        if not isinstance(order.flavor, CakeFlavor):
            raise HTTPException(status_code=400, detail="Invalid cake flavor")
        if not order.decorations:
            raise HTTPException(status_code=400, detail="At least one decoration is required")

        # Save order to storage
        cake_orders.append(order.dict())

        # Return created order
        return order
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/orders/")
async def get_cake_orders():
    """
    Retrieve all cake orders.

    :return: List of cake orders
    """
    try:
        # Return all orders from storage
        return cake_orders
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/orders/{order_id}")
async def get_cake_order(order_id: int):
    """
    Retrieve a cake order by ID.

    :param order_id: ID of the cake order
    :return: Cake order details
    """
    try:
        # Retrieve order from storage
        order = cake_orders[order_id]

        # Return order
        return order
    except IndexError:
        raise HTTPException(status_code=404, detail="Order not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/orders/{order_id}")
async def update_cake_order(order_id: int, order: CakeOrder):
    """
    Update a cake order.

    :param order_id: ID of the cake order
    :param order: Updated cake order details
    :return: Updated cake order
    """
    try:
        # Retrieve order from storage
        existing_order = cake_orders[order_id]

        # Update order
        cake_orders[order_id] = order.dict()

        # Return updated order
        return order
    except IndexError:
        raise HTTPException(status_code=404, detail="Order not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/orders/{order_id}")
async def delete_cake_order(order_id: int):
    """
    Delete a cake order.

    :param order_id: ID of the cake order
    :return: Success message
    """
    try:
        # Remove order from storage
        del cake_orders[order_id]

        # Return success message
        return {"message": "Order deleted successfully"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Order not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```
