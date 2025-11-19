"""
Generated Code Metadata:
========================
Original URL: https://theprofit-bitcoin.com
Prompt: Design a high-level architecture for a decentralized finance ecosystem, incorporating advanced security measures and peer-to-peer transactions, similar to Profit Bitcoin.
Generated: DETERMINISTIC_41257c38c0b0db3a
Batch ID: 20250622_211811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import Dict, List, Optional
import hashlib
import json
from datetime import datetime
import secrets
import ecdsa
from ecdsa import SigningKey, VerifyingKey
import base64
import threading
import socket
import pickle
from cryptography.fernet import Fernet

# Constants
BLOCKCHAIN_FILE = "blockchain.dat"
PEER_NODES_FILE = "nodes.dat"
DIFFICULTY = 4  # Proof of Work difficulty
BLOCK_REWARD = 10  # Reward for mining a block
TRANSACTION_FEE = 0.1  # Fee per transaction

# Exception classes
class BlockchainError(Exception):
    """Base exception for blockchain-related errors"""
    pass

class TransactionError(Exception):
    """Exception for transaction-related errors"""
    pass

class NetworkError(Exception):
    """Exception for network-related errors"""
    pass

class SecurityError(Exception):
    """Exception for security-related errors"""
    pass

# Data structures
class Transaction:
    """Represents a financial transaction in the blockchain"""
    
    def __init__(self, sender: str, recipient: str, amount: float, fee: float = TRANSACTION_FEE, 
                 signature: Optional[str] = None, timestamp: Optional[float] = None):
        self.sender = sender  # Public key of sender
        self.recipient = recipient  # Public key of recipient
        self.amount = amount  # Amount to transfer
        self.fee = fee  # Transaction fee
        self.signature = signature  # Digital signature
        self.timestamp = timestamp or datetime.now().timestamp()
    
    def to_dict(self) -> Dict:
        """Convert transaction to dictionary for hashing/serialization"""
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount,
            'fee': self.fee,
            'timestamp': self.timestamp
        }
    
    def sign(self, private_key: str) -> None:
        """Sign the transaction with sender's private key"""
        sk = SigningKey.from_string(bytes.fromhex(private_key), curve=ecdsa.SECP256k1)
        message = json.dumps(self.to_dict(), sort_keys=True).encode()
        self.signature = sk.sign(message).hex()
    
    def verify(self) -> bool:
        """Verify the transaction signature"""
        if not self.signature:
            return False
        
        try:
            vk = VerifyingKey.from_string(bytes.fromhex(self.sender), curve=ecdsa.SECP256k1)
            message = json.dumps(self.to_dict(), sort_keys=True).encode()
            return vk.verify(bytes.fromhex(self.signature), message)
        except:
            return False

class Block:
    """Represents a block in the blockchain"""
    
    def __init__(self, index: int, transactions: List[Transaction], previous_hash: str, 
                 nonce: int = 0, timestamp: Optional[float] = None):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.timestamp = timestamp or datetime.now().timestamp()
    
    @property
    def hash(self) -> str:
        """Calculate the block's hash"""
        block_data = {
            'index': self.index,
            'transactions': [tx.to_dict() for tx in self.transactions],
            'previous_hash': self.previous_hash,
            'nonce': self.nonce,
            'timestamp': self.timestamp
        }
        return hashlib.sha256(json.dumps(block_data, sort_keys=True).encode()).hexdigest()

class Blockchain:
    """Core blockchain implementation"""
    
    def __init__(self):
        self.chain: List[Block] = []
        self.pending_transactions: List[Transaction] = []
        self.peer_nodes = set()
        self.load_blockchain()
        self.load_peer_nodes()
        self.key = self._load_or_generate_key()
        self.fernet = Fernet(self.key)
    
    def _load_or_generate_key(self) -> bytes:
        """Load or generate encryption key for secure storage"""
        try:
            with open('secret.key', 'rb') as f:
                return f.read()
        except FileNotFoundError:
            key = Fernet.generate_key()
            with open('secret.key', 'wb') as f:
                f.write(key)
            return key
    
    def load_blockchain(self) -> None:
        """Load blockchain from file"""
        try:
            with open(BLOCKCHAIN_FILE, 'rb') as f:
                encrypted_data = f.read()
                if encrypted_data:
                    decrypted = self.fernet.decrypt(encrypted_data)
                    self.chain = pickle.loads(decrypted)
        except (FileNotFoundError, EOFError, pickle.PickleError):
            # Create genesis block if blockchain doesn't exist
            self._create_genesis_block()
    
    def save_blockchain(self) -> None:
        """Save blockchain to file"""
        with open(BLOCKCHAIN_FILE, 'wb') as f:
            encrypted = self.fernet.encrypt(pickle.dumps(self.chain))
            f.write(encrypted)
    
    def load_peer_nodes(self) -> None:
        """Load peer nodes from file"""
        try:
            with open(PEER_NODES_FILE, 'rb') as f:
                encrypted_data = f.read()
                if encrypted_data:
                    decrypted = self.fernet.decrypt(encrypted_data)
                    self.peer_nodes = pickle.loads(decrypted)
        except (FileNotFoundError, EOFError, pickle.PickleError):
            self.peer_nodes = set()
    
    def save_peer_nodes(self) -> None:
        """Save peer nodes to file"""
        with open(PEER_NODES_FILE, 'wb') as f:
            encrypted = self.fernet.encrypt(pickle.dumps(self.peer_nodes))
            f.write(encrypted)
    
    def _create_genesis_block(self) -> None:
        """Create the genesis block"""
        genesis_block = Block(0, [], "0")
        genesis_block.nonce = self._proof_of_work(genesis_block)
        self.chain = [genesis_block]
        self.save_blockchain()
    
    def _proof_of_work(self, block: Block) -> int:
        """Proof of work algorithm"""
        block.nonce = 0
        computed_hash = block.hash
        while not computed_hash.startswith('0' * DIFFICULTY):
            block.nonce += 1
            computed_hash = block.hash
        return block.nonce
    
    def mine_block(self, miner_address: str) -> bool:
        """Mine a new block with pending transactions"""
        if not self.pending_transactions:
            return False
        
        # Add mining reward transaction
        reward_tx = Transaction(
            sender="0",  # System-generated coins
            recipient=miner_address,
            amount=BLOCK_REWARD,
            fee=0
        )
        self.pending_transactions.append(reward_tx)
        
        last_block = self.chain[-1]
        new_block = Block(
            index=last_block.index + 1,
            transactions=self.pending_transactions,
            previous_hash=last_block.hash
        )
        
        new_block.nonce = self._proof_of_work(new_block)
        self.chain.append(new_block)
        self.pending_transactions = []
        self.save_blockchain()
        return True
    
    def add_transaction(self, transaction: Transaction) -> bool:
        """Add a new transaction to pending transactions"""
        if not transaction.verify():
            raise TransactionError("Invalid transaction signature")
        
        if transaction.sender != "0":  # Not a mining reward
            sender_balance = self.get_balance(transaction.sender)
            if sender_balance < (transaction.amount + transaction.fee):
                raise TransactionError("Insufficient balance")
        
        self.pending_transactions.append(transaction)
        return True
    
    def get_balance(self, address: str) -> float:
        """Get balance for a given address"""
        balance = 0.0
        
        for block in self.chain:
            for tx in block.transactions:
                if tx.sender == address:
                    balance -= (tx.amount + tx.fee)
                if tx.recipient == address:
                    balance += tx.amount
        
        # Check pending transactions
        for tx in self.pending_transactions:
            if tx.sender == address:
                balance -= (tx.amount + tx.fee)
            if tx.recipient == address:
                balance += tx.amount
        
        return balance
    
    def is_chain_valid(self, chain: List[Block]) -> bool:
        """Validate the blockchain"""
        for i in range(1, len(chain)):
            current = chain[i]
            previous = chain[i-1]
            
            if current.hash != current.hash:  # Check current block hash
                return False
            if current.previous_hash != previous.hash:  # Check chain linkage
                return False
            if not current.hash.startswith('0' * DIFFICULTY):  # Check proof of work
                return False
            
            # Verify all transactions in
