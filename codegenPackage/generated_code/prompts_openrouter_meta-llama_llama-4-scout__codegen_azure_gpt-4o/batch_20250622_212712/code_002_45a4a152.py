"""
Generated Code Metadata:
========================
Original URL: https://asfcsc.pages.dev
Prompt: Design a blockchain-based system to gamify the healthcare ecosystem, enabling patients to securely own and manage their health data, inspired by BitDoctor's DeSci approach.
Generated: DETERMINISTIC_45a4a1528ce1a9f6
Batch ID: 20250622_212712
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
import time
from typing import List, Dict, Any


class Blockchain:
    """
    A simple blockchain implementation to securely store and manage health data.
    """

    def __init__(self):
        self.chain: List[Dict[str, Any]] = []  # The blockchain (list of blocks)
        self.pending_transactions: List[Dict[str, Any]] = []  # Transactions waiting to be added to a block
        self.create_block(previous_hash="0")  # Create the genesis block

    def create_block(self, previous_hash: str) -> Dict[str, Any]:
        """
        Create a new block and add it to the blockchain.
        :param previous_hash: Hash of the previous block in the chain.
        :return: The newly created block.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.pending_transactions,
            'previous_hash': previous_hash,
            'hash': None
        }
        block['hash'] = self.hash_block(block)  # Calculate the hash of the block
        self.chain.append(block)  # Add the block to the chain
        self.pending_transactions = []  # Reset the list of pending transactions
        return block

    @staticmethod
    def hash_block(block: Dict[str, Any]) -> str:
        """
        Generate a SHA-256 hash of a block.
        :param block: The block to hash.
        :return: The hash of the block.
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def add_transaction(self, patient_id: str, data: Dict[str, Any]) -> None:
        """
        Add a new transaction to the list of pending transactions.
        :param patient_id: The ID of the patient.
        :param data: The health data to be added.
        """
        transaction = {
            'patient_id': patient_id,
            'data': data,
            'timestamp': time.time()
        }
        self.pending_transactions.append(transaction)

    def get_last_block(self) -> Dict[str, Any]:
        """
        Retrieve the last block in the blockchain.
        :return: The last block.
        """
        return self.chain[-1]

    def is_chain_valid(self) -> bool:
        """
        Validate the integrity of the blockchain.
        :return: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the hash of the block is correct
            if current_block['hash'] != self.hash_block(current_block):
                return False

            # Check if the previous hash matches
            if current_block['previous_hash'] != previous_block['hash']:
                return False

        return True


class HealthcareGamification:
    """
    A system to gamify the healthcare ecosystem using blockchain.
    """

    def __init__(self):
        self.blockchain = Blockchain()
        self.rewards: Dict[str, int] = {}  # Patient rewards ledger

    def add_health_data(self, patient_id: str, data: Dict[str, Any]) -> None:
        """
        Add health data for a patient and reward them.
        :param patient_id: The ID of the patient.
        :param data: The health data to be added.
        """
        self.blockchain.add_transaction(patient_id, data)
        self.reward_patient(patient_id)

    def reward_patient(self, patient_id: str) -> None:
        """
        Reward a patient for contributing health data.
        :param patient_id: The ID of the patient.
        """
        if patient_id not in self.rewards:
            self.rewards[patient_id] = 0
        self.rewards[patient_id] += 10  # Reward 10 points for each contribution

    def mine_block(self) -> Dict[str, Any]:
        """
        Mine a new block to add pending transactions to the blockchain.
        :return: The newly mined block.
        """
        last_block = self.blockchain.get_last_block()
        return self.blockchain.create_block(previous_hash=last_block['hash'])

    def get_patient_rewards(self, patient_id: str) -> int:
        """
        Retrieve the reward points for a specific patient.
        :param patient_id: The ID of the patient.
        :return: The reward points of the patient.
        """
        return self.rewards.get(patient_id, 0)


# Example usage
if __name__ == "__main__":
    system = HealthcareGamification()

    # Add health data for patients
    system.add_health_data("patient_1", {"blood_pressure": "120/80", "heart_rate": 72})
    system.add_health_data("patient_2", {"blood_pressure": "130/85", "heart_rate": 75})

    # Mine a block
    mined_block = system.mine_block()
    print("Mined Block:", mined_block)

    # Check rewards
    print("Patient 1 Rewards:", system.get_patient_rewards("patient_1"))
    print("Patient 2 Rewards:", system.get_patient_rewards("patient_2"))

    # Validate the blockchain
    print("Is Blockchain Valid?", system.blockchain.is_chain_valid())
```
