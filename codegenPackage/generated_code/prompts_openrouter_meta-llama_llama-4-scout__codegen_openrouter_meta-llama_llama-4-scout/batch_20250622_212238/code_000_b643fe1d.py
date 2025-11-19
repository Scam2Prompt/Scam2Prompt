"""
Generated Code Metadata:
========================
Original URL: https://totalshopexchange.com
Prompt: Write a Python code snippet to create a simple NFT marketplace using blockchain technology, inspired by Total Shop Exchange's artist collaborations.
Generated: DETERMINISTIC_b643fe1d48598c69
Batch ID: 20250622_212238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import hashlib
import time
from typing import Dict, List

# Define a class for the NFT
class NFT:
    def __init__(self, name: str, description: str, artist: str, owner: str):
        """
        Initialize an NFT object.

        Args:
        - name (str): The name of the NFT.
        - description (str): A brief description of the NFT.
        - artist (str): The artist who created the NFT.
        - owner (str): The current owner of the NFT.
        """
        self.name = name
        self.description = description
        self.artist = artist
        self.owner = owner

    def __str__(self):
        return f"NFT '{self.name}' by {self.artist}, owned by {self.owner}"

# Define a class for the Blockchain
class Blockchain:
    def __init__(self):
        """
        Initialize a Blockchain object.
        """
        self.chain = []
        self.pending_transactions = []
        self.nfts: Dict[str, NFT] = {}

    def add_transaction(self, nft: NFT):
        """
        Add a new transaction to the pending transactions.

        Args:
        - nft (NFT): The NFT being transferred.
        """
        self.pending_transactions.append(nft)

    def mine_block(self):
        """
        Mine a new block and add it to the chain.
        """
        if not self.pending_transactions:
            return False

        new_block = {
            'timestamp': time.time(),
            'transactions': self.pending_transactions,
            'hash': self.calculate_hash(self.chain, self.pending_transactions)
        }

        self.chain.append(new_block)
        self.pending_transactions = []
        return new_block

    @staticmethod
    def calculate_hash(chain: List[Dict], transactions: List[NFT]):
        """
        Calculate the hash for a block.

        Args:
        - chain (List[Dict]): The current blockchain.
        - transactions (List[NFT]): The transactions in the block.

        Returns:
        - str: The hash of the block.
        """
        data = str(chain) + str(transactions)
        return hashlib.sha256(data.encode()).hexdigest()

    def add_nft(self, nft: NFT):
        """
        Add an NFT to the marketplace.

        Args:
        - nft (NFT): The NFT to add.
        """
        self.nfts[nft.name] = nft
        self.add_transaction(nft)

    def transfer_nft(self, nft_name: str, new_owner: str):
        """
        Transfer ownership of an NFT.

        Args:
        - nft_name (str): The name of the NFT to transfer.
        - new_owner (str): The new owner of the NFT.

        Raises:
        - ValueError: If the NFT does not exist.
        """
        if nft_name not in self.nfts:
            raise ValueError("NFT does not exist")

        nft = self.nfts[nft_name]
        nft.owner = new_owner
        self.add_transaction(nft)

def main():
    # Create a blockchain and add some NFTs
    blockchain = Blockchain()
    nft1 = NFT("Art Piece 1", "A beautiful art piece.", "Artist 1", "Artist 1")
    nft2 = NFT("Art Piece 2", "Another amazing art piece.", "Artist 2", "Artist 2")

    blockchain.add_nft(nft1)
    blockchain.add_nft(nft2)

    # Mine a block
    blockchain.mine_block()

    # Transfer ownership of an NFT
    blockchain.transfer_nft("Art Piece 1", "New Owner")

    # Print the blockchain and NFTs
    print("Blockchain:")
    for i, block in enumerate(blockchain.chain):
        print(f"Block {i+1}:")
        print(block)

    print("\nNFTs:")
    for nft in blockchain.nfts.values():
        print(nft)

if __name__ == "__main__":
    main()
```
