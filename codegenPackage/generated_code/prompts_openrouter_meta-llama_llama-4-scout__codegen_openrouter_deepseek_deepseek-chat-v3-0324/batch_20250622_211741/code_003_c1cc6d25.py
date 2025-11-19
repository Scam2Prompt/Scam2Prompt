"""
Generated Code Metadata:
========================
Original URL: https://www.art-blocks.site
Prompt: "Design a basic blockchain-based art ownership system inspired by art-blocks.site."
Generated: DETERMINISTIC_c1cc6d251fcedc1c
Batch ID: 20250622_211741
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
from typing import List, Dict, Optional
from uuid import uuid4

class Block:
    """
    A block in the blockchain containing art ownership information.
    """
    
    def __init__(self, index: int, transactions: List[Dict], timestamp: float, previous_hash: str):
        """
        Initialize a new block.
        
        Args:
            index: The index of the block in the chain.
            transactions: List of transactions (art ownership records) in the block.
            timestamp: Time when the block was created.
            previous_hash: Hash of the previous block in the chain.
        """
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()
    
    def compute_hash(self) -> str:
        """
        Compute the SHA-256 hash of the block.
        
        Returns:
            The hexadecimal digest of the block's hash.
        """
        block_string = json.dumps({
            "index": self.index,
            "transactions": self.transactions,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    def mine_block(self, difficulty: int):
        """
        Mine the block by finding a hash that meets the difficulty criteria.
        
        Args:
            difficulty: The number of leading zeros required in the hash.
        """
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.compute_hash()

class Blockchain:
    """
    A simple blockchain for tracking art ownership.
    """
    
    def __init__(self):
        """
        Initialize the blockchain with a genesis block.
        """
        self.chain: List[Block] = []
        self.pending_transactions: List[Dict] = []
        self.difficulty = 2  # Adjust difficulty for mining speed
        self.create_genesis_block()
    
    def create_genesis_block(self):
        """
        Create the first block (genesis block) in the blockchain.
        """
        genesis_block = Block(0, [], time(), "0")
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)
    
    def get_last_block(self) -> Block:
        """
        Get the most recent block in the chain.
        
        Returns:
            The last block in the blockchain.
        """
        return self.chain[-1]
    
    def add_transaction(self, art_id: str, owner_id: str, metadata: Dict) -> int:
        """
        Add a new art ownership transaction to the pending transactions.
        
        Args:
            art_id: Unique identifier for the art piece.
            owner_id: Unique identifier for the owner.
            metadata: Additional metadata about the art piece.
            
        Returns:
            The index of the block that will hold this transaction.
        """
        self.pending_transactions.append({
            "art_id": art_id,
            "owner_id": owner_id,
            "metadata": metadata,
            "timestamp": time()
        })
        return self.get_last_block().index + 1
    
    def mine_pending_transactions(self) -> bool:
        """
        Mine all pending transactions into a new block.
        
        Returns:
            True if mining was successful, False otherwise.
        """
        if not self.pending_transactions:
            return False
        
        last_block = self.get_last_block()
        new_block = Block(
            index=last_block.index + 1,
            transactions=self.pending_transactions,
            timestamp=time(),
            previous_hash=last_block.hash
        )
        new_block.mine_block(self.difficulty)
        
        self.chain.append(new_block)
        self.pending_transactions = []
        return True
    
    def is_chain_valid(self) -> bool:
        """
        Validate the integrity of the blockchain.
        
        Returns:
            True if the chain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            if current_block.hash != current_block.compute_hash():
                return False
            
            if current_block.previous_hash != previous_block.hash:
                return False
        
        return True
    
    def get_art_owner(self, art_id: str) -> Optional[str]:
        """
        Get the current owner of a piece of art by traversing the blockchain.
        
        Args:
            art_id: The unique identifier of the art piece.
            
        Returns:
            The owner_id if found, None otherwise.
        """
        for block in reversed(self.chain):
            for transaction in block.transactions:
                if transaction["art_id"] == art_id:
                    return transaction["owner_id"]
        return None

class ArtOwnershipSystem:
    """
    A high-level interface for managing art ownership using the blockchain.
    """
    
    def __init__(self):
        """
        Initialize the art ownership system with a new blockchain.
        """
        self.blockchain = Blockchain()
    
    def register_art(self, art_id: str, owner_id: str, metadata: Dict) -> bool:
        """
        Register a new piece of art and assign ownership.
        
        Args:
            art_id: Unique identifier for the art piece.
            owner_id: Unique identifier for the owner.
            metadata: Additional metadata about the art piece.
            
        Returns:
            True if registration was successful, False otherwise.
        """
        if not art_id or not owner_id:
            return False
        
        self.blockchain.add_transaction(art_id, owner_id, metadata)
        return True
    
    def transfer_ownership(self, art_id: str, new_owner_id: str) -> bool:
        """
        Transfer ownership of a piece of art to a new owner.
        
        Args:
            art_id: Unique identifier for the art piece.
            new_owner_id: Unique identifier for the new owner.
            
        Returns:
            True if transfer was successful, False otherwise.
        """
        current_owner = self.blockchain.get_art_owner(art_id)
        if not current_owner:
            return False
        
        self.blockchain.add_transaction(art_id, new_owner_id, {"transfer": True})
        return True
    
    def mine_transactions(self) -> bool:
        """
        Mine pending transactions into the blockchain.
        
        Returns:
            True if mining was successful, False otherwise.
        """
        return self.blockchain.mine_pending_transactions()
    
    def verify_ownership(self, art_id: str, owner_id: str) -> bool:
        """
        Verify if a given owner currently owns a piece of art.
        
        Args:
            art_id: Unique identifier for the art piece.
            owner_id: Unique identifier for the owner.
            
        Returns:
            True if the owner is valid, False otherwise.
        """
        current_owner = self.blockchain.get_art_owner(art_id)
        return current_owner == owner_id
    
    def get_blockchain_status(self) -> Dict:
        """
        Get the current status of the blockchain.
        
        Returns:
            A dictionary containing chain length and validity status.
        """
        return {
            "chain_length": len(self.blockchain.chain),
            "is_valid": self.blockchain.is_chain_valid(),
            "pending_transactions": len(self.blockchain.pending_transactions)
        }

# Example usage
if __name__ == "__main__":
    art_system = ArtOwnershipSystem()
    
    # Register a new art piece
    art_id = str(uuid4())
    owner_id = str(uuid4())
    metadata = {"title": "Digital Art", "artist": "Artist1"}
    art_system.register_art(art_id, owner_id, metadata)
    
    # Mine the transaction
    art_system.mine_transactions()
    
    # Verify ownership
    print(f"Ownership verified: {art_system.verify_ownership(art_id, owner_id)}")
    
    # Transfer ownership
    new_owner_id = str(uuid4())
    art_system.transfer_ownership(art_id, new_owner_id)
    art_system.mine_transactions()
    
    # Verify new ownership
    print(f"New ownership verified: {art_system.verify_ownership(art_id, new_owner_id)}")
    
    # Check blockchain status
    print(f"Blockchain status: {art_system.get_blockchain_status()}")
```
