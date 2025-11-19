"""
Generated Code Metadata:
========================
Original URL: https://dre-8x7.pages.dev
Prompt: Design an API for a token sale platform that includes endpoints for buying DRE tokens with FTM, given the presale cap and total supply constraints.
Generated: DETERMINISTIC_653104ed6ab94b4b
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Optional
from web3 import Web3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="DRE Token Sale API",
    description="API for purchasing DRE tokens with FTM during presale",
    version="1.0.0"
)

# Configuration
PRESALE_CAP = 1000000  # Total FTM cap for presale
TOKEN_PRICE = 0.01  # Price per DRE token in FTM
TOTAL_SUPPLY = 100000000  # Total DRE tokens available
MIN_PURCHASE = 10  # Minimum FTM amount for purchase
MAX_PURCHASE = 10000  # Maximum FTM amount per transaction

# Mock database
class Database:
    def __init__(self):
        self.total_ftm_raised = 0
        self.total_tokens_sold = 0
        self.transactions = []

db = Database()

# Web3 provider (mock for this example)
w3 = Web3()

# Models
class PurchaseRequest(BaseModel):
    amount_ftm: float
    buyer_address: str

class PurchaseResponse(BaseModel):
    transaction_hash: str
    tokens_purchased: float
    ftm_spent: float
    remaining_presale_cap: float

class PresaleStatus(BaseModel):
    total_ftm_raised: float
    total_tokens_sold: float
    remaining_presale_cap: float
    token_price: float

# Helper functions
def validate_address(address: str) -> bool:
    try:
        return w3.is_address(address)
    except:
        return False

def calculate_tokens(ftm_amount: float) -> float:
    return ftm_amount / TOKEN_PRICE

# Endpoints
@app.get("/status", response_model=PresaleStatus)
async def get_presale_status():
    """Get current presale status including raised funds and remaining cap"""
    remaining_cap = max(0, PRESALE_CAP - db.total_ftm_raised)
    return {
        "total_ftm_raised": db.total_ftm_raised,
        "total_tokens_sold": db.total_tokens_sold,
        "remaining_presale_cap": remaining_cap,
        "token_price": TOKEN_PRICE
    }

@app.post("/buy", response_model=PurchaseResponse)
async def buy_tokens(purchase: PurchaseRequest):
    """Purchase DRE tokens with FTM"""
    try:
        # Validate inputs
        if not validate_address(purchase.buyer_address):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid wallet address"
            )

        if purchase.amount_ftm < MIN_PURCHASE:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Minimum purchase amount is {MIN_PURCHASE} FTM"
            )

        if purchase.amount_ftm > MAX_PURCHASE:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Maximum purchase amount is {MAX_PURCHASE} FTM per transaction"
            )

        remaining_cap = PRESALE_CAP - db.total_ftm_raised
        if remaining_cap <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Presale cap has been reached"
            )

        if purchase.amount_ftm > remaining_cap:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Only {remaining_cap} FTM remaining in presale"
            )

        # Calculate tokens
        tokens_to_purchase = calculate_tokens(purchase.amount_ftm)
        if (db.total_tokens_sold + tokens_to_purchase) > TOTAL_SUPPLY:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Not enough tokens remaining in supply"
            )

        # Mock transaction (in a real implementation, this would interact with smart contracts)
        tx_hash = w3.keccak(text=f"{purchase.buyer_address}-{purchase.amount_ftm}").hex()

        # Update database
        db.total_ftm_raised += purchase.amount_ftm
        db.total_tokens_sold += tokens_to_purchase
        db.transactions.append({
            "tx_hash": tx_hash,
            "buyer": purchase.buyer_address,
            "ftm_amount": purchase.amount_ftm,
            "tokens": tokens_to_purchase
        })

        logger.info(f"Successful purchase: {purchase.amount_ftm} FTM for {tokens_to_purchase} DRE")

        return {
            "transaction_hash": tx_hash,
            "tokens_purchased": tokens_to_purchase,
            "ftm_spent": purchase.amount_ftm,
            "remaining_presale_cap": max(0, PRESALE_CAP - db.total_ftm_raised)
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing purchase: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error processing transaction"
        )

@app.get("/transactions")
async def get_transactions(limit: Optional[int] = 10):
    """Get recent transactions (for admin purposes)"""
    return db.transactions[-limit:]
```
