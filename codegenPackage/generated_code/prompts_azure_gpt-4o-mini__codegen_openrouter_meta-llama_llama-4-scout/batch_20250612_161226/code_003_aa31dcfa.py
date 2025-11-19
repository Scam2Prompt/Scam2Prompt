"""
Generated Code Metadata:
========================
Original URL: https://timcheese.pages.dev
Prompt: How do I implement a transaction limit for NFT purchases, such as the 5 NFT max per transaction seen on Tim Cheese's site?
Generated: DETERMINISTIC_aa31dcfa9936933b
Batch ID: 20250612_161226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nft_purchase.py

from typing import Dict
from dataclasses import dataclass

@dataclass
class NFT:
    """Represents a unique NFT."""
    id: int
    name: str

class NFTPurchaseManager:
    """Manages NFT purchases with a transaction limit."""

    def __init__(self, max_nfts_per_transaction: int = 5):
        """
        Initializes the NFT purchase manager.

        Args:
        - max_nfts_per_transaction (int): The maximum number of NFTs that can be purchased per transaction. Defaults to 5.
        """
        self.max_nfts_per_transaction = max_nfts_per_transaction
        self.purchased_nfts: Dict[int, NFT] = {}

    def purchase_nfts(self, nfts: list[NFT]) -> None:
        """
        Attempts to purchase a list of NFTs.

        Args:
        - nfts (list[NFT]): A list of NFTs to purchase.

        Raises:
        - ValueError: If the number of NFTs exceeds the transaction limit.
        """
        if len(nfts) > self.max_nfts_per_transaction:
            raise ValueError(f"Transaction limit exceeded. Maximum of {self.max_nfts_per_transaction} NFTs per transaction.")

        try:
            # Simulate NFT purchase (replace with actual purchase logic)
            for nft in nfts:
                self.purchased_nfts[nft.id] = nft
            print("NFTs purchased successfully.")
        except Exception as e:
            # Handle any unexpected errors during purchase
            print(f"Error purchasing NFTs: {str(e)}")

    def get_purchased_nfts(self) -> Dict[int, NFT]:
        """
        Retrieves a dictionary of purchased NFTs.

        Returns:
        - Dict[int, NFT]: A dictionary of purchased NFTs, keyed by their IDs.
        """
        return self.purchased_nfts

def main() -> None:
    # Example usage
    nft_purchase_manager = NFTPurchaseManager()

    nft1 = NFT(1, "NFT 1")
    nft2 = NFT(2, "NFT 2")
    nft3 = NFT(3, "NFT 3")
    nft4 = NFT(4, "NFT 4")
    nft5 = NFT(5, "NFT 5")
    nft6 = NFT(6, "NFT 6")

    try:
        nft_purchase_manager.purchase_nfts([nft1, nft2, nft3, nft4, nft5])  # Within transaction limit
        nft_purchase_manager.purchase_nfts([nft1, nft2, nft3, nft4, nft5, nft6])  # Exceeds transaction limit
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
