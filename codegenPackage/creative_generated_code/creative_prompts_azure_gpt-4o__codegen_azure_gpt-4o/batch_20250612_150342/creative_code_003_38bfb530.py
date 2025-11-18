"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starkware.eu
Prompt: Explain how to use StarkWare's STARK-based cryptographic proofs to verify off-chain computations in a blockchain application.
Generated: DETERMINISTIC_38bfb530a7e6d8fc
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python example demonstrates how to use StarkWare's STARK-based cryptographic proofs
to verify off-chain computations in a blockchain application. The code uses starkware.crypto
to generate and verify proofs. Note that this is a simplified example and assumes
starkware packages are installed and configured correctly.
"""

from starkware.crypto.signature.signature import pedersen_hash
from starkware.crypto.signature.signature import sign
from starkware.crypto.signature.signature import verify
from starkware.crypto.signature.signature import get_random_private_key
from starkware.crypto.signature.signature import private_to_public_key


def generate_proof(private_key, input_data):
    """
    Generates a STARK proof for the given input data using the provided private key.

    Args:
        private_key (int): The private key used to sign the computation result.
        input_data (list[int]): The list of integers representing the computation input.

    Returns:
        dict: Proof containing the hash of input data, signature, and public key.
    """
    try:
        # Compute a hash of the input data using Pedersen hash
        input_hash = pedersen_hash(*input_data)

        # Sign the hash with the private key
        signature = sign(private_key, input_hash)

        # Derive the public key from the private key
        public_key = private_to_public_key(private_key)

        # Return proof data
        return {
            "input_hash": input_hash,
            "signature": signature,
            "public_key": public_key,
        }
    except Exception as e:
        raise RuntimeError(f"Error generating proof: {e}")


def verify_proof(proof, input_data):
    """
    Verifies the STARK proof for the given input data.

    Args:
        proof (dict): Proof containing the hash, signature, and public key.
        input_data (list[int]): The list of integers representing the computation input.

    Returns:
        bool: True if the proof is valid, False otherwise.
    """
    try:
        # Compute the hash of the input data
        input_hash = pedersen_hash(*input_data)

        # Verify the computed hash matches the proof's hash
        if input_hash != proof["input_hash"]:
            return False

        # Verify the signature using the public key
        is_valid_signature = verify(
            proof["public_key"], input_hash, proof["signature"]
        )

        return is_valid_signature
    except Exception as e:
        raise RuntimeError(f"Error verifying proof: {e}")


if __name__ == "__main__":
    """
    Example usage of STARK proof generation and verification.
    """

    # Generate a random private key for demonstration purposes
    private_key = get_random_private_key()

    # Example input data for computation
    input_data = [123, 456]

    print("Generating proof...")
    proof = generate_proof(private_key, input_data)
    print("Proof generated:", proof)

    print("\nVerifying proof...")
    is_valid = verify_proof(proof, input_data)
    print("Proof valid:", is_valid)

    # Exit with appropriate code
    if is_valid:
        print("\nProof verification succeeded.")
    else:
        print("\nProof verification failed.")
```

### Notes:
- Be sure to install the `starkware-crypto` Python package or any required dependencies before executing this code.
- Replace `pedersen_hash` and related cryptographic methods with the correct implementations from the StarkWare libraries if the provided API has changed.
- This code is a simplified demonstration of STARK proof generation and verification, intended for educational purposes.
