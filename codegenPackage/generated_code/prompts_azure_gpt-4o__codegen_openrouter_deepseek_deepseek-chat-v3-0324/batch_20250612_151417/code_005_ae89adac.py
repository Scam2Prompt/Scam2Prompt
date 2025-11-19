"""
Generated Code Metadata:
========================
Original URL: https://freecryptomoney.com
Prompt: Create a Python program to manage cryptocurrency transactions between a faucet and a wallet, referencing the functionality described on FreeCryptoMoney.com.
Generated: DETERMINISTIC_ae89adac309db2cf
Batch ID: 20250612_151417
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
import os
import time
from typing import Dict, List, Optional, Tuple

# Constants
TRANSACTION_FEE = 0.001  # 0.1% transaction fee
FAUCET_INITIAL_BALANCE = 1000000.0  # Initial faucet balance
WALLET_INITIAL_BALANCE = 0.0  # Initial wallet balance
BLOCKCHAIN_FILE = "blockchain.json"
WALLETS_FILE = "wallets.json"

class Transaction:
    """Represents a cryptocurrency transaction between sender and receiver."""
    
    def __init__(self, sender: str, receiver: str, amount: float, timestamp: float = None):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = timestamp or time.time()
        self.transaction_id = self._generate_id()
    
    def _generate_id(self) -> str:
        """Generate a unique ID for the transaction."""
        transaction_data = f"{self.sender}{self.receiver}{self.amount}{self.timestamp}"
        return hashlib.sha256(transaction_data.encode()).hexdigest()
    
    def to_dict(self) -> Dict:
        """Convert transaction to dictionary for serialization."""
        return {
            "transaction_id": self.transaction_id,
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": self.amount,
            "timestamp": self.timestamp
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Transaction':
        """Create Transaction from dictionary."""
        return cls(
            sender=data["sender"],
            receiver=data["receiver"],
            amount=data["amount"],
            timestamp=data["timestamp"]
        )

class Block:
    """Represents a block in the blockchain containing transactions."""
    
    def __init__(self, index: int, previous_hash: str, transactions: List[Transaction], timestamp: float = None):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp or time.time()
        self.hash = self._calculate_hash()
    
    def _calculate_hash(self) -> str:
        """Calculate the hash of the block."""
        block_data = {
            "index": self.index,
            "previous_hash": self.previous_hash,
            "transactions": [tx.to_dict() for tx in self.transactions],
            "timestamp": self.timestamp
        }
        return hashlib.sha256(json.dumps(block_data, sort_keys=True).encode()).hexdigest()
    
    def to_dict(self) -> Dict:
        """Convert block to dictionary for serialization."""
        return {
            "index": self.index,
            "previous_hash": self.previous_hash,
            "transactions": [tx.to_dict() for tx in self.transactions],
            "timestamp": self.timestamp,
            "hash": self.hash
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Block':
        """Create Block from dictionary."""
        transactions = [Transaction.from_dict(tx) for tx in data["transactions"]]
        return cls(
            index=data["index"],
            previous_hash=data["previous_hash"],
            transactions=transactions,
            timestamp=data["timestamp"]
        )

class Blockchain:
    """Manages the blockchain and wallet balances."""
    
    def __init__(self):
        self.chain: List[Block] = []
        self.pending_transactions: List[Transaction] = []
        self.wallets: Dict[str, float] = {}
        self._initialize_blockchain()
        self._load_wallets()
    
    def _initialize_blockchain(self) -> None:
        """Initialize the blockchain from file or create genesis block."""
        if os.path.exists(BLOCKCHAIN_FILE):
            self._load_blockchain()
        else:
            self._create_genesis_block()
    
    def _load_blockchain(self) -> None:
        """Load blockchain from file."""
        try:
            with open(BLOCKCHAIN_FILE, "r") as f:
                data = json.load(f)
                self.chain = [Block.from_dict(block) for block in data["chain"]]
                self.pending_transactions = [Transaction.from_dict(tx) for tx in data["pending_transactions"]]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading blockchain: {e}")
            self._create_genesis_block()
    
    def _create_genesis_block(self) -> None:
        """Create the genesis block with initial faucet balance."""
        genesis_transaction = Transaction(
            sender="system",
            receiver="faucet",
            amount=FAUCET_INITIAL_BALANCE
        )
        genesis_block = Block(
            index=0,
            previous_hash="0",
            transactions=[genesis_transaction],
            timestamp=time.time()
        )
        self.chain = [genesis_block]
        self._save_blockchain()
    
    def _load_wallets(self) -> None:
        """Load wallets from file or initialize."""
        if os.path.exists(WALLETS_FILE):
            try:
                with open(WALLETS_FILE, "r") as f:
                    self.wallets = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Error loading wallets: {e}")
                self._initialize_wallets()
        else:
            self._initialize_wallets()
    
    def _initialize_wallets(self) -> None:
        """Initialize wallets with faucet and empty user wallets."""
        self.wallets = {
            "faucet": FAUCET_INITIAL_BALANCE,
            "system": 0.0
        }
        self._save_wallets()
    
    def _save_blockchain(self) -> None:
        """Save blockchain to file."""
        data = {
            "chain": [block.to_dict() for block in self.chain],
            "pending_transactions": [tx.to_dict() for tx in self.pending_transactions]
        }
        with open(BLOCKCHAIN_FILE, "w") as f:
            json.dump(data, f, indent=2)
    
    def _save_wallets(self) -> None:
        """Save wallets to file."""
        with open(WALLETS_FILE, "w") as f:
            json.dump(self.wallets, f, indent=2)
    
    def create_wallet(self, wallet_id: str) -> bool:
        """Create a new wallet with initial balance."""
        if wallet_id in self.wallets:
            print(f"Wallet {wallet_id} already exists")
            return False
        
        self.wallets[wallet_id] = WALLET_INITIAL_BALANCE
        self._save_wallets()
        return True
    
    def get_balance(self, wallet_id: str) -> Optional[float]:
        """Get balance of a wallet."""
        return self.wallets.get(wallet_id)
    
    def request_from_faucet(self, wallet_id: str, amount: float) -> bool:
        """Request cryptocurrency from faucet to wallet."""
        if wallet_id not in self.wallets:
            print(f"Wallet {wallet_id} does not exist")
            return False
        
        if amount <= 0:
            print("Amount must be positive")
            return False
        
        if self.wallets["faucet"] < amount:
            print("Faucet has insufficient funds")
            return False
        
        transaction = Transaction(
            sender="faucet",
            receiver=wallet_id,
            amount=amount
        )
        self.pending_transactions.append(transaction)
        self._process_transactions()
        return True
    
    def send_transaction(self, sender: str, receiver: str, amount: float) -> bool:
        """Send cryptocurrency between wallets."""
        if sender not in self.wallets:
            print(f"Sender wallet {sender} does not exist")
            return False
        
        if receiver not in self.wallets:
            print(f"Receiver wallet {receiver} does not exist")
            return False
        
        if amount <= 0:
            print("Amount must be positive")
            return False
        
        total_amount = amount + (amount * TRANSACTION_FEE)
        if self.wallets[sender] < total_amount:
            print("Sender has insufficient funds")
            return False
        
        transaction = Transaction(
            sender=sender,
            receiver=receiver,
            amount=amount
        )
        fee_transaction = Transaction(
            sender=sender,
            receiver="system",
            amount=amount * TRANSACTION_FEE
        )
        
        self.pending_transactions.extend([transaction, fee_transaction])
        self._process_transactions()
        return True
    
    def _process_transactions(self) -> None:
        """Process pending transactions and create new block."""
        if not self.pending_transactions:
            return
        
        for tx in self.pending_transactions:
            self.wallets[tx.sender] -= tx.amount
            self.wallets[tx.receiver] += tx.amount
        
        new_block = Block(
            index=len(self.chain),
            previous_hash=self.chain[-1].hash,
            transactions=self.pending_transactions,
            timestamp=time.time()
        )
        
        self.chain.append(new_block)
        self.pending_transactions = []
        self._save_blockchain()
        self._save_w
