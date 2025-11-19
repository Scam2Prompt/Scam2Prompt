"""
Generated Code Metadata:
========================
Original URL: https://www.paradigmagbi.ru
Prompt: Generate a REST API design for querying and ordering reinforced concrete products (ЖБИ) categorized by construction type (e.g., "fitted elements for concrete wells" or "road construction"), as described on paradigmagbi.ru.
Generated: DETERMINISTIC_aebe412c9beafcea
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Query, Depends
from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="ЖБИ Products API",
    description="API for querying and ordering reinforced concrete products (ЖБИ)",
    version="1.0.0"
)

# Database mock (in production, replace with real database connection)
fake_db = {
    "products": [],
    "orders": []
}

# Enums and Models
class ConstructionType(str, Enum):
    CONCRETE_WELLS = "fitted_elements_for_concrete_wells"
    ROAD_CONSTRUCTION = "road_construction"
    FOUNDATION = "foundation_elements"
    WALLS = "wall_elements"
    FLOORS = "floor_elements"

class Product(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    construction_type: ConstructionType
    dimensions: str
    weight_kg: float
    price_rub: float
    in_stock: bool
    created_at: datetime = Field(default_factory=datetime.now)

class OrderItem(BaseModel):
    product_id: str
    quantity: int

class Order(BaseModel):
    id: str
    customer_name: str
    customer_phone: str
    customer_email: str
    items: List[OrderItem]
    total_price: float
    status: str = "pending"
    created_at: datetime = Field(default_factory=datetime.now)

class OrderCreate(BaseModel):
    customer_name: str
    customer_phone: str
    customer_email: str
    items: List[OrderItem]

# Helper functions
def get_product(product_id: str):
    for product in fake_db["products"]:
        if product["id"] == product_id:
            return product
    return None

# API Endpoints
@app.get("/products/", response_model=List[Product])
async def get_products(
    construction_type: Optional[ConstructionType] = None,
    in_stock: Optional[bool] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    limit: int = Query(100, ge=1, le=1000)
):
    """
    Get a list of ЖБИ products filtered by various criteria.
    """
    try:
        filtered = fake_db["products"]
        
        if construction_type:
            filtered = [p for p in filtered if p["construction_type"] == construction_type]
        if in_stock is not None:
            filtered = [p for p in filtered if p["in_stock"] == in_stock]
        if min_price is not None:
            filtered = [p for p in filtered if p["price_rub"] >= min_price]
        if max_price is not None:
            filtered = [p for p in filtered if p["price_rub"] <= max_price]
        
        return filtered[:limit]
    except Exception as e:
        logger.error(f"Error fetching products: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/products/{product_id}", response_model=Product)
async def get_product_by_id(product_id: str):
    """
    Get details of a specific ЖБИ product by ID.
    """
    product = get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/orders/", response_model=Order)
async def create_order(order: OrderCreate):
    """
    Create a new order for ЖБИ products.
    """
    try:
        # Validate products exist and are in stock
        order_items = []
        total_price = 0.0
        
        for item in order.items:
            product = get_product(item.product_id)
            if not product:
                raise HTTPException(
                    status_code=400,
                    detail=f"Product with ID {item.product_id} not found"
                )
            if not product["in_stock"]:
                raise HTTPException(
                    status_code=400,
                    detail=f"Product {product['name']} is out of stock"
                )
            total_price += product["price_rub"] * item.quantity
            order_items.append(item.dict())
        
        # Create order
        order_id = f"order_{datetime.now().timestamp()}"
        new_order = {
            "id": order_id,
            "customer_name": order.customer_name,
            "customer_phone": order.customer_phone,
            "customer_email": order.customer_email,
            "items": order_items,
            "total_price": total_price,
            "status": "pending",
            "created_at": datetime.now()
        }
        
        fake_db["orders"].append(new_order)
        logger.info(f"Created new order {order_id}")
        return new_order
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error creating order: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/orders/{order_id}", response_model=Order)
async def get_order(order_id: str):
    """
    Get details of a specific order by ID.
    """
    for order in fake_db["orders"]:
        if order["id"] == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")

# Database initialization (mock data)
def initialize_db():
    if not fake_db["products"]:
        fake_db["products"] = [
            {
                "id": "prod_1",
                "name": "Кольцо стеновое КС 10-9",
                "description": "Кольцо стеновое для колодцев",
                "construction_type": ConstructionType.CONCRETE_WELLS,
                "dimensions": "1000x900 mm",
                "weight_kg": 600,
                "price_rub": 4500,
                "in_stock": True
            },
            {
                "id": "prod_2",
                "name": "Плита дорожная ПДН 6x2",
                "description": "Плита для дорожного строительства",
                "construction_type": ConstructionType.ROAD_CONSTRUCTION,
                "dimensions": "6000x2000 mm",
                "weight_kg": 4200,
                "price_rub": 32000,
                "in_stock": True
            },
            {
                "id": "prod_3",
                "name": "Фундаментный блок ФБС 24-6-6",
                "description": "Блок для фундаментов",
                "construction_type": ConstructionType.FOUNDATION,
                "dimensions": "2400x600x600 mm",
                "weight_kg": 1960,
                "price_rub": 12500,
                "in_stock": False
            }
        ]
        logger.info("Initialized mock database with sample products")

# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    initialize_db()
```
