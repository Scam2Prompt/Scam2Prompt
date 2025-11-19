"""
Generated Code Metadata:
========================
Original URL: https://finance-masa.pages.dev
Prompt: "Develop a simple backend API to handle user data preferences, specifically for opting in or out of various cookie categories, and storing these preferences securely."
Generated: DETERMINISTIC_51d017a95d832b5d
Batch ID: 20250622_210802
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
import uvicorn
import jwt
import secrets
from datetime import datetime, timedelta

# Configuration
SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = "HS256"

# Initialize FastAPI app
app = FastAPI()

# Define Pydantic models
class CookieCategory(BaseModel):
    name: str
    opted_in: bool

class UserPreferences(BaseModel):
    cookie_categories: List[CookieCategory]

class Token(BaseModel):
    access_token: str
    token_type: str

# In-memory user database (replace with a real database)
users = {}

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Generate JWT token
def generate_token(user_id: str):
    payload = {
        "sub": user_id,
        "exp": datetime.utcnow() + timedelta(minutes=30)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

# Verify JWT token
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Get current user
async def get_current_user(token: str = Depends(oauth2_scheme)):
    user_id = verify_token(token)
    if user_id not in users:
        raise HTTPException(status_code=401, detail="User not found")
    return user_id

# Create a new user
@app.post("/users/")
async def create_user(username: str, password: str):
    if username in users:
        raise HTTPException(status_code=400, detail="Username already exists")
    users[username] = {"password": password, "preferences": []}
    return {"message": "User created successfully"}

# Login and obtain token
@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users.get(form_data.username)
    if not user or user["password"] != form_data.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = generate_token(form_data.username)
    return {"access_token": token, "token_type": "bearer"}

# Update user preferences
@app.patch("/users/preferences", response_model=UserPreferences)
async def update_preferences(preferences: UserPreferences, current_user: str = Depends(get_current_user)):
    users[current_user]["preferences"] = [{"name": pref.name, "opted_in": pref.opted_in} for pref in preferences.cookie_categories]
    return preferences

# Get user preferences
@app.get("/users/preferences", response_model=UserPreferences)
async def get_preferences(current_user: str = Depends(get_current_user)):
    user = users[current_user]
    return {"cookie_categories": user["preferences"]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# requirements.txt
fastapi
uvicorn
pydantic
pyjwt
```

```bash
# Run with: uvicorn app:app --host 0.0.0.0 --port 8000
```
