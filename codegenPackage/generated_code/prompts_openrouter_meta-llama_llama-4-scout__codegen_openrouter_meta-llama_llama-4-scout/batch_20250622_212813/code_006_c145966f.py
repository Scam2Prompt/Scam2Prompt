"""
Generated Code Metadata:
========================
Original URL: https://forgemints.store
Prompt: Create a Forgemint-like platform for a specific use case, such as a marketplace for virtual real estate or exclusive in-game items, and describe the key features and technical requirements for the platform.
Generated: DETERMINISTIC_c145966fac44f49d
Batch ID: 20250622_212813
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
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
import uvicorn
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize FastAPI app
app = FastAPI()

# Database connection
SQLALCHEMY_DATABASE_URL = "sqlite:///marketplace.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Pydantic models
class ItemBase(BaseModel):
    name: str
    description: str
    price: float

class Item(ItemBase):
    id: int

class UserBase(BaseModel):
    username: str
    email: str

class User(UserBase):
    id: int

# SQLAlchemy models
class ItemModel(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)

Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

# Endpoints
@app.post("/items/", response_model=Item)
async def create_item(item: ItemBase, db: SessionLocal = get_db()):
    db_item = ItemModel(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/items/", response_model=List[Item])
async def read_items(db: SessionLocal = get_db()):
    return db.query(ItemModel).all()

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int, db: SessionLocal = get_db()):
    item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: ItemBase, db: SessionLocal = get_db()):
    db_item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.name = item.name
    db_item.description = item.description
    db_item.price = item.price
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int, db: SessionLocal = get_db()):
    db_item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return JSONResponse(content={"message": "Item deleted"}, status_code=200)

@app.post("/users/", response_model=User)
async def create_user(user: UserBase, db: SessionLocal = get_db()):
    db_user = UserModel(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/", response_model=List[User])
async def read_users(db: SessionLocal = get_db()):
    return db.query(UserModel).all()

@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int, db: SessionLocal = get_db()):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

if __name__ == "__main__":
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
# Run with: uvicorn app:app --host 0.0.0.0 --port 8000
```
