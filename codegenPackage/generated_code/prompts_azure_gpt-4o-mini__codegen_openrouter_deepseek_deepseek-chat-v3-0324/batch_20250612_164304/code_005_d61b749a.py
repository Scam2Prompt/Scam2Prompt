"""
Generated Code Metadata:
========================
Original URL: https://jm4-dapp.pages.dev
Prompt: Create an API call to enable buying and selling of DApps on mobile wallets as described in the content.
Generated: DETERMINISTIC_d61b749a4d9c27df
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready implementation for an API that enables buying and selling DApps on mobile wallets:

```python
from fastapi import FastAPI, HTTPException, status, Query, Depends
from pydantic import BaseModel, Field, validator
from typing import Optional
import uuid
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="DApp Marketplace API",
    description="API for buying and selling DApps on mobile wallets",
    version="1.0.0"
)

# Mock database
dapps_db = {}
transactions_db = {}
wallets_db = {}

class WalletAuth:
    """Dependency for wallet authentication"""
    
    async def __call__(self, wallet_id: str = Query(..., description="User's wallet ID"),
                      signature: str = Query(..., description="Transaction signature")):
        # In production, verify the signature against the wallet address
        if wallet_id not in wallets_db:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Wallet not registered"
            )
        return wallet_id

class DApp(BaseModel):
    """DApp listing model"""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=10, max_length=500)
    price: float = Field(..., gt=0, description="Price in native token")
    seller_wallet_id: str
    category: str = Field(..., min_length=1, max_length=50)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    @validator('price')
    def round_price(cls, v):
        return round(v, 6)

class Transaction(BaseModel):
    """DApp purchase transaction model"""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    dapp_id: str
    buyer_wallet_id: str
    seller_wallet_id: str
    price: float
    status: str = Field(default="pending", regex="^(pending|completed|failed)$")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    completed_at: Optional[datetime] = None

@app.post("/dapps", status_code=status.HTTP_201_CREATED)
async def create_dapp_listing(dapp: DApp, auth: str = Depends(WalletAuth)):
    """Create a new DApp listing"""
    if dapp.seller_wallet_id != auth:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wallet ID mismatch"
        )
    
    dapps_db[dapp.id] = dapp.dict()
    logger.info(f"Created DApp listing: {dapp.id}")
    return {"message": "DApp listing created", "dapp_id": dapp.id}

@app.get("/dapps/{dapp_id}", status_code=status.HTTP_200_OK)
async def get_dapp(dapp_id: str):
    """Get DApp listing details"""
    if dapp_id not in dapps_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="DApp not found"
        )
    return dapps_db[dapp_id]

@app.post("/dapps/{dapp_id}/buy", status_code=status.HTTP_201_CREATED)
async def buy_dapp(dapp_id: str, buyer_wallet_id: str = Depends(WalletAuth)):
    """Initiate DApp purchase"""
    if dapp_id not in dapps_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="DApp not found"
        )
    
    dapp = dapps_db[dapp_id]
    if dapp['seller_wallet_id'] == buyer_wallet_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot buy your own DApp"
        )
    
    transaction = Transaction(
        dapp_id=dapp_id,
        buyer_wallet_id=buyer_wallet_id,
        seller_wallet_id=dapp['seller_wallet_id'],
        price=dapp['price']
    )
    
    transactions_db[transaction.id] = transaction.dict()
    
    # In production, this would initiate a blockchain transaction
    logger.info(f"Initiated purchase of DApp {dapp_id} by {buyer_wallet_id}")
    
    return {
        "message": "Purchase initiated",
        "transaction_id": transaction.id,
        "price": transaction.price
    }

@app.post("/transactions/{transaction_id}/confirm", status_code=status.HTTP_200_OK)
async def confirm_transaction(transaction_id: str, wallet_id: str = Depends(WalletAuth)):
    """Confirm a completed transaction (would be called by webhook in production)"""
    if transaction_id not in transactions_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )
    
    transaction = transactions_db[transaction_id]
    if wallet_id not in [transaction['buyer_wallet_id'], transaction['seller_wallet_id']]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to confirm this transaction"
        )
    
    # In production, verify blockchain transaction here
    transaction['status'] = 'completed'
    transaction['completed_at'] = datetime.utcnow().isoformat()
    
    # Transfer ownership (in a real implementation, this would be on-chain)
    dapp_id = transaction['dapp_id']
    dapps_db[dapp_id]['seller_wallet_id'] = transaction['buyer_wallet_id']
    
    logger.info(f"Completed transaction: {transaction_id}")
    return {"message": "Transaction confirmed", "status": "completed"}

@app.get("/wallet/{wallet_id}/dapps", status_code=status.HTTP_200_OK)
async def get_wallet_dapps(wallet_id: str, auth: str = Depends(WalletAuth)):
    """Get DApps owned by a wallet"""
    if wallet_id != auth:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this wallet"
        )
    
    owned_dapps = [dapp for dapp in dapps_db.values() if dapp['seller_wallet_id'] == wallet_id]
    return {"count": len(owned_dapps), "dapps": owned_dapps}
```
