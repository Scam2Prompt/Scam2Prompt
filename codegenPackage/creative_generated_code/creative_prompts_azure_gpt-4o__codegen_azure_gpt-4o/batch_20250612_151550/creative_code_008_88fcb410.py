"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bip32.net
Prompt: Create a Python function to generate mnemonic phrases of varying lengths (12, 15, 18, 21, 24 words) and validate their entropy, based on the BIP39 standard.
Generated: DETERMINISTIC_88fcb41061ab0e97
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
import unicodedata
from typing import List

# BIP39 Word List (2048 words)
# For simplicity, a small sample list is used here. Replace with the full BIP39 word list in production.
BIP39_WORD_LIST = [
    "abandon", "ability", "able", "about", "above", "absent", "absorb", "abstract", "absurd", "abuse",
    # Add the full list of 2048 words here...
]

def generate_mnemonic(word_count: int) -> str:
    """
    Generate a BIP39 mnemonic phrase of specified word count.

    Args:
        word_count (int): Number of words in the mnemonic (12, 15, 18, 21, 24 are valid).

    Returns:
        str: Generated mnemonic phrase.

    Raises:
        ValueError: If word_count is invalid.
    """
    # Validate word count
    if word_count not in [12, 15, 18, 21, 24]:
        raise ValueError("Invalid word count. Choose one of 12, 15, 18, 21, or 24.")

    # Calculate entropy size (128 to 256 bits in increments of 32 bits)
    entropy_bits = (word_count * 32) // 3
    entropy_bytes = entropy_bits // 8

    # Generate entropy
    entropy = os.urandom(entropy_bytes)

    # Calculate checksum
    checksum_bits = entropy_bits // 32
    checksum = hashlib.sha256(entropy).digest()
    checksum_bin = bin(int.from_bytes(checksum, "big"))[2:].zfill(256)[:checksum_bits]

    # Convert entropy to binary and append checksum
    entropy_bin = bin(int.from_bytes(entropy, "big"))[2:].zfill(entropy_bits)
    full_binary = entropy_bin + checksum_bin

    # Split binary into 11-bit segments and map to word list
    words = []
    for i in range(0, len(full_binary), 11):
        index = int(full_binary[i:i+11], 2)
        words.append(BIP39_WORD_LIST[index])

    return " ".join(words)

def validate_mnemonic(mnemonic: str) -> bool:
    """
    Validate a BIP39 mnemonic phrase.

    Args:
        mnemonic (str): Mnemonic phrase to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    # Convert mnemonic phrase to binary
    words = mnemonic.split()
    if len(words) not in [12, 15, 18, 21, 24]:
        return False

    try:
        binary_string = ""
        for word in words:
            index = BIP39_WORD_LIST.index(word)
            binary_string += bin(index)[2:].zfill(11)
    except ValueError:
        return False  # Word not found in BIP39 list

    # Split binary string into entropy and checksum
    checksum_bits = len(words) // 3
    entropy_bin = binary_string[:-checksum_bits]
    checksum_bin = binary_string[-checksum_bits:]

    # Compute entropy and checksum
    entropy_bytes = int(entropy_bin, 2).to_bytes(len(entropy_bin) // 8, byteorder="big")
    calculated_checksum = hashlib.sha256(entropy_bytes).digest()
    calculated_checksum_bin = bin(int.from_bytes(calculated_checksum, "big"))[2:].zfill(256)[:checksum_bits]

    return checksum_bin == calculated_checksum_bin

# Example usage
if __name__ == "__main__":
    try:
        # Generate a 12-word mnemonic
        mnemonic = generate_mnemonic(12)
        print("Generated Mnemonic:", mnemonic)

        # Validate the mnemonic
        is_valid = validate_mnemonic(mnemonic)
        print("Is Mnemonic Valid?", is_valid)
    except Exception as e:
        print(f"Error: {e}")
```
