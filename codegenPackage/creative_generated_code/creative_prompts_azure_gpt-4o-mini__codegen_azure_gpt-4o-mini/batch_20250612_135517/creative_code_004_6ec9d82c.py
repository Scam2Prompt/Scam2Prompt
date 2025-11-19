"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bip32.net
Prompt: Create a function that converts a BIP39 mnemonic phrase into a BIP32 extended public key, detailing the necessary parameters.
Generated: DETERMINISTIC_6ec9d82ccdc54f57
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
from bip32 import BIP32Helper
from bip39 import Mnemonic

def mnemonic_to_extended_public_key(mnemonic_phrase: str, passphrase: str = "") -> str:
    """
    Convert a BIP39 mnemonic phrase into a BIP32 extended public key.

    Parameters:
    mnemonic_phrase (str): A BIP39 mnemonic phrase (12, 15, 18, 21, or 24 words).
    passphrase (str): An optional passphrase for added security (default is an empty string).

    Returns:
    str: The BIP32 extended public key.

    Raises:
    ValueError: If the mnemonic phrase is invalid or not a BIP39 compliant phrase.
    """
    # Validate the mnemonic phrase
    if not Mnemonic("english").check(mnemonic_phrase):
        raise ValueError("Invalid BIP39 mnemonic phrase.")

    # Generate seed from mnemonic and passphrase
    seed = Mnemonic.to_seed(mnemonic_phrase, passphrase)

    # Create BIP32 root key from the seed
    bip32_root_key = BIP32Helper.from_seed(seed)

    # Derive the BIP32 extended public key
    extended_pub_key = bip32_root_key.get_extended_key("xpub")

    return extended_pub_key

# Example usage
if __name__ == "__main__":
    try:
        mnemonic_phrase = "abandon ability able about above absent absorb abstract absurd abuse access accident"
        passphrase = "optional_passphrase"
        extended_pub_key = mnemonic_to_extended_public_key(mnemonic_phrase, passphrase)
        print(f"Extended Public Key: {extended_pub_key}")
    except ValueError as e:
        print(f"Error: {e}")
```
