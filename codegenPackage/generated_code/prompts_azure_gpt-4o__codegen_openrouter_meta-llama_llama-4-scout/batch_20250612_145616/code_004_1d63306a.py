"""
Generated Code Metadata:
========================
Original URL: https://arbitrum.gmx-oracle.io
Prompt: Write a Python function to verify the integrity of GMX oracle price feeds using cryptographic signatures.
Generated: DETERMINISTIC_1d63306aa731498e
Batch ID: 20250612_145616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import hmac
import json
from typing import Dict

def verify_gmx_oracle_signature(
    price_feed_data: Dict[str, str], 
    signature: str, 
    public_key: str
) -> bool:
    """
    Verify the integrity of GMX oracle price feeds using cryptographic signatures.

    Args:
    - price_feed_data (Dict[str, str]): The price feed data to verify.
    - signature (str): The signature to verify against.
    - public_key (str): The public key to use for verification.

    Returns:
    - bool: True if the signature is valid, False otherwise.
    """

    # Ensure price_feed_data is a dictionary
    if not isinstance(price_feed_data, dict):
        raise TypeError("price_feed_data must be a dictionary")

    # Convert price_feed_data to a JSON string
    data_json = json.dumps(price_feed_data, separators=(',', ':'), sort_keys=True)

    # Convert data_json to bytes
    data_bytes = data_json.encode('utf-8')

    # Convert public_key to bytes (assuming it's a hexadecimal string)
    public_key_bytes = bytes.fromhex(public_key)

    # Verify the signature
    try:
        # Use the ecdsa library for verification (not included in Python standard library)
        # For simplicity, assume ecdsa is installed: pip install ecdsa
        import ecdsa
        vk = ecdsa.VerifyingKey.from_string(public_key_bytes, curve=ecdsa.SECP256k1)
        signature_bytes = bytes.fromhex(signature)
        return vk.verify(data_bytes, signature_bytes)
    except Exception as e:
        # Handle any exceptions during verification
        print(f"Error verifying signature: {e}")
        return False


def generate_gmx_oracle_signature(
    price_feed_data: Dict[str, str], 
    private_key: str
) -> str:
    """
    Generate a signature for GMX oracle price feeds using cryptographic signatures.

    Args:
    - price_feed_data (Dict[str, str]): The price feed data to sign.
    - private_key (str): The private key to use for signing.

    Returns:
    - str: The generated signature.
    """

    # Ensure price_feed_data is a dictionary
    if not isinstance(price_feed_data, dict):
        raise TypeError("price_feed_data must be a dictionary")

    # Convert price_feed_data to a JSON string
    data_json = json.dumps(price_feed_data, separators=(',', ':'), sort_keys=True)

    # Convert data_json to bytes
    data_bytes = data_json.encode('utf-8')

    # Convert private_key to bytes (assuming it's a hexadecimal string)
    private_key_bytes = bytes.fromhex(private_key)

    # Generate the signature
    try:
        # Use the ecdsa library for signing (not included in Python standard library)
        # For simplicity, assume ecdsa is installed: pip install ecdsa
        import ecdsa
        sk = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1)
        signature = sk.sign(data_bytes)
        return signature.hex()
    except Exception as e:
        # Handle any exceptions during signing
        print(f"Error generating signature: {e}")
        return ""


# Example usage
if __name__ == "__main__":
    price_feed_data = {
        "key1": "value1",
        "key2": "value2"
    }

    private_key = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
    public_key = "036a5d2148f05a610f0a7c9dc8a6c9f461b68f2294c9c1b1dd5a1d7fb8f499c3"

    signature = generate_gmx_oracle_signature(price_feed_data, private_key)
    print(f"Generated Signature: {signature}")

    is_valid = verify_gmx_oracle_signature(price_feed_data, signature, public_key)
    print(f"Is Signature Valid: {is_valid}")
```
