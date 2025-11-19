"""
Generated Code Metadata:
========================
Original URL: https://techbinance.com
Prompt: Create a program to simulate cryptocurrency transactions using Python, inspired by Tech Binance's insights into the revolutionary nature of cryptocurrency.
Generated: DETERMINISTIC_79802dece8655f33
Batch ID: 20250612_145913
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
import time
from typing import Dict, List, Optional, Tuple
import uuid
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Transaction:
    sender: str
    recipient: str
    amount: float
    timestamp: float = field(default_factory=time.time)
    transaction_id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def to_dict(self) -> Dict:
        return {
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount,
            "timestamp": self.timestamp,
            "transaction_id": self.transaction_id
        }


@dataclass
class Block:
    index: int
    timestamp: float
    transactions: List[Transaction]
    previous_hash: str
    nonce: int = 0
    hash: str = field(init=False)

    def __post_init__(self):
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        block_data = {
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": [tx.to_dict() for tx in self.transactions],
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }
        block_string = json.dumps(block_data, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty: int):
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()


class Blockchain:
    def __init__(self):
        self.chain: List[Block] = []
        self.pending_transactions: List[Transaction] = []
        self.difficulty = 2
        self.mining_reward = 10
        self.wallets: Dict[str, float] = {}

        # Create the genesis block
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(
            index=0,
            timestamp=time.time(),
            transactions=[],
            previous_hash="0"
        )
        self.chain.append(genesis_block)

    def get_latest_block(self) -> Block:
        return self.chain[-1]

    def mine_pending_transactions(self, mining_reward_address: str):
        if not self.pending_transactions:
            raise ValueError("No transactions to mine")

        block = Block(
            index=len(self.chain),
            timestamp=time.time(),
            transactions=self.pending_transactions,
            previous_hash=self.get_latest_block().hash
        )
        block.mine_block(self.difficulty)

        print(f"Block successfully mined! Hash: {block.hash}")
        self.chain.append(block)

        # Reset pending transactions and add mining reward
        self.pending_transactions = [
            Transaction(
                sender="network",
                recipient=mining_reward_address,
                amount=self.mining_reward
            )
        ]

    def create_transaction(self, sender: str, recipient: str, amount: float) -> Transaction:
        if sender not in self.wallets or recipient not in self.wallets:
            raise ValueError("Sender or recipient wallet does not exist")

        if self.wallets[sender] < amount:
            raise ValueError("Insufficient balance")

        transaction = Transaction(sender, recipient, amount)
        self.pending_transactions.append(transaction)
        return transaction

    def get_balance(self, address: str) -> float:
        if address not in self.wallets:
            raise ValueError("Wallet does not exist")

        balance = self.wallets[address]

        for block in self.chain:
            for tx in block.transactions:
                if tx.sender == address:
                    balance -= tx.amount
                if tx.recipient == address:
                    balance += tx.amount

        # Check pending transactions
        for tx in self.pending_transactions:
            if tx.sender == address:
                balance -= tx.amount
            if tx.recipient == address:
                balance += tx.amount

        return balance

    def is_chain_valid(self) -> bool:
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def create_wallet(self, address: str, initial_balance: float = 100.0):
        if address in self.wallets:
            raise ValueError("Wallet already exists")
        self.wallets[address] = initial_balance

    def display_chain(self):
        for block in self.chain:
            print(f"Block {block.index}")
            print(f"Timestamp: {datetime.fromtimestamp(block.timestamp)}")
            print(f"Transactions: {len(block.transactions)}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print("-" * 50)


def main():
    # Initialize blockchain
    blockchain = Blockchain()

    # Create some wallets
    blockchain.create_wallet("Alice")
    blockchain.create_wallet("Bob")
    blockchain.create_wallet("Miner")

    # Perform some transactions
    try:
        blockchain.create_transaction("Alice", "Bob", 10)
        blockchain.create_transaction("Bob", "Alice", 5)
    except ValueError as e:
        print(f"Transaction error: {e}")

    # Mine pending transactions
    print("Mining pending transactions...")
    blockchain.mine_pending_transactions("Miner")

    # Check balances
    print(f"Alice's balance: {blockchain.get_balance('Alice')}")
    print(f"Bob's balance: {blockchain.get_balance('Bob')}")
    print(f"Miner's balance: {blockchain.get_balance('Miner')}")

    # Display blockchain
    blockchain.display_chain()

    # Validate blockchain
    print(f"Is blockchain valid? {blockchain.is_chain_valid()}")


if __name__ == "__main__":
    main()
```
