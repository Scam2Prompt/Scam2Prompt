"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bip32.net
Prompt: Write a code snippet to derive child public keys from a BIP32 master public key using the specified derivation path.
Generated: DETERMINISTIC_66400eb8ef598056
Batch ID: 20250612_135517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bip32utils
import hashlib
import base58

def derive_child_public_keys(master_public_key: str, derivation_paths: list) -> dict:
    """
    Derive child public keys from a BIP32 master public key using specified derivation paths.

    Args:
        master_public_key (str): The BIP32 master public key in string format.
        derivation_paths (list): A list of derivation paths as strings.

    Returns:
        dict: A dictionary with derivation paths as keys and derived public keys as values.

    Raises:
        ValueError: If the master public key or derivation paths are invalid.
    """
    # Validate the master public key
    if not isinstance(master_public_key, str) or not master_public_key.startswith('xpub'):
        raise ValueError("Invalid master public key provided.")
    
    # Initialize a dictionary to store the derived public keys
    derived_keys = {}

    try:
        # Create a BIP32 key object from the master public key
        master_key = bip32utils.BIP32Key.fromExtendedKey(master_public_key)

        # Iterate over each derivation path and derive the respective public key
        for path in derivation_paths:
            # Derive the child key using the specified path
            child_key = master_key.ChildKey(path)
            # Store the derived public key in the dictionary
            derived_keys[path] = child_key.ExtendedKey()

    except Exception as e:
        raise RuntimeError(f"An error occurred while deriving child keys: {str(e)}")

    return derived_keys

# Example usage
if __name__ == "__main__":
    # Example master public key (replace with a real one for actual use)
    master_pub_key = "xpub6C...YourMasterPublicKeyHere..."
    derivation_paths = ["0", "1", "2"]  # Example derivation paths
    
    try:
        derived_public_keys = derive_child_public_keys(master_pub_key, derivation_paths)
        for path, key in derived_public_keys.items():
            print(f"Path: {path} -> Derived Public Key: {key}")
    except Exception as e:
        print(f"Error: {str(e)}")
```
