"""
Generated Code Metadata:
========================
Original URL: https://wordoflifenw.com
Prompt: Create a RESTful API design for a church community platform that supports features like member engagement and ministry updates, reflecting the mission of Word of Life Northwest.
Generated: DETERMINISTIC_9db6bc4eb9a44303
Batch ID: 20250612_162203
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
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///church_community.db"

# Create a database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# OAuth2 Scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Pydantic Models
class Member(BaseModel):
    id: int
    name: str
    email: str

class MinistryUpdate(BaseModel):
    id: int
    title: str
    content: str

# SQLAlchemy Models
class MemberModel(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

class MinistryUpdateModel(Base):
    __tablename__ = "ministry_updates"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)

# Create the database tables
Base.metadata.create_all(bind=engine)

# FastAPI App
app = FastAPI()

# Token Model
class Token(BaseModel):
    access_token: str
    token_type: str

# User Model (for OAuth2)
class User(BaseModel):
    username: str
    email: str
    full_name: str
    disabled: bool

# In-memory user database (replace with a real database)
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "email": "johndoe@example.com",
        "full_name": "John Doe",
        "disabled": False,
        "password": "secret",
    }
}

# Verify password (for OAuth2)
def verify_password(plain_password: str, hashed_password: str):
    # For simplicity, we will not hash passwords in this example
    return plain_password == hashed_password

# Get user (for OAuth2)
def get_user(db: SessionLocal, username: str):
    if username in fake_users_db:
        user_dict = fake_users_db[username]
        return User(**user_dict)

# Authenticate user (for OAuth2)
def authenticate_user(db: SessionLocal, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.disabled):
        return False
    return user

# Login endpoint (for OAuth2)
@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(SessionLocal(), form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"access_token": user.username, "token_type": "bearer"}

# Members endpoint
@app.get("/members/", response_model=List[Member])
def read_members(db: SessionLocal = Depends(get_db)):
    members = db.query(MemberModel).all()
    return [{"id": m.id, "name": m.name, "email": m.email} for m in members]

# Member endpoint
@app.get("/members/{member_id}", response_model=Member)
def read_member(member_id: int, db: SessionLocal = Depends(get_db)):
    member = db.query(MemberModel).filter(MemberModel.id == member_id).first()
    if member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return {"id": member.id, "name": member.name, "email": member.email}

# Create member endpoint
@app.post("/members/", response_model=Member)
def create_member(member: Member, db: SessionLocal = Depends(get_db)):
    db_member = MemberModel(name=member.name, email=member.email)
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return {"id": db_member.id, "name": db_member.name, "email": db_member.email}

# Ministry updates endpoint
@app.get("/ministry_updates/", response_model=List[MinistryUpdate])
def read_ministry_updates(db: SessionLocal = Depends(get_db)):
    updates = db.query(MinistryUpdateModel).all()
    return [{"id": u.id, "title": u.title, "content": u.content} for u in updates]

# Ministry update endpoint
@app.get("/ministry_updates/{update_id}", response_model=MinistryUpdate)
def read_ministry_update(update_id: int, db: SessionLocal = Depends(get_db)):
    update = db.query(MinistryUpdateModel).filter(MinistryUpdateModel.id == update_id).first()
    if update is None:
        raise HTTPException(status_code=404, detail="Ministry update not found")
    return {"id": update.id, "title": update.title, "content": update.content}

# Create ministry update endpoint
@app.post("/ministry_updates/", response_model=MinistryUpdate)
def create_ministry_update(update: MinistryUpdate, db: SessionLocal = Depends(get_db)):
    db_update = MinistryUpdateModel(title=update.title, content=update.content)
    db.add(db_update)
    db.commit()
    db.refresh(db_update)
    return {"id": db_update.id, "title": db_update.title, "content": db_update.content}
```

```python
# main.py
import uvicorn
from app import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
