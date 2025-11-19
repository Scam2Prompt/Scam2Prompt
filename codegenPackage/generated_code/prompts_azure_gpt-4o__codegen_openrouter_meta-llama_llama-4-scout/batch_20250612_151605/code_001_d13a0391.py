"""
Generated Code Metadata:
========================
Original URL: https://polyhedra.naynacodes.com
Prompt: Generate a Python script that uses zkSNARKs to verify state transitions between sender and receiver chains as outlined in the zkBridge documentation.
Generated: DETERMINISTIC_d13a03914ca75cc2
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sys
from typing import Tuple
from circom.circuit import Circuit
from circom.circuitcompiler import compile
from zkSNARK import generate_proof, verify_proof
from hashlib import sha256

# Define the circuit for state transition
class StateTransitionCircuit(Circuit):
    def __init__(self, sender_chain_id: int, receiver_chain_id: int, 
                 sender_account: int, receiver_account: int, 
                 amount: int, proof: int):
        super().__init__("StateTransitionCircuit")
        self.sender_chain_id = self._var(sender_chain_id, "sender_chain_id")
        self.receiver_chain_id = self._var(receiver_chain_id, "receiver_chain_id")
        self.sender_account = self._var(sender_account, "sender_account")
        self.receiver_account = self._var(receiver_account, "receiver_account")
        self.amount = self._var(amount, "amount")
        self.proof = self._var(proof, "proof")

        # Check if sender account has sufficient balance
        self.balance_check = self._constraint(self.sender_account >= self.amount)

        # Check if chain IDs are valid
        self.chain_id_check = self._constraint(self.sender_chain_id > 0)
        self.chain_id_check = self._constraint(self.receiver_chain_id > 0)

        # Check if accounts are valid
        self.account_check = self._constraint(self.sender_account >= 0)
        self.account_check = self._constraint(self.receiver_account >= 0)

    def run(self):
        return self.calculate_witness()

def generate_state_transition_proof(sender_chain_id: int, receiver_chain_id: int, 
                                    sender_account: int, receiver_account: int, 
                                    amount: int) -> Tuple:
    # Generate the circuit
    circuit = StateTransitionCircuit(sender_chain_id, receiver_chain_id, 
                                     sender_account, receiver_account, 
                                     amount, 0)

    # Compile the circuit
    compile(circuit, "./state_transition_circuit", ["--O2"])

    # Generate the proof
    proof, public_input = generate_proof(circuit, 
                                         [sender_chain_id, receiver_chain_id, 
                                          sender_account, receiver_account, 
                                          amount])

    return proof, public_input

def verify_state_transition_proof(proof: bytes, public_input: Tuple) -> bool:
    # Verify the proof
    return verify_proof(proof, public_input)

def main():
    try:
        sender_chain_id = 1
        receiver_chain_id = 2
        sender_account = 100
        receiver_account = 50
        amount = 20

        # Generate the proof
        proof, public_input = generate_state_transition_proof(sender_chain_id, 
                                                              receiver_chain_id, 
                                                              sender_account, 
                                                              receiver_account, 
                                                              amount)

        # Verify the proof
        is_valid = verify_state_transition_proof(proof, public_input)

        if is_valid:
            print("State transition proof is valid")
        else:
            print("State transition proof is invalid")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
