"""
Generated Code Metadata:
========================
Original URL: https://nfts-satoshivm.pages.dev
Prompt: Develop a proof-of-work based fraud proof system for a Bitcoin Layer2 solution, ensuring maximum simplicity and sustainability.
Generated: DETERMINISTIC_56b4fe7de92d160f
Batch ID: 20250622_205144
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

class ProofOfWork:
    """
    A simple Proof-of-Work system for a Bitcoin Layer2 solution.
    This system ensures fraud-proofing by requiring computational work to validate transactions.
    """

    def __init__(self, difficulty=4):
        """
        Initialize the ProofOfWork system.

        :param difficulty: Number of leading zeros required in the hash (default: 4).
        """
        self.difficulty = difficulty

    def generate_proof(self, data):
        """
        Generate a proof-of-work for the given data.

        :param data: The input data to be hashed.
        :return: A tuple containing the nonce and the valid hash.
        """
        nonce = 0
        prefix = '0' * self.difficulty  # Target hash prefix
        start_time = time.time()

        while True:
            # Combine data and nonce to create a unique input
            input_data = f"{data}{nonce}".encode('utf-8')
            hash_result = hashlib.sha256(input_data).hexdigest()

            # Check if the hash meets the difficulty requirement
            if hash_result.startswith(prefix):
                end_time = time.time()
                print(f"Proof found in {end_time - start_time:.2f} seconds")
                return nonce, hash_result

            nonce += 1

    def validate_proof(self, data, nonce):
        """
        Validate a proof-of-work for the given data and nonce.

        :param data: The original input data.
        :param nonce: The nonce used to generate the proof.
        :return: True if the proof is valid, False otherwise.
        """
        prefix = '0' * self.difficulty
        input_data = f"{data}{nonce}".encode('utf-8')
        hash_result = hashlib.sha256(input_data).hexdigest()

        return hash_result.startswith(prefix)


# Example usage
if __name__ == "__main__":
    # Initialize the ProofOfWork system with a difficulty of 4
    pow_system = ProofOfWork(difficulty=4)

    # Data to be validated
    transaction_data = "Layer2Transaction:UserA->UserB:Amount=0.01BTC"

    try:
        # Generate proof-of-work
        print("Generating proof-of-work...")
        nonce, valid_hash = pow_system.generate_proof(transaction_data)
        print(f"Nonce: {nonce}")
        print(f"Valid Hash: {valid_hash}")

        # Validate proof-of-work
        print("Validating proof-of-work...")
        is_valid = pow_system.validate_proof(transaction_data, nonce)
        print(f"Proof-of-Work Valid: {is_valid}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
