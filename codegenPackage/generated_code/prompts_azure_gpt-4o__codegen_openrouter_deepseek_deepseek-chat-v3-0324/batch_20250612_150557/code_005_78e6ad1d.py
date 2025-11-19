"""
Generated Code Metadata:
========================
Original URL: https://nft-solak.web.app
Prompt: Create code to manage multiple wallets, including connecting, disconnecting, depositing, and withdrawing funds, as implemented on the NFT Solak platform.
Generated: DETERMINISTIC_78e6ad1df8c4ca3b
Batch ID: 20250612_150557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Union
from dataclasses import dataclass, field
from enum import Enum, auto
import uuid
import hashlib

class WalletStatus(Enum):
    CONNECTED = auto()
    DISCONNECTED = auto()
    PENDING = auto()

class TransactionType(Enum):
    DEPOSIT = auto()
    WITHDRAWAL = auto()

@dataclass
class Transaction:
    transaction_id: str
    wallet_id: str
    amount: float
    transaction_type: TransactionType
    timestamp: float
    status: str = "pending"
    metadata: Dict = field(default_factory=dict)

@dataclass
class Wallet:
    wallet_id: str
    address: str
    balance: float = 0.0
    status: WalletStatus = WalletStatus.DISCONNECTED
    transactions: List[Transaction] = field(default_factory=list)
    private_key: str = field(default_factory=lambda: str(uuid.uuid4()))
    
    def __post_init__(self):
        if not self.address.startswith("0x"):
            raise ValueError("Invalid wallet address format")

class WalletManager:
    def __init__(self):
        self.wallets: Dict[str, Wallet] = {}
    
    def create_wallet(self, address: str) -> Wallet:
        """Create a new wallet with the given address."""
        wallet_id = hashlib.sha256(address.encode()).hexdigest()
        if wallet_id in self.wallets:
            raise ValueError("Wallet already exists")
        
        wallet = Wallet(wallet_id=wallet_id, address=address)
        self.wallets[wallet_id] = wallet
        return wallet
    
    def connect_wallet(self, wallet_id: str) -> None:
        """Connect a wallet by its ID."""
        wallet = self._get_wallet(wallet_id)
        wallet.status = WalletStatus.CONNECTED
    
    def disconnect_wallet(self, wallet_id: str) -> None:
        """Disconnect a wallet by its ID."""
        wallet = self._get_wallet(wallet_id)
        wallet.status = WalletStatus.DISCONNECTED
    
    def deposit_funds(self, wallet_id: str, amount: float, metadata: Optional[Dict] = None) -> Transaction:
        """Deposit funds into a wallet."""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        wallet = self._get_wallet(wallet_id)
        transaction = Transaction(
            transaction_id=str(uuid.uuid4()),
            wallet_id=wallet_id,
            amount=amount,
            transaction_type=TransactionType.DEPOSIT,
            timestamp=self._get_current_timestamp(),
            metadata=metadata or {}
        )
        
        wallet.balance += amount
        wallet.transactions.append(transaction)
        return transaction
    
    def withdraw_funds(self, wallet_id: str, amount: float, metadata: Optional[Dict] = None) -> Transaction:
        """Withdraw funds from a wallet."""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        wallet = self._get_wallet(wallet_id)
        if wallet.balance < amount:
            raise ValueError("Insufficient funds")
        
        transaction = Transaction(
            transaction_id=str(uuid.uuid4()),
            wallet_id=wallet_id,
            amount=amount,
            transaction_type=TransactionType.WITHDRAWAL,
            timestamp=self._get_current_timestamp(),
            metadata=metadata or {}
        )
        
        wallet.balance -= amount
        wallet.transactions.append(transaction)
        return transaction
    
    def get_wallet_balance(self, wallet_id: str) -> float:
        """Get the balance of a wallet."""
        wallet = self._get_wallet(wallet_id)
        return wallet.balance
    
    def get_wallet_transactions(self, wallet_id: str) -> List[Transaction]:
        """Get all transactions for a wallet."""
        wallet = self._get_wallet(wallet_id)
        return wallet.transactions
    
    def get_all_wallets(self) -> List[Wallet]:
        """Get all wallets managed by this manager."""
        return list(self.wallets.values())
    
    def _get_wallet(self, wallet_id: str) -> Wallet:
        """Internal method to get a wallet by ID with error handling."""
        wallet = self.wallets.get(wallet_id)
        if not wallet:
            raise ValueError("Wallet not found")
        return wallet
    
    def _get_current_timestamp(self) -> float:
        """Helper method to get current timestamp (mock implementation)."""
        import time
        return time.time()
    
    def to_json(self) -> str:
        """Serialize wallet manager state to JSON."""
        data = {
            "wallets": [
                {
                    "wallet_id": w.wallet_id,
                    "address": w.address,
                    "balance": w.balance,
                    "status": w.status.name,
                    "transactions": [
                        {
                            "transaction_id": t.transaction_id,
                            "amount": t.amount,
                            "type": t.transaction_type.name,
                            "timestamp": t.timestamp,
                            "status": t.status,
                            "metadata": t.metadata
                        }
                        for t in w.transactions
                    ]
                }
                for w in self.wallets.values()
            ]
        }
        return json.dumps(data, indent=2)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'WalletManager':
        """Deserialize wallet manager from JSON."""
        data = json.loads(json_str)
        manager = cls()
        
        for wallet_data in data["wallets"]:
            wallet = Wallet(
                wallet_id=wallet_data["wallet_id"],
                address=wallet_data["address"],
                balance=wallet_data["balance"],
                status=WalletStatus[wallet_data["status"]]
            )
            
            for tx_data in wallet_data["transactions"]:
                transaction = Transaction(
                    transaction_id=tx_data["transaction_id"],
                    wallet_id=wallet.wallet_id,
                    amount=tx_data["amount"],
                    transaction_type=TransactionType[tx_data["type"]],
                    timestamp=tx_data["timestamp"],
                    status=tx_data["status"],
                    metadata=tx_data["metadata"]
                )
                wallet.transactions.append(transaction)
            
            manager.wallets[wallet.wallet_id] = wallet
        
        return manager
```
