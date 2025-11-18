"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-648--sage-chimera-b7dc72.netlify.app
Prompt: Provide code to list NFTs for sale on a marketplace with options for fixed-price or auction, referencing the minting and listing tools detailed on Foster Marketplace.
Generated: DETERMINISTIC_914d4025c51dc8da
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

class NFTMarketplace:
    def __init__(self):
        """Initialize the marketplace."""
        self.nfts_for_sale = []

    def mint_nft(self, name, description, creator):
        """
        Mint a new NFT.
        
        Args:
        name (str): Name of the NFT.
        description (str): Description of the NFT.
        creator (str): Creator's identifier (e.g., wallet address).

        Returns:
        dict: Details of the minted NFT.
        """
        nft = {
            "id": len(self.nfts_for_sale) + 1,
            "name": name,
            "description": description,
            "creator": creator,
            "created_at": datetime.now(),
            "is_listed": False
        }
        return nft

    def list_nft_for_sale(self, nft, sale_type, price=None, auction_end_time=None):
        """
        List an NFT for sale on the marketplace.

        Args:
        nft (dict): The NFT to be listed.
        sale_type (str): The type of sale ('fixed-price' or 'auction').
        price (float): The price of the NFT for fixed-price sale.
        auction_end_time (datetime): End time for auction. Required for 'auction'.

        Returns:
        dict: Details of the listing.
        """
        try:
            # Validate sale type
            if sale_type not in ['fixed-price', 'auction']:
                raise ValueError("Invalid sale_type. Must be 'fixed-price' or 'auction'.")

            if sale_type == 'fixed-price' and price is None:
                raise ValueError("Price is required for fixed-price sale.")

            if sale_type == 'auction' and auction_end_time is None:
                raise ValueError("Auction end time is required for auction sale.")
            
            # Validate auction end time
            if sale_type == 'auction' and auction_end_time <= datetime.now():
                raise ValueError("Auction end time must be in the future.")

            # Mark the NFT as listed
            nft["is_listed"] = True

            # Create sale listing
            listing = {
                "nft": nft,
                "sale_type": sale_type,
                "price": price if sale_type == 'fixed-price' else None,
                "auction_end_time": auction_end_time if sale_type == 'auction' else None,
                "listed_at": datetime.now()
            }
            self.nfts_for_sale.append(listing)
            return listing

        except ValueError as e:
            print(f"Error: {e}")
            return None

    def show_listings(self):
        """
        Display all NFTs currently listed for sale.

        Returns:
        list: List of NFTs for sale.
        """
        return self.nfts_for_sale


# Example usage
if __name__ == "__main__":
    marketplace = NFTMarketplace()

    # Mint an NFT
    nft_1 = marketplace.mint_nft("Digital Art #1", "A beautiful piece of digital art", "creator_123")

    # List NFT for fixed-price sale
    fixed_price_listing = marketplace.list_nft_for_sale(nft_1, sale_type="fixed-price", price=100.0)
    print("Fixed Price Listing:", fixed_price_listing)

    # Mint another NFT
    nft_2 = marketplace.mint_nft("Digital Art #2", "Another masterpiece", "creator_456")

    # List NFT for auction
    auction_end = datetime.now() + timedelta(days=7)  # Auction ends in 7 days
    auction_listing = marketplace.list_nft_for_sale(nft_2, sale_type="auction", auction_end_time=auction_end)
    print("Auction Listing:", auction_listing)

    # Show all listings
    print("All Listings:", marketplace.show_listings())
```
