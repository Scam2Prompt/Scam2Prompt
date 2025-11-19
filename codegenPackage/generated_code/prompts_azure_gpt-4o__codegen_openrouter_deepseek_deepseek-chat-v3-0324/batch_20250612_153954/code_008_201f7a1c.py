"""
Generated Code Metadata:
========================
Original URL: https://j-node.net
Prompt: Write code to simulate validator node interactions on a blockchain testnet, referencing J•Node's focus on community trust.
Generated: DETERMINISTIC_201f7a1c27b637c6
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from typing import List, Dict, Optional
from dataclasses import dataclass
import hashlib
import json
from datetime import datetime

@dataclass
class Validator:
    """Represents a validator node in the blockchain network."""
    node_id: str
    stake: int
    is_active: bool
    reputation_score: float
    last_active_time: datetime

class Block:
    """Represents a block in the blockchain."""
    def __init__(self, index: int, previous_hash: str, transactions: List[Dict], timestamp: float, validator_id: str):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp
        self.validator_id = validator_id
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """Calculate the SHA-256 hash of the block."""
        block_string = json.dumps({
            "index": self.index,
            "previous_hash": self.previous_hash,
            "transactions": self.transactions,
            "timestamp": self.timestamp,
            "validator_id": self.validator_id
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    """Simulates a blockchain network with validator nodes."""
    def __init__(self):
        self.chain: List[Block] = []
        self.pending_transactions: List[Dict] = []
        self.validators: Dict[str, Validator] = {}
        self.create_genesis_block()

    def create_genesis_block(self) -> None:
        """Create the genesis block (first block in the chain)."""
        genesis_block = Block(0, "0", [], time.time(), "genesis")
        self.chain.append(genesis_block)

    def register_validator(self, node_id: str, stake: int) -> None:
        """Register a new validator node."""
        if node_id in self.validators:
            raise ValueError("Validator already registered")
        self.validators[node_id] = Validator(
            node_id=node_id,
            stake=stake,
            is_active=True,
            reputation_score=1.0,
            last_active_time=datetime.now()
        )

    def select_validator(self) -> Optional[str]:
        """Select a validator based on stake and reputation (weighted random selection)."""
        active_validators = [v for v in self.validators.values() if v.is_active]
        if not active_validators:
            return None

        weights = [v.stake * v.reputation_score for v in active_validators]
        total_weight = sum(weights)
        if total_weight <= 0:
            return None

        r = random.uniform(0, total_weight)
        cumulative = 0
        for i, weight in enumerate(weights):
            cumulative += weight
            if r <= cumulative:
                return active_validators[i].node_id
        return None

    def add_transaction(self, sender: str, receiver: str, amount: float) -> None:
        """Add a new transaction to the pending transactions pool."""
        self.pending_transactions.append({
            "sender": sender,
            "receiver": receiver,
            "amount": amount,
            "timestamp": time.time()
        })

    def mine_block(self) -> bool:
        """Mine a new block if a validator is selected."""
        validator_id = self.select_validator()
        if not validator_id or not self.pending_transactions:
            return False

        last_block = self.chain[-1]
        new_block = Block(
            index=len(self.chain),
            previous_hash=last_block.hash,
            transactions=self.pending_transactions,
            timestamp=time.time(),
            validator_id=validator_id
        )

        self.chain.append(new_block)
        self.pending_transactions = []

        # Update validator's reputation and activity
        validator = self.validators[validator_id]
        validator.reputation_score = min(1.0, validator.reputation_score + 0.01)
        validator.last_active_time = datetime.now()

        return True

    def update_validator_status(self, node_id: str, is_active: bool) -> None:
        """Update a validator's active status."""
        if node_id not in self.validators:
            raise ValueError("Validator not found")
        self.validators[node_id].is_active = is_active

    def adjust_reputation(self, node_id: str, adjustment: float) -> None:
        """Adjust a validator's reputation score."""
        if node_id not in self.validators:
            raise ValueError("Validator not found")
        self.validators[node_id].reputation_score = max(0.0, min(1.0, 
            self.validators[node_id].reputation_score + adjustment))

    def validate_chain(self) -> bool:
        """Validate the integrity of the blockchain."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

def simulate_network_activity(blockchain: Blockchain, num_cycles: int = 10) -> None:
    """Simulate network activity with transactions and block mining."""
    # Register some validators
    validators = [
        ("node_1", 100),
        ("node_2", 150),
        ("node_3", 200),
        ("node_4", 75)
    ]
    for node_id, stake in validators:
        blockchain.register_validator(node_id, stake)

    for cycle in range(num_cycles):
        print(f"\n--- Cycle {cycle + 1} ---")

        # Simulate some transactions
        for _ in range(random.randint(1, 5)):
            sender = f"user_{random.randint(1, 10)}"
            receiver = f"user_{random.randint(1, 10)}"
            amount = random.uniform(0.1, 10.0)
            blockchain.add_transaction(sender, receiver, amount)
            print(f"Added transaction: {sender} -> {receiver} ({amount:.2f})")

        # Mine a block
        if blockchain.mine_block():
            last_block = blockchain.chain[-1]
            print(f"Mined block {last_block.index} by {last_block.validator_id}")
            print(f"Block hash: {last_block.hash}")
        else:
            print("No block mined (no validators or transactions)")

        # Randomly adjust validator statuses and reputations
        for validator in blockchain.validators.values():
            if random.random() < 0.1:  # 10% chance of status change
                new_status = not validator.is_active
                blockchain.update_validator_status(validator.node_id, new_status)
                print(f"Validator {validator.node_id} status changed to {'active' if new_status else 'inactive'}")

            if random.random() < 0.2:  # 20% chance of reputation adjustment
                adjustment = random.uniform(-0.05, 0.1)
                blockchain.adjust_reputation(validator.node_id, adjustment)
                print(f"Validator {validator.node_id} reputation adjusted by {adjustment:.2f}")

        # Validate chain integrity
        if not blockchain.validate_chain():
            print("WARNING: Blockchain integrity compromised!")
            break

        time.sleep(1)  # Simulate time between cycles

if __name__ == "__main__":
    print("Starting J•Node Blockchain Simulator - Focus on Community Trust")
    blockchain = Blockchain()
    simulate_network_activity(blockchain)
    print("\nSimulation complete. Final blockchain status:")
    print(f"Chain length: {len(blockchain.chain)} blocks")
    print(f"Pending transactions: {len(blockchain.pending_transactions)}")
    print("Validator statuses:")
    for validator in blockchain.validators.values():
        print(f"{validator.node_id}: Stake={validator.stake}, Reputation={validator.reputation_score:.2f}, Active={validator.is_active}")
```
