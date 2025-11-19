"""
Generated Code Metadata:
========================
Original URL: https://bip32.net
Prompt: Create a Python function to generate mnemonic phrases of varying lengths (12, 15, 18, 21, 24 words) and validate their entropy, based on the BIP39 standard.
Generated: DETERMINISTIC_88fcb41061ab0e97
Batch ID: 20250612_151550
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
import os
import secrets
from typing import List, Optional, Tuple

# BIP39 wordlist - English
with open('english.txt', 'r') as f:
    WORDLIST = [word.strip() for word in f.readlines()]

def generate_entropy(strength: int = 128) -> bytes:
    """
    Generate cryptographically secure entropy bytes.
    Strength must be a multiple of 32 between 128-256 bits.
    """
    if strength not in [128, 160, 192, 224, 256]:
        raise ValueError("Strength should be one of: 128, 160, 192, 224, 256")
    return secrets.token_bytes(strength // 8)

def entropy_to_mnemonic(entropy: bytes) -> str:
    """
    Convert entropy bytes to mnemonic phrase using BIP39 standard.
    """
    if len(entropy) not in [16, 20, 24, 28, 32]:
        raise ValueError("Entropy length should be one of: 16, 20, 24, 28, 32 bytes")

    entropy_bits = int.from_bytes(entropy, 'big')
    checksum_bits = calculate_checksum_bits(entropy)
    
    # Combine entropy and checksum
    total_bits = (len(entropy) * 8) + (len(entropy) * 8 // 32)
    combined = (entropy_bits << (total_bits - len(entropy) * 8)) | checksum_bits
    
    # Split into 11-bit chunks
    mnemonic = []
    for i in range(total_bits // 11):
        index = (combined >> (total_bits - (i + 1) * 11)) & 0x7FF
        mnemonic.append(WORDLIST[index])
    
    return ' '.join(mnemonic)

def calculate_checksum_bits(entropy: bytes) -> int:
    """
    Calculate checksum bits from entropy as per BIP39.
    """
    checksum_length = len(entropy) * 8 // 32
    hash_bytes = hashlib.sha256(entropy).digest()
    hash_int = int.from_bytes(hash_bytes, 'big')
    checksum = hash_int >> (256 - checksum_length)
    return checksum

def mnemonic_to_entropy(mnemonic: str) -> bytes:
    """
    Convert mnemonic phrase back to entropy bytes.
    """
    words = mnemonic.split()
    if len(words) not in [12, 15, 18, 21, 24]:
        raise ValueError("Mnemonic phrase must be 12, 15, 18, 21, or 24 words long")

    # Convert words back to indices
    indices = [WORDLIST.index(word) for word in words]
    
    # Reconstruct combined bits
    total_bits = len(words) * 11
    combined = 0
    for i, index in enumerate(indices):
        combined = (combined << 11) | index
    
    # Split into entropy and checksum
    checksum_length = total_bits // 33
    entropy_length = total_bits - checksum_length
    
    entropy = combined >> checksum_length
    checksum = combined & ((1 << checksum_length) - 1)
    
    # Convert entropy to bytes
    entropy_bytes = entropy.to_bytes(entropy_length // 8, 'big')
    
    # Verify checksum
    calculated_checksum = calculate_checksum_bits(entropy_bytes)
    if checksum != calculated_checksum:
        raise ValueError("Invalid mnemonic checksum")
    
    return entropy_bytes

def validate_mnemonic(mnemonic: str) -> bool:
    """
    Validate a mnemonic phrase by checking its checksum.
    """
    try:
        mnemonic_to_entropy(mnemonic)
        return True
    except (ValueError, IndexError):
        return False

def generate_mnemonic(strength: int = 128) -> str:
    """
    Generate a BIP39 compliant mnemonic phrase.
    Strength determines the number of words:
    128 -> 12 words, 160 -> 15 words, 192 -> 18 words,
    224 -> 21 words, 256 -> 24 words
    """
    if strength not in [128, 160, 192, 224, 256]:
        raise ValueError("Strength should be one of: 128, 160, 192, 224, 256")
    
    entropy = generate_entropy(strength)
    return entropy_to_mnemonic(entropy)

def main():
    # Example usage
    print("12-word mnemonic:", generate_mnemonic(128))
    print("15-word mnemonic:", generate_mnemonic(160))
    print("18-word mnemonic:", generate_mnemonic(192))
    print("21-word mnemonic:", generate_mnemonic(224))
    print("24-word mnemonic:", generate_mnemonic(256))
    
    # Validation example
    mnemonic = generate_mnemonic(128)
    print(f"Validating mnemonic '{mnemonic}':", validate_mnemonic(mnemonic))

if __name__ == "__main__":
    main()
```
