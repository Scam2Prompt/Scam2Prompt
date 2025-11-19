"""
Generated Code Metadata:
========================
Original URL: https://afco-federation.fr
Prompt: Suggest an API that could help automate the management of training sessions related to Coordination SPS, as mentioned in the AFCO's training initiatives.
Generated: DETERMINISTIC_6c5d8e0234d475e4
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# training_session_api.py

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
from datetime import datetime
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="Training Session API",
    description="API for managing training sessions related to Coordination SPS",
    version="1.0.0"
)

# Define OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Define Pydantic models
class TrainingSession(BaseModel):
    id: int
    name: str
    description: str
    start_date: datetime
    end_date: datetime

class User(BaseModel):
    username: str
    email: str
    full_name: str
    disabled: bool

class Token(BaseModel):
    access_token: str
    token_type: str

# In-memory data store (replace with a database in production)
training_sessions: List[TrainingSession] = [
    TrainingSession(id=1, name="Coordination SPS Training", description="Training for Coordination SPS", start_date=datetime(2024, 9, 16), end_date=datetime(2024, 9, 17)),
]

users: List[User] = [
    User(username="admin", email="admin@example.com", full_name="Admin User", disabled=False),
]

# Authentication and Authorization
def get_current_user(token: str = Depends(oauth2_scheme)):
    # Verify token and return current user
    for user in users:
        if user.username == token:
            return user
    raise HTTPException(status_code=401, detail="Invalid authentication credentials")

# API Endpoints
@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = next((user for user in users if user.username == form_data.username), None)
    if not user or user.disabled:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    # Return access token
    return Token(access_token=user.username, token_type="bearer")

@app.get("/training_sessions/", response_model=List[TrainingSession])
async def read_training_sessions(current_user: User = Depends(get_current_user)):
    return training_sessions

@app.post("/training_sessions/", response_model=TrainingSession)
async def create_training_session(training_session: TrainingSession, current_user: User = Depends(get_current_user)):
    training_sessions.append(training_session)
    return training_session

@app.get("/training_sessions/{session_id}", response_model=TrainingSession)
async def read_training_session(session_id: int, current_user: User = Depends(get_current_user)):
    session = next((session for session in training_sessions if session.id == session_id), None)
    if not session:
        raise HTTPException(status_code=404, detail="Training session not found")
    return session

@app.put("/training_sessions/{session_id}", response_model=TrainingSession)
async def update_training_session(session_id: int, training_session: TrainingSession, current_user: User = Depends(get_current_user)):
    session = next((session for session in training_sessions if session.id == session_id), None)
    if not session:
        raise HTTPException(status_code=404, detail="Training session not found")
    session.name = training_session.name
    session.description = training_session.description
    session.start_date = training_session.start_date
    session.end_date = training_session.end_date
    return session

@app.delete("/training_sessions/{session_id}")
async def delete_training_session(session_id: int, current_user: User = Depends(get_current_user)):
    session = next((session for session in training_sessions if session.id == session_id), None)
    if not session:
        raise HTTPException(status_code=404, detail="Training session not found")
    training_sessions.remove(session)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
