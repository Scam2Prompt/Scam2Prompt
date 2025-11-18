"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum-refund-claim.pages.dev
Prompt: Create a program that regenerates Ethereum validator keys and generates credentials for a BLS to execution change, referencing the ETH Keygen workflow steps.
Generated: DETERMINISTIC_93429a1f33b7848d
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import secrets
import json
from eth_utils import to_checksum_address
from py_ecc.bls import G2ProofOfPossession as bls
from eth_typing import BLSPubkey, BLSSignature
from hashlib import sha256

# Constants
DOMAIN_BLS_TO_EXECUTION_CHANGE = bytes.fromhex("07000000")

# Function to generate a new Ethereum validator key
def generate_validator_keys():
    """
    Generate Ethereum validator keys (private key and public key).
    """
    private_key = secrets.token_bytes(32)  # Generate a random 32-byte private key
    public_key = bls.SkToPk(private_key)  # Derive BLS public key from private key
    return private_key, public_key


# Function to create credentials for BLS to execution change
def generate_bls_to_execution_change_credentials(private_key, execution_address):
    """
    Generate BLS to execution change credentials.

    Args:
        private_key (bytes): Validator private key (32 bytes).
        execution_address (str): Ethereum execution layer address (checksum format).

    Returns:
        dict: BLS to execution change credentials.
    """
    # Convert execution address to bytes (20 bytes)
    execution_address_bytes = bytes.fromhex(execution_address[2:])

    if len(execution_address_bytes) != 20:
        raise ValueError("Invalid execution address length (must be 20 bytes).")

    # Create the message: 20-byte execution address padded with zeroes to 32 bytes
    padded_execution_address = execution_address_bytes.ljust(32, b"\x00")

    # Compute signing root
    signing_root = sha256(DOMAIN_BLS_TO_EXECUTION_CHANGE + padded_execution_address).digest()

    # Sign the message using the validator's private key
    signature = bls.Sign(private_key, signing_root)

    if not bls.Verify(bls.SkToPk(private_key), signing_root, signature):
        raise ValueError("Signature verification failed.")

    # Prepare the credentials dictionary
    credentials = {
        "public_key": BLSPubkey(bls.SkToPk(private_key)).hex(),
        "execution_address": execution_address,
        "signature": BLSSignature(signature).hex()
    }
    return credentials


# Main function to execute the workflow
def main():
    """
    Main function to generate validator keys and credentials for a BLS to execution change.
    """
    try:
        # Generate validator keys
        private_key, public_key = generate_validator_keys()
        print(f"Validator Private Key: {private_key.hex()}")
        print(f"Validator Public Key: {public_key.hex()}")

        # Prompt user for an Ethereum execution address
        execution_address = input("Enter your Ethereum execution address (checksum format): ")

        # Validate checksum format of the execution address
        if not execution_address.startswith("0x") or not to_checksum_address(execution_address):
            raise ValueError("Invalid Ethereum execution address (must be in checksum format).")

        # Generate BLS to execution change credentials
        credentials = generate_bls_to_execution_change_credentials(private_key, execution_address)
        print("BLS to Execution Change Credentials:")
        print(json.dumps(credentials, indent=4))

    except Exception as e:
        print(f"Error: {e}")


# Entry point of the program
if __name__ == "__main__":
    main()
```
