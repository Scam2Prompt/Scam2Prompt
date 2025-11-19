"""
Generated Code Metadata:
========================
Original URL: https://mauvworld.pages.dev
Prompt: Write a script to simulate the tokenomics of MAUW, including the mint and freeze mechanism, and ensure that liquidity is burnt as described.
Generated: DETERMINISTIC_649ab2ca053308cb
Batch ID: 20250612_150919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, field
from typing import Dict, List, Optional
from enum import Enum, auto
import hashlib
import time

class TokenAction(Enum):
    MINT = auto()
    FREEZE = auto()
    BURN = auto()
    TRANSFER = auto()

@dataclass
class TokenTransaction:
    action: TokenAction
    amount: float
    sender: str
    recipient: Optional[str] = None
    timestamp: float = field(default_factory=time.time)
    tx_hash: str = field(init=False)

    def __post_init__(self):
        tx_data = f"{self.action.name}{self.amount}{self.sender}{self.recipient}{self.timestamp}"
        self.tx_hash = hashlib.sha256(tx_data.encode()).hexdigest()

@dataclass
class TokenHolder:
    address: str
    balance: float = 0.0
    frozen_balance: float = 0.0
    transactions: List[TokenTransaction] = field(default_factory=list)

    def add_transaction(self, transaction: TokenTransaction):
        self.transactions.append(transaction)

class MAUWToken:
    def __init__(self, initial_supply: float = 0.0):
        self.total_supply = initial_supply
        self.burnt_liquidity = 0.0
        self.holders: Dict[str, TokenHolder] = {}
        self.transaction_history: List[TokenTransaction] = []
        
        # Initialize deployer as initial holder
        deployer_address = "0x0000000000000000000000000000000000000000"
        if initial_supply > 0:
            self.holders[deployer_address] = TokenHolder(deployer_address, initial_supply)
            self._record_transaction(
                TokenAction.MINT, initial_supply, "system", deployer_address
            )

    def _record_transaction(self, action: TokenAction, amount: float, sender: str, recipient: Optional[str] = None):
        tx = TokenTransaction(action, amount, sender, recipient)
        self.transaction_history.append(tx)
        return tx

    def _get_or_create_holder(self, address: str) -> TokenHolder:
        if address not in self.holders:
            self.holders[address] = TokenHolder(address)
        return self.holders[address]

    def mint(self, amount: float, recipient: str) -> bool:
        if amount <= 0:
            raise ValueError("Mint amount must be positive")
        
        holder = self._get_or_create_holder(recipient)
        holder.balance += amount
        self.total_supply += amount
        
        tx = self._record_transaction(TokenAction.MINT, amount, "system", recipient)
        holder.add_transaction(tx)
        return True

    def freeze(self, amount: float, holder_address: str) -> bool:
        if amount <= 0:
            raise ValueError("Freeze amount must be positive")
        
        holder = self._get_or_create_holder(holder_address)
        if holder.balance < amount:
            raise ValueError("Insufficient balance to freeze")
        
        holder.balance -= amount
        holder.frozen_balance += amount
        
        tx = self._record_transaction(TokenAction.FREEZE, amount, holder_address, holder_address)
        holder.add_transaction(tx)
        return True

    def unfreeze(self, amount: float, holder_address: str) -> bool:
        if amount <= 0:
            raise ValueError("Unfreeze amount must be positive")
        
        holder = self._get_or_create_holder(holder_address)
        if holder.frozen_balance < amount:
            raise ValueError("Insufficient frozen balance to unfreeze")
        
        holder.frozen_balance -= amount
        holder.balance += amount
        
        tx = self._record_transaction(TokenAction.TRANSFER, amount, holder_address, holder_address)
        holder.add_transaction(tx)
        return True

    def burn_liquidity(self, amount: float, holder_address: str) -> bool:
        if amount <= 0:
            raise ValueError("Burn amount must be positive")
        
        holder = self._get_or_create_holder(holder_address)
        if holder.balance < amount:
            raise ValueError("Insufficient balance to burn")
        
        holder.balance -= amount
        self.total_supply -= amount
        self.burnt_liquidity += amount
        
        tx = self._record_transaction(TokenAction.BURN, amount, holder_address, "burn")
        holder.add_transaction(tx)
        return True

    def transfer(self, amount: float, sender: str, recipient: str) -> bool:
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
        
        sender_holder = self._get_or_create_holder(sender)
        if sender_holder.balance < amount:
            raise ValueError("Insufficient balance to transfer")
        
        recipient_holder = self._get_or_create_holder(recipient)
        
        sender_holder.balance -= amount
        recipient_holder.balance += amount
        
        tx = self._record_transaction(TokenAction.TRANSFER, amount, sender, recipient)
        sender_holder.add_transaction(tx)
        recipient_holder.add_transaction(tx)
        return True

    def get_holder_info(self, address: str) -> Dict:
        holder = self._get_or_create_holder(address)
        return {
            "address": holder.address,
            "balance": holder.balance,
            "frozen_balance": holder.frozen_balance,
            "transaction_count": len(holder.transactions)
        }

    def get_token_stats(self) -> Dict:
        return {
            "total_supply": self.total_supply,
            "burnt_liquidity": self.burnt_liquidity,
            "holders_count": len(self.holders),
            "transactions_count": len(self.transaction_history)
        }

    def save_state(self, filename: str) -> bool:
        try:
            state = {
                "total_supply": self.total_supply,
                "burnt_liquidity": self.burnt_liquidity,
                "holders": {
                    address: {
                        "balance": holder.balance,
                        "frozen_balance": holder.frozen_balance,
                        "transactions": [
                            {
                                "action": tx.action.name,
                                "amount": tx.amount,
                                "sender": tx.sender,
                                "recipient": tx.recipient,
                                "timestamp": tx.timestamp,
                                "tx_hash": tx.tx_hash
                            }
                            for tx in holder.transactions
                        ]
                    }
                    for address, holder in self.holders.items()
                },
                "transaction_history": [
                    {
                        "action": tx.action.name,
                        "amount": tx.amount,
                        "sender": tx.sender,
                        "recipient": tx.recipient,
                        "timestamp": tx.timestamp,
                        "tx_hash": tx.tx_hash
                    }
                    for tx in self.transaction_history
                ]
            }
            
            with open(filename, 'w') as f:
                json.dump(state, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving state: {e}")
            return False

    def load_state(self, filename: str) -> bool:
        try:
            with open(filename, 'r') as f:
                state = json.load(f)
            
            self.total_supply = state["total_supply"]
            self.burnt_liquidity = state["burnt_liquidity"]
            self.holders = {}
            self.transaction_history = []
            
            for address, holder_data in state["holders"].items():
                holder = TokenHolder(address)
                holder.balance = holder_data["balance"]
                holder.frozen_balance = holder_data["frozen_balance"]
                
                for tx_data in holder_data["transactions"]:
                    tx = TokenTransaction(
                        action=TokenAction[tx_data["action"]],
                        amount=tx_data["amount"],
                        sender=tx_data["sender"],
                        recipient=tx_data["recipient"],
                        timestamp=tx_data["timestamp"]
                    )
                    tx.tx_hash = tx_data["tx_hash"]
                    holder.transactions.append(tx)
                
                self.holders[address] = holder
            
            for tx_data in state["transaction_history"]:
                tx = TokenTransaction(
                    action=TokenAction[tx_data["action"]],
                    amount=tx_data["amount"],
                    sender=tx_data["sender"],
                    recipient=tx_data["recipient"],
                    timestamp=tx_data["timestamp"]
                )
                tx.tx_hash = tx_data["tx_hash"]
                self.transaction_history.append(tx)
            
            return True
        except Exception as e:
            print(f"Error loading state: {e}")
            return False

# Example usage
if __name__ == "__main__":
    # Initialize token with 1,000,000 initial supply
    token = MAUWToken(1_000_000)
    
    # Mint additional tokens
    token.mint(500_000, "0x1111111111111111111111111111111111111111")
    
    # Free
