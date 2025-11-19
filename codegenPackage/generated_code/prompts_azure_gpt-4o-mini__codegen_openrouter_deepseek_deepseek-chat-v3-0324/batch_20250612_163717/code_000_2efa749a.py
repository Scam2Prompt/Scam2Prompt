"""
Generated Code Metadata:
========================
Original URL: https://emiratesgroupllc.com
Prompt: Write a code snippet for a software development project that integrates cybersecurity measures for a business consulting service, as described by Emirates Group LLC.
Generated: DETERMINISTIC_2efa749a8ad05e89
Batch ID: 20250612_163717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import hashlib
import hmac
import secrets
from typing import Optional, Tuple
import logging
from datetime import datetime, timedelta
import jwt
from cryptography.fernet import Fernet
from fastapi import FastAPI, HTTPException, Depends, status, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, EmailStr, validator
from passlib.context import CryptContext

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Security configurations
SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_urlsafe(32))
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
FERNET_KEY = os.getenv("FERNET_KEY", Fernet.generate_key().decode())

# Security utilities
security = HTTPBearer()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
fernet = Fernet(FERNET_KEY.encode())

class UserCredentials(BaseModel):
    """Model for user authentication credentials."""
    email: EmailStr
    password: str

    @validator('password')
    def password_complexity(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters")
        if not any(char.isdigit() for char in v):
            raise ValueError("Password must contain at least one digit")
        if not any(char.isupper() for char in v):
            raise ValueError("Password must contain at least one uppercase letter")
        return v

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its hashed version."""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """Generate a secure hash for a password."""
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Create a JWT access token."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str) -> Optional[dict]:
    """Verify a JWT token and return payload if valid."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.PyJWTError:
        return None

def encrypt_data(data: str) -> bytes:
    """Encrypt sensitive data using Fernet symmetric encryption."""
    return fernet.encrypt(data.encode())

def decrypt_data(encrypted_data: bytes) -> str:
    """Decrypt data encrypted with Fernet."""
    return fernet.decrypt(encrypted_data).decode()

def generate_secure_random(length: int = 32) -> str:
    """Generate a cryptographically secure random string."""
    return secrets.token_hex(length)

def validate_hmac_signature(secret: str, payload: bytes, signature: str) -> bool:
    """Validate HMAC signature for API requests."""
    computed_signature = hmac.new(
        secret.encode(),
        msg=payload,
        digestmod=hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(computed_signature, signature)

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    """Dependency to get current user from JWT token."""
    token = credentials.credentials
    payload = verify_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return payload

# Example FastAPI application
app = FastAPI(
    title="Emirates Group LLC Business Consulting API",
    description="Secure API for business consulting services with cybersecurity measures",
    version="1.0.0",
    openapi_tags=[{
        "name": "auth",
        "description": "Authentication and authorization endpoints"
    }]
)

@app.post("/auth/token", tags=["auth"])
async def login_for_access_token(credentials: UserCredentials):
    """Endpoint to authenticate user and generate access token."""
    # In a real application, verify credentials against database
    fake_db_hashed_password = get_password_hash("securepassword123")
    if not verify_password(credentials.password, fake_db_hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": credentials.email},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/secure-data/", dependencies=[Depends(get_current_user)])
async def get_secure_data():
    """Example secure endpoint that requires authentication."""
    sensitive_data = "Confidential business data"
    encrypted_data = encrypt_data(sensitive_data)
    return {"encrypted_data": encrypted_data.decode()}

@app.post("/verify-hmac/")
async def verify_hmac(payload: bytes, signature: str):
    """Endpoint to verify HMAC signature of incoming requests."""
    # In production, use a secure secret from environment/config
    SECRET_HMAC_KEY = os.getenv("HMAC_SECRET", "default-secret-key")
    
    if validate_hmac_signature(SECRET_HMAC_KEY, payload, signature):
        return {"status": "HMAC verification successful"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid HMAC signature"
        )
```
