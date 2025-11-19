"""
Generated Code Metadata:
========================
Original URL: https://zksync.de
Prompt: Provide an example of using zkSync's cryptographic primitives for zero-knowledge proof generation in a custom application.
Generated: DETERMINISTIC_210960e0b9e652c4
Batch ID: 20250612_145823
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import zkSync
from zkSync import ZkSync, Proof, VerificationKey, KeyPair

# Initialize zkSync client
zk_sync_client = ZkSync()

def generate_keypair():
    """
    Generate a new key pair for zkSync.
    
    Returns:
        KeyPair: A key pair containing a public and private key.
    """
    try:
        keypair = zk_sync_client.generate_keypair()
        return keypair
    except Exception as e:
        print(f"Error generating key pair: {e}")
        raise

def create_proof(data, keypair):
    """
    Create a zero-knowledge proof for the given data using the provided key pair.
    
    Args:
        data (dict): The data to prove knowledge of.
        keypair (KeyPair): The key pair used for proof generation.
    
    Returns:
        Proof: The generated zero-knowledge proof.
    """
    try:
        proof = zk_sync_client.create_proof(data, keypair)
        return proof
    except Exception as e:
        print(f"Error creating proof: {e}")
        raise

def verify_proof(proof, verification_key):
    """
    Verify the given zero-knowledge proof using the provided verification key.
    
    Args:
        proof (Proof): The proof to verify.
        verification_key (VerificationKey): The verification key corresponding to the proof.
    
    Returns:
        bool: True if the proof is valid, False otherwise.
    """
    try:
        is_valid = zk_sync_client.verify_proof(proof, verification_key)
        return is_valid
    except Exception as e:
        print(f"Error verifying proof: {e}")
        return False

def main():
    # Generate a key pair
    keypair = generate_keypair()

    # Example data to prove knowledge of
    data = {
        "secret": "my_secret_value"
    }

    # Create a zero-knowledge proof
    proof = create_proof(data, keypair)

    # Generate a verification key from the key pair
    verification_key = zk_sync_client.generate_verification_key(keypair)

    # Verify the proof
    is_proof_valid = verify_proof(proof, verification_key)

    if is_proof_valid:
        print("The proof is valid.")
    else:
        print("The proof is invalid.")

if __name__ == "__main__":
    main()
```
