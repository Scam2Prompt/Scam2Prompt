"""
Generated Code Metadata:
========================
Original URL: https://ahsjdkkk.pages.dev
Prompt: Write code for a blockchain-based consultation service platform that allows users to book personalized sessions with experts, inspired by the consultation services offered by the Chain Solution Center.
Generated: DETERMINISTIC_69c64a0ae68c80fa
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blockchain_consultation_service.py

import hashlib
import time
from typing import Dict, List

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: Dict, nonce: int = 0):
        """
        Initialize a new block.

        Args:
        - index (int): The index of the block in the blockchain.
        - previous_hash (str): The hash of the previous block.
        - timestamp (float): The timestamp of the block.
        - data (Dict): The data stored in the block.
        - nonce (int): The nonce for proof-of-work. Defaults to 0.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the hash of the block.

        Returns:
        - str: The hash of the block.
        """
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data) + str(self.nonce)
        return hashlib.sha256(data_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        """
        Initialize a new blockchain.
        """
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2
        self.pending_data = []

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        Returns:
        - Block: The genesis block.
        """
        return Block(0, "0", time.time(), {"genesis": "block"})

    def get_latest_block(self) -> Block:
        """
        Get the latest block in the blockchain.

        Returns:
        - Block: The latest block.
        """
        return self.chain[-1]

    def add_block(self, new_block: Block):
        """
        Add a new block to the blockchain.

        Args:
        - new_block (Block): The new block to add.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def mine_block(self, miner: str):
        """
        Mine a new block.

        Args:
        - miner (str): The miner of the block.

        Returns:
        - Block: The mined block.
        """
        if not self.pending_data:
            return None

        new_block = Block(self.get_latest_block().index + 1, self.get_latest_block().hash, time.time(), self.pending_data)
        self.pending_data = []

        while new_block.hash[: self.difficulty] != "0" * self.difficulty:
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()

        new_block.data["miner"] = miner
        self.add_block(new_block)

        return new_block

    def add_consultation_request(self, user: str, expert: str, topic: str):
        """
        Add a consultation request.

        Args:
        - user (str): The user requesting consultation.
        - expert (str): The expert to consult.
        - topic (str): The topic of consultation.
        """
        self.pending_data.append({"user": user, "expert": expert, "topic": topic})


class ConsultationService:
    def __init__(self):
        """
        Initialize a new consultation service.
        """
        self.blockchain = Blockchain()
        self.experts: Dict[str, List[str]] = {}

    def add_expert(self, expert: str, topics: List[str]):
        """
        Add an expert.

        Args:
        - expert (str): The expert to add.
        - topics (List[str]): The topics the expert can consult on.
        """
        self.experts[expert] = topics

    def book_session(self, user: str, expert: str, topic: str):
        """
        Book a consultation session.

        Args:
        - user (str): The user booking the session.
        - expert (str): The expert to consult.
        - topic (str): The topic of consultation.

        Returns:
        - bool: Whether the session was booked successfully.
        """
        if expert not in self.experts or topic not in self.experts[expert]:
            return False

        self.blockchain.add_consultation_request(user, expert, topic)
        return True

    def mine_session(self, miner: str):
        """
        Mine a new session.

        Args:
        - miner (str): The miner of the session.

        Returns:
        - Block: The mined session.
        """
        return self.blockchain.mine_block(miner)


def main():
    consultation_service = ConsultationService()

    consultation_service.add_expert("John Doe", ["Blockchain", "AI"])
    consultation_service.add_expert("Jane Doe", ["Cybersecurity", "Data Science"])

    consultation_service.book_session("User1", "John Doe", "Blockchain")
    consultation_service.book_session("User2", "Jane Doe", "Cybersecurity")

    mined_session = consultation_service.mine_session("Miner1")

    print("Mined Session:")
    print(mined_session.data)


if __name__ == "__main__":
    main()
```
