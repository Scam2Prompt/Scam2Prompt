"""
Generated Code Metadata:
========================
Original URL: https://suiio.vercel.app
Prompt: Provide an example of using Sui’s distributed deterministic execution engine, Pilotfish, to ensure consensus in a decentralized application.
Generated: DETERMINISTIC_6da02d8e8ef48a71
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example of using Sui's Pilotfish for distributed deterministic execution.
This script demonstrates how to achieve consensus in a decentralized application.
"""

import json
import hashlib
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field
from collections import defaultdict
import time
import random

@dataclass
class Transaction:
    """Represents a transaction in the decentralized application."""
    sender: str
    receiver: str
    amount: float
    timestamp: float = field(default_factory=time.time)
    signature: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert transaction to dictionary for serialization."""
        return {
            'sender': self.sender,
            'receiver': self.receiver,
            'amount': self.amount,
            'timestamp': self.timestamp,
            'signature': self.signature
        }

    def hash(self) -> str:
        """Generate a hash of the transaction."""
        tx_dict = self.to_dict()
        tx_str = json.dumps(tx_dict, sort_keys=True)
        return hashlib.sha256(tx_str.encode()).hexdigest()

@dataclass
class Block:
    """Represents a block in the blockchain."""
    index: int
    transactions: List[Transaction]
    previous_hash: str
    timestamp: float = field(default_factory=time.time)
    nonce: int = 0

    def hash(self) -> str:
        """Generate a hash of the block."""
        block_dict = {
            'index': self.index,
            'transactions': [tx.to_dict() for tx in self.transactions],
            'previous_hash': self.previous_hash,
            'timestamp': self.timestamp,
            'nonce': self.nonce
        }
        block_str = json.dumps(block_dict, sort_keys=True)
        return hashlib.sha256(block_str.encode()).hexdigest()

class PilotfishNode:
    """Represents a node in the Pilotfish distributed execution engine."""
    
    def __init__(self, node_id: str):
        self.node_id = node_id
        self.blockchain: List[Block] = []
        self.pending_transactions: List[Transaction] = []
        self.peers: List['PilotfishNode'] = []
        self.consensus_threshold = 0.51  # 51% consensus threshold

    def add_peer(self, peer: 'PilotfishNode') -> None:
        """Add a peer node to communicate with."""
        if peer not in self.peers:
            self.peers.append(peer)
            peer.peers.append(self)

    def add_transaction(self, transaction: Transaction) -> bool:
        """Add a transaction to pending transactions."""
        if not self.validate_transaction(transaction):
            return False
        self.pending_transactions.append(transaction)
        return True

    def validate_transaction(self, transaction: Transaction) -> bool:
        """Validate a transaction before adding to pending."""
        # Basic validation checks
        if transaction.amount <= 0:
            return False
        if transaction.sender == transaction.receiver:
            return False
        return True

    def mine_block(self) -> Optional[Block]:
        """Mine a new block with pending transactions."""
        if not self.pending_transactions:
            return None

        last_block = self.blockchain[-1] if self.blockchain else None
        previous_hash = last_block.hash() if last_block else "0"
        new_block = Block(
            index=len(self.blockchain),
            transactions=self.pending_transactions.copy(),
            previous_hash=previous_hash
        )

        # Simple proof-of-work (for demonstration)
        while not new_block.hash().startswith('00'):
            new_block.nonce += 1

        self.blockchain.append(new_block)
        self.pending_transactions = []
        return new_block

    def broadcast_block(self, block: Block) -> None:
        """Broadcast a mined block to all peers."""
        for peer in self.peers:
            peer.receive_block(block)

    def receive_block(self, block: Block) -> bool:
        """Receive a block from a peer and validate it."""
        if not self.validate_block(block):
            return False

        # Check if we already have this block
        if len(self.blockchain) >= block.index + 1:
            return False

        # Add to blockchain
        self.blockchain.append(block)
        return True

    def validate_block(self, block: Block) -> bool:
        """Validate a received block."""
        # Check block index
        if block.index != len(self.blockchain):
            return False

        # Check previous hash
        last_block = self.blockchain[-1] if self.blockchain else None
        if last_block and block.previous_hash != last_block.hash():
            return False

        # Check proof-of-work
        if not block.hash().startswith('00'):
            return False

        return True

    def resolve_conflicts(self) -> bool:
        """Resolve blockchain conflicts using consensus."""
        longest_chain = None
        max_length = len(self.blockchain)

        # Get all chains from peers
        chains = [peer.blockchain for peer in self.peers]

        for chain in chains:
            if len(chain) > max_length and self.validate_chain(chain):
                max_length = len(chain)
                longest_chain = chain

        if longest_chain:
            self.blockchain = longest_chain.copy()
            return True
        return False

    def validate_chain(self, chain: List[Block]) -> bool:
        """Validate an entire blockchain."""
        for i in range(1, len(chain)):
            current = chain[i]
            previous = chain[i-1]

            if current.previous_hash != previous.hash():
                return False
            if not current.hash().startswith('00'):
                return False
        return True

    def has_consensus(self) -> bool:
        """Check if consensus has been reached on the current state."""
        if not self.peers:
            return True

        # Count how many peers have the same last block hash
        my_last_hash = self.blockchain[-1].hash() if self.blockchain else "0"
        same_hash_count = 0

        for peer in self.peers:
            peer_last_hash = peer.blockchain[-1].hash() if peer.blockchain else "0"
            if peer_last_hash == my_last_hash:
                same_hash_count += 1

        # Check if consensus threshold is met
        return (same_hash_count / len(self.peers)) >= self.consensus_threshold

def main():
    """Demonstrate Pilotfish consensus mechanism."""
    # Create nodes
    node1 = PilotfishNode("node1")
    node2 = PilotfishNode("node2")
    node3 = PilotfishNode("node3")

    # Connect nodes
    node1.add_peer(node2)
    node1.add_peer(node3)
    node2.add_peer(node3)

    # Create some transactions
    tx1 = Transaction("Alice", "Bob", 1.5)
    tx2 = Transaction("Bob", "Charlie", 2.0)
    tx3 = Transaction("Charlie", "Alice", 0.5)

    # Add transactions to node1
    node1.add_transaction(tx1)
    node1.add_transaction(tx2)
    node1.add_transaction(tx3)

    # Mine block on node1
    mined_block = node1.mine_block()
    if mined_block:
        node1.broadcast_block(mined_block)

    # Check consensus
    print(f"Node1 consensus: {node1.has_consensus()}")
    print(f"Node2 consensus: {node2.has_consensus()}")
    print(f"Node3 consensus: {node3.has_consensus()}")

    # Resolve conflicts if any
    for node in [node1, node2, node3]:
        node.resolve_conflicts()

if __name__ == "__main__":
    main()
```
