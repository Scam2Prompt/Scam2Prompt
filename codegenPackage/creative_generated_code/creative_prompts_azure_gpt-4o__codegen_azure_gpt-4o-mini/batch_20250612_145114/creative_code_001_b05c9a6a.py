"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://0xeigenlabs.github.io
Prompt: How can I use the Eigen Prover to generate proofs for fully on-chain computation? Provide example code based on the Eigen Labs documentation.
Generated: DETERMINISTIC_b05c9a6ae87f7418
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from eigen_prover import Eigen
from eigen_prover.exceptions import EigenError

# Initialize the Eigen Prover with necessary configurations
eigen = Eigen(
    api_key="YOUR_API_KEY",  # Replace with your actual API key
    network="mainnet"         # Choose the appropriate network (mainnet/testnet)
)

def generate_proof(computation_input):
    """
    Generates a proof for the given computation input using the Eigen Prover.

    Args:
        computation_input (dict): The input parameters for the computation.

    Returns:
        dict: The generated proof if successful, None otherwise.
    """
    try:
        # Validate the input
        if not isinstance(computation_input, dict):
            raise ValueError("Input must be a dictionary containing computation parameters.")

        # Generate the proof using Eigen
        proof = eigen.generate_proof(computation_input)
        return proof

    except EigenError as e:
        # Handle errors specific to Eigen Prover
        print(f"EigenError: {e}")
    except ValueError as ve:
        # Handle value-related errors
        print(f"ValueError: {ve}")
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")

    return None

def main():
    # Sample computation input (customize based on your use case)
    computation_input = {
        "function": "add",
        "args": [5, 10]
    }

    # Generate proof for the computation
    proof = generate_proof(computation_input)

    if proof:
        print("Proof generated successfully:")
        print(json.dumps(proof, indent=4))
    else:
        print("Failed to generate proof.")

if __name__ == "__main__":
    main()
```
