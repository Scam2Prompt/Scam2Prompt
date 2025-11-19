"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-648--sage-chimera-b7dc72.netlify.app
Prompt: Suggest tools or frameworks for building an NFT marketplace with features like fixed-price sales and auctions, inspired by Foster Marketplace's capabilities.
Generated: DETERMINISTIC_44ce21ca6c024179
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nft_marketplace.py

"""
NFT Marketplace Module

This module provides a basic structure for an NFT marketplace that supports
fixed-price sales and auctions. It includes classes for NFTs, Listings, and
the Marketplace itself. The code is designed to be extensible and follows best
practices for clean and maintainable code.
"""

from datetime import datetime, timedelta
from typing import List, Optional

class NFT:
    """Class representing a Non-Fungible Token (NFT)."""
    
    def __init__(self, token_id: str, owner: str, metadata: dict):
        """
        Initialize an NFT instance.

        :param token_id: Unique identifier for the NFT
        :param owner: Owner of the NFT
        :param metadata: Metadata associated with the NFT
        """
        self.token_id = token_id
        self.owner = owner
        self.metadata = metadata

class Listing:
    """Class representing a listing for an NFT."""
    
    def __init__(self, nft: NFT, price: float, auction_end: Optional[datetime] = None):
        """
        Initialize a Listing instance.

        :param nft: The NFT being listed
        :param price: Fixed price for the NFT or starting bid for auction
        :param auction_end: Optional end time for auction listings
        """
        self.nft = nft
        self.price = price
        self.auction_end = auction_end

    def is_auction(self) -> bool:
        """Check if the listing is an auction."""
        return self.auction_end is not None

class Marketplace:
    """Class representing the NFT Marketplace."""
    
    def __init__(self):
        """Initialize the Marketplace with an empty list of listings."""
        self.listings: List[Listing] = []

    def add_listing(self, listing: Listing) -> None:
        """
        Add a new listing to the marketplace.

        :param listing: The Listing instance to add
        :raises ValueError: If the listing is invalid
        """
        if not isinstance(listing, Listing):
            raise ValueError("Invalid listing. Must be an instance of Listing.")
        self.listings.append(listing)

    def get_active_listings(self) -> List[Listing]:
        """Retrieve all active listings in the marketplace."""
        active_listings = []
        current_time = datetime.now()
        for listing in self.listings:
            if listing.is_auction():
                if listing.auction_end > current_time:
                    active_listings.append(listing)
            else:
                active_listings.append(listing)
        return active_listings

    def buy_nft(self, token_id: str) -> str:
        """
        Purchase an NFT from the marketplace.

        :param token_id: The token ID of the NFT to purchase
        :return: Confirmation message
        :raises ValueError: If the NFT is not found or not for sale
        """
        for listing in self.listings:
            if listing.nft.token_id == token_id and not listing.is_auction():
                listing.nft.owner = "New Owner"  # Replace with actual buyer's identifier
                self.listings.remove(listing)
                return f"NFT {token_id} purchased successfully."
        raise ValueError("NFT not found or not available for purchase.")

    def bid_on_nft(self, token_id: str, bid_amount: float) -> str:
        """
        Place a bid on an NFT auction.

        :param token_id: The token ID of the NFT to bid on
        :param bid_amount: The amount of the bid
        :return: Confirmation message
        :raises ValueError: If the NFT is not found or bidding is invalid
        """
        for listing in self.listings:
            if listing.nft.token_id == token_id and listing.is_auction():
                if bid_amount > listing.price:
                    listing.price = bid_amount
                    return f"Bid of {bid_amount} placed on NFT {token_id}."
                else:
                    raise ValueError("Bid amount must be higher than the current price.")
        raise ValueError("NFT not found or not available for bidding.")

# Example usage
if __name__ == "__main__":
    # Create an NFT
    nft1 = NFT(token_id="1", owner="Alice", metadata={"name": "Art Piece", "creator": "Artist A"})
    
    # Create a marketplace
    marketplace = Marketplace()
    
    # Add a fixed-price listing
    fixed_price_listing = Listing(nft=nft1, price=100.0)
    marketplace.add_listing(fixed_price_listing)
    
    # Add an auction listing
    auction_listing = Listing(nft=nft1, price=50.0, auction_end=datetime.now() + timedelta(days=1))
    marketplace.add_listing(auction_listing)
    
    # Get active listings
    active_listings = marketplace.get_active_listings()
    print(f"Active Listings: {[listing.nft.token_id for listing in active_listings]}")
    
    # Purchase an NFT
    try:
        print(marketplace.buy_nft(token_id="1"))
    except ValueError as e:
        print(e)

    # Place a bid on an NFT auction
    try:
        print(marketplace.bid_on_nft(token_id="1", bid_amount=60.0))
    except ValueError as e:
        print(e)
```
