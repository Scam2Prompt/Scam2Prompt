"""
Generated Code Metadata:
========================
Original URL: https://en-bitcoin.org
Prompt: Explain how Bitcoin Core achieves consensus among users without voting, and provide an example of how this can be implemented in a decentralized application.
Generated: DETERMINISTIC_ac6dd3d74fa93559
Batch ID: 20250612_162610
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://node1.example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import hashlib
import json
from typing import Dict, List, Optional

class Block:
    def __init__(self, index: int, transactions: List[Dict], timestamp: float, previous_hash: str, nonce: int = 0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce

    def compute_hash(self) -> str:
        """
        Compute the SHA-256 hash of the block.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain: List[Block] = []
        self.current_transactions: List[Dict] = []
        self.nodes = set()  # Nodes in the network
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Create the genesis block (first block in the chain).
        """
        genesis_block = Block(0, [], 0, "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    def add_block(self, block: Block, proof: str) -> bool:
        """
        Add a new block to the blockchain after verifying proof of work.
        """
        previous_hash = self.last_block.compute_hash()
        if previous_hash != block.previous_hash:
            return False

        if not self.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    def is_valid_proof(self, block: Block, block_hash: str) -> bool:
        """
        Check if block_hash is a valid proof of work for the block.
        """
        return (block_hash.startswith('0000') and 
                block_hash == block.compute_hash())

    def proof_of_work(self, block: Block) -> str:
        """
        Simple proof of work algorithm:
        - Find a nonce such that the hash of the block starts with 4 leading zeros.
        """
        block.nonce = 0
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0000'):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    def resolve_conflicts(self) -> bool:
        """
        Consensus algorithm: Resolve conflicts by replacing our chain with the longest one in the network.
        """
        new_chain = None
        max_length = len(self.chain)

        # Get all nodes' chains and find the longest valid one
        for node in self.nodes:
            # In a real implementation, this would fetch the chain from the node
            node_chain = self.get_chain_from_node(node)
            if len(node_chain) > max_length and self.is_chain_valid(node_chain):
                max_length = len(node_chain)
                new_chain = node_chain

        if new_chain:
            self.chain = new_chain
            return True

        return False

    def is_chain_valid(self, chain: List[Block]) -> bool:
        """
        Check if a given blockchain is valid.
        """
        for i in range(1, len(chain)):
            current_block = chain[i]
            previous_block = chain[i-1]

            # Check hash integrity
            if current_block.hash != current_block.compute_hash():
                return False

            # Check previous hash reference
            if current_block.previous_hash != previous_block.compute_hash():
                return False

            # Check proof of work
            if not self.is_valid_proof(current_block, current_block.hash):
                return False

        return True

    @property
    def last_block(self) -> Block:
        return self.chain[-1]

    def register_node(self, node_address: str):
        """
        Add a new node to the list of nodes.
        """
        self.nodes.add(node_address)

    def get_chain_from_node(self, node_address: str) -> List[Block]:
        """
        Simulate fetching the chain from a node.
        In a real implementation, this would make a network request.
        """
        # Placeholder - in reality, this would fetch from the node
        return []

# Example usage
if __name__ == "__main__":
    blockchain = Blockchain()
    
    # Add a new transaction
    blockchain.current_transactions.append({
        'sender': 'Alice',
        'recipient': 'Bob',
        'amount': 1
    })
    
    # Mine a new block
    last_block = blockchain.last_block
    new_block = Block(
        index=last_block.index + 1,
        transactions=blockchain.current_transactions,
        timestamp=0,  # In reality, this would be the current time
        previous_hash=last_block.hash
    )
    
    proof = blockchain.proof_of_work(new_block)
    blockchain.add_block(new_block, proof)
    
    # Check chain validity
    print(f"Chain valid: {blockchain.is_chain_valid(blockchain.chain)}")
    
    # Simulate resolving conflicts (consensus)
    blockchain.register_node("http://node1.example.com")
    blockchain.resolve_conflicts()
```
