"""
Generated Code Metadata:
========================
Original URL: https://nhshsvsgdg.pages.dev
Prompt: Design a system to manage NFTs, including minting, transferring, and receiving, using a blockchain-based application.
Generated: DETERMINISTIC_a489baf875910152
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
"""
NFT Management System using Blockchain

This module provides functionality to mint, transfer, and receive NFTs
using a simplified blockchain-based system.
"""

import hashlib
import json
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class NFT:
    """
    Represents a Non-Fungible Token (NFT) with unique properties.
    
    Attributes:
        token_id (str): Unique identifier for the NFT
        owner (str): Current owner's address
        metadata (dict): Metadata associated with the NFT
        created_at (datetime): Timestamp of creation
    """
    
    def __init__(self, token_id: str, owner: str, metadata: dict):
        """
        Initialize a new NFT.
        
        Args:
            token_id: Unique identifier for the NFT
            owner: Owner's blockchain address
            metadata: Dictionary containing NFT metadata
        """
        self.token_id = token_id
        self.owner = owner
        self.metadata = metadata
        self.created_at = datetime.utcnow()
    
    def to_dict(self) -> dict:
        """Convert NFT to dictionary for serialization."""
        return {
            'token_id': self.token_id,
            'owner': self.owner,
            'metadata': self.metadata,
            'created_at': self.created_at.isoformat()
        }

class Blockchain:
    """
    Simplified blockchain implementation for NFT management.
    
    Attributes:
        chain (List[dict]): List of blocks in the blockchain
        current_transactions (List[dict]): Current transactions to be mined
        nfts (Dict[str, NFT]): Mapping of token_id to NFT
    """
    
    def __init__(self):
        """Initialize the blockchain with genesis block."""
        self.chain = []
        self.current_transactions = []
        self.nfts = {}
        self.create_block(previous_hash='1', proof=100)  # Genesis block
    
    def create_block(self, proof: int, previous_hash: Optional[str]) -> dict:
        """
        Create a new block in the blockchain.
        
        Args:
            proof: The proof given by the Proof of Work algorithm
            previous_hash: Hash of previous block
            
        Returns:
            New block dictionary
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': datetime.utcnow().isoformat(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        
        self.current_transactions = []
        self.chain.append(block)
        return block
    
    def create_transaction(self, sender: str, recipient: str, token_id: str) -> int:
        """
        Creates a new transaction to transfer an NFT.
        
        Args:
            sender: Sender's address
            recipient: Recipient's address
            token_id: NFT to transfer
            
        Returns:
            Index of the block that will hold this transaction
            
        Raises:
            ValueError: If NFT doesn't exist or sender isn't owner
        """
        if token_id not in self.nfts:
            raise ValueError("NFT does not exist")
        
        if self.nfts[token_id].owner != sender:
            raise ValueError("Sender is not the owner of this NFT")
        
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'token_id': token_id,
            'timestamp': datetime.utcnow().isoformat()
        })
        
        return self.last_block['index'] + 1
    
    def mint_nft(self, owner: str, metadata: dict) -> NFT:
        """
        Mint a new NFT and assign ownership.
        
        Args:
            owner: Owner's address
            metadata: NFT metadata
            
        Returns:
            The newly created NFT
        """
        token_id = hashlib.sha256(
            (owner + datetime.utcnow().isoformat()).encode()
        ).hexdigest()
        
        nft = NFT(token_id, owner, metadata)
        self.nfts[token_id] = nft
        
        # Record minting as a transaction
        self.current_transactions.append({
            'sender': '0',  # System address
            'recipient': owner,
            'token_id': token_id,
            'timestamp': datetime.utcnow().isoformat()
        })
        
        return nft
    
    def transfer_nft(self, sender: str, recipient: str, token_id: str) -> bool:
        """
        Transfer ownership of an NFT.
        
        Args:
            sender: Current owner's address
            recipient: New owner's address
            token_id: NFT to transfer
            
        Returns:
            True if transfer was successful
            
        Raises:
            ValueError: If NFT doesn't exist or sender isn't owner
        """
        if token_id not in self.nfts:
            raise ValueError("NFT does not exist")
        
        if self.nfts[token_id].owner != sender:
            raise ValueError("Sender is not the owner of this NFT")
        
        self.nfts[token_id].owner = recipient
        self.create_transaction(sender, recipient, token_id)
        return True
    
    def get_nft(self, token_id: str) -> Optional[NFT]:
        """
        Retrieve an NFT by its token_id.
        
        Args:
            token_id: Unique identifier of the NFT
            
        Returns:
            NFT object if found, None otherwise
        """
        return self.nfts.get(token_id)
    
    def get_owned_nfts(self, owner: str) -> List[NFT]:
        """
        Get all NFTs owned by a specific address.
        
        Args:
            owner: Owner's address
            
        Returns:
            List of NFTs owned by the address
        """
        return [nft for nft in self.nfts.values() if nft.owner == owner]
    
    @property
    def last_block(self) -> dict:
        """Get the last block in the chain."""
        return self.chain[-1]
    
    @staticmethod
    def hash(block: dict) -> str:
        """
        Creates a SHA-256 hash of a block.
        
        Args:
            block: Block dictionary
            
        Returns:
            Hex digest of the block
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    def proof_of_work(self, last_proof: int) -> int:
        """
        Simple Proof of Work algorithm for demonstration purposes.
        
        Args:
            last_proof: Previous proof
            
        Returns:
            New proof
        """
        proof = 0
        while not self.valid_proof(last_proof, proof):
            proof += 1
        return proof
    
    @staticmethod
    def valid_proof(last_proof: int, proof: int) -> bool:
        """
        Validates the Proof of Work.
        
        Args:
            last_proof: Previous proof
            proof: Current proof
            
        Returns:
            True if correct, False if not
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

class NFTManager:
    """
    High-level interface for NFT management operations.
    """
    
    def __init__(self):
        self.blockchain = Blockchain()
    
    def mint(self, owner: str, metadata: dict) -> Tuple[NFT, dict]:
        """
        Mint a new NFT and mine a block.
        
        Args:
            owner: Owner's address
            metadata: NFT metadata
            
        Returns:
            Tuple of (NFT, new_block)
        """
        nft = self.blockchain.mint_nft(owner, metadata)
        last_block = self.blockchain.last_block
        proof = self.blockchain.proof_of_work(last_block['proof'])
        new_block = self.blockchain.create_block(proof, None)
        return nft, new_block
    
    def transfer(self, sender: str, recipient: str, token_id: str) -> Tuple[bool, dict]:
        """
        Transfer an NFT and mine a block.
        
        Args:
            sender: Current owner's address
            recipient: New owner's address
            token_id: NFT to transfer
            
        Returns:
            Tuple of (success, new_block)
        """
        success = self.blockchain.transfer_nft(sender, recipient, token_id)
        last_block = self.blockchain.last_block
        proof = self.blockchain.proof_of_work(last_block['proof'])
        new_block = self.blockchain.create_block(proof, None)
        return success, new_block
    
    def get_nft_info(self, token_id: str) -> Optional[dict]:
        """
        Get NFT information.
        
        Args:
            token_id: NFT identifier
            
        Returns:
            NFT info as dict if found, None otherwise
        """
        nft = self.blockchain.get_nft(token_id)
        return nft.to_dict() if nft else None
    
    def get_owner_nfts(self, owner: str) -> List[dict]:
        """
        Get all NFTs owned by an address.
        
        Args:
            owner: Owner's address
            
        Returns:
            List of NFT dictionaries
        """
        return [nft.to_dict() for nft
