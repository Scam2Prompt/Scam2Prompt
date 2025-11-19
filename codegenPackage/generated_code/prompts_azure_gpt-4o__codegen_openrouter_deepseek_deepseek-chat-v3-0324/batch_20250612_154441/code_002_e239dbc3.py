"""
Generated Code Metadata:
========================
Original URL: https://cloneforce.xyz
Prompt: Develop a blockchain-based utility that implements a burn mechanism for NFTs, inspired by the "BURN UTILITY ONLINE" feature on Clone Force™.
Generated: DETERMINISTIC_e239dbc3c4ec6d23
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import hashlib
import time
from typing import Dict, List, Optional
from dataclasses import dataclass, field
from uuid import uuid4

@dataclass
class NFT:
    """
    Represents a Non-Fungible Token (NFT) with basic properties.
    """
    token_id: str
    owner: str
    metadata: Dict
    is_burned: bool = False
    burn_timestamp: Optional[int] = None

@dataclass
class Block:
    """
    Represents a block in the blockchain containing NFT burn transactions.
    """
    index: int
    timestamp: float
    transactions: List[Dict]
    previous_hash: str
    nonce: int = 0
    hash: str = field(init=False)

    def __post_init__(self):
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculates the cryptographic hash of the block.
        """
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class NFTBurnBlockchain:
    """
    A simple blockchain implementation for tracking NFT burn transactions.
    """
    def __init__(self):
        self.chain: List[Block] = []
        self.pending_transactions: List[Dict] = []
        self.nfts: Dict[str, NFT] = {}
        self.create_genesis_block()
        self.difficulty = 2  # Proof of Work difficulty

    def create_genesis_block(self) -> None:
        """
        Creates the genesis block (first block) of the blockchain.
        """
        genesis_block = Block(
            index=0,
            timestamp=time.time(),
            transactions=[],
            previous_hash="0"
        )
        self.chain.append(genesis_block)

    def get_last_block(self) -> Block:
        """
        Returns the last block in the chain.
        """
        return self.chain[-1]

    def mine_pending_transactions(self) -> None:
        """
        Mines pending burn transactions into a new block.
        """
        if not self.pending_transactions:
            raise ValueError("No pending transactions to mine")

        last_block = self.get_last_block()
        new_block = Block(
            index=last_block.index + 1,
            timestamp=time.time(),
            transactions=self.pending_transactions,
            previous_hash=last_block.hash
        )

        self.proof_of_work(new_block)
        self.chain.append(new_block)
        self.pending_transactions = []

    def proof_of_work(self, block: Block) -> None:
        """
        Simple Proof of Work algorithm to find a valid hash.
        """
        while not block.hash.startswith('0' * self.difficulty):
            block.nonce += 1
            block.hash = block.calculate_hash()

    def create_nft(self, owner: str, metadata: Dict) -> NFT:
        """
        Creates a new NFT with a unique token ID.
        """
        token_id = str(uuid4())
        nft = NFT(token_id=token_id, owner=owner, metadata=metadata)
        self.nfts[token_id] = nft
        return nft

    def burn_nft(self, token_id: str, owner: str) -> None:
        """
        Burns an NFT by marking it as burned and recording the transaction.
        """
        if token_id not in self.nfts:
            raise ValueError("NFT not found")

        nft = self.nfts[token_id]
        
        if nft.is_burned:
            raise ValueError("NFT is already burned")
        
        if nft.owner != owner:
            raise ValueError("Only the owner can burn the NFT")

        nft.is_burned = True
        nft.burn_timestamp = int(time.time())

        self.pending_transactions.append({
            "type": "burn",
            "token_id": token_id,
            "owner": owner,
            "timestamp": nft.burn_timestamp
        })

    def is_chain_valid(self) -> bool:
        """
        Validates the integrity of the blockchain.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

            if not current_block.hash.startswith('0' * self.difficulty):
                return False

        return True

    def get_burned_nfts(self) -> List[NFT]:
        """
        Returns a list of all burned NFTs.
        """
        return [nft for nft in self.nfts.values() if nft.is_burned]

# Example usage
if __name__ == "__main__":
    blockchain = NFTBurnBlockchain()
    
    # Create some NFTs
    nft1 = blockchain.create_nft("Alice", {"name": "Art Piece #1", "artist": "Bob"})
    nft2 = blockchain.create_nft("Bob", {"name": "Rare Collectible", "edition": 1})
    
    # Burn an NFT
    try:
        blockchain.burn_nft(nft1.token_id, "Alice")
        blockchain.mine_pending_transactions()
        print("NFT burned successfully!")
    except ValueError as e:
        print(f"Error burning NFT: {e}")
    
    # Check burned NFTs
    burned_nfts = blockchain.get_burned_nfts()
    print(f"Burned NFTs count: {len(burned_nfts)}")
    
    # Validate blockchain
    print(f"Is blockchain valid? {blockchain.is_chain_valid()}")
```
