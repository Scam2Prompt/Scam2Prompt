"""
Generated Code Metadata:
========================
Original URL: https://app-mercle.pages.dev
Prompt: How can I implement a Merkle tree in Python for data integrity verification?
Generated: DETERMINISTIC_af785c63c04adba5
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
from typing import List, Optional

class MerkleNode:
    """Class representing a node in the Merkle tree."""
    
    def __init__(self, left: Optional['MerkleNode'], right: Optional['MerkleNode'], data: Optional[str] = None):
        self.left = left
        self.right = right
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """Calculate the hash of the node."""
        if self.data is not None:
            return hashlib.sha256(self.data.encode()).hexdigest()
        if self.left is not None and self.right is not None:
            return hashlib.sha256((self.left.hash + self.right.hash).encode()).hexdigest()
        return ''

class MerkleTree:
    """Class representing a Merkle tree."""
    
    def __init__(self, data_list: List[str]):
        self.leaves = [MerkleNode(None, None, data) for data in data_list]
        self.root = self.build_tree(self.leaves)

    def build_tree(self, nodes: List[MerkleNode]) -> MerkleNode:
        """Recursively build the Merkle tree from the leaves."""
        if len(nodes) == 1:
            return nodes[0]
        
        # If the number of nodes is odd, duplicate the last node
        if len(nodes) % 2 != 0:
            nodes.append(nodes[-1])
        
        parent_nodes = []
        for i in range(0, len(nodes), 2):
            parent_nodes.append(MerkleNode(nodes[i], nodes[i + 1]))
        
        return self.build_tree(parent_nodes)

    def get_root_hash(self) -> str:
        """Return the root hash of the Merkle tree."""
        return self.root.hash

    def verify_data(self, data: str) -> bool:
        """Verify if the given data is part of the Merkle tree."""
        for leaf in self.leaves:
            if leaf.data == data:
                return True
        return False

# Example usage
if __name__ == "__main__":
    try:
        data = ["data1", "data2", "data3", "data4"]
        merkle_tree = MerkleTree(data)
        
        print("Merkle Root Hash:", merkle_tree.get_root_hash())
        
        # Verify if a piece of data is in the tree
        data_to_verify = "data2"
        is_verified = merkle_tree.verify_data(data_to_verify)
        print(f"Is '{data_to_verify}' part of the Merkle tree? {is_verified}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
