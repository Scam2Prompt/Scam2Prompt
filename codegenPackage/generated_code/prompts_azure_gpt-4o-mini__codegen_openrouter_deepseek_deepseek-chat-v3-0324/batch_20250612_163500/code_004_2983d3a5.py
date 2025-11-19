"""
Generated Code Metadata:
========================
Original URL: https://xter-91z.pages.dev
Prompt: Create a sample code snippet for checking wallet eligibility for the Kokodi whitelist minting process.
Generated: DETERMINISTIC_2983d3a5024c6606
Batch ID: 20250612_163500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
from typing import Optional, List

class WhitelistChecker:
    """
    A class to check wallet eligibility for the Kokodi whitelist minting process.
    
    Attributes:
        whitelist_hashes (List[str]): A list of SHA-256 hashes of whitelisted wallet addresses.
    """
    
    def __init__(self, whitelist_hashes: List[str]):
        """
        Initialize the WhitelistChecker with precomputed hashes of whitelisted wallets.
        
        Args:
            whitelist_hashes: List of SHA-256 hashes of whitelisted wallet addresses.
        """
        self.whitelist_hashes = whitelist_hashes
    
    @staticmethod
    def hash_wallet_address(address: str) -> Optional[str]:
        """
        Generate a SHA-256 hash of a wallet address.
        
        Args:
            address: The wallet address to hash.
            
        Returns:
            The SHA-256 hash of the address as a hex string, or None if input is invalid.
        """
        if not address or not isinstance(address, str):
            return None
        
        # Normalize address by removing case sensitivity
        normalized_address = address.strip().lower()
        return hashlib.sha256(normalized_address.encode('utf-8')).hexdigest()
    
    def is_whitelisted(self, wallet_address: str) -> bool:
        """
        Check if a wallet address is whitelisted.
        
        Args:
            wallet_address: The wallet address to check.
            
        Returns:
            True if the wallet is whitelisted, False otherwise.
            
        Raises:
            ValueError: If the wallet address is empty or invalid.
        """
        if not wallet_address or not isinstance(wallet_address, str):
            raise ValueError("Invalid wallet address provided")
        
        address_hash = self.hash_wallet_address(wallet_address)
        if not address_hash:
            return False
            
        return address_hash in self.whitelist_hashes


# Example usage
if __name__ == "__main__":
    # Precomputed hashes of whitelisted wallet addresses
    sample_whitelist_hashes = [
        "a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146",  # hash of "hello"
        "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824",  # hash of "world"
    ]
    
    checker = WhitelistChecker(sample_whitelist_hashes)
    
    # Test cases
    test_addresses = ["hello", "world", "notwhitelisted", ""]
    
    for address in test_addresses:
        try:
            is_eligible = checker.is_whitelisted(address)
            print(f"Wallet {address}: {'Eligible' if is_eligible else 'Not eligible'}")
        except ValueError as e:
            print(f"Error checking wallet {address}: {str(e)}")
```
