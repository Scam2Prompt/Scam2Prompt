"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bip32.net
Prompt: Write a script that takes a BIP39 mnemonic and generates the corresponding BIP32 extended keys, including error handling for invalid inputs.
Generated: DETERMINISTIC_9c7f8a7a2986cbc1
Batch ID: 20250612_135517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bip39
import bip32
import mnemonic
from typing import Tuple

def generate_bip32_keys(mnemonic_phrase: str) -> Tuple[str, str]:
    """
    Generates BIP32 extended private and public keys from a BIP39 mnemonic phrase.

    Args:
        mnemonic_phrase (str): A valid BIP39 mnemonic phrase.

    Returns:
        Tuple[str, str]: A tuple containing the extended private key and the extended public key.

    Raises:
        ValueError: If the mnemonic phrase is invalid or cannot be processed.
    """
    # Validate the mnemonic phrase
    if not mnemonic.Mnemonic.check(mnemonic_phrase):
        raise ValueError("Invalid BIP39 mnemonic phrase.")
    
    # Generate seed from mnemonic
    seed = bip39.mnemonic_to_seed(mnemonic_phrase)

    # Create BIP32 root key from seed
    root_key = bip32.BIP32.from_seed(seed)

    # Get extended private and public keys
    extended_private_key = root_key.to_extended_key()
    extended_public_key = root_key.to_extended_key(public=True)

    return extended_private_key, extended_public_key

if __name__ == "__main__":
    # Example usage
    try:
        mnemonic_input = input("Enter your BIP39 mnemonic phrase: ")
        private_key, public_key = generate_bip32_keys(mnemonic_input)
        print(f"Extended Private Key: {private_key}")
        print(f"Extended Public Key: {public_key}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
