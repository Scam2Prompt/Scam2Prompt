"""
Generated Code Metadata:
========================
Original URL: https://pepeunchainedclaims.pages.dev
Prompt: Create a tutorial for building a Layer 2 blockchain similar to Pepe Unchained, focusing on features like faster transaction speeds and lower fees.
Generated: DETERMINISTIC_fdf49252f37056bb
Batch ID: 20250612_151038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Layer 2 Blockchain Implementation Tutorial
# Inspired by Pepe Unchained - Focus on Speed and Low Fees

import hashlib
import json
from time import time
from typing import List, Dict, Optional
from dataclasses import dataclass
import pickle
from collections import defaultdict
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature

# Constants
DIFFICULTY = 4  # Lower difficulty for faster block processing
BLOCK_TIME = 2  # Target block time in seconds
MAX_TRANSACTIONS_PER_BLOCK = 500  # Higher throughput
INITIAL_REWARD = 50  # Initial block reward
REWARD_HALVING_INTERVAL = 210000  # Blocks until reward halves
MEMPOOL_LIMIT = 10000  # Max transactions in mempool

@dataclass
class Transaction:
    sender: str
    receiver: str
    amount: float
    fee: float  # Lower fees for L2
    signature: bytes
    timestamp: float = time()

    def serialize(self) -> bytes:
        """Serialize transaction data for hashing/signing"""
        return json.dumps({
            'sender': self.sender,
            'receiver': self.receiver,
            'amount': self.amount,
            'fee': self.fee,
            'timestamp': self.timestamp
        }, sort_keys=True).encode('utf-8')

    def validate(self) -> bool:
        """Validate transaction signature"""
        try:
            public_key = serialization.load_pem_public_key(
                self.sender.encode('utf-8')
            )
            public_key.verify(
                self.signature,
                self.serialize(),
                ec.ECDSA(hashes.SHA256())
            )
            return True
        except (InvalidSignature, ValueError):
            return False

@dataclass
class Block:
    index: int
    timestamp: float
    transactions: List[Transaction]
    previous_hash: str
    nonce: int = 0
    miner: str = None

    @property
    def hash(self) -> str:
        """Calculate block hash"""
        block_string = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'transactions': [tx.serialize().hex() for tx in self.transactions],
            'previous_hash': self.previous_hash,
            'nonce': self.nonce,
            'miner': self.miner
        }, sort_keys=True).encode('utf-8')
        return hashlib.sha256(block_string).hexdigest()

    def mine(self, difficulty: int = DIFFICULTY) -> None:
        """Mine block with given difficulty"""
        while not self.hash.startswith('0' * difficulty):
            self.nonce += 1

class Layer2Blockchain:
    def __init__(self):
        self.chain: List[Block] = []
        self.mempool: List[Transaction] = []
        self.pending_transactions: List[Transaction] = []
        self.state: Dict[str, float] = defaultdict(float)  # Account balances
        self.create_genesis_block()

    def create_genesis_block(self) -> None:
        """Create the genesis block"""
        genesis_block = Block(
            index=0,
            timestamp=time(),
            transactions=[],
            previous_hash="0"
        )
        genesis_block.mine()
        self.chain.append(genesis_block)

    @property
    def last_block(self) -> Block:
        """Get last block in chain"""
        return self.chain[-1]

    def add_transaction(self, transaction: Transaction) -> bool:
        """Add transaction to mempool if valid"""
        if len(self.mempool) >= MEMPOOL_LIMIT:
            return False
        
        if not transaction.validate():
            return False
            
        # Check sender balance (simplified for demo)
        if self.state.get(transaction.sender, 0) < (transaction.amount + transaction.fee):
            return False
            
        self.mempool.append(transaction)
        return True

    def create_block(self, miner_address: str) -> Block:
        """Create new block with transactions from mempool"""
        # Sort by highest fee first (priority for L2)
        sorted_transactions = sorted(
            self.mempool,
            key=lambda tx: tx.fee,
            reverse=True
        )[:MAX_TRANSACTIONS_PER_BLOCK]

        block = Block(
            index=len(self.chain),
            timestamp=time(),
            transactions=sorted_transactions,
            previous_hash=self.last_block.hash,
            miner=miner_address
        )
        return block

    def add_block(self, block: Block) -> bool:
        """Add mined block to chain"""
        # Validate block
        if block.previous_hash != self.last_block.hash:
            return False
            
        if not block.hash.startswith('0' * DIFFICULTY):
            return False
            
        # Process transactions
        for tx in block.transactions:
            self.state[tx.sender] -= (tx.amount + tx.fee)
            self.state[tx.receiver] += tx.amount
            self.mempool.remove(tx)  # Remove from mempool
            
        # Miner reward (simplified)
        reward = INITIAL_REWARD // (2 ** (len(self.chain) // REWARD_HALVING_INTERVAL))
        self.state[block.miner] += reward + sum(tx.fee for tx in block.transactions)
        
        self.chain.append(block)
        return True

    def validate_chain(self) -> bool:
        """Validate entire blockchain"""
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            
            if current.previous_hash != previous.hash:
                return False
                
            if not current.hash.startswith('0' * DIFFICULTY):
                return False
                
        return True

class StateChannel:
    """Implementation of payment channels for off-chain transactions"""
    def __init__(self, participant1: str, participant2: str, deposit: float):
        self.participants = {participant1: deposit, participant2: deposit}
        self.balances = {participant1: deposit, participant2: deposit}
        self.nonce = 0
        self.signatures = {}
        
    def update_balance(self, updates: Dict[str, float], signatures: Dict[str, bytes]) -> bool:
        """Update channel state with signed balance updates"""
        self.nonce += 1
        for participant, new_balance in updates.items():
            if participant not in self.participants:
                return False
            self.balances[participant] = new_balance
        
        self.signatures = signatures
        return True
        
    def close_channel(self, blockchain: Layer2Blockchain) -> bool:
        """Settle final balances on main chain"""
        # Verify all signatures
        for participant, sig in self.signatures.items():
            # In real implementation, would verify signatures
            pass
            
        # Create settlement transactions
        for participant, balance in self.balances.items():
            # Simplified - in reality would create proper transactions
            blockchain.state[participant] += balance
            
        return True

# Example usage
if __name__ == "__main__":
    # Initialize blockchain
    blockchain = Layer2Blockchain()
    
    # Generate some test keys (in production, use proper key generation)
    private_key = ec.generate_private_key(ec.SECP256K1())
    public_key = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode('utf-8')
    
    # Create and sign a transaction
    tx_data = {
        'sender': public_key,
        'receiver': 'recipient_address',
        'amount': 10.0,
        'fee': 0.01  # Low fee for L2
    }
    
    tx = Transaction(**tx_data)
    signature = private_key.sign(
        tx.serialize(),
        ec.ECDSA(hashes.SHA256())
    )
    tx.signature = signature
    
    # Add transaction to mempool
    if blockchain.add_transaction(tx):
        print("Transaction added to mempool")
    
    # Mine a block
    new_block = blockchain.create_block(miner_address="miner_address")
    new_block.mine()
    
    if blockchain.add_block(new_block):
        print("New block added to chain")
    
    # Validate chain
    if blockchain.validate_chain():
        print("Blockchain is valid")
```
