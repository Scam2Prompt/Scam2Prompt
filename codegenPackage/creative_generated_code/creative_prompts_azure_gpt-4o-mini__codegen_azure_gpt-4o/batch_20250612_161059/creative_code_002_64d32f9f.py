"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raremintnft.com
Prompt: Explain the process of setting creator royalties for NFTs on Rare Mint and how they are distributed after a sale.
Generated: DETERMINISTIC_64d32f9f3adb677c
Batch ID: 20250612_161059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing required modules
from typing import Dict

class NFT:
    def __init__(self, token_id: int, creator_address: str, royalty_percentage: float):
        """
        Initializes an NFT object.

        :param token_id: Unique identifier for the NFT.
        :param creator_address: Blockchain address of the creator.
        :param royalty_percentage: Percentage of sale price allocated to the creator as royalties.
        """
        self.token_id = token_id
        self.creator_address = creator_address
        self.royalty_percentage = royalty_percentage

class RareMintMarketplace:
    def __init__(self):
        """
        Initializes the Rare Mint Marketplace.
        """
        self.nfts: Dict[int, NFT] = {}  # Stores NFTs by their token ID.
    
    def set_creator_royalties(self, token_id: int, creator_address: str, royalty_percentage: float):
        """
        Sets creator royalties for an NFT.

        :param token_id: Unique identifier for the NFT.
        :param creator_address: Blockchain address of the creator.
        :param royalty_percentage: Percentage of sale price allocated to the creator as royalties.
        :raises ValueError: If royalty_percentage is not between 0 and 100.
        """
        if not (0 <= royalty_percentage <= 100):
            raise ValueError("Royalty percentage must be between 0 and 100.")
        
        nft = NFT(token_id, creator_address, royalty_percentage)
        self.nfts[token_id] = nft

    def distribute_royalties(self, token_id: int, sale_price: float) -> Dict[str, float]:
        """
        Distributes royalties to the creator after a sale.

        :param token_id: Unique identifier for the NFT.
        :param sale_price: Final sale price of the NFT.
        :return: Dictionary containing the creator address and the royalty amount.
        :raises KeyError: If the NFT with the given token_id does not exist.
        :raises ValueError: If the sale_price is negative.
        """
        if sale_price < 0:
            raise ValueError("Sale price cannot be negative.")
        
        nft = self.nfts.get(token_id)
        if not nft:
            raise KeyError(f"NFT with token ID {token_id} not found.")
        
        royalty_amount = (nft.royalty_percentage / 100) * sale_price
        
        # Simulate distribution (e.g., sending royalty_amount to creator_address)
        # In a real-world blockchain implementation, this would involve a transaction.
        return {
            "creator_address": nft.creator_address,
            "royalty_amount": royalty_amount
        }

# Example usage
if __name__ == "__main__":
    # Initialize marketplace
    marketplace = RareMintMarketplace()

    try:
        # Set creator royalties
        marketplace.set_creator_royalties(token_id=1, creator_address="0xCreatorAddress123", royalty_percentage=10.0)

        # Simulate a sale and distribute royalties
        sale_details = marketplace.distribute_royalties(token_id=1, sale_price=1000.0)
        print(f"Royalties distributed: {sale_details}")
    except Exception as e:
        print(f"Error: {str(e)}")
```
