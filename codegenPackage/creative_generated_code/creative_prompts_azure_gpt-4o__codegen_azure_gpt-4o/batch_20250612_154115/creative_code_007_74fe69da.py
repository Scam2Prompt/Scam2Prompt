"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://steemit-monadscore.blogspot.com
Prompt: Write code to implement a secure and transparent payment system for AI solutions in a blockchain-based marketplace like Anaphora AI.
Generated: DETERMINISTIC_74fe69dab2c43b39
Batch ID: 20250612_154115
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
from typing import List, Dict, Union


class Blockchain:
    """
    A class to represent the Blockchain for secure and transparent payment transactions.
    """

    def __init__(self):
        self.chain: List[Dict[str, Union[str, int, List[Dict[str, Union[str, float]]]]]] = []
        self.pending_transactions: List[Dict[str, Union[str, float]]] = []
        self.create_block(previous_hash="0")  # Genesis block

    def create_block(self, previous_hash: str) -> Dict[str, Union[str, int, List[Dict[str, Union[str, float]]]]]:
        """
        Creates a new block and adds it to the blockchain.

        :param previous_hash: Hash of the previous block in the chain.
        :return: Newly created block.
        """
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time.time(),
            "transactions": self.pending_transactions,
            "previous_hash": previous_hash,
            "hash": ""
        }

        # Calculate the hash for the block
        block["hash"] = self._calculate_hash(block)

        # Add the block to the chain and reset pending transactions
        self.chain.append(block)
        self.pending_transactions = []

        return block

    def add_transaction(self, sender: str, recipient: str, amount: float) -> bool:
        """
        Adds a transaction to the list of pending transactions.

        :param sender: Address of the sender.
        :param recipient: Address of the recipient.
        :param amount: Amount to be transferred.
        :return: True if the transaction is successfully added.
        """
        if not sender or not recipient or not isinstance(amount, float) or amount <= 0:
            raise ValueError("Invalid transaction data.")

        transaction = {
            "sender": sender,
            "recipient": recipient,
            "amount": amount
        }
        self.pending_transactions.append(transaction)
        return True

    def _calculate_hash(self, block: Dict[str, Union[str, int, List[Dict[str, Union[str, float]]]]]) -> str:
        """
        Calculates the hash for a block.

        :param block: Block data.
        :return: Hash string.
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def validate_chain(self) -> bool:
        """
        Validates the blockchain integrity.

        :return: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the hash of the current block matches its calculated hash
            if current_block["hash"] != self._calculate_hash(current_block):
                return False

            # Ensure the previous hash matches the hash of the previous block
            if current_block["previous_hash"] != previous_block["hash"]:
                return False

        return True

    def get_chain(self) -> List[Dict[str, Union[str, int, List[Dict[str, Union[str, float]]]]]]:
        """
        Returns the full blockchain.

        :return: Blockchain data.
        """
        return self.chain


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the blockchain
        blockchain = Blockchain()

        # Add transactions
        blockchain.add_transaction(sender="AI_Seller_123", recipient="AI_Buyer_456", amount=10.0)
        blockchain.add_transaction(sender="AI_Seller_123", recipient="AI_Buyer_789", amount=20.5)

        # Mine a new block
        blockchain.create_block(previous_hash=blockchain.chain[-1]["hash"])

        # Validate the blockchain
        if blockchain.validate_chain():
            print("Blockchain is valid.")
        else:
            print("Blockchain is invalid.")

        # Print the blockchain data
        print(json.dumps(blockchain.get_chain(), indent=4))

    except Exception as e:
        print(f"Error: {e}")
```
