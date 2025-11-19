"""
Generated Code Metadata:
========================
Original URL: https://bitzino.vip
Prompt: Design a rewards program API that tracks user XP and ranks in a gaming platform, inspired by the features of Bitzino's leaderboard system.
Generated: DETERMINISTIC_3750316de08b6df3
Batch ID: 20250612_163751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import databases
import sqlalchemy
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# Database configuration
DATABASE_URL = "sqlite:///./rewards.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# Database models
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String(50), unique=True),
    sqlalchemy.Column("hashed_password", sqlalchemy.String(200)),
    sqlalchemy.Column("xp", sqlalchemy.Integer, default=0),
    sqlalchemy.Column("rank", sqlalchemy.Integer, default=1),
    sqlalchemy.Column("last_active", sqlalchemy.DateTime, default=datetime.utcnow),
)

rewards = sqlalchemy.Table(
    "rewards",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("rank_required", sqlalchemy.Integer),
    sqlalchemy.Column("name", sqlalchemy.String(100)),
    sqlalchemy.Column("description", sqlalchemy.String(200)),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

# Pydantic models
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    xp: int
    rank: int
    last_active: datetime

    class Config:
        orm_mode = True

class Reward(BaseModel):
    id: int
    rank_required: int
    name: str
    description: str

    class Config:
        orm_mode = True

class XPUpdate(BaseModel):
    xp_change: int = Field(..., gt=0, description="Positive XP amount to add")

class Token(BaseModel):
    access_token: str
    token_type: str

# App and security
app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Utility functions
def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

def get_user(db: Session, username: str):
    return db.execute(users.select().where(users.c.username == username)).first()

def authenticate_user(db: Session, username: str, password: str):
    # In production, use proper password hashing like bcrypt
    user = get_user(db, username)
    if not user or user.hashed_password != f"fakehashed{password}":
        return False
    return user

def create_access_token(data: dict):
    # In production, use proper JWT token generation
    return {"access_token": "fake_token", "token_type": "bearer"}

# API endpoints
@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    return create_access_token(data={"sub": user.username})

@app.post("/users/", response_model=User)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    # In production, hash the password properly
    hashed_password = f"fakehashed{user.password}"
    query = users.insert().values(
        username=user.username,
        hashed_password=hashed_password,
        xp=0,
        rank=1
    )
    user_id = db.execute(query).lastrowid
    db.commit()
    return {**user.dict(), "id": user_id, "xp": 0, "rank": 1}

@app.get("/users/me", response_model=User)
async def read_users_me(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    # In production, validate the token properly
    if token != "fake_token":
        raise HTTPException(status_code=401, detail="Invalid token")
    
    # For demo, just return the first user
    user = db.execute(users.select().limit(1)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users/me/xp", response_model=User)
async def add_xp(
    xp_update: XPUpdate,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    if token != "fake_token":
        raise HTTPException(status_code=401, detail="Invalid token")
    
    # For demo, update the first user
    user = db.execute(users.select().limit(1)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    new_xp = user.xp + xp_update.xp_change
    new_rank = min(new_xp // 1000 + 1, 10)  # Simple rank calculation
    
    query = (
        users.update()
        .where(users.c.id == user.id)
        .values(xp=new_xp, rank=new_rank, last_active=datetime.utcnow())
    )
    db.execute(query)
    db.commit()
    
    updated_user = db.execute(users.select().where(users.c.id == user.id)).first()
    return updated_user

@app.get("/leaderboard", response_model=List[User])
async def get_leaderboard(limit: int = 10, db: Session = Depends(get_db)):
    query = users.select().order_by(users.c.xp.desc()).limit(limit)
    top_users = db.execute(query).fetchall()
    return top_users

@app.get("/rewards/available", response_model=List[Reward])
async def get_available_rewards(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    if token != "fake_token":
        raise HTTPException(status_code=401, detail="Invalid token")
    
    # For demo, get the first user's rank
    user = db.execute(users.select().limit(1)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    query = rewards.select().where(rewards.c.rank_required <= user.rank)
    available_rewards = db.execute(query).fetchall()
    return available_rewards

# Startup event
@app.on_event("startup")
async def startup():
    await database.connect()
    # Seed some initial data for demo
    db = Session(engine)
    try:
        if not db.execute(users.select().limit(1)).first():
            db.execute(users.insert().values(
                username="testuser",
                hashed_password="fakehashedpassword",
                xp=500,
                rank=1
            ))
            
        if not db.execute(rewards.select().limit(1)).first():
            db.execute(rewards.insert().values([
                {"rank_required": 1, "name": "Starter Pack", "description": "Welcome reward"},
                {"rank_required": 3, "name": "Bronze Pack", "description": "Bronze level reward"},
                {"rank_required": 5, "name": "Silver Pack", "description": "Silver level reward"},
                {"rank_required": 8, "name": "Gold Pack", "description": "Gold level reward"},
                {"rank_required": 10, "name": "Platinum Pack", "description": "Platinum level reward"},
            ]))
        db.commit()
    finally:
        db.close()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
```
