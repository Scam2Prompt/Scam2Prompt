"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://j-node.net
Prompt: Write code to simulate validator node interactions on a blockchain testnet, referencing J•Node's focus on community trust.
Generated: DETERMINISTIC_201f7a1c27b637c6
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class ValidatorNode:
    def __init__(self, node_id, trust_score=0):
        """
        Initializes a ValidatorNode with a unique ID and a trust score.

        :param node_id: Unique identifier for the validator node
        :param trust_score: Initial trust score for the node (default is 0)
        """
        self.node_id = node_id
        self.trust_score = trust_score
        self.blockchain = []
    
    def validate_transaction(self, transaction):
        """
        Validates a given transaction based on the trust score.

        :param transaction: The transaction to validate
        :return: Boolean indicating whether the transaction is valid
        """
        if self.trust_score >= 5:
            print(f"Validator {self.node_id} validated transaction: {transaction}")
            return True
        else:
            print(f"Validator {self.node_id} rejected transaction: {transaction}")
            return False

    def propose_block(self, transactions):
        """
        Proposes a new block containing validated transactions.

        :param transactions: List of transactions to include in the block
        :return: The new block or None if it is not valid
        """
        if all(self.validate_transaction(tx) for tx in transactions):
            new_block = {
                "block_id": len(self.blockchain) + 1,
                "transactions": transactions,
                "validator": self.node_id,
                "timestamp": time.time()
            }
            self.blockchain.append(new_block)
            print(f"Validator {self.node_id} proposed a new block: {new_block}")
            return new_block
        else:
            print(f"Validator {self.node_id} could not propose a block due to invalid transactions.")
            return None

    def update_trust_score(self, score_change):
        """
        Updates the trust score of the validator node.

        :param score_change: The amount to change the trust score (can be positive or negative)
        """
        self.trust_score = max(0, self.trust_score + score_change)  # Ensure score doesn't go negative
        print(f"Validator {self.node_id} trust score updated to: {self.trust_score}")

def simulate_validator_interactions():
    """
    Simulates interactions among multiple validator nodes on a blockchain testnet.
    """
    # Creating a list of validator nodes
    validators = [ValidatorNode(node_id=f"Validator-{i}") for i in range(5)]
    
    # Simulating transactions and proposings blocks
    for _ in range(10):
        transactions = [f"Transaction-{random.randint(1, 100)}" for _ in range(random.randint(1, 5))]
        for validator in validators:
            if random.random() < 0.7:  # 70% chance to update trust score
                score_change = random.choice([-1, 1])  # Randomly increase or decrease score
                validator.update_trust_score(score_change)
            validator.propose_block(transactions)
        time.sleep(1)  # Sleep for a second to simulate time passing

if __name__ == "__main__":
    try:
        simulate_validator_interactions()
    except Exception as e:
        print(f"An error occurred during simulation: {e}")
```
