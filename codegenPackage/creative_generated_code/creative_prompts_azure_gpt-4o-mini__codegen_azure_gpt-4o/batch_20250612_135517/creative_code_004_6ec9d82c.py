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
import hashlib
from bip_utils import Bip39SeedGenerator, Bip32, Bip44Coins, Bip44

def mnemonic_to_extended_public_key(mnemonic: str, passphrase: str = "", derivation_path: str = "m/44'/0'/0'/0/0") -> str:
    """
    Converts a BIP39 mnemonic phrase into a BIP32 extended public key.

    Parameters:
        mnemonic (str): The BIP39 mnemonic phrase.
        passphrase (str): The optional passphrase for mnemonic protection (default: empty string).
        derivation_path (str): The BIP32 derivation path (default: "m/44'/0'/0'/0/0" for Bitcoin).

    Returns:
        str: The BIP32 extended public key.
    """
    try:
        # Generate the seed from the mnemonic and optional passphrase
        seed = Bip39SeedGenerator(mnemonic).Generate(passphrase)

        # Initialize the BIP32 master key from the seed
        bip32_ctx = Bip32.FromSeed(seed)

        # Derive the key for the given derivation path
        derived_key = bip32_ctx.DerivePath(derivation_path)

        # Get the extended public key
        extended_public_key = derived_key.PublicKey().ToExtended()

        return extended_public_key

    except ValueError as e:
        # Handle invalid mnemonic or derivation path errors
        raise ValueError(f"Error converting mnemonic to extended public key: {e}")

# Example usage:
# Replace with your mnemonic and passphrase
mnemonic_example = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"
passphrase_example = ""
derivation_path_example = "m/44'/0'/0'/0/0"

try:
    extended_pub_key = mnemonic_to_extended_public_key(
        mnemonic_example, passphrase_example, derivation_path_example
    )
    print("Extended Public Key:", extended_pub_key)
except ValueError as error:
    print(error)
```

**Note:** The code uses the `bip_utils` Python library to handle BIP39 and BIP32 operations. Ensure that the library is installed (`pip install bip-utils`) before running the code.
