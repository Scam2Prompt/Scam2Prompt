"""
Generated Code Metadata:
========================
Original URL: https://snackpointemmen.nl
Prompt: Create an API endpoint for a snack bar that allows customers to place orders for items like fries, burgers, and milkshakes, referencing the unique snack wall feature at Snackpoint Emmen.
Generated: DETERMINISTIC_f14e4aa54ad9ca1d
Batch ID: 20250612_161616
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
    title="Snackpoint Emmen API",
    description="API for Snackpoint Emmen's snack bar",
    version="1.0.0"
)

# Define the menu items
menu_items = {
    "fries": 2.99,
    "burger": 5.99,
    "milkshake": 3.99
}

# Define the order model
class OrderItem(BaseModel):
    item: str
    quantity: int

class Order(BaseModel):
    items: List[OrderItem]

# Define the order endpoint
@app.post("/orders/")
async def create_order(order: Order):
    """
    Create a new order.

    :param order: The order to create
    :return: The created order with total cost
    """
    try:
        total_cost = 0
        order_response = []
        for item in order.items:
            if item.item not in menu_items:
                raise HTTPException(status_code=400, detail=f"Item '{item.item}' not found in menu")
            if item.quantity <= 0:
                raise HTTPException(status_code=400, detail=f"Quantity for item '{item.item}' must be greater than 0")
            cost = menu_items[item.item] * item.quantity
            total_cost += cost
            order_response.append({
                "item": item.item,
                "quantity": item.quantity,
                "cost": cost
            })
        return {
            "items": order_response,
            "total_cost": total_cost
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Define the menu endpoint
@app.get("/menu/")
async def get_menu():
    """
    Get the menu items.

    :return: The menu items with prices
    """
    return menu_items

# Define the snack wall feature endpoint
@app.get("/snack-wall/")
async def get_snack_wall():
    """
    Get information about the unique snack wall feature.

    :return: Information about the snack wall feature
    """
    return {
        "feature": "snack wall",
        "description": "Our unique snack wall feature at Snackpoint Emmen allows customers to choose from a variety of snacks."
    }

# Error handler for HTTP exceptions
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {"error": exc.detail}

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```bash
# Dockerfile

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

```bash
# requirements.txt

fastapi
uvicorn
pydantic
```

```bash
# Run with Docker
docker build -t snackpoint-emmen .
docker run -p 8000:8000 snackpoint-emmen
```
