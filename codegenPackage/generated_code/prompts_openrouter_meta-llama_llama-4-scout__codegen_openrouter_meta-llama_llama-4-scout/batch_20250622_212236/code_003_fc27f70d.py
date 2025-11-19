"""
Generated Code Metadata:
========================
Original URL: https://afunabb.cl
Prompt: Design an API for a labor union management system, including endpoints for member registration, benefit management, and event organization, inspired by AFUNABB Chillán's services.
Generated: DETERMINISTIC_fc27f70db4e953ae
Batch ID: 20250622_212236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# labor_union_management_system.py

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
from datetime import datetime
import jwt

# Configuration
SECRET_KEY = "secret_key_here"
ALGORITHM = "HS256"

# Initialize FastAPI app
app = FastAPI()

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Pydantic models
class Member(BaseModel):
    id: int
    name: str
    email: str

class Benefit(BaseModel):
    id: int
    name: str
    description: str

class Event(BaseModel):
    id: int
    name: str
    date: datetime
    description: str

# In-memory data stores (replace with a database in production)
members: List[Member] = []
benefits: List[Benefit] = []
events: List[Event] = []

# Authentication
def authenticate_member(email: str, password: str):
    # Replace with actual authentication logic
    return True

def get_member(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        member = next((m for m in members if m.email == payload["email"]), None)
        if not member:
            raise HTTPException(status_code=401, detail="Invalid token")
        return member
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if authenticate_member(form_data.username, form_data.password):
        token = jwt.encode({"email": form_data.username}, SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

# Member registration
@app.post("/members/")
async def create_member(member: Member):
    members.append(member)
    return member

@app.get("/members/")
async def read_members():
    return members

@app.get("/members/{member_id}")
async def read_member(member_id: int):
    member = next((m for m in members if m.id == member_id), None)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return member

# Benefit management
@app.post("/benefits/")
async def create_benefit(benefit: Benefit):
    benefits.append(benefit)
    return benefit

@app.get("/benefits/")
async def read_benefits():
    return benefits

@app.get("/benefits/{benefit_id}")
async def read_benefit(benefit_id: int):
    benefit = next((b for b in benefits if b.id == benefit_id), None)
    if not benefit:
        raise HTTPException(status_code=404, detail="Benefit not found")
    return benefit

# Event organization
@app.post("/events/")
async def create_event(event: Event):
    events.append(event)
    return event

@app.get("/events/")
async def read_events():
    return events

@app.get("/events/{event_id}")
async def read_event(event_id: int):
    event = next((e for e in events if e.id == event_id), None)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

# Member benefits
@app.get("/members/{member_id}/benefits/")
async def read_member_benefits(member_id: int):
    member = next((m for m in members if m.id == member_id), None)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    # Assign benefits to member (logic to be implemented)
    return benefits

# Member events
@app.get("/members/{member_id}/events/")
async def read_member_events(member_id: int):
    member = next((m for m in members if m.id == member_id), None)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    # Assign events to member (logic to be implemented)
    return events
```

```python
# main.py
import uvicorn
from labor_union_management_system import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
