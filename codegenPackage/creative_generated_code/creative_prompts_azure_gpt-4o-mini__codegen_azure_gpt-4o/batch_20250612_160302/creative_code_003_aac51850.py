"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bip32.tools
Prompt: Explain how to use the entropy feature on bip32.tools to create a secure recovery phrase.
Generated: DETERMINISTIC_aac518501dff8682
Batch ID: 20250612_160302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to generate a secure recovery phrase using entropy
and the BIP-39 standard. It uses the `bip_utils` library for key management 
and follows best practices for securely generating mnemonic phrases.
"""

import os
from bip_utils import Bip39MnemonicGenerator, Bip39EntropyGenerator

def generate_secure_recovery_phrase():
    """
    Generates a secure recovery phrase using high-quality entropy.
    Returns:
        str: The generated recovery phrase (mnemonic).
    """
    try:
        # Generate 256 bits (32 bytes) of entropy for maximum security
        # The entropy is derived from the OS's cryptographic random generator
        entropy_bytes = os.urandom(32)

        # Convert the entropy into a BIP-39 mnemonic phrase
        mnemonic = Bip39MnemonicGenerator.FromEntropy(entropy_bytes)

        return mnemonic
    except Exception as e:
        # Handle any unexpected errors during mnemonic generation
        print(f"An error occurred while generating the recovery phrase: {e}")
        return None

if __name__ == "__main__":
    # Generate and print the recovery phrase
    recovery_phrase = generate_secure_recovery_phrase()
    if recovery_phrase:
        print("Secure Recovery Phrase:")
        print(recovery_phrase)
    else:
        print("Failed to generate the recovery phrase.")
```
