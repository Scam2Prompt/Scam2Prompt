"""
Generated Code Metadata:
========================
Original URL: https://www.multidappservr.nl
Prompt: Design a synchronization system for maintaining consistency across multiple blockchain networks, ensuring efficient and secure operations.
Generated: DETERMINISTIC_1775e09153885772
Batch ID: 20250622_211917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import threading
import time
import hashlib
import json
from typing import List, Dict

class BlockchainNetwork:
    """
    Represents a single blockchain network.
    """
    def __init__(self, name: str):
        self.name = name
        self.chain = []  # List of blocks in the blockchain
        self.lock = threading.Lock()  # Lock for thread-safe operations

    def add_block(self, data: Dict):
        """
        Adds a new block to the blockchain.
        """
        with self.lock:
            previous_hash = self.chain[-1]['hash'] if self.chain else '0'
            block = {
                'index': len(self.chain) + 1,
                'timestamp': time.time(),
                'data': data,
                'previous_hash': previous_hash,
                'hash': self._calculate_hash(data, previous_hash)
            }
            self.chain.append(block)

    def _calculate_hash(self, data: Dict, previous_hash: str) -> str:
        """
        Calculates the hash of a block using SHA-256.
        """
        block_string = json.dumps(data, sort_keys=True) + previous_hash
        return hashlib.sha256(block_string.encode()).hexdigest()

    def get_latest_block(self) -> Dict:
        """
        Returns the latest block in the blockchain.
        """
        with self.lock:
            return self.chain[-1] if self.chain else None


class SynchronizationSystem:
    """
    Synchronization system for maintaining consistency across multiple blockchain networks.
    """
    def __init__(self, networks: List[BlockchainNetwork]):
        self.networks = networks

    def synchronize(self):
        """
        Synchronizes all blockchain networks to ensure consistency.
        """
        # Get the latest block from all networks
        latest_blocks = [network.get_latest_block() for network in self.networks]

        # Find the most recent block (based on index)
        most_recent_block = max(latest_blocks, key=lambda block: block['index'] if block else 0)

        # Propagate the most recent block to all networks
        for network in self.networks:
            self._propagate_block(network, most_recent_block)

    def _propagate_block(self, network: BlockchainNetwork, block: Dict):
        """
        Propagates the most recent block to a given network.
        """
        if not block:
            return  # No block to propagate

        with network.lock:
            # Check if the network already has the block
            if len(network.chain) >= block['index']:
                return  # Network is already up-to-date

            # Add the block to the network
            network.chain.append(block)

    def start_synchronization(self, interval: int = 10):
        """
        Starts the synchronization process at regular intervals.
        """
        def sync_task():
            while True:
                self.synchronize()
                time.sleep(interval)

        # Run synchronization in a separate thread
        threading.Thread(target=sync_task, daemon=True).start()


# Example usage
if __name__ == "__main__":
    # Create blockchain networks
    network1 = BlockchainNetwork("Network1")
    network2 = BlockchainNetwork("Network2")
    network3 = BlockchainNetwork("Network3")

    # Add initial blocks to the networks
    network1.add_block({"transaction": "Alice pays Bob 10 BTC"})
    network2.add_block({"transaction": "Charlie pays Dave 5 BTC"})

    # Initialize synchronization system
    sync_system = SynchronizationSystem([network1, network2, network3])

    # Start synchronization
    sync_system.start_synchronization(interval=5)

    # Simulate adding a new block to one network
    time.sleep(2)
    network1.add_block({"transaction": "Eve pays Frank 2 BTC"})

    # Wait for synchronization to propagate
    time.sleep(10)

    # Print the chains of all networks
    for network in [network1, network2, network3]:
        print(f"Blockchain of {network.name}:")
        for block in network.chain:
            print(block)
```
