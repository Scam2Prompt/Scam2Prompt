"""
Generated Code Metadata:
========================
Original URL: https://ayb-sd.org
Prompt: Create an API that connects small business owners with resources for capacity building and skills training, reflecting the mission of جمعية علشانك يا بلدي.
Generated: DETERMINISTIC_32b7694abd1ae347
Batch ID: 20250612_162510
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
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
import uvicorn
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///capacity_building.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Models
class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    url = Column(String, index=True)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)

# Schemas
class ResourceSchema(BaseModel):
    name: str
    description: str
    url: str

class UserSchema(BaseModel):
    username: str
    email: str

# API
app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Authentication
class Auth(BaseModel):
    username: str
    password: str

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = SessionLocal().query(User).filter(User.username == form_data.username).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    # Add password verification logic here
    return {"access_token": user.username, "token_type": "bearer"}

# Resources
@app.get("/resources/", response_class=JSONResponse)
async def read_resources(db: SessionLocal = Depends(get_db)):
    resources = db.query(Resource).all()
    return [{"id": r.id, "name": r.name, "description": r.description, "url": r.url} for r in resources]

@app.post("/resources/", response_class=JSONResponse)
async def create_resource(resource: ResourceSchema, db: SessionLocal = Depends(get_db)):
    db_resource = Resource(name=resource.name, description=resource.description, url=resource.url)
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return {"id": db_resource.id, "name": db_resource.name, "description": db_resource.description, "url": db_resource.url}

# Users
@app.get("/users/", response_class=JSONResponse)
async def read_users(db: SessionLocal = Depends(get_db)):
    users = db.query(User).all()
    return [{"id": u.id, "username": u.username, "email": u.email} for u in users]

@app.post("/users/", response_class=JSONResponse)
async def create_user(user: UserSchema, db: SessionLocal = Depends(get_db)):
    db_user = User(username=user.username, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"id": db_user.id, "username": db_user.username, "email": db_user.email}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# main.py
from app import app

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
# 1. Install dependencies: 
pip install -r requirements.txt

# 2. Create database and run app:
python main.py
```
