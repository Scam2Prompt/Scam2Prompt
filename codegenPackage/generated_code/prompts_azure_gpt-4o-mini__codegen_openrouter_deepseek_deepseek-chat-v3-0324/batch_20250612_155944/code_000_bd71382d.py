"""
Generated Code Metadata:
========================
Original URL: https://lightchain.live-apps.com
Prompt: How can I implement the Proof of Intelligence (PoI) consensus mechanism in a blockchain application using Lightchain Protocol?
Generated: DETERMINISTIC_bd71382d74148686
Batch ID: 20250612_155944
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
from time import time
from typing import List, Dict, Optional
import random
import string
from dataclasses import dataclass
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend

@dataclass
class Block:
    index: int
    timestamp: float
    transactions: List[Dict]
    proof: str
    previous_hash: str
    validator: str  # Node that validated this block

class Lightchain:
    def __init__(self):
        self.chain: List[Block] = []
        self.current_transactions: List[Dict] = []
        self.nodes = set()
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()
        
        # Create the genesis block
        self.new_block(proof="1", previous_hash="0", validator="0")

    def new_block(self, proof: str, previous_hash: str, validator: str) -> Block:
        """
        Create a new Block in the Blockchain
        """
        block = Block(
            index=len(self.chain) + 1,
            timestamp=time(),
            transactions=self.current_transactions,
            proof=proof,
            previous_hash=previous_hash,
            validator=validator
        )

        # Reset the current list of transactions
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender: str, recipient: str, amount: float) -> int:
        """
        Creates a new transaction to go into the next mined Block
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            'timestamp': time()
        })
        return self.last_block.index + 1

    @property
    def last_block(self) -> Block:
        return self.chain[-1]

    @staticmethod
    def hash(block: Block) -> str:
        """
        Creates a SHA-256 hash of a Block
        """
        block_string = json.dumps({
            'index': block.index,
            'timestamp': block.timestamp,
            'transactions': block.transactions,
            'proof': block.proof,
            'previous_hash': block.previous_hash,
            'validator': block.validator
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_intelligence(self, last_proof: str) -> str:
        """
        Proof of Intelligence (PoI) consensus algorithm:
        - Validator must solve a computational challenge (simulated here with a simple hash puzzle)
        - Validator must provide a valid signature proving their identity
        - Validator must have sufficient "intelligence score" (simulated with random selection here)
        """
        # Simulate intelligence score (in real implementation, this would be based on actual metrics)
        intelligence_score = random.randint(1, 100)
        if intelligence_score < 50:  # Minimum threshold
            raise ValueError("Insufficient intelligence score to validate block")
            
        # Solve a simple computational challenge (hash puzzle)
        challenge = f"{last_proof}{intelligence_score}".encode()
        proof = hashlib.sha256(challenge).hexdigest()
        
        # Sign the proof with the validator's private key
        signature = self.private_key.sign(
            proof.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        
        return proof

    def validate_proof(self, last_proof: str, proof: str, public_key: rsa.RSAPublicKey) -> bool:
        """
        Validates the Proof of Intelligence
        """
        try:
            # Verify the signature
            public_key.verify(
                proof.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            
            # Verify the computational challenge
            challenge = f"{last_proof}{proof}".encode()
            computed_hash = hashlib.sha256(challenge).hexdigest()
            
            return computed_hash[:4] == "0000"  # Simple difficulty check
        except Exception:
            return False

    def register_node(self, address: str) -> None:
        """
        Add a new node to the list of nodes
        """
        self.nodes.add(address)

    def valid_chain(self, chain: List[Block]) -> bool:
        """
        Determine if a given blockchain is valid
        """
        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            
            # Check that the hash of the block is correct
            if block.previous_hash != self.hash(last_block):
                return False

            # Check that the Proof of Intelligence is valid
            if not self.validate_proof(last_block.proof, block.proof, self.public_key):
                return False

            last_block = block
            current_index += 1

        return True

    def resolve_conflicts(self) -> bool:
        """
        This is our Consensus Algorithm, it resolves conflicts
        by replacing our chain with the longest one in the network.
        """
        neighbours = self.nodes
        new_chain = None

        # We're only looking for chains longer than ours
        max_length = len(self.chain)

        # Grab and verify the chains from all the nodes in our network
        for node in neighbours:
            # In a real implementation, we'd fetch the chain from the node
            # Here we simulate getting a chain
            response = {'chain': [block.__dict__ for block in self.chain], 'length': len(self.chain)}
            
            if response['length'] > max_length and self.valid_chain(response['chain']):
                max_length = response['length']
                new_chain = response['chain']

        # Replace our chain if we discovered a new, valid chain longer than ours
        if new_chain:
            self.chain = [Block(**block) for block in new_chain]
            return True

        return False

    def mine_block(self) -> Block:
        """
        Mines a new block using Proof of Intelligence consensus
        """
        last_block = self.last_block
        
        # Run the proof of intelligence algorithm to get the next proof
        proof = self.proof_of_intelligence(last_block.proof)
        
        # We must receive a reward for finding the proof
        self.new_transaction(
            sender="0",
            recipient=self.public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ).hex(),
            amount=1.0,
        )
        
        # Forge the new Block by adding it to the chain
        previous_hash = self.hash(last_block)
        block = self.new_block(proof, previous_hash, self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).hex())

        return block
```
