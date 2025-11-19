"""
Generated Code Metadata:
========================
Original URL: https://tournament-starheroesio.pages.dev
Prompt: Design a simple backend API for managing hero claims and wallet connections, inspired by StarHeroes' functionality.
Generated: DETERMINISTIC_4cb0d4a2b1154718
Batch ID: 20250622_211009
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
from typing import Optional, List
import uuid
from datetime import datetime

app = FastAPI(
    title="StarHeroes Backend API",
    description="API for managing hero claims and wallet connections",
    version="1.0.0"
)

# Database models (in-memory for simplicity)
class Hero(BaseModel):
    id: str
    name: str
    claimed_by: Optional[str] = None  # Wallet address
    claimed_at: Optional[datetime] = None
    rarity: str

class Wallet(BaseModel):
    address: str
    heroes: List[str] = []  # List of hero IDs
    last_connected: datetime

# In-memory storage
heroes_db = {}
wallets_db = {}

# Helper functions
def get_hero_or_404(hero_id: str):
    hero = heroes_db.get(hero_id)
    if not hero:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Hero not found"
        )
    return hero

def get_wallet_or_404(wallet_address: str):
    wallet = wallets_db.get(wallet_address)
    if not wallet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Wallet not found"
        )
    return wallet

# Models for request/response
class HeroClaimRequest(BaseModel):
    wallet_address: str

class WalletConnectRequest(BaseModel):
    wallet_address: str

class HeroResponse(BaseModel):
    id: str
    name: str
    claimed_by: Optional[str]
    claimed_at: Optional[datetime]
    rarity: str

class WalletResponse(BaseModel):
    address: str
    heroes: List[str]
    last_connected: datetime

# Routes
@app.post("/heroes/{hero_id}/claim", response_model=HeroResponse)
async def claim_hero(hero_id: str, claim_request: HeroClaimRequest):
    hero = get_hero_or_404(hero_id)
    
    if hero.claimed_by:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Hero already claimed"
        )
    
    wallet = wallets_db.get(claim_request.wallet_address)
    if not wallet:
        wallet = Wallet(
            address=claim_request.wallet_address,
            heroes=[],
            last_connected=datetime.now()
        )
        wallets_db[wallet.address] = wallet
    
    hero.claimed_by = claim_request.wallet_address
    hero.claimed_at = datetime.now()
    wallet.heroes.append(hero_id)
    wallet.last_connected = datetime.now()
    
    return hero

@app.post("/wallets/connect", response_model=WalletResponse)
async def connect_wallet(connect_request: WalletConnectRequest):
    wallet = wallets_db.get(connect_request.wallet_address)
    
    if wallet:
        wallet.last_connected = datetime.now()
    else:
        wallet = Wallet(
            address=connect_request.wallet_address,
            heroes=[],
            last_connected=datetime.now()
        )
        wallets_db[wallet.address] = wallet
    
    return wallet

@app.get("/wallets/{wallet_address}", response_model=WalletResponse)
async def get_wallet(wallet_address: str):
    return get_wallet_or_404(wallet_address)

@app.get("/heroes/{hero_id}", response_model=HeroResponse)
async def get_hero(hero_id: str):
    return get_hero_or_404(hero_id)

@app.get("/wallets/{wallet_address}/heroes", response_model=List[HeroResponse])
async def get_wallet_heroes(wallet_address: str):
    wallet = get_wallet_or_404(wallet_address)
    heroes = []
    for hero_id in wallet.heroes:
        hero = heroes_db.get(hero_id)
        if hero:
            heroes.append(hero)
    return heroes

# Initialize with some sample data
@app.on_event("startup")
async def startup_event():
    sample_heroes = [
        Hero(id=str(uuid.uuid4()), name="Galactic Guardian", rarity="Legendary"),
        Hero(id=str(uuid.uuid4()), name="Cosmic Striker", rarity="Epic"),
        Hero(id=str(uuid.uuid4()), name="Stellar Defender", rarity="Rare"),
        Hero(id=str(uuid.uuid4()), name="Nebula Scout", rarity="Common"),
    ]
    
    for hero in sample_heroes:
        heroes_db[hero.id] = hero
```
