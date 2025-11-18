"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://evmdappxis-protocol.vercel.app
Prompt: Generate code to import a crypto wallet using a 12/18/24-word recovery phrase, as outlined in the Token DApps platform.
Generated: DETERMINISTIC_f896eff85f0da139
Batch ID: 20250612_154703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bip39
import bip32utils
from web3 import Web3

class CryptoWallet:
    def __init__(self, recovery_phrase: str):
        """
        Initializes the CryptoWallet instance with a recovery phrase.

        Args:
            recovery_phrase (str): A 12, 18, or 24-word recovery phrase.
        """
        if not self.validate_recovery_phrase(recovery_phrase):
            raise ValueError("Invalid recovery phrase. Must be 12, 18, or 24 words.")
        
        self.recovery_phrase = recovery_phrase
        self.seed = bip39.BIP39Key.from_mnemonic(recovery_phrase).to_seed()
        self.root_key = bip32utils.BIP32Key.fromEntropy(self.seed)

    @staticmethod
    def validate_recovery_phrase(recovery_phrase: str) -> bool:
        """
        Validates the recovery phrase for correct word count.

        Args:
            recovery_phrase (str): The recovery phrase to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        words = recovery_phrase.strip().split()
        return len(words) in {12, 18, 24}

    def get_address(self, index: int = 0) -> str:
        """
        Derives the wallet address from the recovery phrase.

        Args:
            index (int): The index of the address in the derivation path.

        Returns:
            str: The derived Ethereum address.
        """
        try:
            # BIP32 derivation path for Ethereum
            path = f"m/44'/60'/0'/0/{index}"
            child_key = self.root_key.ChildKey(int(path.split("'")[2][:-1]))
            address = child_key.Address()
            return address
        except Exception as e:
            raise RuntimeError(f"Error deriving address: {str(e)}")

def main():
    # Example use case
    recovery_phrase = "your 12 or 18 or 24 word recovery phrase goes here"
    try:
        wallet = CryptoWallet(recovery_phrase)
        address = wallet.get_address()
        print(f"Derived address: {address}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
