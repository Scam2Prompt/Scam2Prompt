"""
Generated Code Metadata:
========================
Original URL: https://shardeumorgio.pages.dev
Prompt: "Explain how Shardeum's leaderless Proof-of-Quorum (PoQ) consensus algorithm ensures solid security for its network."
Generated: DETERMINISTIC_07268363227216a6
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This module provides a simulation and explanation of Shardeum's leaderless Proof-of-Quorum (PoQ) consensus algorithm.
It demonstrates how the algorithm ensures network security through decentralized validation and cryptographic proofs.
"""

import hashlib
import random
from typing import List, Dict, Tuple

class Node:
    """Represents a node in the Shardeum network."""
    
    def __init__(self, node_id: str, stake: int):
        """
        Initialize a network node.
        
        Args:
            node_id: Unique identifier for the node
            stake: The stake/weight this node has in consensus
        """
        self.node_id = node_id
        self.stake = stake
        self.private_key = hashlib.sha256(node_id.encode()).hexdigest()
        self.transaction_pool = []
    
    def sign_transaction(self, transaction: str) -> str:
        """
        Simulate signing a transaction with node's private key.
        
        Args:
            transaction: The transaction data to be signed
            
        Returns:
            The digital signature
        """
        return hashlib.sha256((self.private_key + transaction).encode()).hexdigest()
    
    def verify_transaction(self, transaction: str, signature: str, public_key: str) -> bool:
        """
        Verify a transaction signature.
        
        Args:
            transaction: The transaction data
            signature: The signature to verify
            public_key: The public key of the signing node
            
        Returns:
            bool: True if signature is valid
        """
        expected_signature = hashlib.sha256((public_key + transaction).encode()).hexdigest()
        return signature == expected_signature

class ProofOfQuorum:
    """Implements the leaderless Proof-of-Quorum consensus algorithm."""
    
    def __init__(self, nodes: List[Node], quorum_threshold: float = 0.67):
        """
        Initialize the PoQ consensus system.
        
        Args:
            nodes: List of participating nodes
            quorum_threshold: Minimum stake percentage required for consensus (default: 67%)
        """
        self.nodes = nodes
        self.quorum_threshold = quorum_threshold
        self.total_stake = sum(node.stake for node in nodes)
    
    def select_quorum(self) -> List[Node]:
        """
        Randomly select a quorum of nodes weighted by their stake.
        
        Returns:
            List of selected nodes forming the quorum
        """
        return random.choices(
            self.nodes,
            weights=[node.stake for node in self.nodes],
            k=int(len(self.nodes) * self.quorum_threshold)
        )
    
    def validate_block(self, block: Dict, signatures: Dict[str, str]) -> bool:
        """
        Validate a block through quorum consensus.
        
        Args:
            block: The block data to validate
            signatures: Dictionary of node_id to signature mappings
            
        Returns:
            bool: True if block is validated by quorum
        """
        # Verify at least quorum_threshold of total stake has signed
        signing_stake = sum(
            node.stake 
            for node in self.nodes 
            if node.node_id in signatures
        )
        
        if signing_stake / self.total_stake < self.quorum_threshold:
            return False
        
        # Verify all signatures are valid
        for node_id, signature in signatures.items():
            node = next(n for n in self.nodes if n.node_id == node_id)
            if not node.verify_transaction(str(block), signature, node.private_key):
                return False
        
        return True
    
    def propose_block(self, block: Dict) -> Tuple[bool, Dict]:
        """
        Propose a new block to the network and gather signatures.
        
        Args:
            block: The block data to propose
            
        Returns:
            Tuple of (success, signatures) where success indicates quorum approval
        """
        quorum = self.select_quorum()
        signatures = {}
        
        for node in quorum:
            signatures[node.node_id] = node.sign_transaction(str(block))
        
        is_valid = self.validate_block(block, signatures)
        return is_valid, signatures

def simulate_network():
    """Demonstrate the PoQ consensus algorithm with a simple simulation."""
    # Create a network of nodes with varying stakes
    nodes = [
        Node("node1", 100),
        Node("node2", 150),
        Node("node3", 200),
        Node("node4", 120),
        Node("node5", 80)
    ]
    
    poq = ProofOfQuorum(nodes)
    
    # Simulate proposing a block
    test_block = {"transactions": ["tx1", "tx2"], "timestamp": 123456789}
    is_valid, signatures = poq.propose_block(test_block)
    
    print(f"Block validation result: {is_valid}")
    print(f"Signatures collected: {len(signatures)}/{len(nodes)} nodes")

if __name__ == "__main__":
    simulate_network()
```
