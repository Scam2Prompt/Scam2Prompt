"""
Generated Code Metadata:
========================
Original URL: https://teeny-activity-colossal.on-fleek.app
Prompt: Create a REST API specification for a comic book store, including endpoints for retrieving comic details, checking stock for limited editions, and placing orders.
Generated: DETERMINISTIC_5a2d1a4cc7e5cb6c
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4
from datetime import datetime

app = FastAPI(
    title="Comic Book Store API",
    description="API for managing comic book inventory and orders",
    version="1.0.0",
    contact={
        "name": "API Support",
        "email": "support@comicstore.com"
    },
    license_info={
        "name": "MIT",
    },
)

# Database models (in-memory for example purposes)
class Comic(BaseModel):
    id: UUID
    title: str
    issue: int
    publisher: str
    author: str
    artist: str
    release_date: datetime
    price: float
    is_limited_edition: bool
    stock: int

class OrderItem(BaseModel):
    comic_id: UUID
    quantity: int

class Order(BaseModel):
    id: UUID
    customer_name: str
    customer_email: str
    items: List[OrderItem]
    total_amount: float
    order_date: datetime
    status: str = "pending"

# In-memory database
comics_db = {}
orders_db = {}

# Helper functions
def get_comic_or_404(comic_id: UUID):
    comic = comics_db.get(comic_id)
    if not comic:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comic not found"
        )
    return comic

# API Endpoints
@app.get("/comics", response_model=List[Comic], tags=["Inventory"])
async def list_comics(publisher: Optional[str] = None, limit: int = 100):
    """
    Get a list of all comics in inventory.
    Can be filtered by publisher.
    """
    comics = list(comics_db.values())
    if publisher:
        comics = [c for c in comics if c.publisher.lower() == publisher.lower()]
    return comics[:limit]

@app.get("/comics/{comic_id}", response_model=Comic, tags=["Inventory"])
async def get_comic(comic_id: UUID):
    """Get details for a specific comic by ID"""
    return get_comic_or_404(comic_id)

@app.get("/comics/limited-edition/stock", tags=["Inventory"])
async def check_limited_edition_stock():
    """Check stock levels for all limited edition comics"""
    limited_editions = [
        comic for comic in comics_db.values() 
        if comic.is_limited_edition and comic.stock > 0
    ]
    return {
        "count": len(limited_editions),
        "comics": limited_editions
    }

@app.post("/orders", response_model=Order, status_code=status.HTTP_201_CREATED, tags=["Orders"])
async def create_order(customer_name: str, customer_email: str, items: List[OrderItem]):
    """
    Create a new comic book order.
    Validates stock availability before creating the order.
    """
    order_id = uuid4()
    order_items = []
    total_amount = 0.0
    
    for item in items:
        comic = get_comic_or_404(item.comic_id)
        
        if comic.stock < item.quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Not enough stock for comic {comic.title} (ID: {comic.id})"
            )
            
        total_amount += comic.price * item.quantity
        order_items.append(item)
    
    order = Order(
        id=order_id,
        customer_name=customer_name,
        customer_email=customer_email,
        items=order_items,
        total_amount=total_amount,
        order_date=datetime.now()
    )
    
    orders_db[order_id] = order
    
    # Update stock (in a real app, this would be transactional)
    for item in order_items:
        comic = comics_db[item.comic_id]
        comic.stock -= item.quantity
    
    return order

@app.get("/orders/{order_id}", response_model=Order, tags=["Orders"])
async def get_order(order_id: UUID):
    """Get details for a specific order by ID"""
    order = orders_db.get(order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    return order

# Sample data initialization
@app.on_event("startup")
async def startup_event():
    """Initialize sample data"""
    sample_comics = [
        Comic(
            id=uuid4(),
            title="The Amazing Spider-Man",
            issue=1,
            publisher="Marvel",
            author="Stan Lee",
            artist="Steve Ditko",
            release_date=datetime(1963, 3, 10),
            price=12.99,
            is_limited_edition=True,
            stock=5
        ),
        Comic(
            id=uuid4(),
            title="Batman: The Dark Knight Returns",
            issue=1,
            publisher="DC",
            author="Frank Miller",
            artist="Frank Miller",
            release_date=datetime(1986, 2, 1),
            price=9.99,
            is_limited_edition=False,
            stock=20
        ),
        Comic(
            id=uuid4(),
            title="Saga",
            issue=1,
            publisher="Image",
            author="Brian K. Vaughan",
            artist="Fiona Staples",
            release_date=datetime(2012, 3, 14),
            price=7.99,
            is_limited_edition=True,
            stock=3
        )
    ]
    
    for comic in sample_comics:
        comics_db[comic.id] = comic
```
