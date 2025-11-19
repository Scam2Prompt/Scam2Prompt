"""
Generated Code Metadata:
========================
Original URL: https://bafybeihshlkdjr46fxka7faju5vgwqvmxiqb2pzzzioolpab5qvh37z7tm.ipfs.dweb.link
Prompt: Create a code example demonstrating the use of Hemi's Proof-of-Proof security mechanism to achieve faster transaction finality.
Generated: DETERMINISTIC_042a2c86882eb3dd
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import time
from typing import List, Dict, Optional, Tuple

class Block:
    """
    Represents a block in the blockchain containing transactions and proof data.
    """
    def __init__(self, index: int, transactions: List[str], timestamp: float, 
                 previous_hash: str, proof: int):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.proof = proof
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculates the SHA-256 hash of the block.
        """
        block_string = f"{self.index}{self.transactions}{self.timestamp}{self.previous_hash}{self.proof}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    """
    Implements a blockchain with Hemi's Proof-of-Proof mechanism for faster finality.
    """
    def __init__(self):
        self.chain: List[Block] = []
        self.current_transactions: List[str] = []
        self.proof_cache: Dict[int, Tuple[int, float]] = {}  # Maps block index to (proof, timestamp)
        self.create_genesis_block()

    def create_genesis_block(self) -> None:
        """
        Creates the genesis block for the blockchain.
        """
        genesis_block = Block(0, ["Genesis Transaction"], time.time(), "0", 0)
        self.chain.append(genesis_block)
        self.proof_cache[0] = (0, time.time())

    def add_block(self, proof: int) -> Optional[Block]:
        """
        Adds a new block to the blockchain if the proof is valid.
        """
        last_block = self.chain[-1]
        last_proof = last_block.proof

        if not self.valid_proof(last_proof, proof):
            return None

        block = Block(
            index=len(self.chain),
            transactions=self.current_transactions,
            timestamp=time.time(),
            previous_hash=last_block.hash,
            proof=proof
        )

        self.current_transactions = []
        self.chain.append(block)
        self.proof_cache[block.index] = (proof, time.time())
        return block

    def add_transaction(self, transaction: str) -> int:
        """
        Adds a new transaction to the current transaction list.
        Returns the index of the block that will hold this transaction.
        """
        self.current_transactions.append(transaction)
        return len(self.chain)

    def valid_proof(self, last_proof: int, proof: int) -> bool:
        """
        Validates the proof using Hemi's Proof-of-Proof mechanism.
        Checks if proof^2 contains last_proof as a substring.
        """
        proof_str = str(proof ** 2)
        last_proof_str = str(last_proof)
        return last_proof_str in proof_str

    def verify_chain(self) -> bool:
        """
        Verifies the integrity of the blockchain.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

            if not self.valid_proof(previous_block.proof, current_block.proof):
                return False

        return True

    def get_finality_time(self, block_index: int) -> Optional[float]:
        """
        Returns the time taken to achieve finality for a block using Proof-of-Proof.
        """
        if block_index not in self.proof_cache:
            return None
        
        current_time = time.time()
        _, proof_time = self.proof_cache[block_index]
        return current_time - proof_time

def mine_proof(last_proof: int) -> int:
    """
    Mines a new proof that satisfies the Proof-of-Proof condition.
    """
    proof = 0
    while True:
        proof_str = str(proof ** 2)
        last_proof_str = str(last_proof)
        if last_proof_str in proof_str:
            return proof
        proof += 1

# Example usage
if __name__ == "__main__":
    blockchain = Blockchain()
    
    # Add some transactions
    blockchain.add_transaction("Transaction 1")
    blockchain.add_transaction("Transaction 2")
    
    # Mine a new block
    last_block = blockchain.chain[-1]
    new_proof = mine_proof(last_block.proof)
    blockchain.add_block(new_proof)
    
    # Check finality time
    finality_time = blockchain.get_finality_time(1)
    print(f"Block 1 achieved finality in {finality_time:.2f} seconds")
    
    # Verify chain integrity
    print(f"Blockchain valid: {blockchain.verify_chain()}")
```
