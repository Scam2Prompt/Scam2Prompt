"""
Generated Code Metadata:
========================
Original URL: https://bafybeigix4apwqk6fyecm444vwmi65rxaxhb23mlme4in2u5oa4cl7abza.ipfs.dweb.link
Prompt: Explain how the Botanix EVM achieves probabilistic finality by posting the Merkle tree root back to the Bitcoin base layer, ensuring protection against long-range attacks.
Generated: DETERMINISTIC_2c0e7636a15cc418
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# botanic_evm_finality.py

import hashlib
import json
from typing import List, Dict, Optional

class Block:
    def __init__(self, height: int, transactions: List[str], previous_hash: str):
        self.height = height
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        block_data = {
            'height': self.height,
            'transactions': self.transactions,
            'previous_hash': self.previous_hash
        }
        block_string = json.dumps(block_data, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class BotanixEVM:
    def __init__(self):
        self.blocks: List[Block] = []
        self.merkle_roots: Dict[int, str] = {}  # Maps block height to Merkle root
        self.bitcoin_anchors: Dict[int, str] = {}  # Maps block height to Bitcoin TXID

    def add_block(self, transactions: List[str]) -> None:
        previous_hash = self.blocks[-1].hash if self.blocks else "0"
        new_block = Block(len(self.blocks), transactions, previous_hash)
        self.blocks.append(new_block)

    def calculate_merkle_root(self, block_hashes: List[str]) -> str:
        if not block_hashes:
            return ""
        
        current_level = block_hashes
        while len(current_level) > 1:
            next_level = []
            for i in range(0, len(current_level), 2):
                left = current_level[i]
                right = current_level[i + 1] if i + 1 < len(current_level) else current_level[i]
                combined = left + right
                next_level.append(hashlib.sha256(combined.encode()).hexdigest())
            current_level = next_level
        
        return current_level[0]

    def checkpoint_to_bitcoin(self, block_height: int, bitcoin_client) -> Optional[str]:
        """
        Posts the Merkle root of recent blocks to Bitcoin blockchain
        Returns Bitcoin transaction ID if successful
        """
        if block_height >= len(self.blocks):
            return None
        
        # Get recent block hashes (e.g., last 100 blocks)
        recent_blocks = self.blocks[max(0, block_height-100):block_height+1]
        block_hashes = [block.hash for block in recent_blocks]
        
        merkle_root = self.calculate_merkle_root(block_hashes)
        self.merkle_roots[block_height] = merkle_root
        
        try:
            # Simulate posting to Bitcoin (in a real implementation, this would use a Bitcoin client)
            txid = bitcoin_client.post_data(merkle_root)
            self.bitcoin_anchors[block_height] = txid
            return txid
        except Exception as e:
            print(f"Error posting to Bitcoin: {e}")
            return None

    def verify_finality(self, block_height: int, bitcoin_client) -> bool:
        """
        Verifies probabilistic finality by checking Bitcoin anchor
        Returns True if the block is considered final
        """
        if block_height not in self.merkle_roots or block_height not in self.bitcoin_anchors:
            return False
        
        try:
            # Verify the Merkle root exists in Bitcoin blockchain
            merkle_root = self.merkle_roots[block_height]
            txid = self.bitcoin_anchors[block_height]
            
            # In a real implementation, this would verify the Merkle root is in the Bitcoin transaction
            if not bitcoin_client.verify_data(txid, merkle_root):
                return False
            
            # Check that enough confirmations have passed (e.g., 6 blocks)
            confirmations = bitcoin_client.get_confirmations(txid)
            return confirmations >= 6
        except Exception as e:
            print(f"Error verifying finality: {e}")
            return False

class MockBitcoinClient:
    """Mock Bitcoin client for demonstration purposes"""
    def __init__(self):
        self.posted_data = {}
    
    def post_data(self, data: str) -> str:
        txid = hashlib.sha256(data.encode()).hexdigest()
        self.posted_data[txid] = data
        return txid
    
    def verify_data(self, txid: str, data: str) -> bool:
        return self.posted_data.get(txid) == data
    
    def get_confirmations(self, txid: str) -> int:
        return 6  # Always return 6 confirmations for demo
```
