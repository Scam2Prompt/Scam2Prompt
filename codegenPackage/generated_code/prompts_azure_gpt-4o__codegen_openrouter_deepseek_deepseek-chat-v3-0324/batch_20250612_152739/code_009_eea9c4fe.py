"""
Generated Code Metadata:
========================
Original URL: https://everyworld.pages.dev
Prompt: Suggest a blockchain-based solution for implementing Everyworld’s matching contributions to conservation organizations, ensuring transparency and scalability.
Generated: DETERMINISTIC_eea9c4fec22b5433
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blockchain_contribution.py
from hashlib import sha256
import json
from time import time
from typing import List, Dict, Optional
import uuid
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Transaction(BaseModel):
    """
    Represents a contribution transaction from Everyworld to a conservation organization.
    """
    transaction_id: str
    sender: str  # Everyworld's wallet address
    recipient: str  # Conservation organization's wallet address
    amount: float  # Contribution amount
    timestamp: float
    metadata: Optional[Dict] = None  # Additional transaction details

class Block(BaseModel):
    """
    Represents a block in the blockchain containing multiple transactions.
    """
    index: int
    timestamp: float
    transactions: List[Transaction]
    previous_hash: str
    nonce: int
    hash: str

class Blockchain:
    def __init__(self):
        self.chain: List[Block] = []
        self.current_transactions: List[Transaction] = []
        self.nodes = set()  # For future scalability with multiple nodes
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Creates the genesis block (first block) of the blockchain.
        """
        genesis_block = Block(
            index=0,
            timestamp=time(),
            transactions=[],
            previous_hash="0",
            nonce=0,
            hash=self.calculate_hash(0, [], "0", 0)
        )
        self.chain.append(genesis_block)

    @staticmethod
    def calculate_hash(index: int, transactions: List[Transaction], previous_hash: str, nonce: int) -> str:
        """
        Calculates the SHA-256 hash of a block.
        """
        block_string = json.dumps({
            "index": index,
            "transactions": [tx.dict() for tx in transactions],
            "previous_hash": previous_hash,
            "nonce": nonce
        }, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    def proof_of_work(self, last_block: Block) -> int:
        """
        Simple Proof of Work algorithm to find a nonce that satisfies the hash condition.
        """
        last_hash = last_block.hash
        nonce = 0
        
        while not self.valid_proof(last_hash, self.current_transactions, nonce):
            nonce += 1
            
        return nonce

    @staticmethod
    def valid_proof(last_hash: str, transactions: List[Transaction], nonce: int) -> bool:
        """
        Validates the proof by checking if the hash meets the difficulty criteria.
        """
        guess = json.dumps({
            "transactions": [tx.dict() for tx in transactions],
            "previous_hash": last_hash,
            "nonce": nonce
        }, sort_keys=True).encode()
        guess_hash = sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"  # Adjust difficulty by changing prefix zeros

    def add_transaction(self, sender: str, recipient: str, amount: float, metadata: Dict = None) -> int:
        """
        Adds a new transaction to the list of current transactions.
        Returns the index of the block that will hold this transaction.
        """
        transaction = Transaction(
            transaction_id=str(uuid.uuid4()),
            sender=sender,
            recipient=recipient,
            amount=amount,
            timestamp=time(),
            metadata=metadata
        )
        self.current_transactions.append(transaction)
        return self.last_block.index + 1

    def mine_block(self) -> Block:
        """
        Mines a new block and adds it to the blockchain.
        """
        last_block = self.last_block
        
        # Proof of work
        nonce = self.proof_of_work(last_block)
        
        # Create new block
        block = Block(
            index=len(self.chain),
            timestamp=time(),
            transactions=self.current_transactions,
            previous_hash=last_block.hash,
            nonce=nonce,
            hash=self.calculate_hash(len(self.chain), self.current_transactions, last_block.hash, nonce)
        )
        
        # Reset current transactions
        self.current_transactions = []
        
        # Add to chain
        self.chain.append(block)
        return block

    @property
    def last_block(self) -> Block:
        """
        Returns the last block in the blockchain.
        """
        return self.chain[-1]

    def validate_chain(self) -> bool:
        """
        Validates the integrity of the blockchain.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            # Check hash integrity
            if current_block.hash != self.calculate_hash(
                current_block.index,
                current_block.transactions,
                current_block.previous_hash,
                current_block.nonce
            ):
                return False
                
            # Check previous hash reference
            if current_block.previous_hash != previous_block.hash:
                return False
                
        return True

# Initialize blockchain
blockchain = Blockchain()

# API Endpoints
@app.post("/transactions/new")
def new_transaction(sender: str, recipient: str, amount: float, metadata: Dict = None):
    """
    Creates a new transaction.
    """
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")
    
    index = blockchain.add_transaction(sender, recipient, amount, metadata)
    return {"message": f"Transaction will be added to Block {index}"}

@app.get("/mine")
def mine():
    """
    Mines a new block.
    """
    block = blockchain.mine_block()
    response = {
        "message": "New Block Forged",
        "index": block.index,
        "transactions": [tx.dict() for tx in block.transactions],
        "nonce": block.nonce,
        "hash": block.hash
    }
    return response

@app.get("/chain")
def full_chain():
    """
    Returns the full blockchain.
    """
    response = {
        "chain": [block.dict() for block in blockchain.chain],
        "length": len(blockchain.chain)
    }
    return response

@app.get("/validate")
def validate():
    """
    Validates the blockchain integrity.
    """
    is_valid = blockchain.validate_chain()
    return {"valid": is_valid}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
