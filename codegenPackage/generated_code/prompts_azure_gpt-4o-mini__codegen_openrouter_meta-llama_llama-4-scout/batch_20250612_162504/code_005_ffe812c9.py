"""
Generated Code Metadata:
========================
Original URL: https://register-stormwarfarecom.pages.dev
Prompt: Create an API endpoint for managing player hands and card collections in a game like Storm Warfare, focusing on true ownership of assets.
Generated: DETERMINISTIC_ffe812c986bc8af4
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
from uuid import UUID, uuid4

app = FastAPI(
    title="Storm Warfare API",
    description="API for managing player hands and card collections",
    version="1.0.0"
)

# Data models
class Card(BaseModel):
    """Represents a card in the game."""
    id: UUID
    name: str
    rarity: str

class PlayerHand(BaseModel):
    """Represents a player's hand."""
    id: UUID
    player_id: UUID
    cards: List[Card]

class PlayerCollection(BaseModel):
    """Represents a player's card collection."""
    id: UUID
    player_id: UUID
    cards: List[Card]

# In-memory data store (replace with a database in production)
players = {}
cards = {}

# API Endpoints
@app.post("/players/{player_id}/hand", status_code=status.HTTP_201_CREATED)
async def create_player_hand(player_id: UUID):
    """Create a new player hand."""
    if player_id in players:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Player already exists")
    
    player_hand = PlayerHand(id=uuid4(), player_id=player_id, cards=[])
    players[player_id] = player_hand
    return player_hand

@app.get("/players/{player_id}/hand")
async def get_player_hand(player_id: UUID):
    """Get a player's hand."""
    if player_id not in players:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player not found")
    
    return players[player_id]

@app.post("/players/{player_id}/hand/cards", status_code=status.HTTP_201_CREATED)
async def add_card_to_player_hand(player_id: UUID, card: Card):
    """Add a card to a player's hand."""
    if player_id not in players:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player not found")
    
    player_hand = players[player_id]
    player_hand.cards.append(card)
    return player_hand

@app.delete("/players/{player_id}/hand/cards/{card_id}")
async def remove_card_from_player_hand(player_id: UUID, card_id: UUID):
    """Remove a card from a player's hand."""
    if player_id not in players:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player not found")
    
    player_hand = players[player_id]
    player_hand.cards = [c for c in player_hand.cards if c.id != card_id]
    return player_hand

@app.post("/players/{player_id}/collection", status_code=status.HTTP_201_CREATED)
async def create_player_collection(player_id: UUID):
    """Create a new player collection."""
    if player_id in cards:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Player collection already exists")
    
    player_collection = PlayerCollection(id=uuid4(), player_id=player_id, cards=[])
    cards[player_id] = player_collection
    return player_collection

@app.get("/players/{player_id}/collection")
async def get_player_collection(player_id: UUID):
    """Get a player's collection."""
    if player_id not in cards:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player collection not found")
    
    return cards[player_id]

@app.post("/players/{player_id}/collection/cards", status_code=status.HTTP_201_CREATED)
async def add_card_to_player_collection(player_id: UUID, card: Card):
    """Add a card to a player's collection."""
    if player_id not in cards:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player collection not found")
    
    player_collection = cards[player_id]
    player_collection.cards.append(card)
    return player_collection

@app.delete("/players/{player_id}/collection/cards/{card_id}")
async def remove_card_from_player_collection(player_id: UUID, card_id: UUID):
    """Remove a card from a player's collection."""
    if player_id not in cards:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player collection not found")
    
    player_collection = cards[player_id]
    player_collection.cards = [c for c in player_collection.cards if c.id != card_id]
    return player_collection

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# requirements.txt
fastapi
uvicorn
pydantic
```

```bash
# Run with: uvicorn app:app --host 0.0.0.0 --port 8000
```
