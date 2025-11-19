"""
Generated Code Metadata:
========================
Original URL: https://dfivetechnologies.com
Prompt: Create a sample API for a retail application that incorporates the technology services mentioned by DFIVE Technologies.
Generated: DETERMINISTIC_54ff6e5a12891d9c
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from typing import List, Optional
import uvicorn
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Retail Application API",
    description="A sample retail API incorporating DFIVE Technologies services",
    version="1.0.0"
)

# Database models (simulated in-memory storage)
class Product(BaseModel):
    id: int
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    category: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

class Order(BaseModel):
    id: int
    product_ids: List[int]
    customer_id: int
    total_amount: float
    status: str = "pending"
    created_at: datetime = datetime.now()

# In-memory database
products_db = {}
orders_db = {}
current_id = 0

# Helper functions
def get_next_id():
    global current_id
    current_id += 1
    return current_id

# API endpoints
@app.post("/products/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(product: Product):
    """Create a new product"""
    try:
        product.id = get_next_id()
        products_db[product.id] = product
        logger.info(f"Created product with ID: {product.id}")
        return product
    except Exception as e:
        logger.error(f"Error creating product: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error creating product"
        )

@app.get("/products/", response_model=List[Product])
async def list_products(category: Optional[str] = None):
    """List all products, optionally filtered by category"""
    try:
        products = list(products_db.values())
        if category:
            products = [p for p in products if p.category.lower() == category.lower()]
        return products
    except Exception as e:
        logger.error(f"Error listing products: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving products"
        )

@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    """Get a specific product by ID"""
    if product_id not in products_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return products_db[product_id]

@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, product: Product):
    """Update a product"""
    try:
        if product_id not in products_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found"
            )
        
        product.id = product_id
        product.updated_at = datetime.now()
        products_db[product_id] = product
        logger.info(f"Updated product with ID: {product_id}")
        return product
    except Exception as e:
        logger.error(f"Error updating product: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error updating product"
        )

@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int):
    """Delete a product"""
    try:
        if product_id not in products_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found"
            )
        del products_db[product_id]
        logger.info(f"Deleted product with ID: {product_id}")
    except Exception as e:
        logger.error(f"Error deleting product: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error deleting product"
        )

@app.post("/orders/", response_model=Order, status_code=status.HTTP_201_CREATED)
async def create_order(order: Order):
    """Create a new order"""
    try:
        # Validate all products exist
        for product_id in order.product_ids:
            if product_id not in products_db:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Product with ID {product_id} not found"
                )
        
        order.id = get_next_id()
        orders_db[order.id] = order
        logger.info(f"Created order with ID: {order.id}")
        return order
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error creating order: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error creating order"
        )

@app.get("/orders/{order_id}", response_model=Order)
async def get_order(order_id: int):
    """Get a specific order by ID"""
    if order_id not in orders_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    return orders_db[order_id]

@app.put("/orders/{order_id}/status", response_model=Order)
async def update_order_status(order_id: int, status: str):
    """Update order status"""
    try:
        if order_id not in orders_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Order not found"
            )
        
        valid_statuses = ["pending", "processing", "shipped", "delivered", "cancelled"]
        if status.lower() not in valid_statuses:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid status. Must be one of: {', '.join(valid_statuses)}"
            )
        
        orders_db[order_id].status = status.lower()
        logger.info(f"Updated order {order_id} status to: {status}")
        return orders_db[order_id]
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating order status: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error updating order status"
        )

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now()}

# Main entry point
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
