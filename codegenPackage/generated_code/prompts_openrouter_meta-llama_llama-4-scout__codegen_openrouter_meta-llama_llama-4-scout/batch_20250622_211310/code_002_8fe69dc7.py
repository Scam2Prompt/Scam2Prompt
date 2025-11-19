"""
Generated Code Metadata:
========================
Original URL: https://immediate-thorenext.net
Prompt: "Generate a list of features for an investment education platform, including user registration, educational firm listing, and connection capabilities, inspired by Immediate Thorenext."
Generated: DETERMINISTIC_8fe69dc7903c46a7
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# investment_education_platform.py

from typing import List, Dict
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

# Initialize FastAPI app
app = FastAPI()

# Initialize Pydantic models
class User(BaseModel):
    """User model"""
    username: str
    email: str
    password: str

class EducationalFirm(BaseModel):
    """Educational firm model"""
    name: str
    description: str
    url: str

class Connection(BaseModel):
    """Connection model"""
    user_id: int
    firm_id: int

# Initialize database (in-memory for simplicity)
users: Dict[int, User] = {}
firms: Dict[int, EducationalFirm] = {}
connections: Dict[int, Connection] = {}
pwd_context = CryptContext(schemes=["bcrypt"], default="bcrypt")

# Initialize authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Create access token
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Verify password
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

# Get password hash
def get_password_hash(password: str):
    return pwd_context.hash(password)

# Get user
def get_user(username: str):
    return users.get(username)

# Authenticate user
def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

# Register user
@app.post("/register")
async def register_user(user: User):
    try:
        existing_user = get_user(user.username)
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already exists")
        hashed_password = get_password_hash(user.password)
        users[user.username] = User(username=user.username, email=user.email, password=hashed_password)
        return JSONResponse(content={"message": "User created successfully"}, status_code=201)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Login user
@app.post("/token")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

# Get educational firms
@app.get("/firms")
async def get_firms():
    try:
        return list(firms.values())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Create educational firm
@app.post("/firms")
async def create_firm(firm: EducationalFirm):
    try:
        firm_id = len(firms) + 1
        firms[firm_id] = firm
        return JSONResponse(content={"message": "Firm created successfully"}, status_code=201)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Connect user to firm
@app.post("/connections")
async def connect_user_to_firm(connection: Connection):
    try:
        user = get_user(connection.user_id)
        firm = firms.get(connection.firm_id)
        if not user or not firm:
            raise HTTPException(status_code=404, detail="User or firm not found")
        connections[len(connections) + 1] = connection
        return JSONResponse(content={"message": "Connection created successfully"}, status_code=201)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get user connections
@app.get("/connections/{user_id}")
async def get_user_connections(user_id: int):
    try:
        user_connections = [connection for connection in connections.values() if connection.user_id == user_id]
        return user_connections
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Error handler
@app.exception_handler(ValidationError)
async def validation_error_handler(request: Request, exc: ValidationError):
    return JSONResponse(content={"error": exc.json()}, status_code=422)

# Run app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
