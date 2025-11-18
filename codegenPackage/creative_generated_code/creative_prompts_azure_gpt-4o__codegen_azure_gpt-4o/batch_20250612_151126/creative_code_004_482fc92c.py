"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet-core.com
Prompt: Create a function to recover a wallet using a Bip39 mnemonic phrase and the Wallet-Core library.
Generated: DETERMINISTIC_482fc92cc8e480a6
Batch ID: 20250612_151126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import the necessary modules from Wallet-Core
from wallet_core import HDWallet, WalletError

def recover_wallet_from_mnemonic(mnemonic: str, passphrase: str = "") -> HDWallet:
    """
    Recovers a wallet using a Bip39 mnemonic phrase and Wallet-Core library.

    Args:
        mnemonic (str): Bip39 mnemonic phrase.
        passphrase (str): Optional passphrase associated with the mnemonic. Default is an empty string.

    Returns:
        HDWallet: The recovered wallet object.

    Raises:
        ValueError: If the mnemonic is invalid.
        WalletError: If wallet recovery fails due to other issues.
    """
    # Validate input
    if not isinstance(mnemonic, str) or not mnemonic.strip():
        raise ValueError("Mnemonic must be a non-empty string.")

    try:
        # Create a wallet instance using the mnemonic and optional passphrase
        wallet = HDWallet.recover_wallet(mnemonic=mnemonic, passphrase=passphrase)
        
        # Ensure the wallet was successfully created
        if not wallet:
            raise WalletError("Failed to recover wallet. Please check your input.")

        return wallet

    except WalletError as e:
        # Handle Wallet-Core specific errors
        raise WalletError(f"Wallet recovery failed: {str(e)}")
    except Exception as e:
        # Handle unforeseen errors
        raise RuntimeError(f"An unexpected error occurred: {str(e)}")

# Example usage:
# Replace 'your mnemonic phrase here' with your actual Bip39 mnemonic
# mnemonic = "your mnemonic phrase here"
# recovered_wallet = recover_wallet_from_mnemonic(mnemonic)
```
