"""
Generated Code Metadata:
========================
Original URL: https://dappsconnectonline.com
Prompt: "Design a basic blockchain-based protocol for a DeFi service that operates without centralized control."
Generated: DETERMINISTIC_f2986177b097c844
Batch ID: 20250622_212236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Basic Blockchain-based DeFi Protocol Implementation

import hashlib
import json
from time import time
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
import ecdsa
from ecdsa import SigningKey, VerifyingKey

@dataclass
class Transaction:
    sender: str
    receiver: str
    amount: float
    timestamp: float
    signature: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            'sender': self.sender,
            'receiver': self.receiver,
            'amount': self.amount,
            'timestamp': self.timestamp
        }

    def sign(self, private_key: SigningKey) -> None:
        transaction_dict = self.to_dict()
        transaction_str = json.dumps(transaction_dict, sort_keys=True).encode()
        self.signature = private_key.sign(transaction_str).hex()

    def verify(self) -> bool:
        if not self.signature:
            return False
        try:
            vk = VerifyingKey.from_string(bytes.fromhex(self.sender), curve=ecdsa.SECP256k1)
            transaction_dict = self.to_dict()
            transaction_str = json.dumps(transaction_dict, sort_keys=True).encode()
            return vk.verify(bytes.fromhex(self.signature), transaction_str)
        except:
            return False

class Block:
    def __init__(self, index: int, transactions: List[Transaction], timestamp: float, previous_hash: str):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        block_string = json.dumps({
            'index': self.index,
            'transactions': [tx.to_dict() for tx in self.transactions],
            'timestamp': self.timestamp,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty: int) -> None:
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.compute_hash()

class Blockchain:
    def __init__(self):
        self.chain: List[Block] = []
        self.difficulty = 2
        self.pending_transactions: List[Transaction] = []
        self.mining_reward = 1.0

        # Create genesis block
        self.create_genesis_block()

    def create_genesis_block(self) -> None:
        genesis_block = Block(0, [], time(), "0")
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)

    def get_last_block(self) -> Block:
        return self.chain[-1]

    def add_transaction(self, transaction: Transaction) -> bool:
        if not transaction.verify():
            return False
        
        self.pending_transactions.append(transaction)
        return True

    def mine_pending_transactions(self, miner_address: str) -> None:
        if not self.pending_transactions:
            return

        block = Block(
            len(self.chain),
            self.pending_transactions,
            time(),
            self.get_last_block().hash
        )
        block.mine_block(self.difficulty)

        print(f"Block mined: {block.hash}")
        self.chain.append(block)

        # Reset pending transactions and add mining reward
        self.pending_transactions = [
            Transaction("0", miner_address, self.mining_reward, time())
        ]

    def is_chain_valid(self) -> bool:
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.compute_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

            for tx in current_block.transactions:
                if not tx.verify():
                    return False

        return True

    def get_balance(self, address: str) -> float:
        balance = 0.0

        for block in self.chain:
            for tx in block.transactions:
                if tx.sender == address:
                    balance -= tx.amount
                if tx.receiver == address:
                    balance += tx.amount

        return balance

class DeFiProtocol:
    def __init__(self):
        self.blockchain = Blockchain()
        self.users: Dict[str, SigningKey] = {}

    def create_user(self) -> str:
        private_key = SigningKey.generate(curve=ecdsa.SECP256k1)
        public_key = private_key.get_verifying_key().to_string().hex()
        self.users[public_key] = private_key
        return public_key

    def transfer(self, sender: str, receiver: str, amount: float) -> bool:
        if sender not in self.users:
            return False

        if self.blockchain.get_balance(sender) < amount:
            return False

        tx = Transaction(sender, receiver, amount, time())
        tx.sign(self.users[sender])
        return self.blockchain.add_transaction(tx)

    def mine(self, miner_address: str) -> None:
        self.blockchain.mine_pending_transactions(miner_address)

    def get_balance(self, address: str) -> float:
        return self.blockchain.get_balance(address)

    def validate_chain(self) -> bool:
        return self.blockchain.is_chain_valid()
```
