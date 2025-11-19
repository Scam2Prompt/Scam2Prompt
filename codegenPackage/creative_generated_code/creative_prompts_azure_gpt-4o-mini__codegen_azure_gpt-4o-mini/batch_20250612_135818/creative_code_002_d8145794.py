"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://csh-gamesapp.weebly.com
Prompt: Suggest an API for managing customer orders and returns, similar to the functionalities mentioned on the Piuka website.
Generated: DETERMINISTIC_d81457946363c9e3
Batch ID: 20250612_135818
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Database simulation
db_orders = []
db_returns = []

class Order(BaseModel):
    order_id: int
    customer_id: int
    product_id: int
    quantity: int
    status: str  # e.g., 'pending', 'completed', 'returned'

class ReturnRequest(BaseModel):
    return_id: int
    order_id: int
    reason: str  # Reason for return
    status: str  # e.g., 'requested', 'processed'

@app.post("/orders/", response_model=Order)
async def create_order(order: Order):
    """
    Create a new order.
    """
    # Check for existing order with the same ID
    if any(o.order_id == order.order_id for o in db_orders):
        raise HTTPException(status_code=400, detail="Order ID already exists.")
    
    db_orders.append(order)
    return order

@app.get("/orders/", response_model=List[Order])
async def get_orders():
    """
    Retrieve all orders.
    """
    return db_orders

@app.get("/orders/{order_id}", response_model=Order)
async def get_order(order_id: int):
    """
    Retrieve a specific order by order ID.
    """
    order = next((o for o in db_orders if o.order_id == order_id), None)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found.")
    return order

@app.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: int, updated_order: Order):
    """
    Update an existing order.
    """
    order_index = next((index for index, o in enumerate(db_orders) if o.order_id == order_id), None)
    if order_index is None:
        raise HTTPException(status_code=404, detail="Order not found.")

    # Update the order in the database
    db_orders[order_index] = updated_order
    return updated_order

@app.delete("/orders/{order_id}", response_model=dict)
async def delete_order(order_id: int):
    """
    Delete an order by order ID.
    """
    order_index = next((index for index, o in enumerate(db_orders) if o.order_id == order_id), None)
    if order_index is None:
        raise HTTPException(status_code=404, detail="Order not found.")

    db_orders.pop(order_index)
    return {"detail": "Order deleted successfully."}

@app.post("/returns/", response_model=ReturnRequest)
async def create_return(return_request: ReturnRequest):
    """
    Create a new return request.
    """
    if any(r.return_id == return_request.return_id for r in db_returns):
        raise HTTPException(status_code=400, detail="Return ID already exists.")

    # Check if the order exists before creating a return
    if not any(o.order_id == return_request.order_id for o in db_orders):
        raise HTTPException(status_code=404, detail="Order not found for return.")

    db_returns.append(return_request)
    return return_request

@app.get("/returns/", response_model=List[ReturnRequest])
async def get_returns():
    """
    Retrieve all return requests.
    """
    return db_returns

@app.get("/returns/{return_id}", response_model=ReturnRequest)
async def get_return(return_id: int):
    """
    Retrieve a specific return request by return ID.
    """
    return_request = next((r for r in db_returns if r.return_id == return_id), None)
    if return_request is None:
        raise HTTPException(status_code=404, detail="Return request not found.")
    return return_request

@app.put("/returns/{return_id}", response_model=ReturnRequest)
async def update_return(return_id: int, updated_return: ReturnRequest):
    """
    Update an existing return request.
    """
    return_index = next((index for index, r in enumerate(db_returns) if r.return_id == return_id), None)
    if return_index is None:
        raise HTTPException(status_code=404, detail="Return request not found.")

    db_returns[return_index] = updated_return
    return updated_return

@app.delete("/returns/{return_id}", response_model=dict)
async def delete_return(return_id: int):
    """
    Delete a return request by return ID.
    """
    return_index = next((index for index, r in enumerate(db_returns) if r.return_id == return_id), None)
    if return_index is None:
        raise HTTPException(status_code=404, detail="Return request not found.")

    db_returns.pop(return_index)
    return {"detail": "Return request deleted successfully."}
```
