"""
Generated Code Metadata:
========================
Original URL: https://ethershares.blogspot.nl
Prompt: Generate code for a simple blockchain-based commenting system for a blog.
Generated: DETERMINISTIC_b12b717f17843d8a
Batch ID: 20250622_205537
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

class Block:
    """
    A single block in the blockchain containing comment data.
    """
    def __init__(self, index: int, timestamp: float, comment: str, previous_hash: str):
        self.index = index
        self.timestamp = timestamp
        self.comment = comment
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the SHA-256 hash of the block.
        """
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "comment": self.comment,
            "previous_hash": self.previous_hash
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def to_dict(self) -> Dict:
        """
        Convert block to dictionary for easy serialization.
        """
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "comment": self.comment,
            "previous_hash": self.previous_hash,
            "hash": self.hash
        }

class Blockchain:
    """
    A simple blockchain implementation for storing comments.
    """
    def __init__(self):
        self.chain: List[Block] = []
        self.create_genesis_block()

    def create_genesis_block(self) -> None:
        """
        Create the first block in the blockchain (genesis block).
        """
        genesis_block = Block(0, time(), "Genesis Block", "0")
        self.chain.append(genesis_block)

    def get_latest_block(self) -> Block:
        """
        Get the most recent block in the chain.
        """
        return self.chain[-1]

    def add_block(self, comment: str) -> Optional[Block]:
        """
        Add a new block with the given comment to the chain.
        Returns None if the chain is invalid after adding the block.
        """
        if not self.is_chain_valid():
            return None

        previous_block = self.get_latest_block()
        new_block = Block(
            index=previous_block.index + 1,
            timestamp=time(),
            comment=comment,
            previous_hash=previous_block.hash
        )
        self.chain.append(new_block)
        return new_block

    def is_chain_valid(self) -> bool:
        """
        Validate the integrity of the blockchain.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            # Check if current block's hash is correct
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if current block points to the correct previous hash
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def get_all_comments(self) -> List[Dict]:
        """
        Get all comments in the blockchain as a list of dictionaries.
        """
        return [block.to_dict() for block in self.chain[1:]]  # Exclude genesis block

class BlogCommentSystem:
    """
    A simple blog commenting system using blockchain.
    """
    def __init__(self):
        self.blockchain = Blockchain()

    def add_comment(self, comment_text: str) -> Optional[Dict]:
        """
        Add a new comment to the blockchain.
        Returns None if the comment couldn't be added (invalid chain).
        """
        if not comment_text.strip():
            raise ValueError("Comment cannot be empty")
        
        new_block = self.blockchain.add_block(comment_text)
        if new_block is None:
            return None
        return new_block.to_dict()

    def get_comments(self) -> List[Dict]:
        """
        Get all comments from the blockchain.
        """
        return self.blockchain.get_all_comments()

    def validate_chain(self) -> bool:
        """
        Validate the integrity of the blockchain.
        """
        return self.blockchain.is_chain_valid()

# Example usage
if __name__ == "__main__":
    blog = BlogCommentSystem()
    
    # Add some comments
    blog.add_comment("First comment on this blog!")
    blog.add_comment("Blockchain is awesome!")
    blog.add_comment("This is a secure commenting system.")
    
    # Get all comments
    comments = blog.get_comments()
    print("All Comments:")
    for comment in comments:
        print(f"{comment['index']}: {comment['comment']} (Timestamp: {comment['timestamp']})")
    
    # Validate chain
    print("\nBlockchain valid:", blog.validate_chain())
```
