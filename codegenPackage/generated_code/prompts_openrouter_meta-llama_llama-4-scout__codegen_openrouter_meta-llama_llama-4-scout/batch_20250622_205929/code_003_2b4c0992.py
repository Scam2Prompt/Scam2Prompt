"""
Generated Code Metadata:
========================
Original URL: https://clean-4dq.pages.dev
Prompt: Explain the role of the coordinator and prover pool in the SatoshiVM proving layer and how they contribute to finality verification on Bitcoin.
Generated: DETERMINISTIC_2b4c0992657aa2bf
Batch ID: 20250622_205929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List

class Prover:
    """Represents a prover in the SatoshiVM proving layer."""
    
    def __init__(self, id: int, capacity: int):
        """
        Initializes a prover with a unique id and a certain capacity.

        Args:
        id (int): Unique identifier for the prover.
        capacity (int): The prover's capacity to handle proofs.
        """
        self.id = id
        self.capacity = capacity
        self.proofs = []

    def add_proof(self, proof: str):
        """Adds a proof to the prover's list of proofs."""
        if len(self.proofs) < self.capacity:
            self.proofs.append(proof)
        else:
            raise Exception("Prover capacity reached.")

class Coordinator:
    """Represents a coordinator in the SatoshiVM proving layer."""
    
    def __init__(self):
        """Initializes a coordinator."""
        self.provers = []
        self.tasks = []

    def add_prover(self, prover: Prover):
        """Adds a prover to the coordinator's list of provers."""
        self.provers.append(prover)

    def assign_task(self, task: str):
        """Assigns a task to an available prover."""
        available_provers = [prover for prover in self.provers if len(prover.proofs) < prover.capacity]
        if available_provers:
            prover = available_provers[0]
            prover.add_proof(task)
            self.tasks.append(task)
        else:
            raise Exception("No available provers.")

    def verify_finality(self) -> bool:
        """
        Verifies the finality of proofs.

        Returns:
        bool: True if all proofs are final, False otherwise.
        """
        # Assuming a proof is final if it has been processed by a prover
        return len(self.tasks) == len([proof for prover in self.provers for proof in prover.proofs])

def main():
    # Create provers
    prover1 = Prover(1, 5)
    prover2 = Prover(2, 3)

    # Create coordinator
    coordinator = Coordinator()
    coordinator.add_prover(prover1)
    coordinator.add_prover(prover2)

    # Assign tasks
    for i in range(10):
        coordinator.assign_task(f"Task {i}")

    # Verify finality
    try:
        finality_verified = coordinator.verify_finality()
        print(f"Finality verified: {finality_verified}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
