"""
Generated Code Metadata:
========================
Original URL: https://openswe.io
Prompt: Design a blockchain-based platform for buying and selling software engineering services as NFTs, incorporating elements from OpenSwe.
Generated: DETERMINISTIC_e32ae13c2eea6a4d
Batch ID: 20250622_211052
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
from typing import List

# Define a class for the NFT
class NFT:
    def __init__(self, id: str, name: str, description: str, price: float, owner: str):
        """
        Initialize an NFT object.

        Args:
        id (str): Unique identifier for the NFT.
        name (str): Name of the NFT.
        description (str): Description of the NFT.
        price (float): Price of the NFT.
        owner (str): Owner of the NFT.
        """
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.owner = owner

# Define a class for the Blockchain
class Blockchain:
    def __init__(self):
        """
        Initialize a Blockchain object.
        """
        self.chain = []
        self.pending_transactions = []

    def add_transaction(self, transaction: dict):
        """
        Add a transaction to the pending transactions.

        Args:
        transaction (dict): Transaction to add.
        """
        self.pending_transactions.append(transaction)

    def mine_block(self):
        """
        Mine a new block and add it to the chain.
        """
        if not self.pending_transactions:
            return False

        new_block_index = len(self.chain)
        new_block_timestamp = time.time()
        new_block_transactions = self.pending_transactions
        new_block_hash = self.calculate_hash(new_block_index, new_block_timestamp, new_block_transactions)

        new_block = {
            'index': new_block_index,
            'timestamp': new_block_timestamp,
            'transactions': new_block_transactions,
            'hash': new_block_hash,
            'previous_hash': self.calculate_hash(len(self.chain) - 1, self.chain[-1]['timestamp'], self.chain[-1]['transactions']) if self.chain else '0'
        }

        self.chain.append(new_block)
        self.pending_transactions = []
        return new_block

    def calculate_hash(self, index: int, timestamp: float, transactions: List[dict]):
        """
        Calculate the hash for a block.

        Args:
        index (int): Index of the block.
        timestamp (float): Timestamp of the block.
        transactions (List[dict]): Transactions in the block.

        Returns:
        str: Hash of the block.
        """
        data_string = str(index) + str(timestamp) + str(transactions)
        return hashlib.sha256(data_string.encode()).hexdigest()

# Define a class for the OpenSwe platform
class OpenSwe:
    def __init__(self):
        """
        Initialize an OpenSwe platform object.
        """
        self.nfts = {}
        self.blockchain = Blockchain()

    def create_nft(self, id: str, name: str, description: str, price: float, owner: str):
        """
        Create a new NFT.

        Args:
        id (str): Unique identifier for the NFT.
        name (str): Name of the NFT.
        description (str): Description of the NFT.
        price (float): Price of the NFT.
        owner (str): Owner of the NFT.

        Returns:
        NFT: Created NFT object.
        """
        nft = NFT(id, name, description, price, owner)
        self.nfts[id] = nft
        return nft

    def buy_nft(self, id: str, buyer: str):
        """
        Buy an NFT.

        Args:
        id (str): Unique identifier for the NFT.
        buyer (str): Buyer of the NFT.

        Returns:
        bool: Whether the transaction was successful.
        """
        if id not in self.nfts:
            return False

        nft = self.nfts[id]
        if nft.owner == buyer:
            return False

        # Create a transaction
        transaction = {
            'type': 'buy_nft',
            'nft_id': id,
            'buyer': buyer,
            'seller': nft.owner,
            'price': nft.price
        }

        # Add transaction to the blockchain
        self.blockchain.add_transaction(transaction)

        # Mine a new block
        new_block = self.blockchain.mine_block()

        # Update the NFT owner
        nft.owner = buyer

        return True

    def sell_nft(self, id: str, seller: str, price: float):
        """
        Sell an NFT.

        Args:
        id (str): Unique identifier for the NFT.
        seller (str): Seller of the NFT.
        price (float): Price of the NFT.

        Returns:
        bool: Whether the transaction was successful.
        """
        if id not in self.nfts:
            return False

        nft = self.nfts[id]
        if nft.owner != seller:
            return False

        # Create a transaction
        transaction = {
            'type': 'sell_nft',
            'nft_id': id,
            'seller': seller,
            'price': price
        }

        # Add transaction to the blockchain
        self.blockchain.add_transaction(transaction)

        # Mine a new block
        new_block = self.blockchain.mine_block()

        # Update the NFT price
        nft.price = price

        return True

# Example usage
if __name__ == "__main__":
    openswe = OpenSwe()

    # Create NFTs
    nft1 = openswe.create_nft('1', 'NFT 1', 'This is NFT 1', 100.0, 'Alice')
    nft2 = openswe.create_nft('2', 'NFT 2', 'This is NFT 2', 200.0, 'Bob')

    # Buy NFT
    openswe.buy_nft('1', 'Bob')

    # Sell NFT
    openswe.sell_nft('2', 'Bob', 250.0)

    # Print NFTs
    for nft in openswe.nfts.values():
        print(f"NFT {nft.id}: {nft.name}, Price: {nft.price}, Owner: {nft.owner}")

    # Print Blockchain
    for block in openswe.blockchain.chain:
        print(f"Block {block['index']}:")
        print(f"Timestamp: {block['timestamp']}")
        print(f"Transactions: {block['transactions']}")
        print(f"Hash: {block['hash']}")
        print(f"Previous Hash: {block['previous_hash']}")
        print('------------------------')
```
