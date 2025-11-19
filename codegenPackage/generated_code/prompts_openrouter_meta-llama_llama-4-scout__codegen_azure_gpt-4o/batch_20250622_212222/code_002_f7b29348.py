"""
Generated Code Metadata:
========================
Original URL: https://lightchain-dapp.web.app
Prompt: "Design a high-level architecture for a decentralized AI system using blockchain and AI technologies, incorporating elements of Lightchain AI's PoI consensus and AIVM."
Generated: DETERMINISTIC_f7b29348e0081648
Batch ID: 20250622_212222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Decentralized AI System Architecture using Blockchain and AI Technologies
This code provides a high-level implementation of a decentralized AI system that incorporates:
1. Proof of Intelligence (PoI) consensus mechanism inspired by Lightchain AI.
2. AI Virtual Machine (AIVM) for executing AI models and tasks on-chain.

Note: This is a conceptual implementation and may require further refinement for production use.
"""

import hashlib
import json
import time
from typing import List, Dict, Any

# Blockchain Node Class
class BlockchainNode:
    """
    Represents a node in the decentralized AI system.
    Each node can participate in the PoI consensus and execute AI tasks using AIVM.
    """
    def __init__(self, node_id: str):
        self.node_id = node_id
        self.chain = []  # Blockchain ledger
        self.pending_tasks = []  # AI tasks waiting to be processed
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Creates the genesis block for the blockchain.
        """
        genesis_block = {
            'index': 0,
            'timestamp': time.time(),
            'previous_hash': '0',
            'tasks': [],
            'proof': 0
        }
        genesis_block['hash'] = self.hash_block(genesis_block)
        self.chain.append(genesis_block)

    @staticmethod
    def hash_block(block: Dict[str, Any]) -> str:
        """
        Generates a SHA-256 hash for a given block.
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def add_task(self, task: Dict[str, Any]):
        """
        Adds an AI task to the pending tasks queue.
        """
        self.pending_tasks.append(task)

    def proof_of_intelligence(self, previous_proof: int) -> int:
        """
        Proof of Intelligence (PoI) consensus mechanism.
        Nodes must solve an AI-related computational challenge to validate the block.
        """
        proof = 0
        while not self.validate_proof(previous_proof, proof):
            proof += 1
        return proof

    @staticmethod
    def validate_proof(previous_proof: int, proof: int) -> bool:
        """
        Validates the PoI proof by checking if the hash meets the difficulty criteria.
        """
        guess = f'{previous_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"  # Example difficulty: hash must start with '0000'

    def create_block(self, proof: int) -> Dict[str, Any]:
        """
        Creates a new block and adds it to the blockchain.
        """
        previous_block = self.chain[-1]
        block = {
            'index': len(self.chain),
            'timestamp': time.time(),
            'previous_hash': previous_block['hash'],
            'tasks': self.pending_tasks,
            'proof': proof
        }
        block['hash'] = self.hash_block(block)
        self.chain.append(block)
        self.pending_tasks = []  # Clear pending tasks
        return block

    def is_chain_valid(self) -> bool:
        """
        Validates the blockchain to ensure integrity.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check hash integrity
            if current_block['previous_hash'] != previous_block['hash']:
                return False

            # Validate PoI proof
            if not self.validate_proof(previous_block['proof'], current_block['proof']):
                return False

        return True


# AI Virtual Machine (AIVM) Class
class AIVM:
    """
    AI Virtual Machine (AIVM) for executing AI models and tasks on-chain.
    """
    def __init__(self):
        self.models = {}  # Registered AI models

    def register_model(self, model_id: str, model_function: Any):
        """
        Registers an AI model with the AIVM.
        """
        self.models[model_id] = model_function

    def execute_task(self, model_id: str, input_data: Any) -> Any:
        """
        Executes an AI task using the specified model.
        """
        if model_id not in self.models:
            raise ValueError(f"Model {model_id} not found in AIVM.")
        return self.models[model_id](input_data)


# Example Usage
if __name__ == "__main__":
    # Initialize blockchain node and AIVM
    node = BlockchainNode(node_id="Node1")
    aivm = AIVM()

    # Register a simple AI model
    def example_model(data):
        return f"Processed: {data}"

    aivm.register_model("example_model", example_model)

    # Add AI tasks to the blockchain node
    node.add_task({"model_id": "example_model", "input_data": "Hello, AI!"})

    # Perform PoI consensus and create a new block
    previous_proof = node.chain[-1]['proof']
    proof = node.proof_of_intelligence(previous_proof)
    new_block = node.create_block(proof)

    # Execute AI tasks using AIVM
    for task in new_block['tasks']:
        result = aivm.execute_task(task['model_id'], task['input_data'])
        print(f"Task Result: {result}")

    # Validate blockchain integrity
    print(f"Blockchain valid: {node.is_chain_valid()}")
```
