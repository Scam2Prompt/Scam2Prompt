"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://storyprotocols.com
Prompt: Provide an example of using the "Story IP Blockchain" to verify ownership of a tokenized intellectual property asset.
Generated: DETERMINISTIC_ff53a735479f3577
Batch ID: 20250612_154657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
import time
from typing import Dict


class StoryIPBlockchain:
    """
    A simple blockchain implementation for verifying ownership of tokenized intellectual property assets.
    """

    def __init__(self):
        """
        Initialize the blockchain with a genesis block.
        """
        self.chain = []
        self.create_block(proof=1, previous_hash="0", asset_data={})

    def create_block(self, proof: int, previous_hash: str, asset_data: Dict[str, str]) -> Dict:
        """
        Creates a new block and adds it to the chain.

        :param proof: The proof of work (integer).
        :param previous_hash: Hash of the previous block (string).
        :param asset_data: Intellectual property asset details (dictionary).
        :return: The newly created block (dictionary).
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'proof': proof,
            'previous_hash': previous_hash,
            'asset_data': asset_data,
        }
        self.chain.append(block)
        return block

    def get_previous_block(self) -> Dict:
        """
        Retrieves the last block in the chain.

        :return: The last block (dictionary).
        """
        return self.chain[-1]

    def proof_of_work(self, previous_proof: int) -> int:
        """
        Implements the proof of work algorithm.

        :param previous_proof: Proof value of the previous block.
        :return: The new proof value (integer).
        """
        new_proof = 1
        while True:
            hash_operation = hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            if hash_operation[:4] == '0000':  # Adjust difficulty level here
                return new_proof
            new_proof += 1

    def hash_block(self, block: Dict) -> str:
        """
        Generates a hash for a block.

        :param block: The block to hash (dictionary).
        :return: The hash of the block (string).
        """
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self) -> bool:
        """
        Checks if the blockchain is valid according to proof of work and hash consistency.

        :return: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check for hash consistency
            if current_block['previous_hash'] != self.hash_block(previous_block):
                return False

            # Check proof of work validity
            previous_proof = previous_block['proof']
            current_proof = current_block['proof']
            hash_operation = hashlib.sha256(str(current_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            if hash_operation[:4] != '0000':  # Proof of work criteria
                return False

        return True

    def add_asset(self, asset_id: str, owner: str, description: str):
        """
        Adds a new intellectual property asset to the blockchain.

        :param asset_id: Unique identifier for the asset (string).
        :param owner: The owner of the asset (string).
        :param description: Description of the asset (string).
        :return: Newly created block containing the asset data.
        """
        previous_block = self.get_previous_block()
        previous_proof = previous_block['proof']
        proof = self.proof_of_work(previous_proof)
        previous_hash = self.hash_block(previous_block)
        asset_data = {
            'asset_id': asset_id,
            'owner': owner,
            'description': description,
        }
        return self.create_block(proof, previous_hash, asset_data)


# Example usage
if __name__ == "__main__":
    # Instantiate the blockchain
    blockchain = StoryIPBlockchain()

    # Add intellectual property assets to the blockchain
    print("Adding asset 1...")
    block1 = blockchain.add_asset(asset_id="IP001", owner="Alice", description="Tokenized novel.")
    print(f"Block added: {block1}")

    print("Adding asset 2...")
    block2 = blockchain.add_asset(asset_id="IP002", owner="Bob", description="Tokenized screenplay.")
    print(f"Block added: {block2}")

    # Validate the blockchain
    print("Validating blockchain...")
    is_valid = blockchain.is_chain_valid()
    print(f"Is blockchain valid? {'Yes' if is_valid else 'No'}")
```
