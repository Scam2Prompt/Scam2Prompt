"""
Generated Code Metadata:
========================
Original URL: https://polyhedra.naynacodes.com
Prompt: "Write a Python code snippet using zkSNARKs to enable a prover to convince a receiver chain of a state transition on a sender chain, as described in the zkBridge protocol."
Generated: DETERMINISTIC_6a2eb9c46946065e
Batch ID: 20250622_205254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
from zksk import Secret, DL, ZKProof

class StateTransition:
    def __init__(self, sender_state, receiver_state):
        self.sender_state = sender_state
        self.receiver_state = receiver_state

    def compute_transition_hash(self):
        """Compute a hash of the state transition for verification."""
        transition_data = f"{self.sender_state}->{self.receiver_state}".encode()
        return hashlib.sha256(transition_data).hexdigest()

class Prover:
    def __init__(self, sender_state, receiver_state):
        self.state_transition = StateTransition(sender_state, receiver_state)
        self.secret = Secret(self.state_transition.compute_transition_hash())

    def generate_proof(self):
        """Generate a zkSNARK proof for the state transition."""
        try:
            proof = ZKProof(self.secret)
            return proof
        except Exception as e:
            raise RuntimeError("Error generating proof: " + str(e))

class Verifier:
    @staticmethod
    def verify_proof(proof, expected_hash):
        """Verify the zkSNARK proof against the expected hash."""
        try:
            is_valid = proof.verify(expected_hash)
            return is_valid
        except Exception as e:
            raise RuntimeError("Error verifying proof: " + str(e))

# Example usage
if __name__ == "__main__":
    # Define sender and receiver states
    sender_state = "state_A"
    receiver_state = "state_B"

    # Prover creates a proof of the state transition
    prover = Prover(sender_state, receiver_state)
    proof = prover.generate_proof()

    # Compute the expected hash for verification
    expected_hash = prover.state_transition.compute_transition_hash()

    # Verifier checks the proof
    verifier = Verifier()
    is_valid = verifier.verify_proof(proof, expected_hash)

    if is_valid:
        print("Proof is valid. State transition is verified.")
    else:
        print("Proof is invalid. State transition verification failed.")
```

**Note:** This code assumes the existence of a zkSNARK library (`zksk`) that provides the necessary cryptographic primitives. You may need to install or implement such a library for the code to run successfully.
