"""
Generated Code Metadata:
========================
Original URL: https://anonymouscryptoexchange.com
Prompt: Design an API for a decentralized, non-KYC crypto exchange that supports a wide asset selection, including popular pairs like BTC/USD, ETH/USD, and offers robust security features such as 2FA and end-to-end encryption.
Generated: DETERMINISTIC_27c7578da161e489
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# crypto_exchange_api.py
import hashlib
import hmac
import json
import os
import time
from typing import Dict, List, Optional, Union

import requests
from fastapi import FastAPI, HTTPException, Depends, status, Security
from fastapi.security import APIKeyHeader, OAuth2PasswordBearer
from pydantic import BaseModel, Field, validator
from starlette.middleware.cors import CORSMiddleware

# Constants
API_KEY_HEADER = APIKeyHeader(name="X-API-KEY", auto_error=False)
OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl="token", auto_error=False)
HMAC_SECRET = os.getenv("HMAC_SECRET", "default_secret_key")
TWO_FACTOR_ENABLED = os.getenv("TWO_FACTOR_ENABLED", "true").lower() == "true"

# Initialize FastAPI
app = FastAPI(
    title="Decentralized Crypto Exchange API",
    description="Non-KYC cryptocurrency exchange with wide asset selection",
    version="1.0.0",
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class Asset(BaseModel):
    symbol: str
    name: str
    decimals: int
    is_crypto: bool

class Pair(BaseModel):
    base: str
    quote: str
    min_trade_size: float
    price_precision: int
    amount_precision: int

class Order(BaseModel):
    id: str
    pair: str
    side: str  # 'buy' or 'sell'
    type: str  # 'limit', 'market'
    price: Optional[float]
    amount: float
    filled: float = 0.0
    status: str  # 'open', 'filled', 'cancelled'
    created_at: float

class Trade(BaseModel):
    id: str
    order_id: str
    pair: str
    side: str
    price: float
    amount: float
    fee: float
    timestamp: float

class Balance(BaseModel):
    asset: str
    total: float
    available: float
    locked: float

class APIKey(BaseModel):
    key: str
    secret: str
    permissions: List[str]

class TwoFactorRequest(BaseModel):
    code: str = Field(..., min_length=6, max_length=6)

# Database mock
class Database:
    def __init__(self):
        self.assets = self._load_assets()
        self.pairs = self._load_pairs()
        self.orders = {}
        self.trades = {}
        self.balances = {}
        self.api_keys = {}

    def _load_assets(self) -> Dict[str, Asset]:
        return {
            "BTC": Asset(symbol="BTC", name="Bitcoin", decimals=8, is_crypto=True),
            "ETH": Asset(symbol="ETH", name="Ethereum", decimals=18, is_crypto=True),
            "USD": Asset(symbol="USD", name="US Dollar", decimals=2, is_crypto=False),
        }

    def _load_pairs(self) -> Dict[str, Pair]:
        return {
            "BTC/USD": Pair(
                base="BTC",
                quote="USD",
                min_trade_size=0.0001,
                price_precision=2,
                amount_precision=8,
            ),
            "ETH/USD": Pair(
                base="ETH",
                quote="USD",
                min_trade_size=0.001,
                price_precision=2,
                amount_precision=8,
            ),
        }

db = Database()

# Security utilities
def generate_api_key() -> APIKey:
    key = hashlib.sha256(os.urandom(32)).hexdigest()
    secret = hashlib.sha256(os.urandom(32)).hexdigest()
    return APIKey(key=key, secret=secret, permissions=["read", "trade"])

def verify_api_key(api_key: str = Security(API_KEY_HEADER)) -> bool:
    if api_key in db.api_keys:
        return True
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid API key",
    )

def verify_hmac_signature(data: Dict, signature: str) -> bool:
    message = json.dumps(data, sort_keys=True).encode()
    expected_signature = hmac.new(
        HMAC_SECRET.encode(), message, hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(signature, expected_signature)

def verify_2fa(code: str) -> bool:
    # In production, integrate with a 2FA service like Google Authenticator
    return True  # Mock implementation

# API endpoints
@app.get("/assets", response_model=List[Asset])
async def get_assets():
    """Get all available assets"""
    return list(db.assets.values())

@app.get("/pairs", response_model=List[Pair])
async def get_pairs():
    """Get all available trading pairs"""
    return list(db.pairs.values())

@app.get("/orders", response_model=List[Order])
async def get_orders(api_key: str = Security(API_KEY_HEADER)):
    """Get all user orders"""
    verify_api_key(api_key)
    return list(db.orders.values())

@app.post("/orders", response_model=Order)
async def create_order(
    order: Order,
    api_key: str = Security(API_KEY_HEADER),
    two_factor: Optional[TwoFactorRequest] = None,
):
    """Create a new order"""
    verify_api_key(api_key)
    
    if TWO_FACTOR_ENABLED:
        if not two_factor or not verify_2fa(two_factor.code):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="2FA verification failed",
            )
    
    if order.pair not in db.pairs:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid trading pair",
        )
    
    order.id = hashlib.sha256(os.urandom(32)).hexdigest()
    order.created_at = time.time()
    order.status = "open"
    db.orders[order.id] = order
    return order

@app.delete("/orders/{order_id}", response_model=Order)
async def cancel_order(
    order_id: str,
    api_key: str = Security(API_KEY_HEADER),
    two_factor: Optional[TwoFactorRequest] = None,
):
    """Cancel an order"""
    verify_api_key(api_key)
    
    if TWO_FACTOR_ENABLED:
        if not two_factor or not verify_2fa(two_factor.code):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="2FA verification failed",
            )
    
    if order_id not in db.orders:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found",
        )
    
    order = db.orders[order_id]
    order.status = "cancelled"
    return order

@app.get("/trades", response_model=List[Trade])
async def get_trades(api_key: str = Security(API_KEY_HEADER)):
    """Get all user trades"""
    verify_api_key(api_key)
    return list(db.trades.values())

@app.get("/balance", response_model=List[Balance])
async def get_balance(api_key: str = Security(API_KEY_HEADER)):
    """Get user balances"""
    verify_api_key(api_key)
    return list(db.balances.values())

@app.post("/api-key", response_model=APIKey)
async def create_api_key():
    """Create a new API key"""
    api_key = generate_api_key()
    db.api_keys[api_key.key] = api_key
    return api_key

@app.delete("/api-key/{key}")
async def revoke_api_key(key: str, api_key: str = Security(API_KEY_HEADER)):
    """Revoke an API key"""
    verify_api_key(api_key)
    if key in db.api_keys:
        del db.api_keys[key]
    return {"message": "API key revoked"}

# WebSocket endpoints for real-time updates
from fastapi import WebSocket, WebSocketDisconnect

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            # Handle WebSocket messages
            await websocket.send_text(f"Message received: {data}")
    except WebSocketDisconnect:
        await websocket.close()

# Health check
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Main entry point
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
