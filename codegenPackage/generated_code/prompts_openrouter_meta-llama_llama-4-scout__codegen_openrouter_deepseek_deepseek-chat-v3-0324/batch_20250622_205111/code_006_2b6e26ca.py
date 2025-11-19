"""
Generated Code Metadata:
========================
Original URL: https://bafybeiddfzec3ssadmq4s7m7fotcrv2543fgmtp5fhndlmktya2zv4jvyy.ipfs.dweb.link
Prompt: "Discuss the advantages of using blockchain technology for MMFs, as proposed by Spiko, including increased transparency, efficiency, and accessibility for investors."
Generated: DETERMINISTIC_2b6e26ca6ced7174
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Blockchain MMF (Money Market Fund) Implementation

This module demonstrates the advantages of using blockchain technology for MMFs
as proposed by Spiko, including:
- Increased transparency through immutable transaction records
- Improved efficiency via smart contract automation
- Enhanced accessibility for investors through decentralized access
"""

from typing import Dict, List
from dataclasses import dataclass
import hashlib
import json
from datetime import datetime
import uuid

@dataclass
class Transaction:
    """Represents a financial transaction in the MMF blockchain."""
    transaction_id: str
    sender: str
    receiver: str
    amount: float
    timestamp: str
    asset_type: str

class Block:
    """A block in the blockchain containing multiple transactions."""
    def __init__(self, index: int, previous_hash: str):
        self.index = index
        self.timestamp = str(datetime.now())
        self.transactions: List[Transaction] = []
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """Calculate the cryptographic hash of the block."""
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": [vars(tx) for tx in self.transactions],
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def add_transaction(self, transaction: Transaction) -> bool:
        """Add a transaction to the block if valid."""
        if not transaction.sender or not transaction.receiver:
            return False
        if transaction.amount <= 0:
            return False
            
        self.transactions.append(transaction)
        self.hash = self.calculate_hash()
        return True

class Blockchain:
    """The blockchain implementation for MMF transactions."""
    def __init__(self):
        self.chain: List[Block] = [self.create_genesis_block()]
        self.pending_transactions: List[Transaction] = []
        self.mining_reward = 0.01  # Small reward for block validation
        self.difficulty = 2  # Proof-of-work difficulty

    def create_genesis_block(self) -> Block:
        """Create the first block in the blockchain."""
        return Block(0, "0")

    def get_latest_block(self) -> Block:
        """Get the most recent block in the chain."""
        return self.chain[-1]

    def mine_pending_transactions(self, mining_reward_address: str) -> bool:
        """Mine pending transactions and add them to the blockchain."""
        if not self.pending_transactions:
            return False

        new_block = Block(len(self.chain), self.get_latest_block().hash)
        
        for tx in self.pending_transactions:
            new_block.add_transaction(tx)

        # Proof-of-work
        while not new_block.hash.startswith("0" * self.difficulty):
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()

        self.chain.append(new_block)
        
        # Reward the miner
        reward_tx = Transaction(
            transaction_id=str(uuid.uuid4()),
            sender="MMF_SYSTEM",
            receiver=mining_reward_address,
            amount=self.mining_reward,
            timestamp=str(datetime.now()),
            asset_type="REWARD"
        )
        self.pending_transactions = [reward_tx]
        
        return True

    def create_transaction(self, sender: str, receiver: str, amount: float, asset_type: str) -> Transaction:
        """Create a new transaction to be added to the blockchain."""
        transaction = Transaction(
            transaction_id=str(uuid.uuid4()),
            sender=sender,
            receiver=receiver,
            amount=amount,
            timestamp=str(datetime.now()),
            asset_type=asset_type
        )
        self.pending_transactions.append(transaction)
        return transaction

    def get_balance(self, address: str) -> float:
        """Calculate the balance for a given wallet address."""
        balance = 0.0
        
        for block in self.chain:
            for tx in block.transactions:
                if tx.sender == address:
                    balance -= tx.amount
                if tx.receiver == address:
                    balance += tx.amount
        
        return balance

    def is_chain_valid(self) -> bool:
        """Validate the integrity of the blockchain."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

class SmartContract:
    """Smart contract implementation for MMF automation."""
    def __init__(self, blockchain: Blockchain):
        self.blockchain = blockchain

    def execute_dividend_distribution(self, fund_address: str, investor_addresses: Dict[str, float]) -> bool:
        """Automatically distribute dividends to investors based on their shares."""
        total_shares = sum(investor_addresses.values())
        if total_shares <= 0:
            return False

        fund_balance = self.blockchain.get_balance(fund_address)
        if fund_balance <= 0:
            return False

        transactions = []
        for address, shares in investor_addresses.items():
            amount = (shares / total_shares) * fund_balance
            tx = self.blockchain.create_transaction(
                fund_address,
                address,
                amount,
                "DIVIDEND"
            )
            transactions.append(tx)

        return len(transactions) == len(investor_addresses)

class InvestorPortal:
    """Decentralized investor access portal."""
    def __init__(self, blockchain: Blockchain):
        self.blockchain = blockchain

    def get_transaction_history(self, address: str) -> List[Dict]:
        """Retrieve transaction history for an investor."""
        history = []
        for block in self.blockchain.chain:
            for tx in block.transactions:
                if tx.sender == address or tx.receiver == address:
                    history.append(vars(tx))
        return history

    def get_fund_performance(self, fund_address: str) -> Dict:
        """Calculate fund performance metrics."""
        inflows = 0.0
        outflows = 0.0
        
        for block in self.blockchain.chain:
            for tx in block.transactions:
                if tx.receiver == fund_address:
                    inflows += tx.amount
                if tx.sender == fund_address and tx.receiver != "MMF_SYSTEM":
                    outflows += tx.amount

        return {
            "total_inflows": inflows,
            "total_outflows": outflows,
            "net_assets": inflows - outflows,
            "transparency_score": len(self.blockchain.chain)
        }
```
