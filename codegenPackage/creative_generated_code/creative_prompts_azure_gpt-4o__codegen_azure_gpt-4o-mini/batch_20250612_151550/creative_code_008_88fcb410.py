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
import os
import hashlib
import binascii
import random

class MnemonicGenerator:
    def __init__(self):
        # BIP39 English wordlist
        self.wordlist = self.load_wordlist()

    @staticmethod
    def load_wordlist():
        """Load the BIP39 English wordlist from a text file."""
        with open('bip39_wordlist.txt', 'r') as file:
            return [line.strip() for line in file.readlines()]

    def generate_entropy(self, num_words):
        """Generate entropy based on the number of words needed for the mnemonic."""
        entropy_bits = num_words * 32 // 3  # Each word represents 32 bits of entropy
        entropy = os.urandom(entropy_bits // 8)  # Generate random bytes
        return entropy

    @staticmethod
    def calculate_checksum(entropy):
        """Calculate the checksum for the given entropy."""
        entropy_bits = bin(int.from_bytes(entropy, 'big'))[2:].zfill(len(entropy) * 8)
        hash_ = hashlib.sha256(entropy).hexdigest()
        checksum_length = len(entropy_bits) // 32  # Checksum is 1/32 of entropy length
        checksum_bits = bin(int(hash_, 16))[2:].zfill(256)[:checksum_length]
        return entropy_bits + checksum_bits

    def generate_mnemonic(self, num_words):
        """Generate a mnemonic phrase of the specified number of words."""
        if num_words not in [12, 15, 18, 21, 24]:
            raise ValueError("Number of words must be one of [12, 15, 18, 21, 24]")
        
        entropy = self.generate_entropy(num_words)
        checksum = self.calculate_checksum(entropy)

        # Split the checksum into chunks of 11 bits to map to words
        mnemonic_indices = [int(checksum[i:i+11], 2) for i in range(0, len(checksum), 11)]
        mnemonic_words = [self.wordlist[index] for index in mnemonic_indices]
        
        return ' '.join(mnemonic_words)

    def validate_entropy(self, phrase):
        """Validate the entropy of a given mnemonic phrase."""
        words = phrase.split()
        num_words = len(words)

        # Validate the number of words
        if num_words not in [12, 15, 18, 21, 24]:
            return False

        # Check if all words are in the wordlist
        if any(word not in self.wordlist for word in words):
            return False

        # Reconstruct the entropy and checksum
        mnemonic_indices = [self.wordlist.index(word) for word in words]
        checksum_length = num_words // 3
        checksum_bits = ''.join(f'{index:011b}' for index in mnemonic_indices)

        # Extract checksum and entropy from the bits
        entropy_bits = checksum_bits[:-checksum_length]
        checksum = checksum_bits[-checksum_length:]

        # Validate the checksum
        entropy = int(entropy_bits, 2).to_bytes(len(entropy_bits) // 8, 'big')
        expected_checksum = self.calculate_checksum(entropy)[-checksum_length:]
        
        return expected_checksum == checksum

# Example usage:
if __name__ == '__main__':
    generator = MnemonicGenerator()
    
    try:
        # Generate a 12-word mnemonic
        mnemonic = generator.generate_mnemonic(12)
        print("Generated Mnemonic:", mnemonic)

        # Validate the generated mnemonic
        is_valid = generator.validate_entropy(mnemonic)
        print("Is the mnemonic valid?", is_valid)

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", str(e))
``` 

Make sure to have the BIP39 wordlist saved in a file named `bip39_wordlist.txt` in the same directory as this script for it to work correctly.
