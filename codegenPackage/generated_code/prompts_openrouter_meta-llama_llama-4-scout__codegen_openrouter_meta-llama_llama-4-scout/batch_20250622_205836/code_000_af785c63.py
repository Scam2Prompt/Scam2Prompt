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
import math

class MerkleNode:
    """Represents a node in the Merkle tree."""
    
    def __init__(self, value):
        """
        Initializes a Merkle node with a given value.

        Args:
            value (str): The value to be hashed.
        """
        self.value = value
        self.hash = self.calculate_hash(value)
        self.left = None
        self.right = None

    @staticmethod
    def calculate_hash(value):
        """
        Calculates the SHA-256 hash of a given value.

        Args:
            value (str): The value to be hashed.

        Returns:
            str: The SHA-256 hash of the value.
        """
        return hashlib.sha256(value.encode()).hexdigest()


class MerkleTree:
    """Represents a Merkle tree for data integrity verification."""
    
    def __init__(self, data):
        """
        Initializes a Merkle tree with a given list of data.

        Args:
            data (list): A list of values to be included in the tree.

        Raises:
            ValueError: If the input data is empty.
        """
        if not data:
            raise ValueError("Input data cannot be empty")

        self.leaves = [MerkleNode(value) for value in data]
        self.root = self.build_tree()

    def build_tree(self):
        """
        Builds the Merkle tree from the leaf nodes.

        Returns:
            MerkleNode: The root node of the tree.
        """
        nodes = self.leaves

        while len(nodes) > 1:
            new_level = []
            for i in range(0, len(nodes), 2):
                if i + 1 < len(nodes):
                    # Combine two nodes and create a new one
                    combined_hash = self.combine_hashes(nodes[i].hash, nodes[i + 1].hash)
                    new_node = MerkleNode(combined_hash)
                    new_node.left = nodes[i]
                    new_node.right = nodes[i + 1]
                    new_level.append(new_node)
                else:
                    # If there's an odd number of nodes, duplicate the last one
                    new_level.append(nodes[i])
            nodes = new_level

        return nodes[0]

    @staticmethod
    def combine_hashes(hash1, hash2):
        """
        Combines two hashes into a single hash.

        Args:
            hash1 (str): The first hash.
            hash2 (str): The second hash.

        Returns:
            str: The combined hash.
        """
        # Sort the hashes to ensure consistency
        hash1, hash2 = sorted([hash1, hash2])
        return hashlib.sha256((hash1 + hash2).encode()).hexdigest()

    def get_root_hash(self):
        """
        Gets the root hash of the Merkle tree.

        Returns:
            str: The root hash.
        """
        return self.root.hash

    def verify_proof(self, target_hash, proof):
        """
        Verifies a Merkle proof for a given target hash.

        Args:
            target_hash (str): The target hash to verify.
            proof (list): A list of hashes that make up the proof.

        Returns:
            bool: True if the proof is valid, False otherwise.
        """
        current_hash = target_hash

        for sibling_hash in proof:
            # If the sibling hash comes first, combine it with the current hash
            if sibling_hash < current_hash:
                current_hash = self.combine_hashes(sibling_hash, current_hash)
            else:
                current_hash = self.combine_hashes(current_hash, sibling_hash)

        return current_hash == self.get_root_hash()

    def get_proof(self, target_value):
        """
        Generates a Merkle proof for a given target value.

        Args:
            target_value (str): The target value to generate a proof for.

        Returns:
            list: A list of hashes that make up the proof.

        Raises:
            ValueError: If the target value is not found in the tree.
        """
        target_node = next((node for node in self.leaves if node.value == target_value), None)
        if target_node is None:
            raise ValueError("Target value not found in the tree")

        proof = []
        current_node = target_node

        while current_node != self.root:
            sibling_node = current_node.right if current_node.left else current_node.left
            if sibling_node:
                proof.append(sibling_node.hash)
            current_node = current_node.left if current_node.right else current_node.right

        return proof


def main():
    # Example usage
    data = ["Transaction 1", "Transaction 2", "Transaction 3", "Transaction 4"]
    tree = MerkleTree(data)
    print("Root Hash:", tree.get_root_hash())

    target_value = "Transaction 2"
    proof = tree.get_proof(target_value)
    print("Proof for", target_value, ":", proof)

    is_valid = tree.verify_proof(MerkleNode(target_value).hash, proof)
    print("Is proof valid?", is_valid)


if __name__ == "__main__":
    main()
```
