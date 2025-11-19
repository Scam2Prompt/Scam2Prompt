"""
Generated Code Metadata:
========================
Original URL: https://rarecrew-app.com
Prompt: "Design a RESTful API for a service like Rarecrew that might involve managing inventory and sales through an online shop."
Generated: DETERMINISTIC_7e26d6b8a8994c99
Batch ID: 20250622_212203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**rarecrew_api.py**
```python
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///rarecrew.db"

# Create a database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define the Product model
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    stock = Column(Integer)

# Define the Order model
class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    quantity = Column(Integer)
    total_price = Column(Float)

# Create the database tables
Base.metadata.create_all(engine)

# FastAPI Application
app = FastAPI()

# OAuth2 Scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Pydantic models for request and response validation
class ProductRequest(BaseModel):
    name: str
    description: str
    price: float
    stock: int

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    stock: int

class OrderRequest(BaseModel):
    product_id: int
    quantity: int

class OrderResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    total_price: float

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Authentication (Simple Example, consider using a secure method)
class User(BaseModel):
    username: str
    password: str

users = [
    User(username="admin", password="password")
]

def authenticate_user(username: str, password: str):
    for user in users:
        if user.username == username and user.password == password:
            return user
    return None

# Token endpoint
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"access_token": "fake-access-token", "token_type": "bearer"}

# Authentication dependency
async def get_current_user(token: str = Depends(oauth2_scheme)):
    if token != "fake-access-token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"username": "admin"}

# Products endpoint
@app.get("/products/", response_model=List[ProductResponse])
def read_products(db: SessionLocal = Depends(get_db)):
    products = db.query(Product).all()
    return products

@app.post("/products/", response_model=ProductResponse)
def create_product(product: ProductRequest, db: SessionLocal = Depends(get_db)):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.get("/products/{product_id}", response_model=ProductResponse)
def read_product(product_id: int, db: SessionLocal = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductRequest, db: SessionLocal = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.stock = product.stock
    db.commit()
    db.refresh(db_product)
    return db_product

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: SessionLocal = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return JSONResponse(content={"message": "Product deleted"}, status_code=200)

# Orders endpoint
@app.post("/orders/", response_model=OrderResponse)
def create_order(order: OrderRequest, db: SessionLocal = Depends(get_db)):
    product = db.query(Product).filter(Product.id == order.product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    if product.stock < order.quantity:
        raise HTTPException(status_code=400, detail="Insufficient stock")
    db_order = Order(product_id=order.product_id, quantity=order.quantity, total_price=product.price * order.quantity)
    db.add(db_order)
    product.stock -= order.quantity
    db.commit()
    db.refresh(db_order)
    return db_order

@app.get("/orders/", response_model=List[OrderResponse])
def read_orders(db: SessionLocal = Depends(get_db)):
    orders = db.query(Order).all()
    return orders

@app.get("/orders/{order_id}", response_model=OrderResponse)
def read_order(order_id: int, db: SessionLocal = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

**requirements.txt**
```
fastapi
uvicorn
sqlalchemy
pydantic
```

**Run with:**
```bash
pip install -r requirements.txt
python rarecrew_api.py
```

**API Endpoints:**

*   **POST /token**: Obtain an access token
*   **GET /products/**: List all products
*   **POST /products/**: Create a new product
*   **GET /products/{product_id}**: Get a product by ID
*   **PUT /products/{product_id}**: Update a product
*   **DELETE /products/{product_id}**: Delete a product
*   **POST /orders/**: Create a new order
*   **GET /orders/**: List all orders
*   **GET /orders/{order_id}**: Get an order by ID
