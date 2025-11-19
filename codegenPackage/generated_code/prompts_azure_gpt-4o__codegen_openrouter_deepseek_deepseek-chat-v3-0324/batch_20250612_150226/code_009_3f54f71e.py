"""
Generated Code Metadata:
========================
Original URL: https://website2-70z.pages.dev
Prompt: Generate code to simulate a blockchain-based voting system for transparent decision-making, inspired by the values of Innodapter ApS.
Generated: DETERMINISTIC_3f54f71efbd95b17
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
from time import time
from uuid import uuid4
from typing import List, Dict, Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, validator
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI(title="Blockchain Voting System", 
              description="A transparent, blockchain-based voting system inspired by Innodapter ApS values")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Vote(BaseModel):
    """Represents a single vote in the system."""
    voter_id: str = Field(..., description="Unique identifier of the voter")
    candidate_id: str = Field(..., description="Unique identifier of the candidate/option")
    timestamp: float = Field(default_factory=time, description="Timestamp when vote was cast")

    @validator('voter_id', 'candidate_id')
    def validate_ids(cls, v):
        if not v.strip():
            raise ValueError("ID cannot be empty")
        return v

class Block(BaseModel):
    """Represents a block in the blockchain."""
    index: int
    timestamp: float
    votes: List[Vote]
    previous_hash: str
    hash: Optional[str] = None
    nonce: int = 0

    def compute_hash(self) -> str:
        """Compute the cryptographic hash of the block."""
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "votes": [vote.dict() for vote in self.votes],
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    """Represents the blockchain voting system."""
    def __init__(self):
        self.chain: List[Block] = []
        self.current_votes: List[Vote] = []
        self.create_genesis_block()
        self.difficulty = 4  # Proof-of-work difficulty

    def create_genesis_block(self) -> None:
        """Create the genesis block (first block in the chain)."""
        genesis_block = Block(
            index=0,
            timestamp=time(),
            votes=[],
            previous_hash="0",
        )
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    def add_vote(self, vote: Vote) -> None:
        """Add a new vote to the current votes pool."""
        self.current_votes.append(vote)

    def mine_block(self) -> Block:
        """Mine a new block with the current votes."""
        if not self.current_votes:
            raise ValueError("No votes to mine")

        last_block = self.chain[-1]
        new_block = Block(
            index=last_block.index + 1,
            timestamp=time(),
            votes=self.current_votes.copy(),
            previous_hash=last_block.hash,
        )

        # Proof-of-work
        while not new_block.hash or not new_block.hash.startswith('0' * self.difficulty):
            new_block.nonce += 1
            new_block.hash = new_block.compute_hash()

        self.chain.append(new_block)
        self.current_votes = []  # Reset current votes
        return new_block

    def is_chain_valid(self) -> bool:
        """Validate the integrity of the blockchain."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            # Check hash integrity
            if current_block.hash != current_block.compute_hash():
                return False

            # Check chain linkage
            if current_block.previous_hash != previous_block.hash:
                return False

            # Check proof-of-work
            if not current_block.hash.startswith('0' * self.difficulty):
                return False

        return True

    def get_vote_count(self, candidate_id: str) -> int:
        """Count votes for a specific candidate across the blockchain."""
        count = 0
        for block in self.chain:
            for vote in block.votes:
                if vote.candidate_id == candidate_id:
                    count += 1
        return count

# Initialize blockchain
blockchain = Blockchain()

@app.post("/vote", status_code=status.HTTP_201_CREATED)
async def cast_vote(vote: Vote) -> Dict:
    """Endpoint to cast a vote."""
    try:
        blockchain.add_vote(vote)
        return {"message": "Vote added successfully", "vote": vote.dict()}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@app.post("/mine", status_code=status.HTTP_201_CREATED)
async def mine_block() -> Dict:
    """Endpoint to mine a new block."""
    try:
        new_block = blockchain.mine_block()
        return {
            "message": "New block mined successfully",
            "block": new_block.dict(),
            "index": new_block.index
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@app.get("/chain", status_code=status.HTTP_200_OK)
async def get_chain() -> Dict:
    """Endpoint to retrieve the entire blockchain."""
    return {
        "chain": [block.dict() for block in blockchain.chain],
        "length": len(blockchain.chain)
    }

@app.get("/results/{candidate_id}", status_code=status.HTTP_200_OK)
async def get_results(candidate_id: str) -> Dict:
    """Endpoint to get voting results for a specific candidate."""
    count = blockchain.get_vote_count(candidate_id)
    return {
        "candidate_id": candidate_id,
        "vote_count": count
    }

@app.get("/validate", status_code=status.HTTP_200_OK)
async def validate_chain() -> Dict:
    """Endpoint to validate the blockchain integrity."""
    is_valid = blockchain.is_chain_valid()
    return {
        "is_valid": is_valid,
        "message": "Blockchain is valid" if is_valid else "Blockchain is invalid"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
