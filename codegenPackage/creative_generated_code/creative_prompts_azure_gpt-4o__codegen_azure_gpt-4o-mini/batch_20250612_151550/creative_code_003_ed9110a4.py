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
import hashlib
import os
import binascii
import mnemonic  # Install with: pip install mnemonic
from typing import Tuple

def pbkdf2_hmac_sha512(password: bytes, salt: bytes, iterations: int, dklen: int) -> bytes:
    """Derives a key using PBKDF2-HMAC-SHA512.
    
    Args:
        password (bytes): The password to derive the key from.
        salt (bytes): The salt to use for the key derivation.
        iterations (int): The number of iterations.
        dklen (int): The length of the derived key in bytes.
    
    Returns:
        bytes: The derived key.
    """
    return hashlib.pbkdf2_hmac('sha512', password, salt, iterations, dklen)

def generate_mnemonic() -> str:
    """Generates a random mnemonic phrase.
    
    Returns:
        str: A mnemonic phrase.
    """
    mnemonic_gen = mnemonic.Mnemonic("english")
    return mnemonic_gen.generate(strength=256)

def mnemonic_to_seed(mnemonic_phrase: str, passphrase: str = '') -> bytes:
    """Converts a mnemonic phrase into a seed using PBKDF2-HMAC-SHA512.
    
    Args:
        mnemonic_phrase (str): The mnemonic phrase.
        passphrase (str): An optional passphrase. Defaults to an empty string.
    
    Returns:
        bytes: The generated seed.
    
    Raises:
        ValueError: If the mnemonic is invalid.
    """
    # Validate the mnemonic phrase
    if not mnemonic.Mnemonic("english").check(mnemonic_phrase):
        raise ValueError("Invalid mnemonic phrase")
    
    # Create a salt using the mnemonic and passphrase
    salt = b'mnemonic' + passphrase.encode('utf-8')
    
    # Generate the seed using PBKDF2
    seed = pbkdf2_hmac_sha512(mnemonic_phrase.encode('utf-8'), salt, 2048, 64)
    
    return seed

def main() -> None:
    """Main function to generate a Bitcoin seed from a mnemonic phrase and an optional passphrase."""
    try:
        # Generate a random mnemonic phrase
        mnemonic_phrase = generate_mnemonic()
        print(f'Mnemonic Phrase: {mnemonic_phrase}')
        
        # Optional: Ask user for passphrase
        passphrase = input("Enter an optional passphrase (leave blank for none): ")
        
        # Generate the seed from the mnemonic phrase and passphrase
        seed = mnemonic_to_seed(mnemonic_phrase, passphrase)
        
        # Display the resulting seed in hexadecimal format
        print(f'Seed (hex): {binascii.hexlify(seed).decode("utf-8")}')
        
    except Exception as e:
        print(f'Error: {str(e)}')

if __name__ == "__main__":
    main()
```
