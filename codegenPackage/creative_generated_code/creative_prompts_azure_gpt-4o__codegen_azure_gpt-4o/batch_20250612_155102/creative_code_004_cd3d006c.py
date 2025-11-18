"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grokxcoinai.com
Prompt: Develop a blockchain-based system to allocate tokens at preferential pricing for verified participants, referencing $GROK's exclusive presale process.
Generated: DETERMINISTIC_cd3d006c28e09e51
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import hashlib
import json
from datetime import datetime


class Blockchain:
    """
    A simple blockchain implementation to handle allocation of tokens at 
    preferential pricing for verified participants.
    """

    def __init__(self):
        """
        Initialize the blockchain with a genesis block and an empty list of participants.
        """
        self.chain = []  # The blockchain
        self.pending_transactions = []  # Transactions waiting to be added
        self.participants = {}  # Verified participants with their allocation
        self.create_block(proof=1, previous_hash='0')  # Genesis block

    def create_block(self, proof, previous_hash):
        """
        Create a new block in the blockchain.

        Args:
            proof (int): The proof of work value.
            previous_hash (str): Hash of the previous block.

        Returns:
            dict: Newly created block.
        """
        block = {
            'index': len(self.chain) + 1,  # Block index
            'timestamp': str(datetime.now()),  # Timestamp for the block
            'transactions': self.pending_transactions,  # Transactions in this block
            'proof': proof,  # Proof of work
            'previous_hash': previous_hash  # Hash of the previous block
        }
        self.pending_transactions = []  # Reset the pending transactions after block creation
        self.chain.append(block)  # Add block to the chain
        return block

    def get_previous_block(self):
        """
        Get the last block in the blockchain.

        Returns:
            dict: Last block in the chain.
        """
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        """
        Perform proof of work to validate the block.

        Args:
            previous_proof (int): Proof of the previous block.

        Returns:
            int: The new proof value.
        """
        new_proof = 1
        check_proof = False
        while not check_proof:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == "0000":  # Simple proof of work condition
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        """
        Generate a hash for a given block.

        Args:
            block (dict): Block data.

        Returns:
            str: Hash of the block.
        """
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self):
        """
        Validate the blockchain.

        Returns:
            bool: True if the blockchain is valid, False otherwise.
        """
        previous_block = self.chain[0]
        block_index = 1
        while block_index < len(self.chain):
            block = self.chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):  # Check hash linkage
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != "0000":  # Check proof of work validity
                return False
            previous_block = block
            block_index += 1
        return True

    def add_transaction(self, participant_id, token_amount):
        """
        Add a transaction to the list of pending transactions.

        Args:
            participant_id (str): ID of the verified participant.
            token_amount (int): Amount of tokens to allocate.

        Returns:
            int: Index of the block where the transaction will be stored.
        """
        if participant_id not in self.participants:
            raise ValueError("Participant not verified.")
        self.pending_transactions.append({
            'participant_id': participant_id,
            'token_amount': token_amount,
            'preferential_pricing': True  # Mark as preferential pricing
        })
        return self.get_previous_block()['index'] + 1

    def verify_participant(self, participant_id):
        """
        Verify a participant for preferential token allocation.

        Args:
            participant_id (str): ID of the participant.

        Returns:
            bool: True if the participant is successfully verified.
        """
        if participant_id in self.participants:
            raise ValueError("Participant already verified.")
        self.participants[participant_id] = {'verified': True}
        return True


# Example Usage
if __name__ == "__main__":
    # Initialize the blockchain
    blockchain = Blockchain()

    # Verify participants
    try:
        blockchain.verify_participant("user123")
    except ValueError as e:
        print(f"Error: {e}")

    # Add transactions for verified participants
    try:
        blockchain.add_transaction("user123", 100)
    except ValueError as e:
        print(f"Error: {e}")

    # Perform mining (add a new block)
    previous_proof = blockchain.get_previous_block()['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(blockchain.get_previous_block())
    blockchain.create_block(proof, previous_hash)

    # Output the blockchain
    print(json.dumps(blockchain.chain, indent=4))
```

This code implements a simplified blockchain for allocating tokens at preferential pricing for verified participants, following best practices for Python coding.
