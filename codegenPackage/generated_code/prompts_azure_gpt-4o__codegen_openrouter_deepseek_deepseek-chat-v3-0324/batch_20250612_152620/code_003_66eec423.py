"""
Generated Code Metadata:
========================
Original URL: https://betswirl.xyz
Prompt: Create a user authentication system for a blockchain-based gaming platform like BetSwirl that leverages decentralized storage for enhanced security.
Generated: DETERMINISTIC_66eec4232652aab1
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import hashlib
import binascii
from datetime import datetime, timedelta
from typing import Optional, Dict, Any

from web3 import Web3
from web3.auto import w3
from eth_account.messages import encode_defunct
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from jose import JWTError, jwt
from passlib.context import CryptContext

# Configuration
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Initialize FastAPI app
app = FastAPI(title="Blockchain Gaming Auth System")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Mock database (in production, use a real database)
fake_users_db = {}

# Models
class User(BaseModel):
    username: str
    email: str
    wallet_address: str
    disabled: bool = False

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class SignatureRequest(BaseModel):
    message: str
    signature: str
    wallet_address: str

# Utility functions
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def get_user(db, username: str) -> Optional[UserInDB]:
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
    return None

def authenticate_user(fake_db, username: str, password: str) -> Optional[UserInDB]:
    user = get_user(fake_db, username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_signature(message: str, signature: str, wallet_address: str) -> bool:
    try:
        message_hash = encode_defunct(text=message)
        recovered_address = w3.eth.account.recover_message(message_hash, signature=signature)
        return recovered_address.lower() == wallet_address.lower()
    except:
        return False

# Routes
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.post("/register")
async def register_user(username: str, email: str, password: str, wallet_address: str):
    if username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = get_password_hash(password)
    user = UserInDB(
        username=username,
        email=email,
        wallet_address=wallet_address,
        hashed_password=hashed_password,
        disabled=False
    )
    fake_users_db[username] = user.dict()
    return {"message": "User created successfully"}

@app.post("/verify-wallet")
async def verify_wallet(signature_request: SignatureRequest):
    if not verify_signature(
        signature_request.message,
        signature_request.signature,
        signature_request.wallet_address
    ):
        raise HTTPException(status_code=400, detail="Invalid signature")
    
    return {"verified": True, "wallet_address": signature_request.wallet_address}

# Dependency
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# IPFS Storage (Mock - in production use actual IPFS client)
class IPFSStorage:
    @staticmethod
    def store_data(data: Dict[str, Any]) -> str:
        # In production, this would upload to IPFS and return CID
        mock_cid = hashlib.sha256(json.dumps(data).encode()).hexdigest()
        return mock_cid

    @staticmethod
    def retrieve_data(cid: str) -> Dict[str, Any]:
        # In production, this would retrieve from IPFS using CID
        return {"mock": "data"}

# Main
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
