"""
Generated Code Metadata:
========================
Original URL: https://polkadot.fi
Prompt: What is Polkadot and how does it relate to blockchain interoperability, considering the information typically found on https://polkadot.fi?
Generated: DETERMINISTIC_04efa11e588bd01e
Batch ID: 20250622_212502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Polkadot Blockchain Interoperability Demo

This script demonstrates Polkadot's role in blockchain interoperability 
by simulating cross-chain communication between parachains.
"""

import json
from typing import Dict, List, Optional
from dataclasses import dataclass
import hashlib
import random

@dataclass
class Block:
    """Represents a blockchain block with basic properties."""
    index: int
    timestamp: float
    data: Dict
    previous_hash: str
    nonce: int = 0
    hash: Optional[str] = None

    def compute_hash(self) -> str:
        """Calculate the SHA-256 hash of the block."""
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Parachain:
    """Represents a Polkadot parachain with basic blockchain functionality."""
    
    def __init__(self, name: str):
        self.name = name
        self.chain: List[Block] = []
        self.create_genesis_block()
    
    def create_genesis_block(self) -> None:
        """Initialize the parachain with a genesis block."""
        genesis_block = Block(
            index=0,
            timestamp=0,
            data={"message": f"Genesis block of {self.name}"},
            previous_hash="0"
        )
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)
    
    def add_block(self, data: Dict) -> Block:
        """Add a new block to the parachain."""
        last_block = self.chain[-1]
        new_block = Block(
            index=last_block.index + 1,
            timestamp=random.random(),  # Simulated timestamp
            data=data,
            previous_hash=last_block.hash
        )
        new_block.hash = new_block.compute_hash()
        self.chain.append(new_block)
        return new_block
    
    def get_last_block(self) -> Block:
        """Get the most recent block in the parachain."""
        return self.chain[-1]

class RelayChain:
    """Represents Polkadot's relay chain that connects parachains."""
    
    def __init__(self):
        self.parachains: Dict[str, Parachain] = {}
    
    def register_parachain(self, parachain: Parachain) -> None:
        """Register a new parachain with the relay chain."""
        if parachain.name in self.parachains:
            raise ValueError(f"Parachain {parachain.name} already registered")
        self.parachains[parachain.name] = parachain
    
    def validate_cross_chain_message(self, sender: str, recipient: str, message: Dict) -> bool:
        """Validate a cross-chain message between parachains."""
        if sender not in self.parachains or recipient not in self.parachains:
            return False
        return True
    
    def send_cross_chain_message(self, sender: str, recipient: str, message: Dict) -> bool:
        """Send a message from one parachain to another."""
        if not self.validate_cross_chain_message(sender, recipient, message):
            return False
        
        # Simulate message passing through relay chain
        self.parachains[recipient].add_block({
            "type": "cross_chain_message",
            "from": sender,
            "content": message
        })
        return True

def demo_polkadot_interoperability():
    """Demonstrate Polkadot's interoperability features."""
    # Create relay chain (Polkadot)
    relay_chain = RelayChain()
    
    # Create and register parachains
    parachain_a = Parachain("ParachainA")
    parachain_b = Parachain("ParachainB")
    relay_chain.register_parachain(parachain_a)
    relay_chain.register_parachain(parachain_b)
    
    # Add some blocks to parachains
    parachain_a.add_block({"message": "First block on ParachainA"})
    parachain_b.add_block({"message": "First block on ParachainB"})
    
    # Send cross-chain message
    message = {"action": "transfer", "amount": 100, "asset": "DOT"}
    success = relay_chain.send_cross_chain_message(
        "ParachainA",
        "ParachainB",
        message
    )
    
    if success:
        print("Cross-chain message successfully delivered!")
        print(f"Latest block on ParachainB: {parachain_b.get_last_block().data}")
    else:
        print("Failed to deliver cross-chain message")

if __name__ == "__main__":
    demo_polkadot_interoperability()
```
