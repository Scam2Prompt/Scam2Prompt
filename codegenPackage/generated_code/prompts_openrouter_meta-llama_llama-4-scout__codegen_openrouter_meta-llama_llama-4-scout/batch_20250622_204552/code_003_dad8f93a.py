"""
Generated Code Metadata:
========================
Original URL: https://teamelevenx1.xyz
Prompt: Design a RESTful API for managing orders and payments on the Ayuwin platform, including endpoints for creating, updating, and canceling orders.
Generated: DETERMINISTIC_dad8f93a135c2801
Batch ID: 20250622_204552
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
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
from uuid import UUID
from datetime import datetime

# Initialize FastAPI app
app = FastAPI(
    title="Ayuwin Order and Payment Management API",
    description="API for managing orders and payments on the Ayuwin platform",
    version="1.0.0"
)

# Define Pydantic models
class Order(BaseModel):
    id: UUID
    user_id: UUID
    order_date: datetime
    total: float
    status: str

class Payment(BaseModel):
    id: UUID
    order_id: UUID
    payment_date: datetime
    amount: float
    payment_method: str

class OrderUpdate(BaseModel):
    status: str

class PaymentUpdate(BaseModel):
    amount: float
    payment_method: str

# In-memory data store (replace with a database in production)
orders: List[Order] = []
payments: List[Payment] = []

# Create order endpoint
@app.post("/orders", status_code=status.HTTP_201_CREATED)
async def create_order(order: Order):
    """Create a new order"""
    orders.append(order)
    return JSONResponse(content={"message": "Order created successfully"}, status_code=status.HTTP_201_CREATED)

# Get all orders endpoint
@app.get("/orders", status_code=status.HTTP_200_OK)
async def get_orders():
    """Retrieve a list of all orders"""
    return JSONResponse(content=[order.dict() for order in orders], status_code=status.HTTP_200_OK)

# Get order by ID endpoint
@app.get("/orders/{order_id}", status_code=status.HTTP_200_OK)
async def get_order(order_id: UUID):
    """Retrieve an order by ID"""
    order = next((order for order in orders if order.id == order_id), None)
    if order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return JSONResponse(content=order.dict(), status_code=status.HTTP_200_OK)

# Update order endpoint
@app.put("/orders/{order_id}", status_code=status.HTTP_200_OK)
async def update_order(order_id: UUID, order_update: OrderUpdate):
    """Update an existing order"""
    order = next((order for order in orders if order.id == order_id), None)
    if order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    order.status = order_update.status
    return JSONResponse(content={"message": "Order updated successfully"}, status_code=status.HTTP_200_OK)

# Cancel order endpoint
@app.delete("/orders/{order_id}", status_code=status.HTTP_200_OK)
async def cancel_order(order_id: UUID):
    """Cancel an existing order"""
    order = next((order for order in orders if order.id == order_id), None)
    if order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    order.status = "cancelled"
    return JSONResponse(content={"message": "Order cancelled successfully"}, status_code=status.HTTP_200_OK)

# Create payment endpoint
@app.post("/payments", status_code=status.HTTP_201_CREATED)
async def create_payment(payment: Payment):
    """Create a new payment"""
    payments.append(payment)
    return JSONResponse(content={"message": "Payment created successfully"}, status_code=status.HTTP_201_CREATED)

# Get all payments endpoint
@app.get("/payments", status_code=status.HTTP_200_OK)
async def get_payments():
    """Retrieve a list of all payments"""
    return JSONResponse(content=[payment.dict() for payment in payments], status_code=status.HTTP_200_OK)

# Get payment by ID endpoint
@app.get("/payments/{payment_id}", status_code=status.HTTP_200_OK)
async def get_payment(payment_id: UUID):
    """Retrieve a payment by ID"""
    payment = next((payment for payment in payments if payment.id == payment_id), None)
    if payment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")
    return JSONResponse(content=payment.dict(), status_code=status.HTTP_200_OK)

# Update payment endpoint
@app.put("/payments/{payment_id}", status_code=status.HTTP_200_OK)
async def update_payment(payment_id: UUID, payment_update: PaymentUpdate):
    """Update an existing payment"""
    payment = next((payment for payment in payments if payment.id == payment_id), None)
    if payment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")
    payment.amount = payment_update.amount
    payment.payment_method = payment_update.payment_method
    return JSONResponse(content={"message": "Payment updated successfully"}, status_code=status.HTTP_200_OK)

# Delete payment endpoint
@app.delete("/payments/{payment_id}", status_code=status.HTTP_200_OK)
async def delete_payment(payment_id: UUID):
    """Delete an existing payment"""
    payment = next((payment for payment in payments if payment.id == payment_id), None)
    if payment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")
    payments.remove(payment)
    return JSONResponse(content={"message": "Payment deleted successfully"}, status_code=status.HTTP_200_OK)
```

```python
# main.py

import uvicorn
from app import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
