"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bip32.tools
Prompt: Write a Python script to generate a BIP39 mnemonic phrase using entropy values in formats like binary, hex, or dice rolls, as described on https://bip32.tools.
Generated: DETERMINISTIC_1cbc6ca28ce4b893
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import binascii
import hashlib
import random
from typing import List

# Constants for BIP39
WORDLIST_PATH = 'wordlist.txt'  # Path to a file containing BIP39 English wordlist
WORDLIST_SIZE = 2048  # BIP39 wordlist size

def load_wordlist(path: str) -> List[str]:
    """Load the BIP39 wordlist from a file."""
    try:
        with open(path, 'r') as f:
            words = f.read().splitlines()
            if len(words) != WORDLIST_SIZE:
                raise ValueError("Wordlist must contain exactly 2048 words.")
            return words
    except Exception as e:
        raise RuntimeError(f"Error loading wordlist: {e}")

def generate_entropy(size: int) -> bytes:
    """Generate random entropy of a specific byte size."""
    if size not in (16, 20, 24, 28, 32):  # Valid entropy sizes (128, 160, 192, 224, 256 bits)
        raise ValueError("Entropy size must be one of 16, 20, 24, 28, or 32 bytes.")
    return os.urandom(size)

def bytes_to_bin(byte_data: bytes) -> str:
    """Convert bytes to a binary string."""
    return ''.join(f'{byte:08b}' for byte in byte_data)

def add_checksum(entropy: bytes) -> str:
    """Calculate and append checksum to the binary representation of entropy."""
    # Get the SHA256 hash of the entropy
    entropy_hash = hashlib.sha256(entropy).digest()
    
    # Calculate the number of bits for the checksum
    checksum_length = len(entropy) * 8 // 32  # Length in bits (size of entropy in bytes / 4)
    
    # Get the first `checksum_length` bits of the hash as checksum
    checksum = bin(int.from_bytes(entropy_hash, 'big'))[2:].zfill(256)[:checksum_length]
    
    return checksum

def mnemonic_from_entropy(entropy: bytes) -> str:
    """Generate a BIP39 mnemonic from the given entropy."""
    # Convert entropy to binary
    entropy_bin = bytes_to_bin(entropy)
    
    # Add checksum to binary
    checksum = add_checksum(entropy)
    
    # Combine entropy and checksum
    combined = entropy_bin + checksum
    
    # Split into 11-bit chunks
    word_indices = [int(combined[i:i + 11], 2) for i in range(0, len(combined), 11)]
    
    # Load wordlist
    wordlist = load_wordlist(WORDLIST_PATH)

    # Create mnemonic by selecting words from wordlist
    mnemonic = ' '.join(wordlist[index] for index in word_indices)
    
    return mnemonic

def main():
    """Main function to generate a BIP39 mnemonic phrase."""
    try:
        # Generate entropy of 16 bytes (128 bits)
        entropy = generate_entropy(16)
        
        # Get the mnemonic phrase
        mnemonic_phrase = mnemonic_from_entropy(entropy)
        
        # Output the mnemonic phrase
        print("Generated BIP39 Mnemonic Phrase:")
        print(mnemonic_phrase)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

### Note:
- Ensure that the `wordlist.txt` file, containing the BIP39 English wordlist (2048 words), is available in the same directory as this script. You can find the wordlist online or generate it as required.
