"""
Generated Code Metadata:
========================
Original URL: https://clais.pages.dev
Prompt: Write a code snippet to create a first-come, first-served airdrop claim system similar to the one described for $BROCK.
Generated: DETERMINISTIC_d36a0fb1610b5b4f
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import hashlib
import secrets
from fastapi import FastAPI, HTTPException, status, Depends, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, validator
import uvicorn

# Security token for API authentication
security = HTTPBearer()

# Database simulation (in production, use a real database)
class Database:
    def __init__(self):
        self.airdrops: Dict[str, Dict] = {}  # airdrop_id -> airdrop_data
        self.claims: Dict[str, Dict] = {}    # claim_id -> claim_data
        self.users: Dict[str, Dict] = {}     # user_id -> user_data

    def save_airdrop(self, airdrop_id: str, data: Dict) -> None:
        self.airdrops[airdrop_id] = data

    def get_airdrop(self, airdrop_id: str) -> Optional[Dict]:
        return self.airdrops.get(airdrop_id)

    def save_claim(self, claim_id: str, data: Dict) -> None:
        self.claims[claim_id] = data

    def get_claim(self, claim_id: str) -> Optional[Dict]:
        return self.claims.get(claim_id)

    def get_user_claims(self, user_id: str) -> List[Dict]:
        return [claim for claim in self.claims.values() if claim.get('user_id') == user_id]

    def user_exists(self, user_id: str) -> bool:
        return user_id in self.users

    def save_user(self, user_id: str, data: Dict) -> None:
        self.users[user_id] = data

# Models
class AirdropCreate(BaseModel):
    name: str
    total_supply: int
    start_time: datetime
    end_time: datetime
    claim_limit_per_user: int
    token_address: str

    @validator('end_time')
    def validate_end_time(cls, v, values):
        if 'start_time' in values and v <= values['start_time']:
            raise ValueError('End time must be after start time')
        return v

class ClaimRequest(BaseModel):
    user_id: str
    wallet_address: str
    amount: int

class ClaimResponse(BaseModel):
    claim_id: str
    status: str
    amount: int
    timestamp: datetime

# App setup
app = FastAPI()
db = Database()

# Helper functions
def generate_id() -> str:
    return secrets.token_hex(16)

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    # In production, implement proper token verification
    token = credentials.credentials
    if token != "SECURE_API_TOKEN":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )
    return token

# API Endpoints
@app.post("/airdrops", status_code=status.HTTP_201_CREATED)
async def create_airdrop(
    airdrop: AirdropCreate,
    token: str = Depends(verify_token)
):
    airdrop_id = generate_id()
    airdrop_data = {
        **airdrop.dict(),
        "id": airdrop_id,
        "remaining_supply": airdrop.total_supply,
        "created_at": datetime.utcnow()
    }
    db.save_airdrop(airdrop_id, airdrop_data)
    return {"airdrop_id": airdrop_id}

@app.post("/airdrops/{airdrop_id}/claims", response_model=ClaimResponse)
async def claim_airdrop(
    airdrop_id: str,
    claim_request: ClaimRequest,
    request: Request
):
    # Check if airdrop exists
    airdrop = db.get_airdrop(airdrop_id)
    if not airdrop:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Airdrop not found"
        )

    # Check if airdrop is active
    now = datetime.utcnow()
    if now < airdrop["start_time"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Airdrop has not started yet"
        )
    
    if now > airdrop["end_time"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Airdrop has ended"
        )

    # Check remaining supply
    if claim_request.amount > airdrop["remaining_supply"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Claim amount exceeds remaining supply"
        )

    # Check user claim limit
    user_claims = db.get_user_claims(claim_request.user_id)
    user_claims_for_airdrop = [
        claim for claim in user_claims 
        if claim.get("airdrop_id") == airdrop_id
    ]
    
    if len(user_claims_for_airdrop) >= airdrop["claim_limit_per_user"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User has reached claim limit for this airdrop"
        )

    # Create claim
    claim_id = generate_id()
    claim_data = {
        "id": claim_id,
        "airdrop_id": airdrop_id,
        "user_id": claim_request.user_id,
        "wallet_address": claim_request.wallet_address,
        "amount": claim_request.amount,
        "status": "pending",
        "timestamp": now,
        "ip_address": request.client.host
    }
    
    # Update airdrop remaining supply
    airdrop["remaining_supply"] -= claim_request.amount
    db.save_airdrop(airdrop_id, airdrop)
    db.save_claim(claim_id, claim_data)

    return ClaimResponse(
        claim_id=claim_id,
        status="success",
        amount=claim_request.amount,
        timestamp=now
    )

@app.get("/airdrops/{airdrop_id}/claims/{claim_id}", response_model=ClaimResponse)
async def get_claim(
    airdrop_id: str,
    claim_id: str,
    token: str = Depends(verify_token)
):
    claim = db.get_claim(claim_id)
    if not claim or claim.get("airdrop_id") != airdrop_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Claim not found"
        )
    
    return ClaimResponse(
        claim_id=claim_id,
        status=claim["status"],
        amount=claim["amount"],
        timestamp=claim["timestamp"]
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
