"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet-core.com
Prompt: Create an automated script using the Wallet-Core library to verify wallet version compatibility with Bip39 recovery phrases.
Generated: DETERMINISTIC_80d17adcfe42fa00
Batch ID: 20250612_151126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys
from wallet import Wallet
from bip39 import BIP39

def verify_wallet_version_compatibility(mnemonic_phrase, expected_version):
    """
    Verify if the wallet created from the given BIP39 mnemonic phrase is compatible
    with the expected wallet version.

    Args:
        mnemonic_phrase (str): The BIP39 mnemonic recovery phrase.
        expected_version (str): The expected version of the wallet.

    Returns:
        bool: True if compatible, False otherwise.

    Raises:
        ValueError: If the mnemonic phrase is invalid or incompatible.
    """
    try:
        # Create a BIP39 instance
        bip39 = BIP39(mnemonic_phrase)
        
        # Generate a wallet from the mnemonic
        wallet = Wallet.from_bip39(bip39)
        
        # Check version compatibility
        actual_version = wallet.get_version()
        
        if actual_version != expected_version:
            raise ValueError(f"Incompatible wallet version: expected {expected_version}, got {actual_version}")

        return True

    except ValueError as ve:
        print(f"ValueError: {ve}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    # Example usage
    if len(sys.argv) != 3:
        print("Usage: python verify_wallet.py <mnemonic_phrase> <expected_version>")
        sys.exit(1)

    mnemonic = sys.argv[1]
    expected_version = sys.argv[2]

    is_compatible = verify_wallet_version_compatibility(mnemonic, expected_version)
    
    if is_compatible:
        print("The wallet is compatible with the expected version.")
    else:
        print("The wallet is NOT compatible with the expected version.")
```
