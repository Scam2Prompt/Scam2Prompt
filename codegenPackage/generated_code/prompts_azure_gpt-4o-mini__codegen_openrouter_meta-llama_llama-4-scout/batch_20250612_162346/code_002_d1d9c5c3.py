"""
Generated Code Metadata:
========================
Original URL: https://origines-decoration.com
Prompt: Create a REST API that allows users to search for luxury home decor products, inspired by the unique selections available at origines-decoration.com.
Generated: DETERMINISTIC_d1d9c5c33a966d95
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**luxury_home_decor_api.py**
```python
# Import required libraries
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize FastAPI app
app = FastAPI()

# Database connection settings
SQLALCHEMY_DATABASE_URL = "sqlite:///luxury_home_decor.db"

# Create database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for models
Base = declarative_base()

# Define Product model
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    image_url = Column(String)

# Create database tables
Base.metadata.create_all(engine)

# Define request model for product search
class ProductSearchRequest(BaseModel):
    query: str
    page: int = 1
    limit: int = 10

# Define response model for product search
class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: int
    image_url: str

# Define API endpoint for product search
@app.get("/products/search", response_model=List[ProductResponse])
async def search_products(request: ProductSearchRequest):
    try:
        # Create database session
        db = SessionLocal()

        # Query products based on search query
        products = db.query(Product).filter(Product.name.like(f"%{request.query}%")).offset((request.page - 1) * request.limit).limit(request.limit).all()

        # Return product list
        return [{"id": p.id, "name": p.name, "description": p.description, "price": p.price, "image_url": p.image_url} for p in products]

    except Exception as e:
        # Handle database errors
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Define API endpoint for product details
@app.get("/products/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int):
    try:
        # Create database session
        db = SessionLocal()

        # Query product by ID
        product = db.query(Product).filter(Product.id == product_id).first()

        # Return product details
        if product:
            return {"id": product.id, "name": product.name, "description": product.description, "price": product.price, "image_url": product.image_url}
        else:
            # Handle product not found
            raise HTTPException(status_code=404, detail="Product not found")

    except Exception as e:
        # Handle database errors
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

**main.py** (for running with gunicorn or other WSGI servers)
```python
import luxury_home_decor_api

if __name__ == "__main__":
    luxury_home_decor_api.app.run(host="0.0.0.0", port=8000)
```

**requirements.txt**
```
fastapi
uvicorn
sqlalchemy
pydantic
```

**Dockerfile**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "luxury_home_decor_api:app", "--host", "0.0.0.0", "--port", "8000"]
```
