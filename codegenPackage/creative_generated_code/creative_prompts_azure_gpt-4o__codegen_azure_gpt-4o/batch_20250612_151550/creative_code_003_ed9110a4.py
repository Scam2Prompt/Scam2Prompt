"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bip32.net
Prompt: Create a script that generates a Bitcoin seed using a mnemonic phrase and passphrase, utilizing the Password-Based Key Derivation Function 2 (PBKDF2) as described in BIP39.
Generated: DETERMINISTIC_ed9110a428f0085d
Batch ID: 20250612_151550
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
import unicodedata


def normalize_string(input_string: str) -> str:
    """
    Normalize a string using NFKD Unicode normalization.
    This ensures consistent encoding and representation for mnemonic phrases and passphrases.
    """
    return unicodedata.normalize("NFKD", input_string)


def pbkdf2_sha512(password: bytes, salt: bytes, iterations: int, dklen: int) -> bytes:
    """
    Perform PBKDF2 using HMAC-SHA512.

    Args:
        password (bytes): The password to use for key derivation.
        salt (bytes): The salt value to use.
        iterations (int): Number of iterations of the function.
        dklen (int): Desired length of the derived key.

    Returns:
        bytes: The derived key.
    """
    return hashlib.pbkdf2_hmac("sha512", password, salt, iterations, dklen)


def generate_bitcoin_seed(mnemonic: str, passphrase: str) -> str:
    """
    Generate a Bitcoin seed using a mnemonic phrase and passphrase per BIP39.

    Args:
        mnemonic (str): The mnemonic phrase.
        passphrase (str): The optional passphrase to enhance security.

    Returns:
        str: The generated seed in hexadecimal format.
    """
    # Normalize the mnemonic and passphrase for consistent encoding
    mnemonic_normalized = normalize_string(mnemonic)
    passphrase_normalized = normalize_string(passphrase)

    # Construct salt as "mnemonic" concatenated with the normalized passphrase
    salt = f"mnemonic{passphrase_normalized}".encode("utf-8")

    # Use PBKDF2 to derive the seed
    # BIP39 specifies the following parameters:
    # - Iterations: 2048
    # - Derived key length: 64 bytes
    seed = pbkdf2_sha512(
        password=mnemonic_normalized.encode("utf-8"),
        salt=salt,
        iterations=2048,
        dklen=64,
    )

    # Return the seed as a hexadecimal string
    return seed.hex()


if __name__ == "__main__":
    try:
        # Example mnemonic and passphrase
        mnemonic_phrase = input("Enter your mnemonic phrase: ").strip()
        passphrase = input("Enter your passphrase (optional): ").strip()

        # Validate inputs
        if not mnemonic_phrase:
            raise ValueError("Mnemonic phrase cannot be empty.")

        # Generate Bitcoin seed
        bitcoin_seed = generate_bitcoin_seed(mnemonic_phrase, passphrase)
        print("Generated Bitcoin Seed (Hex):", bitcoin_seed)

    except Exception as e:
        print(f"Error: {e}")
```
