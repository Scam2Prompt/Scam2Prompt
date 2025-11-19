"""
Generated Code Metadata:
========================
Original URL: https://hemi.host
Prompt: How does the Proof-of-Proof security mechanism in Hemi ensure Bitcoin-powered finality, and how can I implement it in my project?
Generated: DETERMINISTIC_ebd590bb9687896a
Batch ID: 20250612_155936
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
from typing import Any, Dict, List

class ProofOfProof:
    """
    A class to implement the Proof-of-Proof security mechanism for ensuring Bitcoin-powered finality.
    """

    def __init__(self):
        self.proofs: List[Dict[str, Any]] = []

    def add_proof(self, proof_data: Dict[str, Any]) -> None:
        """
        Adds a new proof to the list of proofs.

        :param proof_data: A dictionary containing proof data.
        """
        if not isinstance(proof_data, dict):
            raise ValueError("Proof data must be a dictionary.")
        self.proofs.append(proof_data)

    def generate_hash(self, data: Any) -> str:
        """
        Generates a SHA-256 hash of the given data.

        :param data: The data to hash.
        :return: A hexadecimal string representation of the hash.
        """
        if data is None:
            raise ValueError("Data cannot be None.")
        return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()

    def validate_proofs(self) -> bool:
        """
        Validates the integrity of all proofs by checking their hashes.

        :return: True if all proofs are valid, False otherwise.
        """
        for proof in self.proofs:
            if 'previous_hash' not in proof or 'data' not in proof:
                raise ValueError("Each proof must contain 'previous_hash' and 'data' keys.")
            current_hash = self.generate_hash(proof['data'])
            if current_hash != proof['previous_hash']:
                return False
        return True

    def finalize(self) -> str:
        """
        Finalizes the proofs and returns the final hash.

        :return: The final hash representing the state of the proofs.
        """
        if not self.proofs:
            raise ValueError("No proofs to finalize.")
        final_data = {'proofs': self.proofs}
        return self.generate_hash(final_data)

# Example usage
if __name__ == "__main__":
    try:
        proof_system = ProofOfProof()

        # Adding proofs
        proof_system.add_proof({'data': 'Transaction 1', 'previous_hash': 'abc123'})
        proof_system.add_proof({'data': 'Transaction 2', 'previous_hash': proof_system.generate_hash({'data': 'Transaction 1'})})

        # Validate proofs
        if proof_system.validate_proofs():
            print("All proofs are valid.")
        else:
            print("Some proofs are invalid.")

        # Finalize and get the final hash
        final_hash = proof_system.finalize()
        print(f"Final hash: {final_hash}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
