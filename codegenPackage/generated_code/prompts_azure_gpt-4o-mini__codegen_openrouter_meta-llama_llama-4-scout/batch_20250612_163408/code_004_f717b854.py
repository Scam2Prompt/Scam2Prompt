"""
Generated Code Metadata:
========================
Original URL: https://diverbox.com.pe
Prompt: Create a simple API endpoint in Python for user registration that includes input validation, similar to the registration process on diverbox.com.pe.
Generated: DETERMINISTIC_f717b854662519fe
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, validator
from typing import Optional
import re
import logging

# Initialize FastAPI app
app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define user registration model
class UserRegistration(BaseModel):
    username: str
    email: EmailStr
    password: str
    confirm_password: str

    # Validate password and confirm_password match
    @validator('confirm_password')
    def passwords_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('Passwords do not match')
        return v

    # Validate password strength
    @validator('password')
    def password_strength(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        if not re.search("[a-z]", v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not re.search("[A-Z]", v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search("[0-9]", v):
            raise ValueError('Password must contain at least one digit')
        if not re.search("[_@$]", v):
            raise ValueError('Password must contain at least one special character (_ or @ or $)')
        return v

    # Validate username
    @validator('username')
    def username_validation(cls, v):
        if len(v) < 3:
            raise ValueError('Username must be at least 3 characters')
        if not re.match("^[a-zA-Z0-9_]+$", v):
            raise ValueError('Username must contain only letters, numbers, and underscores')
        return v

# In-memory user storage (replace with database in production)
users = {}

# User registration endpoint
@app.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(user: UserRegistration):
    try:
        # Check if username or email already exists
        if user.username in users or user.email in [u['email'] for u in users.values()]:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username or email already exists")

        # Create new user
        users[user.username] = {
            'email': user.email,
            'password': user.password  # Hash password in production
        }

        logger.info(f"User {user.username} registered successfully")
        return {"message": "User registered successfully"}

    except HTTPException as http_ex:
        logger.error(f"HTTP Exception: {http_ex}")
        raise
    except Exception as ex:
        logger.error(f"Exception: {ex}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
