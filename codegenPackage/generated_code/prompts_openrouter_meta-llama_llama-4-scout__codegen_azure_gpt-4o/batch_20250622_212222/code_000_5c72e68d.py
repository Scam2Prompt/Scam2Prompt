"""
Generated Code Metadata:
========================
Original URL: https://lightchain-dapp.web.app
Prompt: "Write a Python code snippet to implement a basic Proof of Intelligence (PoI) consensus mechanism, considering AI computations such as model training and inference tasks."
Generated: DETERMINISTIC_5c72e68dd2ecb408
Batch ID: 20250622_212222
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
import random

class ProofOfIntelligence:
    """
    A basic implementation of Proof of Intelligence (PoI) consensus mechanism.
    This mechanism rewards computational work related to AI tasks such as model training and inference.
    """

    def __init__(self, difficulty=4):
        """
        Initialize the PoI system.

        :param difficulty: Number of leading zeros required in the hash for a valid proof.
        """
        self.difficulty = difficulty
        self.chain = []  # Blockchain to store valid proofs
        self.current_task = None  # Current AI task to be solved

    def generate_ai_task(self):
        """
        Generate a random AI task for the proof.
        For simplicity, we'll simulate this as a random number to be "processed".
        """
        self.current_task = random.randint(1, 1000)
        print(f"Generated AI task: {self.current_task}")

    def perform_ai_computation(self, task):
        """
        Simulate AI computation (e.g., model training or inference).
        Here, we'll simply square the task as a placeholder for actual computation.

        :param task: The input task to process.
        :return: The result of the computation.
        """
        return task ** 2

    def validate_proof(self, task, computation_result, nonce):
        """
        Validate the proof by checking if the hash meets the difficulty criteria.

        :param task: The original AI task.
        :param computation_result: The result of the AI computation.
        :param nonce: The nonce used to generate the hash.
        :return: True if the proof is valid, False otherwise.
        """
        proof_string = f"{task}{computation_result}{nonce}"
        proof_hash = hashlib.sha256(proof_string.encode()).hexdigest()
        return proof_hash.startswith("0" * self.difficulty)

    def mine_proof(self):
        """
        Perform the mining process to find a valid proof.
        """
        if self.current_task is None:
            raise ValueError("No AI task generated. Call generate_ai_task() first.")

        computation_result = self.perform_ai_computation(self.current_task)
        nonce = 0

        print("Mining proof...")
        start_time = time.time()

        while True:
            if self.validate_proof(self.current_task, computation_result, nonce):
                end_time = time.time()
                print(f"Proof found! Nonce: {nonce}, Time taken: {end_time - start_time:.2f} seconds")
                self.chain.append({
                    "task": self.current_task,
                    "computation_result": computation_result,
                    "nonce": nonce,
                    "timestamp": time.time()
                })
                break
            nonce += 1

    def display_chain(self):
        """
        Display the blockchain containing all valid proofs.
        """
        print("Blockchain:")
        for block in self.chain:
            print(block)


# Example usage
if __name__ == "__main__":
    poi = ProofOfIntelligence(difficulty=4)  # Adjust difficulty as needed
    poi.generate_ai_task()
    poi.mine_proof()
    poi.display_chain()
```
