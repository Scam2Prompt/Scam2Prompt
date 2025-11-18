"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taikoairdrops.vercel.app
Prompt: Create a function to calculate Merkle proofs for Taiko token claims using the provided eligibility data and tokenomics rules.
Generated: DETERMINISTIC_5a827d1125668be9
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
from typing import List, Tuple, Dict


class MerkleTree:
    """
    A class representing a Merkle Tree, which can be used to generate and verify Merkle proofs.
    """

    def __init__(self, data: List[str]):
        """
        Initialize the Merkle Tree with a list of data elements.

        :param data: List of data elements to create the tree.
        """
        self.leaves = [self.hash_data(item) for item in data]  # Hash the input data
        self.tree = self.build_tree(self.leaves)

    @staticmethod
    def hash_data(data: str) -> str:
        """
        Hash a data element using SHA256.

        :param data: The data to hash, in string format.
        :return: The hashed value in hexadecimal format.
        """
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    def build_tree(self, leaves: List[str]) -> List[List[str]]:
        """
        Build the Merkle Tree from the hashed leaves.

        :param leaves: A list of hashed leaf nodes.
        :return: A 2D list representing the levels of the Merkle Tree.
        """
        tree = [leaves]
        while len(tree[-1]) > 1:
            current_level = tree[-1]
            next_level = []
            for i in range(0, len(current_level), 2):
                # Pair up adjacent nodes; if odd, duplicate the last node
                left = current_level[i]
                right = current_level[i + 1] if i + 1 < len(current_level) else left
                next_level.append(self.hash_data(left + right))
            tree.append(next_level)
        return tree

    def get_root(self) -> str:
        """
        Get the Merkle root of the tree.

        :return: The Merkle root as a hexadecimal string.
        """
        return self.tree[-1][0] if self.tree else None

    def get_proof(self, index: int) -> List[Tuple[str, str]]:
        """
        Generate a Merkle proof for a specific leaf.

        :param index: The index of the leaf in the original data.
        :return: A list of tuples representing the proof; each tuple contains
                 the sibling hash and its position ('left' or 'right').
        """
        proof = []
        for level in self.tree[:-1]:  # Exclude the root level
            sibling_index = index ^ 1  # XOR to find sibling index
            sibling_position = 'left' if sibling_index < index else 'right'
            if sibling_index < len(level):
                proof.append((level[sibling_index], sibling_position))
            index //= 2  # Move to the next level in the tree
        return proof


# Tokenomics Rules and Eligibility Data
def calculate_merkle_proof(claim_data: Dict[str, float], user: str) -> Tuple[List[Tuple[str, str]], str]:
    """
    Calculate the Merkle proof for a specific user's eligibility for a token claim.

    :param claim_data: A dictionary mapping user identifiers (e.g., addresses) to claim amounts.
    :param user: The user identifier for which to calculate the proof.
    :return: A tuple containing the proof and the Merkle root.
    """
    try:
        if user not in claim_data:
            raise ValueError("User not found in eligibility data.")

        # Generate the Merkle Tree
        data_items = [f"{addr}:{amount}" for addr, amount in claim_data.items()]
        merkle_tree = MerkleTree(data_items)

        # Find the index of the user's data in the list
        user_data = f"{user}:{claim_data[user]}"
        index = data_items.index(user_data)

        # Generate the proof
        proof = merkle_tree.get_proof(index)
        merkle_root = merkle_tree.get_root()

        return proof, merkle_root

    except Exception as e:
        raise RuntimeError(f"Error calculating Merkle proof: {e}")


# Example Usage
if __name__ == "__main__":
    # Sample eligibility data
    eligibility_data = {
        "user1": 100.0,
        "user2": 200.0,
        "user3": 300.0,
        "user4": 400.0
    }

    # Calculate proof for a specific user
    user_to_check = "user3"
    try:
        proof, root = calculate_merkle_proof(eligibility_data, user_to_check)
        print(f"Merkle Proof for {user_to_check}: {proof}")
        print(f"Merkle Root: {root}")
    except RuntimeError as error:
        print(f"Failed to calculate Merkle proof: {error}")
```
