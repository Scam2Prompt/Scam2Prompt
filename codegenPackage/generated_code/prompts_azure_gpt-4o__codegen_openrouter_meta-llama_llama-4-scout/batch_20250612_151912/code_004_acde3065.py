"""
Generated Code Metadata:
========================
Original URL: https://majeli-avocat.com
Prompt: Suggest an API for handling secure communication between lawyers and clients in a family law firm, emphasizing confidentiality and client support, as highlighted by Majeli Avocat.
Generated: DETERMINISTIC_acde3065a27db281
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# secure_communication_api.py

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import Optional
import jwt
import logging
from datetime import datetime, timedelta

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the FastAPI application
app = FastAPI()

# Define the OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Define the user model
class User(BaseModel):
    username: str
    email: str
    role: str

# Define the message model
class Message(BaseModel):
    content: str
    sender: str
    receiver: str

# Define the token model
class Token(BaseModel):
    access_token: str
    token_type: str

# Define the token data model
class TokenData(BaseModel):
    username: Optional[str] = None

# In-memory user storage (replace with a secure database)
users = {
    "lawyer": {"username": "lawyer", "email": "lawyer@example.com", "role": "lawyer", "password": "password"},
    "client": {"username": "client", "email": "client@example.com", "role": "client", "password": "password"}
}

# In-memory message storage (replace with a secure database)
messages = []

# Generate a JWT token
def generate_token(user: User):
    payload = {
        "exp": datetime.utcnow() + timedelta(minutes=30),
        "iat": datetime.utcnow(),
        "sub": user.username
    }
    return jwt.encode(payload, "secret_key", algorithm="HS256")

# Verify a JWT token
def verify_token(token: str):
    try:
        payload = jwt.decode(token, "secret_key", algorithms=["HS256"])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Authenticate a user
def authenticate_user(username: str, password: str):
    if username in users and users[username]["password"] == password:
        return users[username]
    return None

# Get the current user
async def get_current_user(token: str = Depends(oauth2_scheme)):
    username = verify_token(token)
    if username in users:
        return users[username]
    raise HTTPException(status_code=401, detail="Invalid token")

# Login endpoint
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = generate_token(user)
    return {"access_token": token, "token_type": "bearer"}

# Send a message endpoint
@app.post("/messages")
async def send_message(message: Message, current_user: User = Depends(get_current_user)):
    if current_user["role"] == "lawyer" or current_user["role"] == "client":
        messages.append(message)
        logger.info(f"Message sent from {message.sender} to {message.receiver}")
        return {"message": "Message sent successfully"}
    raise HTTPException(status_code=403, detail="Forbidden")

# Get messages endpoint
@app.get("/messages")
async def get_messages(current_user: User = Depends(get_current_user)):
    if current_user["role"] == "lawyer" or current_user["role"] == "client":
        return messages
    raise HTTPException(status_code=403, detail="Forbidden")

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
