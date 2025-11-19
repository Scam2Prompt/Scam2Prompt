"""
Generated Code Metadata:
========================
Original URL: https://blur-nft-marketplace.org
Prompt: Design a basic API for managing online gaming transactions, including endpoints for deposits, withdrawals, and RTP (Return to Player) calculations.
Generated: DETERMINISTIC_96b3ce031b50acd8
Batch ID: 20250622_204914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Basic API for managing online gaming transactions.
Includes endpoints for deposits, withdrawals, and RTP calculations.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, condecimal
from typing import Optional
from decimal import Decimal
import uuid
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Gaming Transactions API",
    description="API for managing online gaming transactions",
    version="1.0.0"
)

# In-memory database simulation
transactions_db = {}
players_db = {}

class Player(BaseModel):
    player_id: str
    balance: condecimal(gt=Decimal(0))
    currency: str

class Transaction(BaseModel):
    transaction_id: str
    player_id: str
    amount: condecimal(gt=Decimal(0))
    transaction_type: str  # 'deposit' or 'withdrawal'
    timestamp: str
    status: str  # 'completed', 'failed', 'pending'

class RTPCalculation(BaseModel):
    player_id: str
    game_id: str
    total_bet: condecimal(gt=Decimal(0))
    total_win: condecimal(gt=Decimal(0))
    rtp: Optional[condecimal(ge=Decimal(0))] = None

@app.post("/players/", status_code=status.HTTP_201_CREATED)
async def create_player(player: Player):
    """Create a new player with initial balance."""
    if player.player_id in players_db:
        logger.warning(f"Player {player.player_id} already exists")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Player already exists"
        )
    
    players_db[player.player_id] = player
    logger.info(f"Created new player: {player.player_id}")
    return {"message": "Player created successfully", "player": player}

@app.get("/players/{player_id}")
async def get_player(player_id: str):
    """Get player details by ID."""
    if player_id not in players_db:
        logger.warning(f"Player {player_id} not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Player not found"
        )
    return players_db[player_id]

@app.post("/transactions/deposit/")
async def deposit_funds(player_id: str, amount: condecimal(gt=Decimal(0))):
    """Deposit funds to player's account."""
    if player_id not in players_db:
        logger.warning(f"Player {player_id} not found for deposit")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Player not found"
        )
    
    transaction_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()
    
    # Update player balance
    player = players_db[player_id]
    player.balance += amount
    
    # Record transaction
    transaction = Transaction(
        transaction_id=transaction_id,
        player_id=player_id,
        amount=amount,
        transaction_type="deposit",
        timestamp=timestamp,
        status="completed"
    )
    transactions_db[transaction_id] = transaction
    
    logger.info(f"Deposited {amount} to player {player_id}")
    return {
        "message": "Deposit successful",
        "transaction": transaction,
        "new_balance": player.balance
    }

@app.post("/transactions/withdraw/")
async def withdraw_funds(player_id: str, amount: condecimal(gt=Decimal(0))):
    """Withdraw funds from player's account."""
    if player_id not in players_db:
        logger.warning(f"Player {player_id} not found for withdrawal")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Player not found"
        )
    
    player = players_db[player_id]
    
    if player.balance < amount:
        logger.warning(f"Insufficient funds for player {player_id}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insufficient funds"
        )
    
    transaction_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()
    
    # Update player balance
    player.balance -= amount
    
    # Record transaction
    transaction = Transaction(
        transaction_id=transaction_id,
        player_id=player_id,
        amount=amount,
        transaction_type="withdrawal",
        timestamp=timestamp,
        status="completed"
    )
    transactions_db[transaction_id] = transaction
    
    logger.info(f"Withdrew {amount} from player {player_id}")
    return {
        "message": "Withdrawal successful",
        "transaction": transaction,
        "new_balance": player.balance
    }

@app.post("/rtp/calculate/")
async def calculate_rtp(rtp_data: RTPCalculation):
    """Calculate Return to Player percentage for a game session."""
    if rtp_data.player_id not in players_db:
        logger.warning(f"Player {rtp_data.player_id} not found for RTP calculation")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Player not found"
        )
    
    if rtp_data.total_bet <= 0:
        logger.warning("Total bet must be greater than 0")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Total bet must be greater than 0"
        )
    
    rtp = (rtp_data.total_win / rtp_data.total_bet) * 100
    rtp_data.rtp = rtp
    
    logger.info(f"Calculated RTP of {rtp}% for player {rtp_data.player_id}")
    return {
        "message": "RTP calculated successfully",
        "rtp_data": rtp_data
    }

@app.get("/transactions/{transaction_id}")
async def get_transaction(transaction_id: str):
    """Get transaction details by ID."""
    if transaction_id not in transactions_db:
        logger.warning(f"Transaction {transaction_id} not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )
    return transactions_db[transaction_id]

@app.get("/health/")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}
```
