"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-648--sage-chimera-b7dc72.netlify.app
Prompt: Can you provide a code snippet for listing NFTs for auction on Foster Marketplace?
Generated: DETERMINISTIC_f2ec5ffc928afb9e
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Union

# Define a class to represent an NFT
class NFT:
    def __init__(self, nft_id: str, name: str, owner: str):
        """
        Initialize an instance of NFT.

        :param nft_id: Unique identifier for the NFT
        :param name: Human-readable name of the NFT
        :param owner: Owner's address or username
        """
        self.nft_id = nft_id
        self.name = name
        self.owner = owner

    def __repr__(self):
        return f"NFT(id={self.nft_id}, name={self.name}, owner={self.owner})"

# Define a class to represent an auction listing
class AuctionListing:
    def __init__(self, nft: NFT, starting_price: float, end_time: datetime.datetime):
        """
        Initialize an auction listing.

        :param nft: NFT object to be listed for auction
        :param starting_price: Starting price for the auction
        :param end_time: End time for the auction (UTC)
        """
        if starting_price <= 0:
            raise ValueError("Starting price must be greater than zero.")
        if end_time <= datetime.datetime.utcnow():
            raise ValueError("End time must be in the future.")
        
        self.nft = nft
        self.starting_price = starting_price
        self.end_time = end_time

    def __repr__(self):
        return (f"AuctionListing(nft={repr(self.nft)}, starting_price={self.starting_price}, "
                f"end_time={self.end_time.isoformat()})")

# Function to list NFTs for auction
def list_nfts_for_auction(nfts: List[NFT], auction_data: List[Dict[str, Union[float, datetime.datetime]]]) -> List[AuctionListing]:
    """
    List multiple NFTs for auction.

    :param nfts: List of NFTs to be listed
    :param auction_data: List of dictionaries containing auction details (starting_price, end_time)
    :return: List of AuctionListing objects
    """
    if len(nfts) != len(auction_data):
        raise ValueError("Number of NFTs must match number of auction data entries.")

    auction_listings = []
    for nft, data in zip(nfts, auction_data):
        try:
            # Validate auction data
            starting_price = data.get("starting_price")
            end_time = data.get("end_time")
            if starting_price is None or end_time is None:
                raise ValueError("Auction data must include 'starting_price' and 'end_time'.")
            
            # Create an auction listing
            auction_listing = AuctionListing(nft=nft, starting_price=starting_price, end_time=end_time)
            auction_listings.append(auction_listing)
        except Exception as e:
            print(f"Error listing NFT {nft.nft_id}: {e}")
    
    return auction_listings

# Example usage:
if __name__ == "__main__":
    # Create some sample NFTs
    nfts = [
        NFT(nft_id="nft001", name="Golden Dragon", owner="user123"),
        NFT(nft_id="nft002", name="Silver Phoenix", owner="user456"),
    ]

    # Define their respective auction details
    auction_data = [
        {"starting_price": 100.0, "end_time": datetime.datetime.utcnow() + datetime.timedelta(days=3)},
        {"starting_price": 200.0, "end_time": datetime.datetime.utcnow() + datetime.timedelta(days=7)},
    ]

    # List NFTs for auction
    auction_listings = list_nfts_for_auction(nfts, auction_data)

    # Print auction listings
    for listing in auction_listings:
        print(listing)
```
