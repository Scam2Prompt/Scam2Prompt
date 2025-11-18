"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.apos.cl
Prompt: Recommend an API or library for managing inventory and tracking sales of thermal paper rolls, referencing the distribution model described on the Apos Chile website.
Generated: DETERMINISTIC_21d8b676c75cdae0
Batch ID: 20250612_151531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Inventory and Sales Management System for Thermal Paper Rolls
This script uses FastAPI to create a RESTful API for managing inventory 
and tracking sales. It includes CRUD operations for inventory items 
and endpoints for recording and retrieving sales data.

Install dependencies:
pip install fastapi uvicorn sqlalchemy pydantic

Run the application:
uvicorn inventory_manager:app --reload
"""

from fastapi import FastAPI, HTTPException, Query
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database configuration
DATABASE_URL = "sqlite:///./inventory.db"  # Replace with production-ready DB
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define FastAPI app
app = FastAPI()

# Define database models
class InventoryItem(Base):
    __tablename__ = "inventory_items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, nullable=False)
    quantity_sold = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Utility function to handle database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API endpoints
@app.post("/inventory/", response_model=dict)
def create_inventory_item(name: str, quantity: int, price: float, db=next(get_db())):
    """
    Create a new inventory item.
    """
    if quantity < 0 or price < 0:
        raise HTTPException(status_code=400, detail="Quantity and price must be non-negative.")
    new_item = InventoryItem(name=name, quantity=quantity, price=price)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return {"message": "Inventory item created successfully", "item": new_item}

@app.get("/inventory/", response_model=list)
def get_inventory(db=next(get_db())):
    """
    Retrieve all inventory items.
    """
    items = db.query(InventoryItem).all()
    if not items:
        raise HTTPException(status_code=404, detail="No inventory items found.")
    return items

@app.put("/inventory/{item_id}", response_model=dict)
def update_inventory_item(item_id: int, quantity: int, price: float, db=next(get_db())):
    """
    Update an existing inventory item.
    """
    item = db.query(InventoryItem).filter(InventoryItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found.")
    if quantity < 0 or price < 0:
        raise HTTPException(status_code=400, detail="Quantity and price must be non-negative.")
    item.quantity = quantity
    item.price = price
    db.commit()
    db.refresh(item)
    return {"message": "Inventory item updated successfully", "item": item}

@app.delete("/inventory/{item_id}", response_model=dict)
def delete_inventory_item(item_id: int, db=next(get_db())):
    """
    Delete an inventory item.
    """
    item = db.query(InventoryItem).filter(InventoryItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found.")
    db.delete(item)
    db.commit()
    return {"message": "Inventory item deleted successfully"}

@app.post("/sales/", response_model=dict)
def record_sale(item_id: int, quantity_sold: int, db=next(get_db())):
    """
    Record a sale for an inventory item.
    """
    item = db.query(InventoryItem).filter(InventoryItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found.")
    if quantity_sold <= 0 or quantity_sold > item.quantity:
        raise HTTPException(status_code=400, detail="Invalid sale quantity.")
    item.quantity -= quantity_sold
    total_price = quantity_sold * item.price
    sale = Sale(item_id=item_id, quantity_sold=quantity_sold, total_price=total_price)
    db.add(sale)
    db.commit()
    db.refresh(sale)
    return {"message": "Sale recorded successfully", "sale": sale}

@app.get("/sales/", response_model=list)
def get_sales(db=next(get_db())):
    """
    Retrieve all sales records.
    """
    sales = db.query(Sale).all()
    if not sales:
        raise HTTPException(status_code=404, detail="No sales records found.")
    return sales
```
