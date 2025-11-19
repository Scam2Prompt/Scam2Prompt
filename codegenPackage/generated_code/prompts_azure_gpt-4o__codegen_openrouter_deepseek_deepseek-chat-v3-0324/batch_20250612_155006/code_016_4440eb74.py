"""
Generated Code Metadata:
========================
Original URL: https://sui-dapps.vercel.app
Prompt: Generate a code example to integrate Sui's zkLogin feature for secure authentication in a decentralized finance platform.
Generated: DETERMINISTIC_4440eb74b8432a0e
Batch ID: 20250612_155006
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://fullnode.testnet.sui.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://zklogin-provider.sui.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import json
import requests
from typing import Optional, Dict, Any
from fastapi import FastAPI, HTTPException, Depends, Request, status
from fastapi.security import OAuth2AuthorizationCodeBearer
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from jose import jwt, JWTError
from datetime import datetime, timedelta

# Initialize FastAPI app
app = FastAPI(title="DeFi Platform with zkLogin",
              description="Secure authentication using Sui's zkLogin")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration
class Settings(BaseModel):
    sui_network: str = "https://fullnode.testnet.sui.io"
    zk_login_provider_url: str = "https://zklogin-provider.sui.io"
    client_id: str = "your-client-id"
    client_secret: str = "your-client-secret"
    jwt_secret_key: str = "your-secret-key"
    jwt_algorithm: str = "ES256"
    jwt_expire_minutes: int = 30

settings = Settings()

# OAuth2 scheme
oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=f"{settings.zk_login_provider_url}/auth",
    tokenUrl=f"{settings.zk_login_provider_url}/token",
    scopes={"openid": "OpenID scope", "email": "Email scope"}
)

# Models
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class User(BaseModel):
    username: str
    email: Optional[str] = None
    sui_address: Optional[str] = None
    disabled: Optional[bool] = None

# Utility functions
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    # In a real app, you would fetch user from DB here
    user = User(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# zkLogin integration
async def verify_zk_login_proof(proof: Dict[str, Any], sui_address: str) -> bool:
    try:
        # Verify proof with Sui zkLogin provider
        response = requests.post(
            f"{settings.zk_login_provider_url}/verify",
            json={
                "proof": proof,
                "sui_address": sui_address,
                "client_id": settings.client_id
            }
        )
        response.raise_for_status()
        return response.json().get("valid", False)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Proof verification failed: {str(e)}"
        )

# Routes
@app.post("/login", response_model=Token)
async def login_for_access_token(request: Request):
    form_data = await request.json()
    proof = form_data.get("proof")
    sui_address = form_data.get("sui_address")
    
    if not proof or not sui_address:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Proof and Sui address are required"
        )
    
    is_valid = await verify_zk_login_proof(proof, sui_address)
    if not is_valid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid zkLogin proof"
        )
    
    # In a real app, you would create or fetch user here
    access_token_expires = timedelta(minutes=settings.jwt_expire_minutes)
    access_token = create_access_token(
        data={"sub": sui_address}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@app.get("/protected")
async def protected_route(current_user: User = Depends(get_current_active_user)):
    return {"message": "This is a protected route", "user": current_user.username}

# Health check
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Main entry point
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
