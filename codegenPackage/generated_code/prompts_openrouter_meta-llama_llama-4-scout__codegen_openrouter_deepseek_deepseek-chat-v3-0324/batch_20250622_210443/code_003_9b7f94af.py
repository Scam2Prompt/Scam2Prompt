"""
Generated Code Metadata:
========================
Original URL: https://crop-6qi.pages.dev
Prompt: Design an API for managing lucky rolls and token allocations for a blockchain gaming project, with a focus on personalized rewards for players.
Generated: DETERMINISTIC_9b7f94af2a9e31f4
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# lucky_rolls_api.py
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Optional, List
import uuid
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Lucky Rolls API", description="API for managing lucky rolls and token allocations")

# Database models (in-memory for demonstration)
class Player(BaseModel):
    player_id: str
    wallet_address: str
    total_tokens: float = 0.0
    rolls_available: int = 0
    last_roll_time: Optional[datetime] = None

class LuckyRoll(BaseModel):
    roll_id: str
    player_id: str
    roll_value: int
    tokens_awarded: float
    timestamp: datetime

# In-memory storage
players_db = {}
rolls_db = {}

# Helper functions
def generate_id() -> str:
    return str(uuid.uuid4())

def validate_player(player_id: str) -> Player:
    if player_id not in players_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Player not found"
        )
    return players_db[player_id]

# Token allocation configuration
TOKEN_ALLOCATION_RULES = {
    1: 10.0,   # Lowest roll gets 10 tokens
    2: 20.0,
    3: 30.0,
    4: 50.0,
    5: 75.0,
    6: 100.0,  # Highest roll gets 100 tokens
}

# API Endpoints
@app.post("/players/", status_code=status.HTTP_201_CREATED)
async def create_player(wallet_address: str):
    """Create a new player with the given wallet address."""
    player_id = generate_id()
    new_player = Player(
        player_id=player_id,
        wallet_address=wallet_address,
        rolls_available=3  # Initial rolls
    )
    players_db[player_id] = new_player
    logger.info(f"Created new player with ID: {player_id}")
    return {"player_id": player_id}

@app.get("/players/{player_id}")
async def get_player(player_id: str):
    """Retrieve player information."""
    player = validate_player(player_id)
    return player

@app.post("/players/{player_id}/roll", status_code=status.HTTP_201_CREATED)
async def perform_lucky_roll(player_id: str):
    """Perform a lucky roll for the player and allocate tokens."""
    player = validate_player(player_id)
    
    if player.rolls_available <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No rolls available"
        )
    
    # Generate random roll (1-6)
    import random
    roll_value = random.randint(1, 6)
    
    # Calculate tokens based on roll
    tokens_awarded = TOKEN_ALLOCATION_RULES.get(roll_value, 0.0)
    
    # Create roll record
    roll_id = generate_id()
    new_roll = LuckyRoll(
        roll_id=roll_id,
        player_id=player_id,
        roll_value=roll_value,
        tokens_awarded=tokens_awarded,
        timestamp=datetime.utcnow()
    )
    rolls_db[roll_id] = new_roll
    
    # Update player stats
    player.total_tokens += tokens_awarded
    player.rolls_available -= 1
    player.last_roll_time = datetime.utcnow()
    
    logger.info(f"Player {player_id} rolled {roll_value}, awarded {tokens_awarded} tokens")
    return {
        "roll_id": roll_id,
        "roll_value": roll_value,
        "tokens_awarded": tokens_awarded,
        "remaining_rolls": player.rolls_available
    }

@app.get("/players/{player_id}/rolls")
async def get_player_rolls(player_id: str):
    """Get all rolls for a player."""
    validate_player(player_id)
    player_rolls = [roll for roll in rolls_db.values() if roll.player_id == player_id]
    return {"rolls": player_rolls}

@app.post("/players/{player_id}/add_rolls")
async def add_rolls_to_player(player_id: str, amount: int):
    """Add additional rolls to a player's account."""
    if amount <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Amount must be positive"
        )
    
    player = validate_player(player_id)
    player.rolls_available += amount
    logger.info(f"Added {amount} rolls to player {player_id}")
    return {"message": f"Added {amount} rolls", "total_rolls": player.rolls_available}

@app.get("/rolls/{roll_id}")
async def get_roll(roll_id: str):
    """Get details of a specific roll."""
    if roll_id not in rolls_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Roll not found"
        )
    return rolls_db[roll_id]

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "timestamp": datetime.utcnow()}
```
