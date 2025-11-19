"""
Generated Code Metadata:
========================
Original URL: https://ipolattibraz.blogspot.com
Prompt: Design a RESTful API for managing orders and deliveries for an e-commerce platform like sipollati, including endpoints for tracking shipments.
Generated: DETERMINISTIC_da08e26c30b9443d
Batch ID: 20250622_212010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///ecommerce.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Pydantic Models
class Order(BaseModel):
    id: int
    customer_name: str
    order_date: str
    total: float

class Delivery(BaseModel):
    id: int
    order_id: int
    shipment_date: str
    tracking_number: str

class ShipmentTracking(BaseModel):
    tracking_number: str
    status: str

# SQLAlchemy Models
class OrderDB(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    order_date = Column(String)
    total = Column(Integer)

class DeliveryDB(Base):
    __tablename__ = "deliveries"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer)
    shipment_date = Column(String)
    tracking_number = Column(String)

Base.metadata.create_all(engine)

# FastAPI App
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoints
@app.post("/orders/")
def create_order(order: Order, db: SessionLocal = Depends(get_db)):
    try:
        db_order = OrderDB(**order.dict())
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        return JSONResponse(content={"message": "Order created successfully"}, status_code=201)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/orders/")
def read_orders(db: SessionLocal = Depends(get_db)):
    try:
        orders = db.query(OrderDB).all()
        return JSONResponse(content=[order.to_dict() for order in orders], status_code=200)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/orders/{order_id}")
def read_order(order_id: int, db: SessionLocal = Depends(get_db)):
    try:
        order = db.query(OrderDB).filter(OrderDB.id == order_id).first()
        if order is None:
            raise HTTPException(status_code=404, detail="Order not found")
        return JSONResponse(content=order.to_dict(), status_code=200)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/deliveries/")
def create_delivery(delivery: Delivery, db: SessionLocal = Depends(get_db)):
    try:
        db_delivery = DeliveryDB(**delivery.dict())
        db.add(db_delivery)
        db.commit()
        db.refresh(db_delivery)
        return JSONResponse(content={"message": "Delivery created successfully"}, status_code=201)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/deliveries/")
def read_deliveries(db: SessionLocal = Depends(get_db)):
    try:
        deliveries = db.query(DeliveryDB).all()
        return JSONResponse(content=[delivery.to_dict() for delivery in deliveries], status_code=200)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/deliveries/{delivery_id}")
def read_delivery(delivery_id: int, db: SessionLocal = Depends(get_db)):
    try:
        delivery = db.query(DeliveryDB).filter(DeliveryDB.id == delivery_id).first()
        if delivery is None:
            raise HTTPException(status_code=404, detail="Delivery not found")
        return JSONResponse(content=delivery.to_dict(), status_code=200)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/track-shipment/")
def track_shipment(shipment_tracking: ShipmentTracking):
    try:
        # Simulating shipment tracking API call
        tracking_data = {"tracking_number": shipment_tracking.tracking_number, "status": shipment_tracking.status}
        return JSONResponse(content=tracking_data, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# requirements.txt
fastapi
uvicorn
sqlalchemy
pydantic
```

```bash
# Run
# Create a virtual environment and install dependencies
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run the app
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
