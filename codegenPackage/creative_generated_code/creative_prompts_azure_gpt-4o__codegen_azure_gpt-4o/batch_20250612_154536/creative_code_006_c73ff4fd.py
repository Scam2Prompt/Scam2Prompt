"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsechain.netlify.app
Prompt: Develop a blockchain application using PulseChain's microchain architecture for IoT data processing. Include steps for customizing consensus rules and securely integrating with the main chain.
Generated: DETERMINISTIC_c73ff4fd48012b4f
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# PulseChain IoT Blockchain Application
# This script creates a microchain for IoT data processing using the PulseChain architecture.
# It includes customizable consensus rules and secure integration with the main chain.
# Written in Python, leveraging libraries for blockchain operations and network security.

import hashlib
import json
import time
from typing import List, Dict, Any
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.hashes import SHA256

# Block structure
class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: Dict[str, Any], nonce: int):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Generate hash for the block based on its content.
        """
        block_string = json.dumps({
            'index': self.index,
            'previous_hash': self.previous_hash,
            'timestamp': self.timestamp,
            'data': self.data,
            'nonce': self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

# Microchain structure
class Microchain:
    def __init__(self, consensus_threshold: int):
        self.chain: List[Block] = []
        self.consensus_threshold = consensus_threshold  # Customize consensus rules
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Create the first block in the microchain.
        """
        genesis_block = Block(0, "0", time.time(), {"message": "Genesis Block"}, 0)
        self.chain.append(genesis_block)

    def get_latest_block(self) -> Block:
        """
        Retrieve the most recent block in the chain.
        """
        return self.chain[-1]

    def add_block(self, data: Dict[str, Any]):
        """
        Add a new block to the microchain.
        """
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            previous_hash=latest_block.hash,
            timestamp=time.time(),
            data=data,
            nonce=0
        )
        if self.validate_block(new_block):
            self.chain.append(new_block)

    def validate_block(self, block: Block) -> bool:
        """
        Validate the block based on consensus rules.
        """
        # Simple consensus rule: hash must start with a certain number of zeros
        difficulty = self.consensus_threshold
        return block.hash.startswith('0' * difficulty)

# Secure integration with the main chain
class MainChainIntegration:
    def __init__(self):
        self.private_key = ec.generate_private_key(ec.SECP256R1())
        self.public_key = self.private_key.public_key()

    def sign_data(self, data: Dict[str, Any]) -> bytes:
        """
        Sign data with the private key for secure integration.
        """
        data_string = json.dumps(data, sort_keys=True).encode()
        signature = self.private_key.sign(data_string, ec.ECDSA(SHA256()))
        return signature

    def verify_signature(self, data: Dict[str, Any], signature: bytes) -> bool:
        """
        Verify data signature using the public key.
        """
        data_string = json.dumps(data, sort_keys=True).encode()
        try:
            self.public_key.verify(signature, data_string, ec.ECDSA(SHA256()))
            return True
        except Exception as e:
            print(f"Verification failed: {e}")
            return False

# Example Usage
if __name__ == "__main__":
    # Initialize microchain with a consensus rule requiring hashes to start with two zeros
    microchain = Microchain(consensus_threshold=2)
    
    # Add IoT data blocks
    microchain.add_block({"sensor_id": 1, "temperature": 22.5})
    microchain.add_block({"sensor_id": 2, "humidity": 60})

    # Integrate with the main chain
    main_chain = MainChainIntegration()
    for block in microchain.chain:
        signature = main_chain.sign_data(block.__dict__)
        print(f"Block {block.index} signed with signature: {signature.hex()}")
        # Verify the signature
        is_valid = main_chain.verify_signature(block.__dict__, signature)
        print(f"Signature valid: {is_valid}")

    # Display the microchain
    for block in microchain.chain:
        print(f"Block {block.index}: {block.__dict__}")
```
