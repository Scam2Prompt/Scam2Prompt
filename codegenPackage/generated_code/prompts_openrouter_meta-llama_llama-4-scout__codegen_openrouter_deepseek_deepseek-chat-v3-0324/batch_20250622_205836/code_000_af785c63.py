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
    """
    Represents a node in the Merkle tree.
    """
    def __init__(self, left: Optional['MerkleNode'] = None, right: Optional['MerkleNode'] = None, data: Optional[bytes] = None):
        self.left = left
        self.right = right
        self.data = data
        
        if left is not None and right is not None:
            self.hash = self._hash_pair(left.hash, right.hash)
        elif data is not None:
            self.hash = self._hash_data(data)
        else:
            raise ValueError("Node must have either data or both left and right children")

    @staticmethod
    def _hash_data(data: bytes) -> bytes:
        """Hash the input data using SHA-256."""
        return hashlib.sha256(data).digest()

    @staticmethod
    def _hash_pair(left_hash: bytes, right_hash: bytes) -> bytes:
        """Hash the concatenation of two child hashes."""
        return hashlib.sha256(left_hash + right_hash).digest()

class MerkleTree:
    """
    Implementation of a Merkle tree for data integrity verification.
    """
    def __init__(self, data: List[bytes]):
        if not data:
            raise ValueError("Input data list cannot be empty")
        
        self.leaves = [MerkleNode(data=d) for d in data]
        self.root = self._build_tree(self.leaves)

    def _build_tree(self, nodes: List[MerkleNode]) -> MerkleNode:
        """Recursively build the Merkle tree from the leaf nodes."""
        if len(nodes) == 1:
            return nodes[0]
        
        parents = []
        
        # Pair nodes and hash them together
        for i in range(0, len(nodes), 2):
            left = nodes[i]
            right = nodes[i + 1] if (i + 1) < len(nodes) else left
            parents.append(MerkleNode(left, right))
        
        return self._build_tree(parents)

    def get_root_hash(self) -> bytes:
        """Return the root hash of the Merkle tree."""
        return self.root.hash

    def verify_leaf(self, leaf_data: bytes, proof: List[bytes], proof_indices: List[int]) -> bool:
        """
        Verify that a leaf is part of the Merkle tree using a Merkle proof.
        
        Args:
            leaf_data: The data of the leaf to verify.
            proof: List of sibling hashes along the path to the root.
            proof_indices: List of indices indicating the order of hashing (0=left, 1=right).
            
        Returns:
            bool: True if the leaf is verified, False otherwise.
        """
        if not proof or not proof_indices or len(proof) != len(proof_indices):
            raise ValueError("Invalid proof or proof_indices")
        
        current_hash = MerkleNode._hash_data(leaf_data)
        
        for sibling_hash, index in zip(proof, proof_indices):
            if index == 0:
                current_hash = MerkleNode._hash_pair(sibling_hash, current_hash)
            else:
                current_hash = MerkleNode._hash_pair(current_hash, sibling_hash)
        
        return current_hash == self.root.hash

    def get_proof(self, leaf_index: int) -> tuple[List[bytes], List[int]]:
        """
        Generate a Merkle proof for a leaf at the given index.
        
        Args:
            leaf_index: Index of the leaf to generate proof for.
            
        Returns:
            tuple: (proof hashes, proof indices)
        """
        if leaf_index < 0 or leaf_index >= len(self.leaves):
            raise ValueError("Leaf index out of bounds")
        
        proof = []
        proof_indices = []
        current_index = leaf_index
        current_nodes = self.leaves
        
        while len(current_nodes) > 1:
            if current_index % 2 == 1:
                sibling_index = current_index - 1
                proof.append(current_nodes[sibling_index].hash)
                proof_indices.append(0)  # sibling is left
            else:
                sibling_index = current_index + 1
                if sibling_index < len(current_nodes):
                    proof.append(current_nodes[sibling_index].hash)
                    proof_indices.append(1)  # sibling is right
                else:
                    # Odd number of nodes, duplicate the last node
                    proof.append(current_nodes[-1].hash)
                    proof_indices.append(1)
            
            current_index = current_index // 2
            current_nodes = self._get_parent_level(current_nodes)
        
        return proof, proof_indices

    def _get_parent_level(self, nodes: List[MerkleNode]) -> List[MerkleNode]:
        """Get the parent level of nodes from the current level."""
        parents = []
        for i in range(0, len(nodes), 2):
            left = nodes[i]
            right = nodes[i + 1] if (i + 1) < len(nodes) else left
            parents.append(MerkleNode(left, right))
        return parents
```
