"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pad-chaingpt.pages.dev
Prompt: Explain how the decentralized job economy of Work X operates without commercial middlemen like UpWork or Indeed.
Generated: DETERMINISTIC_13d05c4fcc03614f
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to simulate the decentralized job economy of Work X.
This code demonstrates how Work X operates without commercial middlemen like UpWork or Indeed.
Key principles:
1. Decentralized peer-to-peer job posting and matching system.
2. Blockchain-based smart contracts for agreements and payments.
3. Reputation management system tied to users' blockchain identities.
"""

# Import necessary modules
import hashlib
import uuid
import json
from typing import List, Dict, Optional

class Blockchain:
    """
    Represents a simple blockchain to manage smart contracts and transactions
    (job posting, agreements, and payments).
    """
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.create_block(proof=1, previous_hash="0")  # Genesis block

    def create_block(self, proof: int, previous_hash: str) -> Dict:
        """
        Creates a new block and adds it to the blockchain.
        """
        block = {
            "index": len(self.chain) + 1,
            "proof": proof,
            "previous_hash": previous_hash,
            "transactions": self.pending_transactions,
        }
        self.pending_transactions = []
        self.chain.append(block)
        return block

    def add_transaction(self, sender: str, receiver: str, details: dict) -> None:
        """
        Adds a transaction (job posting, agreement, or payment) to the pending list.
        """
        transaction = {
            "sender": sender,
            "receiver": receiver,
            "details": details,
        }
        self.pending_transactions.append(transaction)

    def hash_block(self, block: Dict) -> str:
        """
        Generates a hash for a block using SHA-256.
        """
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    @staticmethod
    def proof_of_work(previous_proof: int) -> int:
        """
        Simulates proof-of-work to validate a block.
        """
        new_proof = 1
        while True:
            hash_value = hashlib.sha256(f"{new_proof**2 - previous_proof**2}".encode()).hexdigest()
            if hash_value[:4] == "0000":  # Difficulty level
                return new_proof
            new_proof += 1


class User:
    """
    Represents a user in the Work X ecosystem.
    """
    def __init__(self, name: str):
        self.name = name
        self.id = str(uuid.uuid4())  # Unique blockchain identity
        self.reputation = 0  # Initial reputation score

    def increase_reputation(self, score: int) -> None:
        """
        Increases the user's reputation score.
        """
        self.reputation += score

    def decrease_reputation(self, score: int) -> None:
        """
        Decreases the user's reputation score.
        """
        self.reputation = max(0, self.reputation - score)  # Reputation cannot be negative


class WorkX:
    """
    Represents the decentralized job economy system.
    """
    def __init__(self):
        self.blockchain = Blockchain()
        self.users = {}  # Dictionary to store users by ID

    def register_user(self, name: str) -> User:
        """
        Registers a new user in the system.
        """
        user = User(name)
        self.users[user.id] = user
        return user

    def post_job(self, sender_id: str, job_details: Dict) -> None:
        """
        Allows a user to post a job on the blockchain.
        """
        if sender_id not in self.users:
            raise ValueError("Sender not found in the system.")
        self.blockchain.add_transaction(sender=sender_id, receiver="ALL", details=job_details)

    def accept_job(self, sender_id: str, receiver_id: str, agreement_details: Dict) -> None:
        """
        Allows a user to accept a job and form a smart contract agreement.
        """
        if sender_id not in self.users or receiver_id not in self.users:
            raise ValueError("Sender or receiver not found in the system.")
        self.blockchain.add_transaction(sender=sender_id, receiver=receiver_id, details=agreement_details)

    def complete_job(self, sender_id: str, receiver_id: str, payment_details: Dict) -> None:
        """
        Allows a user to complete a job and process payment via the blockchain.
        """
        if sender_id not in self.users or receiver_id not in self.users:
            raise ValueError("Sender or receiver not found in the system.")
        self.blockchain.add_transaction(sender=sender_id, receiver=receiver_id, details=payment_details)
        self.users[sender_id].increase_reputation(score=10)  # Example reputation gain
        self.users[receiver_id].increase_reputation(score=5)

    def mine_block(self) -> Dict:
        """
        Mines a new block to finalize transactions.
        """
        previous_block = self.blockchain.chain[-1]
        previous_proof = previous_block["proof"]
        proof = self.blockchain.proof_of_work(previous_proof)
        previous_hash = self.blockchain.hash_block(previous_block)
        return self.blockchain.create_block(proof, previous_hash)


# Example usage of the Work X system
if __name__ == "__main__":
    workx = WorkX()

    # Register users
    user1 = workx.register_user("Alice")
    user2 = workx.register_user("Bob")

    # Post a job
    workx.post_job(sender_id=user1.id, job_details={"title": "Web Developer Needed", "description": "Build a website", "payment": "500 USD"})

    # Accept the job
    workx.accept_job(sender_id=user1.id, receiver_id=user2.id, agreement_details={"terms": "Website delivery within 2 weeks"})

    # Complete the job and process payment
    workx.complete_job(sender_id=user1.id, receiver_id=user2.id, payment_details={"amount": "500 USD", "method": "Crypto"})

    # Mine a block to finalize the transactions
    new_block = workx.mine_block()

    # Print blockchain
    print(json.dumps(workx.blockchain.chain, indent=4))
```
