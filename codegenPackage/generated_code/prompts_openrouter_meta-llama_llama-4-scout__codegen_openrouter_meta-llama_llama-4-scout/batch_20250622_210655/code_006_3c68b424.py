"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: "Develop a Python API to handle requests and responses for a fire safety service company's customer portal."
Generated: DETERMINISTIC_3c68b424dee2a927
Batch ID: 20250622_210655
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
from typing import Optional
import uvicorn
from datetime import datetime, timedelta
import jwt

# Configuration
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Initialize FastAPI app
app = FastAPI()

# Define OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Define Pydantic models
class Customer(BaseModel):
    id: int
    name: str
    email: str

class ServiceRequest(BaseModel):
    customer_id: int
    description: str
    status: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# In-memory data store (replace with a database in production)
customers = [
    Customer(id=1, name="John Doe", email="john@example.com"),
    Customer(id=2, name="Jane Doe", email="jane@example.com"),
]

service_requests = []

# Authentication functions
def verify_password(plain_password: str, hashed_password: str):
    # For simplicity, we assume passwords are not hashed in this example
    return plain_password == hashed_password

def get_password_hash(password: str):
    # For simplicity, we assume passwords are not hashed in this example
    return password

def authenticate_customer(email: str, password: str):
    customer = next((c for c in customers if c.email == email), None)
    if not customer:
        return False
    if not verify_password(password, get_password_hash(password)):
        return False
    return customer

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Dependency to get current customer
async def get_current_customer(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except jwt.ExpiredSignatureError:
        raise credentials_exception
    except jwt.InvalidTokenError:
        raise credentials_exception
    customer = next((c for c in customers if c.email == token_data.username), None)
    if customer is None:
        raise credentials_exception
    return customer

# API Endpoints
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    customer = authenticate_customer(form_data.username, form_data.password)
    if not customer:
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": customer.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/customers/me", response_model=Customer)
async def read_customers_me(current_customer: Customer = Depends(get_current_customer)):
    return current_customer

@app.post("/service_requests/", response_model=ServiceRequest)
async def create_service_request(service_request: ServiceRequest, current_customer: Customer = Depends(get_current_customer)):
    service_requests.append(service_request)
    return service_request

@app.get("/service_requests/", response_model=list[ServiceRequest])
async def read_service_requests(current_customer: Customer = Depends(get_current_customer)):
    return service_requests

@app.get("/service_requests/{request_id}", response_model=ServiceRequest)
async def read_service_request(request_id: int, current_customer: Customer = Depends(get_current_customer)):
    request = next((r for r in service_requests if r.customer_id == current_customer.id and r.description == f"Request {request_id}"), None)
    if request is None:
        raise HTTPException(status_code=404, detail="Service request not found")
    return request

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
