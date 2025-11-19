"""
Generated Code Metadata:
========================
Original URL: https://gasprofitsoftware.com
Prompt: Write Python code to simulate peer-to-peer transactions using blockchain technology, incorporating features like enhanced security with cryptography as described on the Gas Profit platform.
Generated: DETERMINISTIC_fdace3428d8e2894
Batch ID: 20250612_150130
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
from typing import List, Dict, Any, Optional
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption, PublicFormat
from cryptography.hazmat.backends import default_backend

class Transaction:
    """Represents a single transaction between two parties."""
    
    def __init__(self, sender: str, recipient: str, amount: float, signature: str = None):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = signature
        self.transaction_id = str(uuid4()).replace('-', '')
        self.timestamp = time()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert transaction to dictionary for hashing/serialization."""
        return {
            'transaction_id': self.transaction_id,
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount,
            'timestamp': self.timestamp
        }
    
    def sign_transaction(self, private_key: rsa.RSAPrivateKey) -> None:
        """Sign the transaction with the sender's private key."""
        transaction_dict = self.to_dict()
        transaction_bytes = json.dumps(transaction_dict, sort_keys=True).encode()
        
        signature = private_key.sign(
            transaction_bytes,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        self.signature = signature.hex()
    
    def verify_signature(self, public_key: rsa.RSAPublicKey) -> bool:
        """Verify the transaction signature with the sender's public key."""
        if not self.signature:
            return False
        
        transaction_dict = self.to_dict()
        transaction_bytes = json.dumps(transaction_dict, sort_keys=True).encode()
        signature_bytes = bytes.fromhex(self.signature)
        
        try:
            public_key.verify(
                signature_bytes,
                transaction_bytes,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception:
            return False

class Block:
    """Represents a block in the blockchain."""
    
    def __init__(self, index: int, transactions: List[Transaction], previous_hash: str, nonce: int = 0):
        self.index = index
        self.transactions = transactions
        self.timestamp = time()
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()
    
    def calculate_hash(self) -> str:
        """Calculate the SHA-256 hash of the block."""
        block_string = json.dumps({
            'index': self.index,
            'transactions': [tx.to_dict() for tx in self.transactions],
            'timestamp': self.timestamp,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    def mine_block(self, difficulty: int) -> None:
        """Mine the block by finding a nonce that satisfies the difficulty."""
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    """Represents the blockchain network."""
    
    def __init__(self):
        self.chain: List[Block] = []
        self.pending_transactions: List[Transaction] = []
        self.difficulty = 4  # Adjust for production
        self.mining_reward = 10  # Reward for mining a block
        self.generate_genesis_block()
    
    def generate_genesis_block(self) -> None:
        """Create the genesis block (first block in the chain)."""
        genesis_block = Block(0, [], "0")
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)
    
    def get_last_block(self) -> Block:
        """Get the most recent block in the chain."""
        return self.chain[-1]
    
    def add_transaction(self, transaction: Transaction, public_key: rsa.RSAPublicKey) -> bool:
        """Add a new transaction to the pending transactions list."""
        if not transaction.verify_signature(public_key):
            return False
        
        self.pending_transactions.append(transaction)
        return True
    
    def mine_pending_transactions(self, miner_address: str) -> None:
        """Mine all pending transactions and add them to the blockchain."""
        if not self.pending_transactions:
            return
        
        new_block = Block(
            len(self.chain),
            self.pending_transactions,
            self.get_last_block().hash
        )
        new_block.mine_block(self.difficulty)
        
        self.chain.append(new_block)
        self.pending_transactions = [
            Transaction("network", miner_address, self.mining_reward)
        ]
    
    def is_chain_valid(self) -> bool:
        """Validate the integrity of the blockchain."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            # Check block hash integrity
            if current_block.hash != current_block.calculate_hash():
                return False
            
            # Check chain linkage
            if current_block.previous_hash != previous_block.hash:
                return False
            
            # Verify all transactions in the block
            for tx in current_block.transactions:
                if tx.sender == "network":  # Skip mining rewards
                    continue
                
                # In a real implementation, we'd need to get the public key from the sender's address
                # For this simulation, we'll assume all transactions are valid
                pass
        
        return True
    
    def get_balance(self, address: str) -> float:
        """Get the balance of an address by aggregating all transactions."""
        balance = 0.0
        
        for block in self.chain:
            for tx in block.transactions:
                if tx.sender == address:
                    balance -= tx.amount
                if tx.recipient == address:
                    balance += tx.amount
        
        return balance

class Wallet:
    """Represents a user's wallet with public/private key pair."""
    
    def __init__(self):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()
        self.address = self.generate_address()
    
    def generate_address(self) -> str:
        """Generate a wallet address from the public key."""
        public_key_bytes = self.public_key.public_bytes(
            Encoding.PEM,
            PublicFormat.SubjectPublicKeyInfo
        )
        return hashlib.sha256(public_key_bytes).hexdigest()
    
    def create_transaction(self, recipient: str, amount: float) -> Transaction:
        """Create and sign a new transaction."""
        transaction = Transaction(self.address, recipient, amount)
        transaction.sign_transaction(self.private_key)
        return transaction

# Example usage
if __name__ == "__main__":
    # Create blockchain
    blockchain = Blockchain()
    
    # Create wallets
    wallet1 = Wallet()
    wallet2 = Wallet()
    
    # Create and add transactions
    tx1 = wallet1.create_transaction(wallet2.address, 5)
    blockchain.add_transaction(tx1, wallet1.public_key)
    
    tx2 = wallet2.create_transaction(wallet1.address, 2)
    blockchain.add_transaction(tx2, wallet2.public_key)
    
    # Mine pending transactions
    blockchain.mine_pending_transactions(wallet1.address)
    
    # Check balances
    print(f"Wallet 1 balance: {blockchain.get_balance(wallet1.address)}")
    print(f"Wallet 2 balance: {blockchain.get_balance(wallet2.address)}")
    
    # Validate chain
    print(f"Blockchain valid: {blockchain.is_chain_valid()}")
```
