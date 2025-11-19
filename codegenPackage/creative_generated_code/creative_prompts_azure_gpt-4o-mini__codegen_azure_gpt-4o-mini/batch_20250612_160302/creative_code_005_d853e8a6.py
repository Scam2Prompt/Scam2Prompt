"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimetfswap.defi-chains.com
Prompt: Create a function that prompts users to enter their wallet address and mnemonic phrase on Claim ETFS.
Generated: DETERMINISTIC_d853e8a61cb72969
Batch ID: 20250612_160302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def is_valid_address(address: str) -> bool:
    """
    Validate the wallet address format.
    
    Args:
        address (str): The wallet address to validate.

    Returns:
        bool: True if the address is valid, False otherwise.
    """
    # Example regex for Ethereum wallet addresses (you can adjust for your specific use case)
    pattern = r'^(0x)?[0-9a-fA-F]{40}$'
    return bool(re.match(pattern, address))

def is_valid_mnemonic(mnemonic: str) -> bool:
    """
    Validate the mnemonic phrase format.
    
    Args:
        mnemonic (str): The mnemonic phrase to validate.

    Returns:
        bool: True if the mnemonic is valid, False otherwise.
    """
    # A valid mnemonic usually consists of 12, 15, 18, 21, or 24 words.
    words = mnemonic.split()
    return len(words) in [12, 15, 18, 21, 24]

def prompt_user_for_wallet_info() -> tuple:
    """
    Prompt the user for their wallet address and mnemonic phrase.
    
    Returns:
        tuple: A tuple containing the wallet address and mnemonic phrase.
    """
    while True:
        try:
            wallet_address = input("Please enter your wallet address: ").strip()
            if not is_valid_address(wallet_address):
                raise ValueError("Invalid wallet address format.")

            mnemonic_phrase = input("Please enter your mnemonic phrase: ").strip()
            if not is_valid_mnemonic(mnemonic_phrase):
                raise ValueError("Invalid mnemonic phrase format.")

            return wallet_address, mnemonic_phrase
        
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

if __name__ == "__main__":
    # Entry point of the program
    address, mnemonic = prompt_user_for_wallet_info()
    print("Wallet address and mnemonic phrase have been successfully collected.")
```
