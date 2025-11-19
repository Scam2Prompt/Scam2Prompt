"""
Generated Code Metadata:
========================
Original URL: https://daoweb3system.web.app
Prompt: "Design an API for a cryptocurrency wallet management system that includes features like NFT whitelisting, rewards/airdrop distribution, and transaction validation."
Generated: DETERMINISTIC_54bea81c1ff9c59b
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Cryptocurrency Wallet Management System API
"""
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field, EmailStr, validator
from typing import List, Optional
from datetime import datetime
import uuid
import hashlib
import secrets

app = FastAPI(
    title="Crypto Wallet Management API",
    description="API for managing cryptocurrency wallets with NFT whitelisting, rewards distribution, and transaction validation",
    version="1.0.0"
)

# Database models (in-memory for example purposes)
class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr
    hashed_password: str
    wallets: List[str] = []
    is_admin: bool = False

class Wallet(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    address: str
    owner_id: str
    balance: float = 0.0
    nfts: List[str] = []
    whitelisted: bool = False

class NFT(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    contract_address: str
    token_id: str

class Transaction(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    sender: str
    receiver: str
    amount: float
    timestamp: datetime = Field(default_factory=datetime.now)
    status: str = "pending"  # pending, completed, failed
    tx_hash: Optional[str] = None

class Reward(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    wallet_address: str
    amount: float
    reward_type: str  # airdrop, staking, referral, etc.
    timestamp: datetime = Field(default_factory=datetime.now)
    distributed: bool = False

# In-memory databases
users_db = {}
wallets_db = {}
nfts_db = {}
transactions_db = {}
rewards_db = {}
whitelist_db = set()

# Helper functions
def hash_password(password: str) -> str:
    salt = secrets.token_hex(16)
    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000).hex()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    salt = hashed_password[:32]
    return hashed_password == hashlib.pbkdf2_hmac('sha256', plain_password.encode(), salt.encode(), 100000).hex()

def get_current_user(token: str):
    if token not in users_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )
    return users_db[token]

def validate_transaction(sender: str, receiver: str, amount: float) -> bool:
    if sender not in wallets_db or receiver not in wallets_db:
        return False
    if wallets_db[sender].balance < amount:
        return False
    return True

# Models for request/response
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class WalletCreate(BaseModel):
    owner_id: str

class TransactionCreate(BaseModel):
    sender: str
    receiver: str
    amount: float

class RewardCreate(BaseModel):
    wallet_address: str
    amount: float
    reward_type: str

class NFTWhitelistRequest(BaseModel):
    wallet_address: str
    nft_id: str

# API Endpoints
@app.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    if user.email in [u.email for u in users_db.values()]:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = hash_password(user.password)
    user_id = str(uuid.uuid4())
    new_user = User(id=user_id, email=user.email, hashed_password=hashed_password)
    users_db[user_id] = new_user
    return new_user

@app.post("/wallets/", response_model=Wallet, status_code=status.HTTP_201_CREATED)
def create_wallet(wallet: WalletCreate, current_user: User = Depends(get_current_user)):
    if wallet.owner_id != current_user.id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not authorized to create wallet for this user")
    new_wallet = Wallet(address=str(uuid.uuid4()), owner_id=wallet.owner_id)
    wallets_db[new_wallet.address] = new_wallet
    if wallet.owner_id in users_db:
        users_db[wallet.owner_id].wallets.append(new_wallet.address)
    return new_wallet

@app.get("/wallets/{wallet_address}", response_model=Wallet)
def get_wallet(wallet_address: str, current_user: User = Depends(get_current_user)):
    if wallet_address not in wallets_db:
        raise HTTPException(status_code=404, detail="Wallet not found")
    wallet = wallets_db[wallet_address]
    if wallet.owner_id != current_user.id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not authorized to access this wallet")
    return wallet

@app.post("/transactions/", response_model=Transaction, status_code=status.HTTP_201_CREATED)
def create_transaction(transaction: TransactionCreate, current_user: User = Depends(get_current_user)):
    if not validate_transaction(transaction.sender, transaction.receiver, transaction.amount):
        raise HTTPException(status_code=400, detail="Invalid transaction")
    
    new_transaction = Transaction(
        sender=transaction.sender,
        receiver=transaction.receiver,
        amount=transaction.amount
    )
    transactions_db[new_transaction.id] = new_transaction
    
    # Simulate transaction processing
    wallets_db[transaction.sender].balance -= transaction.amount
    wallets_db[transaction.receiver].balance += transaction.amount
    new_transaction.status = "completed"
    new_transaction.tx_hash = hashlib.sha256(new_transaction.id.encode()).hexdigest()
    
    return new_transaction

@app.post("/rewards/", response_model=Reward, status_code=status.HTTP_201_CREATED)
def create_reward(reward: RewardCreate, current_user: User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Only admins can create rewards")
    if reward.wallet_address not in wallets_db:
        raise HTTPException(status_code=404, detail="Wallet not found")
    
    new_reward = Reward(
        wallet_address=reward.wallet_address,
        amount=reward.amount,
        reward_type=reward.reward_type
    )
    rewards_db[new_reward.id] = new_reward
    
    # Distribute reward
    wallets_db[reward.wallet_address].balance += reward.amount
    new_reward.distributed = True
    
    return new_reward

@app.post("/nfts/whitelist/", status_code=status.HTTP_200_OK)
def whitelist_nft(request: NFTWhitelistRequest, current_user: User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Only admins can whitelist NFTs")
    if request.wallet_address not in wallets_db:
        raise HTTPException(status_code=404, detail="Wallet not found")
    if request.nft_id not in nfts_db:
        raise HTTPException(status_code=404, detail="NFT not found")
    
    whitelist_db.add((request.wallet_address, request.nft_id))
    wallets_db[request.wallet_address].whitelisted = True
    return {"message": "NFT whitelisted successfully"}

@app.get("/nfts/whitelist/check/{wallet_address}/{nft_id}", status_code=status.HTTP_200_OK)
def check_whitelist(wallet_address: str, nft_id: str):
    is_whitelisted = (wallet_address, nft_id) in whitelist_db
    return {"is_whitelisted": is_whitelisted}

@app.post("/nfts/", response_model=NFT, status_code=status.HTTP_201_CREATED)
def create_nft(name: str, description: str, contract_address: str, token_id: str, current_user: User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Only admins can create NFTs")
    
    new_nft = NFT(
        name=name,
        description=description,
        contract_address=contract_address,
        token_id=token_id
    )
    nfts_db[new_nft.id] = new_nft
    return new_nft

@app.get("/transactions/{transaction_id}", response_model=Transaction)
def get_transaction(transaction_id: str, current_user: User = Depends(get_current_user)):
