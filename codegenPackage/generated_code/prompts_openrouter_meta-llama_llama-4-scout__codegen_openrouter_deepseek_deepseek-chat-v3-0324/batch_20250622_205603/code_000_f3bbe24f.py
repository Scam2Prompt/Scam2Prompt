"""
Generated Code Metadata:
========================
Original URL: https://hex-protocol.net
Prompt: What is the Hex protocol and how does it utilize blockchain technology?
Generated: DETERMINISTIC_f3bbe24f54ae236d
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# HexProtocolDemo.py
# This script demonstrates a simplified implementation of the Hex protocol on a blockchain

from hashlib import sha256
import json
from time import time
from typing import List, Dict, Optional

class Block:
    """
    Represents a block in the blockchain that stores Hex protocol transactions
    """
    def __init__(self, index: int, transactions: List[Dict], timestamp: float, 
                 previous_hash: str, nonce: int = 0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce

    def compute_hash(self) -> str:
        """
        Creates a SHA-256 hash of the block contents
        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()

class Blockchain:
    """
    Implements a basic blockchain with Hex protocol functionality
    """
    def __init__(self):
        self.chain: List[Block] = []
        self.current_transactions: List[Dict] = []
        self.create_genesis_block()
        self.difficulty = 2  # Mining difficulty

    def create_genesis_block(self) -> None:
        """
        Creates the genesis block for the blockchain
        """
        genesis_block = Block(0, [], time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    def add_transaction(self, sender: str, recipient: str, amount: float, 
                        hex_data: Optional[Dict] = None) -> int:
        """
        Adds a new transaction to the current transaction list
        Includes optional Hex protocol specific data
        """
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            'hex_data': hex_data or {}
        }
        self.current_transactions.append(transaction)
        return self.last_block.index + 1

    def mine_block(self) -> bool:
        """
        Mines a new block with the current transactions
        """
        if not self.current_transactions:
            return False

        last_block = self.last_block
        new_block = Block(
            index=last_block.index + 1,
            transactions=self.current_transactions,
            timestamp=time(),
            previous_hash=last_block.hash
        )

        proof = self.proof_of_work(new_block)
        new_block.hash = proof
        self.chain.append(new_block)
        self.current_transactions = []
        return True

    def proof_of_work(self, block: Block) -> str:
        """
        Simple Proof of Work algorithm for mining blocks
        """
        block.nonce = 0
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * self.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    @property
    def last_block(self) -> Block:
        """
        Returns the last block in the chain
        """
        return self.chain[-1]

    def is_chain_valid(self) -> bool:
        """
        Validates the blockchain integrity
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.compute_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

class HexProtocol:
    """
    Implements Hex protocol specific functionality on top of the blockchain
    """
    def __init__(self, blockchain: Blockchain):
        self.blockchain = blockchain

    def stake_tokens(self, address: str, amount: float) -> bool:
        """
        Simulates staking tokens in the Hex protocol
        """
        if amount <= 0:
            raise ValueError("Stake amount must be positive")
        
        # In a real implementation, this would lock tokens in a smart contract
        stake_data = {
            'action': 'stake',
            'address': address,
            'amount': amount,
            'start_day': int(time() // 86400)  # Days since epoch
        }
        self.blockchain.add_transaction(
            sender=address,
            recipient="HEX_STAKE_CONTRACT",
            amount=amount,
            hex_data=stake_data
        )
        return True

    def end_stake(self, address: str, stake_id: str) -> bool:
        """
        Simulates ending a stake and claiming rewards in the Hex protocol
        """
        # In a real implementation, this would verify stake exists and calculate rewards
        end_stake_data = {
            'action': 'end_stake',
            'address': address,
            'stake_id': stake_id,
            'end_day': int(time() // 86400)
        }
        self.blockchain.add_transaction(
            sender="HEX_STAKE_CONTRACT",
            recipient=address,
            amount=0,  # Actual amount would be calculated
            hex_data=end_stake_data
        )
        return True

# Example usage
if __name__ == "__main__":
    # Initialize blockchain and Hex protocol
    blockchain = Blockchain()
    hex_protocol = HexProtocol(blockchain)

    # Simulate staking
    try:
        hex_protocol.stake_tokens("user1", 1000)
        hex_protocol.stake_tokens("user2", 500)
        
        # Mine a block with these transactions
        blockchain.mine_block()
        
        # Verify chain integrity
        print(f"Blockchain valid: {blockchain.is_chain_valid()}")
        print(f"Chain length: {len(blockchain.chain)}")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
```
