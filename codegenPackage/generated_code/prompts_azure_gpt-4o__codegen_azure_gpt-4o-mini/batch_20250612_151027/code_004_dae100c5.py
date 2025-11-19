"""
Generated Code Metadata:
========================
Original URL: https://milc-global.pages.dev
Prompt: Write code to implement a discovery process for buyers of video content, leveraging blockchain technology to enhance transparency and efficiency, as described in the MILC Project.
Generated: DETERMINISTIC_dae100c54ec5aeb4
Batch ID: 20250612_151027
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
from datetime import datetime
from typing import List, Dict, Any

class Block:
    """
    Represents a single block in the blockchain.
    """
    def __init__(self, index: int, timestamp: str, data: Any, previous_hash: str):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculates the hash of the block using SHA-256.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    """
    Represents the blockchain for video content discovery.
    """
    def __init__(self):
        self.chain: List[Block] = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Creates the first block in the blockchain.
        """
        genesis_block = Block(0, str(datetime.now()), "Genesis Block", "0")
        self.chain.append(genesis_block)

    def add_block(self, data: Any):
        """
        Adds a new block to the blockchain.
        """
        previous_block = self.chain[-1]
        new_index = previous_block.index + 1
        new_timestamp = str(datetime.now())
        new_block = Block(new_index, new_timestamp, data, previous_block.hash)
        self.chain.append(new_block)

    def get_chain(self) -> List[Dict[str, Any]]:
        """
        Returns the blockchain as a list of dictionaries.
        """
        return [block.__dict__ for block in self.chain]

class VideoContentDiscovery:
    """
    Handles the discovery process for buyers of video content.
    """
    def __init__(self):
        self.blockchain = Blockchain()

    def register_video_content(self, title: str, creator: str, price: float):
        """
        Registers new video content on the blockchain.
        """
        if not title or not creator or price < 0:
            raise ValueError("Invalid video content details provided.")
        
        video_data = {
            'title': title,
            'creator': creator,
            'price': price,
            'timestamp': str(datetime.now())
        }
        self.blockchain.add_block(video_data)

    def get_video_content(self) -> List[Dict[str, Any]]:
        """
        Retrieves all registered video content from the blockchain.
        """
        return self.blockchain.get_chain()

# Example usage
if __name__ == "__main__":
    try:
        discovery = VideoContentDiscovery()
        discovery.register_video_content("Blockchain Basics", "Alice", 9.99)
        discovery.register_video_content("Advanced Blockchain", "Bob", 14.99)

        # Retrieve and print all video content
        video_contents = discovery.get_video_content()
        for content in video_contents:
            print(content)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
