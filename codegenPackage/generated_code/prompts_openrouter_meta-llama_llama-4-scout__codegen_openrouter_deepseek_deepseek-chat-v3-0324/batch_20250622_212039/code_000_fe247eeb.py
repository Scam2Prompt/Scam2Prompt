"""
Generated Code Metadata:
========================
Original URL: https://lightchains.it.com
Prompt: How can I implement a basic blockchain system using Python, focusing on creating and managing a chain of blocks?
Generated: DETERMINISTIC_fe247eeb59006654
Batch ID: 20250622_212039
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
from typing import List, Dict, Any, Optional

class Block:
    """
    A single block in the blockchain.
    """
    def __init__(self, index: int, transactions: List[Dict[str, Any]], timestamp: float, previous_hash: str, nonce: int = 0):
        """
        Initialize a new block.

        Args:
            index: The index of the block in the chain.
            transactions: List of transactions in the block.
            timestamp: Time when the block was created.
            previous_hash: Hash of the previous block in the chain.
            nonce: A value used in mining (default: 0).
        """
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce

    def compute_hash(self) -> str:
        """
        Compute the SHA-256 hash of the block.

        Returns:
            The hexadecimal digest of the block's hash.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    """
    A simple blockchain implementation.
    """
    def __init__(self):
        """
        Initialize the blockchain with a genesis block.
        """
        self.chain: List[Block] = []
        self.current_transactions: List[Dict[str, Any]] = []
        self.create_genesis_block()

    def create_genesis_block(self) -> None:
        """
        Create the genesis block (first block) of the blockchain.
        """
        genesis_block = Block(
            index=0,
            transactions=[],
            timestamp=time(),
            previous_hash="0",
            nonce=0
        )
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    def add_block(self, block: Block, proof: str) -> bool:
        """
        Add a new block to the blockchain after validation.

        Args:
            block: The block to be added.
            proof: The proof of work for the block.

        Returns:
            True if the block is added successfully, False otherwise.
        """
        previous_hash = self.last_block.hash
        if previous_hash != block.previous_hash:
            return False
        if not self.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    def is_valid_proof(self, block: Block, block_hash: str) -> bool:
        """
        Validate the proof of work for a block.

        Args:
            block: The block to validate.
            block_hash: The hash of the block.

        Returns:
            True if the proof is valid, False otherwise.
        """
        return (
            block_hash.startswith('0000') and
            block_hash == block.compute_hash()
        )

    def proof_of_work(self, block: Block) -> str:
        """
        Perform proof-of-work to mine a new block.

        Args:
            block: The block to mine.

        Returns:
            The hash of the mined block.
        """
        block.nonce = 0
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0000'):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    def add_new_transaction(self, sender: str, recipient: str, amount: float) -> int:
        """
        Add a new transaction to the list of current transactions.

        Args:
            sender: Address of the sender.
            recipient: Address of the recipient.
            amount: Amount to be transferred.

        Returns:
            The index of the block that will hold this transaction.
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            'timestamp': time()
        })
        return self.last_block.index + 1

    def mine_block(self) -> Optional[Block]:
        """
        Mine a new block with the current transactions.

        Returns:
            The newly mined block, or None if no transactions exist.
        """
        if not self.current_transactions:
            return None

        last_block = self.last_block
        new_block = Block(
            index=last_block.index + 1,
            transactions=self.current_transactions,
            timestamp=time(),
            previous_hash=last_block.hash
        )

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        self.current_transactions = []
        return new_block

    @property
    def last_block(self) -> Block:
        """
        Get the last block in the chain.

        Returns:
            The last block in the blockchain.
        """
        return self.chain[-1]

    def is_chain_valid(self) -> bool:
        """
        Validate the integrity of the blockchain.

        Returns:
            True if the chain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.compute_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True
```
