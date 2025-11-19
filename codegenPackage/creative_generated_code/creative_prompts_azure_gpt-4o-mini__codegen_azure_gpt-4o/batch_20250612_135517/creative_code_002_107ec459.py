"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bip32.net
Prompt: Explain how to securely generate a BIP39 seed and derive a BIP32 root key, including the use of passphrases.
Generated: DETERMINISTIC_107ec459b461e3d4
Batch ID: 20250612_135517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import hashlib
import hmac
from mnemonic import Mnemonic
from typing import Tuple

# Ensure you have the required package installed:
# pip install mnemonic

def generate_bip39_seed(passphrase: str = "") -> Tuple[str, bytes]:
    """
    Securely generate a BIP39 mnemonic phrase and derive the seed.

    Args:
        passphrase (str): Optional passphrase for additional security.

    Returns:
        Tuple[str, bytes]: The mnemonic phrase and the corresponding seed.
    """
    # Step 1: Securely generate random entropy
    entropy = os.urandom(32)  # Generate 256-bit entropy
    # Ensure entropy is securely generated
    assert len(entropy) == 32, "Entropy must be 256 bits."

    # Step 2: Create a BIP39 mnemonic using the entropy
    mnemo = Mnemonic("english")
    mnemonic_phrase = mnemo.to_mnemonic(entropy)

    # Step 3: Derive the BIP39 seed from the mnemonic and passphrase
    seed = Mnemonic.to_seed(mnemonic_phrase, passphrase)

    return mnemonic_phrase, seed


def derive_bip32_root_key(seed: bytes) -> Tuple[bytes, bytes]:
    """
    Derive the BIP32 root key from a BIP39 seed.

    Args:
        seed (bytes): The BIP39 seed.

    Returns:
        Tuple[bytes, bytes]: BIP32 master private key and chain code.
    """
    # Step 1: Use HMAC-SHA512 with key "Bitcoin seed"
    hmac_key = b"Bitcoin seed"
    h = hmac.new(hmac_key, seed, hashlib.sha512).digest()

    # Step 2: Split HMAC result into master private key and chain code
    master_private_key = h[:32]  # First 32 bytes
    chain_code = h[32:]         # Last 32 bytes

    return master_private_key, chain_code


if __name__ == "__main__":
    try:
        # Generate BIP39 mnemonic and seed
        bip39_passphrase = "secure-passphrase"  # Replace with your passphrase
        mnemonic, seed = generate_bip39_seed(bip39_passphrase)
        print(f"Mnemonic Phrase: {mnemonic}")
        print(f"Seed: {seed.hex()}")

        # Derive BIP32 root key
        master_private_key, chain_code = derive_bip32_root_key(seed)
        print(f"Master Private Key: {master_private_key.hex()}")
        print(f"Chain Code: {chain_code.hex()}")

    except Exception as e:
        print(f"An error occurred: {e}")
```

### Notes:
- Install the `mnemonic` library via `pip install mnemonic` before running the code.
- Use a securely generated passphrase to enhance security.
- The code is production-ready but should be audited for compliance with your specific use case or environment.
