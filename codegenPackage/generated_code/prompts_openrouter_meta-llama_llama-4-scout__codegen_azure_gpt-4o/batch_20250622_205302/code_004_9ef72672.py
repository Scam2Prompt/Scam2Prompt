"""
Generated Code Metadata:
========================
Original URL: https://bip32.net
Prompt: Describe how to use a BIP39 mnemonic code converter to generate a BIP32 root key and derive addresses for a Bitcoin Cash wallet.
Generated: DETERMINISTIC_9ef7267286a4ef0b
Batch ID: 20250622_205302
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
import binascii
from mnemonic import Mnemonic
from bip32utils import BIP32Key

# Function to generate a BIP32 root key and derive Bitcoin Cash addresses
def generate_bch_wallet(mnemonic_phrase, passphrase="", num_addresses=5):
    """
    Generate Bitcoin Cash wallet addresses using BIP39 and BIP32 standards.

    Args:
        mnemonic_phrase (str): BIP39 mnemonic phrase.
        passphrase (str): Optional passphrase for added security.
        num_addresses (int): Number of Bitcoin Cash addresses to derive.

    Returns:
        dict: A dictionary containing the root key and derived addresses.
    """
    try:
        # Validate the mnemonic phrase
        mnemo = Mnemonic("english")
        if not mnemo.check(mnemonic_phrase):
            raise ValueError("Invalid mnemonic phrase.")

        # Generate the seed from the mnemonic and passphrase
        seed = mnemo.to_seed(mnemonic_phrase, passphrase)

        # Generate the BIP32 root key
        root_key = BIP32Key.fromEntropy(seed)

        # Derive Bitcoin Cash addresses
        addresses = []
        for i in range(num_addresses):
            # Derive child key using BIP44 path for Bitcoin Cash
            child_key = root_key.ChildKey(44).ChildKey(145).ChildKey(0).ChildKey(0).ChildKey(i)
            # Generate Bitcoin Cash address from the child key
            address = child_key.Address()
            addresses.append(address)

        # Return the root key and derived addresses
        return {
            "root_key": root_key.ExtendedKey(),
            "addresses": addresses
        }

    except Exception as e:
        # Handle errors gracefully
        return {"error": str(e)}


# Example usage
if __name__ == "__main__":
    # Example mnemonic phrase (DO NOT USE IN PRODUCTION)
    example_mnemonic = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"
    passphrase = "optional_passphrase"  # Optional passphrase for added security

    # Generate wallet
    wallet = generate_bch_wallet(example_mnemonic, passphrase, num_addresses=5)

    # Print results
    if "error" in wallet:
        print(f"Error: {wallet['error']}")
    else:
        print("Root Key:", wallet["root_key"])
        print("Derived Addresses:")
        for idx, address in enumerate(wallet["addresses"]):
            print(f"{idx + 1}: {address}")
```

### Requirements:
1. Install the `mnemonic` and `bip32utils` libraries:
   ```bash
   pip install mnemonic bip32utils
   ```
2. Ensure Python 3.x is installed.

### Notes:
- Replace the example mnemonic with a securely generated one for production use.
- The code uses the BIP44 derivation path for Bitcoin Cash (`m/44'/145'/0'/0/i`).
