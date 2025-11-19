"""
Generated Code Metadata:
========================
Original URL: https://jobbo.com.au
Prompt: "Suggest a set of features and functionalities for a mobile app aimed at connecting tractor pulling enthusiasts, inspired by the community aspects of jobbo.com.au."
Generated: DETERMINISTIC_e24efa46b3a0aca5
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tractor_pulling_app.py

"""
Tractor Pulling App API

Inspired by the community aspects of jobbo.com.au, this mobile app aims to connect tractor pulling enthusiasts.

Endpoints:
    - Register user
    - Login user
    - Create event
    - Get events
    - Join event
    - Get user events
"""

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
from datetime import datetime

# Initialize FastAPI app
app = FastAPI()

# Define OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Define Pydantic models
class User(BaseModel):
    """User model"""
    id: int
    username: str
    email: str

class Event(BaseModel):
    """Event model"""
    id: int
    name: str
    date: datetime
    location: str
    users: List[User]

class UserEvent(BaseModel):
    """User event model"""
    user_id: int
    event_id: int

# In-memory data store (replace with database in production)
users = []
events = []
user_events = []

# Register user endpoint
@app.post("/register")
async def register_user(username: str, email: str, password: str):
    """
    Register a new user.

    Args:
    - username (str): Username chosen by the user.
    - email (str): User's email address.
    - password (str): User's password.

    Returns:
    - User: The newly created user.
    """
    new_user = User(id=len(users) + 1, username=username, email=email)
    users.append(new_user)
    return new_user

# Login user endpoint
@app.post("/token")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Login an existing user.

    Args:
    - form_data (OAuth2PasswordRequestForm): Username and password.

    Returns:
    - token (str): Authentication token.
    """
    user = next((user for user in users if user.username == form_data.username), None)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    # In a real app, use a secure method to verify the password
    token = "example_token"
    return {"access_token": token, "token_type": "bearer"}

# Create event endpoint
@app.post("/events")
async def create_event(name: str, date: datetime, location: str, token: str = Depends(oauth2_scheme)):
    """
    Create a new event.

    Args:
    - name (str): Event name.
    - date (datetime): Event date and time.
    - location (str): Event location.
    - token (str): Authentication token.

    Returns:
    - Event: The newly created event.
    """
    new_event = Event(id=len(events) + 1, name=name, date=date, location=location, users=[])
    events.append(new_event)
    return new_event

# Get events endpoint
@app.get("/events")
async def get_events():
    """
    Get a list of all events.

    Returns:
    - List[Event]: List of events.
    """
    return events

# Join event endpoint
@app.post("/events/{event_id}/join")
async def join_event(event_id: int, token: str = Depends(oauth2_scheme)):
    """
    Join an event.

    Args:
    - event_id (int): ID of the event to join.
    - token (str): Authentication token.

    Returns:
    - Event: The event with the joined user.
    """
    event = next((event for event in events if event.id == event_id), None)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    # Get the current user from the token (replace with actual user retrieval)
    user = next((user for user in users), None)
    event.users.append(user)
    user_event = UserEvent(user_id=user.id, event_id=event_id)
    user_events.append(user_event)
    return event

# Get user events endpoint
@app.get("/users/me/events")
async def get_user_events(token: str = Depends(oauth2_scheme)):
    """
    Get a list of events joined by the current user.

    Args:
    - token (str): Authentication token.

    Returns:
    - List[Event]: List of events joined by the user.
    """
    # Get the current user from the token (replace with actual user retrieval)
    user = next((user for user in users), None)
    user_event_ids = [ue.event_id for ue in user_events if ue.user_id == user.id]
    user_events = [event for event in events if event.id in user_event_ids]
    return user_events
```
