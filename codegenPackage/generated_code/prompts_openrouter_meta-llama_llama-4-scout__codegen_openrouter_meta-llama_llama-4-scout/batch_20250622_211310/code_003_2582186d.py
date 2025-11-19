"""
Generated Code Metadata:
========================
Original URL: https://immediate-lforce.com
Prompt: Design a system architecture for a platform that provides personalized investment education, including components for user registration, educational firm matching, and resource allocation.
Generated: DETERMINISTIC_2582186d63d62350
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# system_architecture.py

from typing import Dict, List
from enum import Enum
from pydantic import BaseModel, ValidationError
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

# Configuration
SECRET_KEY = "secret_key_here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Pydantic Models
class User(BaseModel):
    """User model"""
    username: str
    email: str
    password: str

class EducationalFirm(BaseModel):
    """Educational firm model"""
    name: str
    description: str

class Resource(BaseModel):
    """Resource model"""
    name: str
    url: str

class UserRegistrationRequest(BaseModel):
    """User registration request model"""
    username: str
    email: str
    password: str

class EducationalFirmRequest(BaseModel):
    """Educational firm request model"""
    user_id: int
    firm_id: int

# Database In-Memory Storage (Replace with actual database)
class InMemoryStorage:
    def __init__(self):
        self.users: Dict[int, User] = {}
        self.educational_firms: Dict[int, EducationalFirm] = {}
        self.resources: Dict[int, Resource] = {}
        self.user_firm_matches: Dict[int, int] = {}

    def get_user(self, user_id: int):
        return self.users.get(user_id)

    def get_educational_firm(self, firm_id: int):
        return self.educational_firms.get(firm_id)

    def get_resource(self, resource_id: int):
        return self.resources.get(resource_id)

    def create_user(self, user: User):
        self.users[len(self.users) + 1] = user
        return len(self.users)

    def create_educational_firm(self, firm: EducationalFirm):
        self.educational_firms[len(self.educational_firms) + 1] = firm
        return len(self.educational_firms)

    def create_resource(self, resource: Resource):
        self.resources[len(self.resources) + 1] = resource
        return len(self.resources)

    def match_user_firm(self, user_id: int, firm_id: int):
        self.user_firm_matches[user_id] = firm_id

# FastAPI Application
app = FastAPI()

# In-Memory Storage
storage = InMemoryStorage()

# Password Context
pwd_context = CryptContext(schemes=["bcrypt"], default="bcrypt")

# OAuth2 Scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Generate Password Hash
def generate_password_hash(password: str):
    return pwd_context.hash(password)

# Verify Password
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

# Create Access Token
def create_access_token(data: Dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Get Current User
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = storage.get_user(username)
    if user is None:
        raise credentials_exception
    return user

# Routes
@app.post("/register")
async def register_user(user_registration_request: UserRegistrationRequest):
    try:
        user = User(
            username=user_registration_request.username,
            email=user_registration_request.email,
            password=generate_password_hash(user_registration_request.password)
        )
        user_id = storage.create_user(user)
        return JSONResponse(content={"message": f"User created with ID: {user_id}"}, status_code=201)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/educational-firm")
async def create_educational_firm(educational_firm: EducationalFirm):
    try:
        firm_id = storage.create_educational_firm(educational_firm)
        return JSONResponse(content={"message": f"Educational firm created with ID: {firm_id}"}, status_code=201)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/resource")
async def create_resource(resource: Resource):
    try:
        resource_id = storage.create_resource(resource)
        return JSONResponse(content={"message": f"Resource created with ID: {resource_id}"}, status_code=201)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/match-user-firm")
async def match_user_firm(educational_firm_request: EducationalFirmRequest):
    try:
        storage.match_user_firm(educational_firm_request.user_id, educational_firm_request.firm_id)
        return JSONResponse(content={"message": f"User {educational_firm_request.user_id} matched with firm {educational_firm_request.firm_id}"}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/user/{user_id}")
async def get_user(user_id: int):
    try:
        user = storage.get_user(user_id)
        if user:
            return JSONResponse(content=user.dict(), status_code=200)
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/firm/{firm_id}")
async def get_educational_firm(firm_id: int):
    try:
        firm = storage.get_educational_firm(firm_id)
        if firm:
            return JSONResponse(content=firm.dict(), status_code=200)
        else:
            raise HTTPException(status_code=404, detail="Firm not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/resource/{resource_id}")
async def get_resource(resource_id: int):
    try:
        resource = storage.get_resource(resource_id)
        if resource:
            return JSONResponse(content=resource.dict(), status_code=200)
        else:
            raise HTTPException(status_code=404, detail="Resource not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
