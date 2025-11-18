"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-phantomwallet.github.io
Prompt: Create a function to generate and validate a seed phrase for wallet recovery, adhering to Phantom Wallet's non-custodial principles.
Generated: DETERMINISTIC_66fc37041112c1b5
Batch ID: 20250612_153725
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


# Constants
WORDLIST_PATH = 'english.txt'  # Path to the BIP-39 wordlist file
WORDLIST = []

# Load BIP-39 wordlist
try:
    with open(WORDLIST_PATH, 'r', encoding='utf-8') as wordlist_file:
        WORDLIST = wordlist_file.read().splitlines()
except FileNotFoundError:
    raise Exception(f"Wordlist file '{WORDLIST_PATH}' not found. Ensure the BIP-39 wordlist is available.")


def generate_seed_phrase(num_words: int = 12) -> str:
    """
    Generate a seed phrase for wallet recovery.

    Args:
        num_words (int): Number of words in the seed phrase (default is 12).

    Returns:
        str: The generated seed phrase.
    """
    if num_words not in [12, 15, 18, 21, 24]:
        raise ValueError("Seed phrase must contain 12, 15, 18, 21, or 24 words.")

    # Generate random entropy
    entropy_bits = num_words * 11  
    entropy = os.urandom(entropy_bits // 8)

    # Hash entropy and calculate checksum
    checksum_bits = len(entropy) * 8 // 32
    checksum = hashlib.sha256(entropy).digest()

    # Combine entropy and checksum
    combined_bits = int.from_bytes(entropy, 'big') << checksum_bits | int.from_bytes(checksum, 'big') >> (256 - checksum_bits)

    # Convert to mnemonic
    mnemonic = []
    for i in range(num_words):
        index = (combined_bits >> (11 * (num_words - i - 1))) & 0x7FF
        mnemonic.append(WORDLIST[index])

    return ' '.join(mnemonic)


def validate_seed_phrase(seed_phrase: str) -> bool:
    """
    Validate a seed phrase to ensure it adheres to BIP-39 standards.

    Args:
        seed_phrase (str): The seed phrase to validate.

    Returns:
        bool: True if the seed phrase is valid, False otherwise.
    """
    words = seed_phrase.split()
    if len(words) not in [12, 15, 18, 21, 24]:
        return False

    # Ensure all words exist in the wordlist
    if not all(word in WORDLIST for word in words):
        return False

    # Recreate entropy and checksum
    indices = [WORDLIST.index(word) for word in words]
    combined_bits = sum(index << (11 * (len(words) - i - 1)) for i, index in enumerate(indices))

    entropy_bits = len(words) * 11 - len(words) * 11 // 33
    entropy = (combined_bits >> (len(words) * 11 - entropy_bits)).to_bytes(entropy_bits // 8, 'big')
    checksum_bits = len(words) * 11 // 33
    checksum = combined_bits & (2**checksum_bits - 1)

    # Validate checksum
    expected_checksum = int.from_bytes(hashlib.sha256(entropy).digest(), 'big') >> (256 - checksum_bits)
    return checksum == expected_checksum


# Example usage
if __name__ == "__main__":
    try:
        seed_phrase = generate_seed_phrase()
        print("Generated Seed Phrase:", seed_phrase)
        is_valid = validate_seed_phrase(seed_phrase)
        print("Is Seed Phrase Valid?:", is_valid)
    except Exception as e:
        print(f"Error: {e}")
```
