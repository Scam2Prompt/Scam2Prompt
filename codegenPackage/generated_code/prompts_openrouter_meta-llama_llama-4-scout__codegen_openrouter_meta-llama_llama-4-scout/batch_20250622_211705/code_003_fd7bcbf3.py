"""
Generated Code Metadata:
========================
Original URL: https://connectsync.org
Prompt: Design a basic API for managing subscriptions and sending updates to users for a product like Connect Sync.
Generated: DETERMINISTIC_fd7bcbf366bbedbf
Batch ID: 20250622_211705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# subscription_api.py

from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
from datetime import datetime
import jwt
import secrets

# Configuration
SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = "HS256"

# Initialize FastAPI app
app = FastAPI()

# Define OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Define Pydantic models
class User(BaseModel):
    username: str
    email: str

class Subscription(BaseModel):
    user_id: int
    product_id: int
    expires_at: datetime

class Update(BaseModel):
    product_id: int
    message: str

# In-memory data store (replace with a database in production)
users: List[User] = []
subscriptions: List[Subscription] = []
updates: List[Update] = []

# Authentication functions
def authenticate_user(username: str, password: str):
    # Replace with actual authentication logic
    for user in users:
        if user.username == username and password == "password":  # Hardcoded password for demo
            return user
    return None

def create_access_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# API Endpoints
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = next((user for user in users if user.username == payload["sub"]), None)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/subscriptions")
async def create_subscription(subscription: Subscription, token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = next((user for user in users if user.username == payload["sub"]), None)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid token")
        subscriptions.append(subscription)
        return JSONResponse(content={"message": "Subscription created successfully"}, status_code=201)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/subscriptions")
async def read_subscriptions(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = next((user for user in users if user.username == payload["sub"]), None)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid token")
        return subscriptions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/updates")
async def send_update(update: Update):
    try:
        updates.append(update)
        return JSONResponse(content={"message": "Update sent successfully"}, status_code=201)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/updates")
async def read_updates(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = next((user for user in users if user.username == payload["sub"]), None)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid token")
        return updates
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
