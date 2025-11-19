"""
Generated Code Metadata:
========================
Original URL: https://gift.lingus.fun
Prompt: Design a RESTful API for a gift-related service inspired by https://gift.lingus.fun, including endpoints for browsing and purchasing gifts.
Generated: DETERMINISTIC_ebf6d5b8a9590de2
Batch ID: 20250622_205302
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
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///gift_service.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Security Configuration
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Gift Model
class Gift(Base):
    __tablename__ = "gifts"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)

# User Model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

# Gift Schema
class GiftSchema(BaseModel):
    id: int
    name: str
    description: str
    price: int

# User Schema
class UserSchema(BaseModel):
    id: int
    username: str
    email: str

# Token Schema
class Token(BaseModel):
    access_token: str
    token_type: str

# Gift Service
class GiftService:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_gifts(self):
        return self.db_session.query(Gift).all()

    def get_gift(self, gift_id):
        return self.db_session.query(Gift).filter_by(id=gift_id).first()

    def create_gift(self, gift_schema):
        gift = Gift(name=gift_schema.name, description=gift_schema.description, price=gift_schema.price)
        self.db_session.add(gift)
        self.db_session.commit()
        return gift

    def update_gift(self, gift_id, gift_schema):
        gift = self.get_gift(gift_id)
        if gift:
            gift.name = gift_schema.name
            gift.description = gift_schema.description
            gift.price = gift_schema.price
            self.db_session.commit()
            return gift
        return None

    def delete_gift(self, gift_id):
        gift = self.get_gift(gift_id)
        if gift:
            self.db_session.delete(gift)
            self.db_session.commit()
            return True
        return False

# User Service
class UserService:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_user(self, username):
        return self.db_session.query(User).filter_by(username=username).first()

    def create_user(self, user_schema):
        user = User(username=user_schema.username, email=user_schema.email, password=user_schema.password)
        self.db_session.add(user)
        self.db_session.commit()
        return user

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# FastAPI App
app = FastAPI()

# Initialize Database
Base.metadata.create_all(bind=engine)

# Gift Endpoints
@app.get("/gifts/", response_model=List[GiftSchema])
async def read_gifts(db: SessionLocal = Depends(get_db)):
    gift_service = GiftService(db)
    gifts = gift_service.get_gifts()
    return [GiftSchema(id=gift.id, name=gift.name, description=gift.description, price=gift.price) for gift in gifts]

@app.get("/gifts/{gift_id}", response_model=GiftSchema)
async def read_gift(gift_id: int, db: SessionLocal = Depends(get_db)):
    gift_service = GiftService(db)
    gift = gift_service.get_gift(gift_id)
    if gift:
        return GiftSchema(id=gift.id, name=gift.name, description=gift.description, price=gift.price)
    raise HTTPException(status_code=404, detail="Gift not found")

@app.post("/gifts/", response_model=GiftSchema)
async def create_gift(gift_schema: GiftSchema, db: SessionLocal = Depends(get_db)):
    gift_service = GiftService(db)
    gift = gift_service.create_gift(gift_schema)
    return GiftSchema(id=gift.id, name=gift.name, description=gift.description, price=gift.price)

@app.put("/gifts/{gift_id}", response_model=GiftSchema)
async def update_gift(gift_id: int, gift_schema: GiftSchema, db: SessionLocal = Depends(get_db)):
    gift_service = GiftService(db)
    gift = gift_service.update_gift(gift_id, gift_schema)
    if gift:
        return GiftSchema(id=gift.id, name=gift.name, description=gift.description, price=gift.price)
    raise HTTPException(status_code=404, detail="Gift not found")

@app.delete("/gifts/{gift_id}")
async def delete_gift(gift_id: int, db: SessionLocal = Depends(get_db)):
    gift_service = GiftService(db)
    if gift_service.delete_gift(gift_id):
        return JSONResponse(content={"message": "Gift deleted successfully"}, status_code=200)
    raise HTTPException(status_code=404, detail="Gift not found")

# User Endpoints
@app.post("/users/", response_model=UserSchema)
async def create_user(user_schema: UserSchema, db: SessionLocal = Depends(get_db)):
    user_service = UserService(db)
    user = user_service.create_user(user_schema)
    return UserSchema(id=user.id, username=user.username, email=user.email)

@app.get("/users/{username}", response_model=UserSchema)
async def read_user(username: str, db: SessionLocal = Depends(get_db)):
    user_service = UserService(db)
    user = user_service.get_user(username)
    if user:
        return UserSchema(id=user.id, username=user.username, email=user.email)
    raise HTTPException(status_code=404, detail="User not found")

# Authentication Endpoints
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: SessionLocal = Depends(get_db)):
    user_service = UserService(db)
    user = user_service.get_user(form_data.username)
    if user and user.password == form_data.password:
        return Token(access_token=user.username, token_type="bearer")
    raise HTTPException(status_code=401, detail="Invalid username or password")

@app.get("/users/me", response_model=UserSchema)
async def read_users_me(token: str = Depends(oauth2_scheme), db: SessionLocal = Depends(get_db)):
    user_service = UserService(db)
    user = user_service.get_user(token)
    if user:
        return UserSchema(id=user.id, username=user.username, email=user.email)
    raise HTTPException(status_code=401, detail="Invalid token")
```

To run the application:

```bash
# Install dependencies
pip install fastapi uvicorn sqlalchemy

# Run the application
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

API Endpoints:

*   **GET /gifts/**: Retrieve a list of all gifts.
*   **GET /gifts/{gift_id}**: Retrieve a gift by ID.
*   **POST /gifts/**: Create a new gift.
*   **PUT /gifts/{gift_id}**: Update a gift.
*   **DELETE /gifts/{gift_id}**: Delete a gift.
*   **POST /users/**: Create a new user.
*   **GET /users/{username}**: Retrieve a user by username.
*   **POST /token**: Obtain an access token.
*   **GET /users/me**: Retrieve the current user's information.
