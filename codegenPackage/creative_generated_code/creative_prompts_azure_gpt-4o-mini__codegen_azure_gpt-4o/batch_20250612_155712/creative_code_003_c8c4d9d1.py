"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://looks-rare.com
Prompt: Explain how Looks-Rare supports artists in creating income streams through blockchain technology.
Generated: DETERMINISTIC_c8c4d9d1047f4385
Batch ID: 20250612_155712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to simulate how LooksRare supports artists in creating income streams through blockchain technology.
This example showcases a smart contract-like implementation where artists can mint NFTs and receive royalties
from secondary sales. It is a simplified Python representation meant to demonstrate the core concepts.

Note: Blockchain functionality typically requires specialized frameworks like Solidity for Ethereum,
but this Python example provides a conceptual overview.
"""

class NFTMarketplace:
    """
    A simplified NFT Marketplace that supports minting NFTs and tracking sales with royalties for artists.
    """

    def __init__(self):
        # Initialize the marketplace with empty data structures for NFTs and sales
        self.nfts = {}             # Stores NFT data (artist address, price, royalties)
        self.sales_history = []    # Tracks all NFT sales
        self.artist_earnings = {}  # Tracks earnings for each artist

    def mint_nft(self, artist_address, price, royalty_percentage):
        """
        Mint a new NFT and add it to the marketplace.

        :param artist_address: Address of the artist (string)
        :param price: Initial price of the NFT (float)
        :param royalty_percentage: Percentage of royalties the artist earns from secondary sales (float, e.g., 10 for 10%)
        :return: NFT ID (integer)
        """
        try:
            # Validate inputs
            if price <= 0 or not (0 <= royalty_percentage <= 100):
                raise ValueError("Invalid price or royalty percentage.")

            # Create a unique NFT ID
            nft_id = len(self.nfts) + 1

            # Store NFT data
            self.nfts[nft_id] = {
                "artist_address": artist_address,
                "price": price,
                "royalty_percentage": royalty_percentage
            }

            # Initialize artist earnings if not already tracked
            if artist_address not in self.artist_earnings:
                self.artist_earnings[artist_address] = 0.0

            print(f"NFT with ID {nft_id} minted successfully by artist {artist_address}.")
            return nft_id
        except Exception as error:
            print(f"Error minting NFT: {error}")
            return None

    def buy_nft(self, nft_id, buyer_address):
        """
        Simulate buying an NFT. Tracks royalties for the artist.

        :param nft_id: ID of the NFT being purchased (integer)
        :param buyer_address: Address of the buyer (string)
        :return: None
        """
        try:
            # Ensure the NFT exists
            if nft_id not in self.nfts:
                raise ValueError("NFT does not exist.")

            # Retrieve NFT data
            nft_data = self.nfts[nft_id]
            artist_address = nft_data["artist_address"]
            price = nft_data["price"]
            royalty_percentage = nft_data["royalty_percentage"]

            # Calculate royalties for the artist
            royalty_amount = (price * royalty_percentage) / 100.0
            self.artist_earnings[artist_address] += royalty_amount

            # Log the sale
            self.sales_history.append({
                "nft_id": nft_id,
                "buyer_address": buyer_address,
                "price": price,
                "royalty_amount": royalty_amount
            })

            print(f"NFT with ID {nft_id} purchased by {buyer_address}.")
            print(f"Artist {artist_address} earned {royalty_amount:.2f} in royalties.")
        except Exception as error:
            print(f"Error buying NFT: {error}")

    def get_artist_earnings(self, artist_address):
        """
        Retrieve the total earnings of an artist.

        :param artist_address: Address of the artist (string)
        :return: Total earnings (float)
        """
        try:
            return self.artist_earnings.get(artist_address, 0.0)
        except Exception as error:
            print(f"Error retrieving artist earnings: {error}")
            return 0.0


# Example usage
if __name__ == "__main__":
    # Create an instance of the marketplace
    marketplace = NFTMarketplace()

    # Mint NFTs
    nft_id_1 = marketplace.mint_nft("artist_1", price=100.0, royalty_percentage=10.0)
    nft_id_2 = marketplace.mint_nft("artist_2", price=200.0, royalty_percentage=15.0)

    # Buy NFTs
    marketplace.buy_nft(nft_id_1, "buyer_1")
    marketplace.buy_nft(nft_id_2, "buyer_2")

    # Retrieve artist earnings
    earnings_artist_1 = marketplace.get_artist_earnings("artist_1")
    earnings_artist_2 = marketplace.get_artist_earnings("artist_2")

    print(f"Artist 1 total earnings: {earnings_artist_1:.2f}")
    print(f"Artist 2 total earnings: {earnings_artist_2:.2f}")
```
