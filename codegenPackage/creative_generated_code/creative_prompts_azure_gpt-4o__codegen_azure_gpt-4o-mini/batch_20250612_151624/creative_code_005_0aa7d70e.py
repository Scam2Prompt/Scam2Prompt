"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://test.fulviomenegozzo.com
Prompt: Write a function to enforce a limit of 5 NFTs per wallet during a pre-sale event, using the constraints mentioned on the Memeland pre-sale webpage.
Generated: DETERMINISTIC_0aa7d70e98c6b3fe
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class NFTPresale:
    def __init__(self):
        """
        Initialize the NFT Presale with an empty wallet tracking dictionary.
        """
        self.wallets = {}

    def purchase_nft(self, wallet_address):
        """
        Allow a wallet to purchase an NFT during the presale.

        Args:
            wallet_address (str): The address of the wallet attempting to purchase an NFT.

        Raises:
            ValueError: If the wallet address is invalid or if the purchase exceeds the limit.
        """
        # Check for valid wallet address format
        if not self._is_valid_wallet(wallet_address):
            raise ValueError("Invalid wallet address.")

        # Initialize the wallet count if it doesn't exist
        if wallet_address not in self.wallets:
            self.wallets[wallet_address] = 0

        # Check if the wallet has reached the purchase limit
        if self.wallets[wallet_address] >= 5:
            raise ValueError("Wallet has reached the limit of 5 NFTs.")

        # Process the NFT purchase
        self.wallets[wallet_address] += 1
        return f"NFT purchased successfully! Total NFTs for this wallet: {self.wallets[wallet_address]}"

    def _is_valid_wallet(self, wallet_address):
        """
        Validate the wallet address format.

        Args:
            wallet_address (str): The wallet address to validate.

        Returns:
            bool: True if the wallet address is valid, False otherwise.
        """
        # Placeholder for actual wallet validation logic
        return isinstance(wallet_address, str) and len(wallet_address) > 0

    def get_wallet_count(self, wallet_address):
        """
        Get the current count of NFTs held by a wallet.

        Args:
            wallet_address (str): The address of the wallet.

        Returns:
            int: The number of NFTs held by the wallet.
        """
        return self.wallets.get(wallet_address, 0)

# Example usage:
if __name__ == "__main__":
    presale = NFTPresale()
    try:
        print(presale.purchase_nft("0x123456789abcdef"))  # Successful purchase
        print(presale.purchase_nft("0x123456789abcdef"))  # Successful purchase
        print(presale.purchase_nft("0x123456789abcdef"))  # Successful purchase
        print(presale.purchase_nft("0x123456789abcdef"))  # Successful purchase
        print(presale.purchase_nft("0x123456789abcdef"))  # Successful purchase
        print(presale.purchase_nft("0x123456789abcdef"))  # Raises an error
    except ValueError as e:
        print(e)
```
