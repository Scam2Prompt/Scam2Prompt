"""
Generated Code Metadata:
========================
Original URL: https://mintsolutions.io
Prompt: Create a sample API for a mentorship program that tracks individual development plans and progress, similar to the services offered by Mint Solutions.
Generated: DETERMINISTIC_1e8687d6a470a615
Batch ID: 20250612_135906
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
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize FastAPI app
app = FastAPI()

# Database configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///mentorship.db"

# Create database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for models
Base = declarative_base()

# Define models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

class DevelopmentPlan(Base):
    __tablename__ = "development_plans"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    goal = Column(String, index=True)
    progress = Column(String, index=True)

# Create database tables
Base.metadata.create_all(bind=engine)

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic models for request and response validation
class UserCreate(BaseModel):
    name: str
    email: str

class DevelopmentPlanCreate(BaseModel):
    goal: str
    progress: str

class DevelopmentPlanUpdate(BaseModel):
    goal: str | None
    progress: str | None

# API Endpoints
@app.post("/users/", response_model=User)
def create_user(user: UserCreate, db: SessionLocal = Depends(get_db)):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/", response_model=List[User])
def read_users(db: SessionLocal = Depends(get_db)):
    return db.query(User).all()

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: SessionLocal = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/users/{user_id}/development-plans/", response_model=DevelopmentPlan)
def create_development_plan(user_id: int, development_plan: DevelopmentPlanCreate, db: SessionLocal = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_development_plan = DevelopmentPlan(user_id=user_id, goal=development_plan.goal, progress=development_plan.progress)
    db.add(db_development_plan)
    db.commit()
    db.refresh(db_development_plan)
    return db_development_plan

@app.get("/users/{user_id}/development-plans/", response_model=List[DevelopmentPlan])
def read_development_plans(user_id: int, db: SessionLocal = Depends(get_db)):
    return db.query(DevelopmentPlan).filter(DevelopmentPlan.user_id == user_id).all()

@app.get("/development-plans/{development_plan_id}", response_model=DevelopmentPlan)
def read_development_plan(development_plan_id: int, db: SessionLocal = Depends(get_db)):
    db_development_plan = db.query(DevelopmentPlan).filter(DevelopmentPlan.id == development_plan_id).first()
    if db_development_plan is None:
        raise HTTPException(status_code=404, detail="Development plan not found")
    return db_development_plan

@app.put("/development-plans/{development_plan_id}", response_model=DevelopmentPlan)
def update_development_plan(development_plan_id: int, development_plan: DevelopmentPlanUpdate, db: SessionLocal = Depends(get_db)):
    db_development_plan = db.query(DevelopmentPlan).filter(DevelopmentPlan.id == development_plan_id).first()
    if db_development_plan is None:
        raise HTTPException(status_code=404, detail="Development plan not found")
    if development_plan.goal:
        db_development_plan.goal = development_plan.goal
    if development_plan.progress:
        db_development_plan.progress = development_plan.progress
    db.commit()
    db.refresh(db_development_plan)
    return db_development_plan

@app.delete("/development-plans/{development_plan_id}")
def delete_development_plan(development_plan_id: int, db: SessionLocal = Depends(get_db)):
    db_development_plan = db.query(DevelopmentPlan).filter(DevelopmentPlan.id == development_plan_id).first()
    if db_development_plan is None:
        raise HTTPException(status_code=404, detail="Development plan not found")
    db.delete(db_development_plan)
    db.commit()
    return {"message": "Development plan deleted"}
```

```python
# main.py
from app import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
