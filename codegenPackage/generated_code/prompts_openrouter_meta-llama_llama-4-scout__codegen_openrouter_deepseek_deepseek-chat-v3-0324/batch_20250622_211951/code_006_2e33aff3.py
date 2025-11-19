"""
Generated Code Metadata:
========================
Original URL: https://encodeencryptor.pages.dev
Prompt: What are some best practices for implementing a secure and decentralized protocol for rectifying issues related to NFTs, such as minting and transfer problems?
Generated: DETERMINISTIC_2e33aff346ee55a5
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Secure and Decentralized NFT Protocol Implementation

import hashlib
import json
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import ecdsa
from ecdsa import SigningKey, VerifyingKey
import uuid
import time

# Constants
BLOCK_TIME = 60  # seconds
MAX_RETRIES = 3
VERSION = "1.0"

@dataclass
class NFT:
    token_id: str
    owner: str
    metadata: Dict
    created_at: float
    last_updated: float

@dataclass
class Transaction:
    tx_id: str
    sender: str
    receiver: str
    token_id: str
    action: str  # "MINT", "TRANSFER", "BURN", "CORRECT"
    status: str  # "PENDING", "COMPLETED", "FAILED"
    signature: str
    timestamp: float
    correction_data: Optional[Dict] = None

class NFTProtocol:
    def __init__(self):
        self.chain: List[Dict] = []
        self.pending_transactions: List[Transaction] = []
        self.nfts: Dict[str, NFT] = {}
        self.node_id = str(uuid.uuid4())
        
    def initialize_genesis_block(self):
        """Initialize the blockchain with a genesis block"""
        genesis_block = {
            'index': 0,
            'timestamp': time.time(),
            'transactions': [],
            'previous_hash': '0',
            'nonce': 0,
            'hash': self._calculate_hash(0, '0', [], 0)
        }
        self.chain.append(genesis_block)
        
    def _calculate_hash(self, index: int, previous_hash: str, transactions: List[Transaction], nonce: int) -> str:
        """Calculate SHA-256 hash of a block"""
        block_string = json.dumps({
            'index': index,
            'previous_hash': previous_hash,
            'transactions': [tx.__dict__ for tx in transactions],
            'nonce': nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    def _verify_signature(self, public_key: str, signature: str, message: str) -> bool:
        """Verify ECDSA signature"""
        try:
            vk = VerifyingKey.from_string(bytes.fromhex(public_key), curve=ecdsa.SECP256k1)
            return vk.verify(bytes.fromhex(signature), message.encode())
        except Exception:
            return False
    
    def _validate_transaction(self, tx: Transaction) -> bool:
        """Validate transaction structure and signature"""
        if tx.action not in ["MINT", "TRANSFER", "BURN", "CORRECT"]:
            return False
            
        if tx.action == "MINT" and tx.token_id in self.nfts:
            return False
            
        if tx.action in ["TRANSFER", "BURN", "CORRECT"]:
            if tx.token_id not in self.nfts:
                return False
            if tx.sender != self.nfts[tx.token_id].owner:
                return False
                
        message = f"{tx.tx_id}{tx.sender}{tx.receiver}{tx.token_id}{tx.action}{tx.timestamp}"
        return self._verify_signature(tx.sender, tx.signature, message)
    
    def add_transaction(self, tx: Transaction) -> bool:
        """Add a transaction to pending transactions after validation"""
        if not self._validate_transaction(tx):
            return False
            
        self.pending_transactions.append(tx)
        return True
    
    def mine_block(self) -> bool:
        """Mine a new block with pending transactions"""
        if not self.pending_transactions:
            return False
            
        last_block = self.chain[-1]
        new_block = {
            'index': last_block['index'] + 1,
            'timestamp': time.time(),
            'transactions': [],
            'previous_hash': last_block['hash'],
            'nonce': 0
        }
        
        # Process transactions
        for tx in self.pending_transactions:
            if tx.status != "PENDING":
                continue
                
            try:
                if tx.action == "MINT":
                    self._process_mint(tx)
                elif tx.action == "TRANSFER":
                    self._process_transfer(tx)
                elif tx.action == "BURN":
                    self._process_burn(tx)
                elif tx.action == "CORRECT":
                    self._process_correction(tx)
                    
                tx.status = "COMPLETED"
                new_block['transactions'].append(tx)
            except Exception as e:
                tx.status = "FAILED"
                print(f"Transaction {tx.tx_id} failed: {str(e)}")
        
        # Proof of Work
        new_block['hash'] = self._calculate_hash(
            new_block['index'],
            new_block['previous_hash'],
            new_block['transactions'],
            new_block['nonce']
        )
        
        self.chain.append(new_block)
        self.pending_transactions = [
            tx for tx in self.pending_transactions 
            if tx.status == "PENDING"
        ]
        return True
    
    def _process_mint(self, tx: Transaction):
        """Process NFT minting transaction"""
        if tx.token_id in self.nfts:
            raise ValueError("Token ID already exists")
            
        self.nfts[tx.token_id] = NFT(
            token_id=tx.token_id,
            owner=tx.receiver,
            metadata=tx.correction_data or {},
            created_at=time.time(),
            last_updated=time.time()
        )
    
    def _process_transfer(self, tx: Transaction):
        """Process NFT transfer transaction"""
        if tx.token_id not in self.nfts:
            raise ValueError("Token ID doesn't exist")
            
        self.nfts[tx.token_id].owner = tx.receiver
        self.nfts[tx.token_id].last_updated = time.time()
    
    def _process_burn(self, tx: Transaction):
        """Process NFT burn transaction"""
        if tx.token_id not in self.nfts:
            raise ValueError("Token ID doesn't exist")
            
        del self.nfts[tx.token_id]
    
    def _process_correction(self, tx: Transaction):
        """Process NFT correction transaction"""
        if tx.token_id not in self.nfts:
            raise ValueError("Token ID doesn't exist")
            
        if not tx.correction_data:
            raise ValueError("Correction data required")
            
        # Update metadata with correction data
        self.nfts[tx.token_id].metadata.update(tx.correction_data)
        self.nfts[tx.token_id].last_updated = time.time()
    
    def verify_chain(self) -> bool:
        """Verify the integrity of the blockchain"""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            # Check hash linkage
            if current_block['previous_hash'] != previous_block['hash']:
                return False
                
            # Check hash validity
            calculated_hash = self._calculate_hash(
                current_block['index'],
                current_block['previous_hash'],
                current_block['transactions'],
                current_block['nonce']
            )
            if current_block['hash'] != calculated_hash:
                return False
                
        return True
    
    def get_nft_history(self, token_id: str) -> List[Transaction]:
        """Get transaction history for an NFT"""
        history = []
        for block in self.chain:
            for tx in block['transactions']:
                if tx['token_id'] == token_id:
                    history.append(tx)
        return history

# Example usage
if __name__ == "__main__":
    protocol = NFTProtocol()
    protocol.initialize_genesis_block()
    
    # Generate test keys
    sk = SigningKey.generate(curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    public_key = vk.to_string().hex()
    
    # Create and sign a mint transaction
    tx_id = str(uuid.uuid4())
    message = f"{tx_id}{public_key}{public_key}test123MINT{time.time()}"
    signature = sk.sign(message.encode()).hex()
    
    mint_tx = Transaction(
        tx_id=tx_id,
        sender=public_key,
        receiver=public_key,
        token_id="test123",
        action="MINT",
        status="PENDING",
        signature=signature,
        timestamp=time.time(),
        correction_data={"name": "Test NFT", "description": "Example NFT"}
    )
    
    protocol.add_transaction(mint_tx)
    protocol.mine_block()
    
    print("Blockchain valid:", protocol.verify_chain())
    print("NFT exists:", "test123" in protocol.nfts)
```
