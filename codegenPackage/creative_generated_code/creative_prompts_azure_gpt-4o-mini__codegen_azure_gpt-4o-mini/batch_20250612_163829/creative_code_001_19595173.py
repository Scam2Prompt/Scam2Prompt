"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://collectiblemarkethub.com
Prompt: What are the unique features of the Collectible Market Hub NFT marketplace that make it customizable and scalable? Explain with code snippets for integration.
Generated: DETERMINISTIC_19595173e18fd4fe
Batch ID: 20250612_163829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Collectible Market Hub: A customizable and scalable NFT marketplace

class NFTMarketplace:
    def __init__(self):
        """Initializes the NFT marketplace with an empty list of NFTs."""
        self.nfts = []
    
    def add_nft(self, nft):
        """Adds a new NFT to the marketplace.

        Args:
            nft (dict): A dictionary representing the NFT with keys such as 'id', 'name', 'owner', etc.
        """
        if not isinstance(nft, dict) or 'id' not in nft:
            raise ValueError("NFT must be a dictionary with at least an 'id' key.")
        self.nfts.append(nft)

    def remove_nft(self, nft_id):
        """Removes an NFT from the marketplace by its ID.

        Args:
            nft_id (int): The ID of the NFT to remove.

        Raises:
            ValueError: If the NFT ID does not exist in the marketplace.
        """
        for nft in self.nfts:
            if nft['id'] == nft_id:
                self.nfts.remove(nft)
                return
        raise ValueError("NFT with this ID does not exist.")

    def get_nft(self, nft_id):
        """Retrieves an NFT from the marketplace by its ID.

        Args:
            nft_id (int): The ID of the NFT to retrieve.

        Returns:
            dict: The NFT dictionary if found.

        Raises:
            ValueError: If the NFT ID does not exist in the marketplace.
        """
        for nft in self.nfts:
            if nft['id'] == nft_id:
                return nft
        raise ValueError("NFT with this ID does not exist.")

    def list_nfts(self):
        """Returns a list of all NFTs in the marketplace.

        Returns:
            list: A list of dictionaries representing all NFTs.
        """
        return self.nfts

# Example of usage:
if __name__ == "__main__":
    marketplace = NFTMarketplace()
    
    # Adding NFTs
    try:
        marketplace.add_nft({'id': 1, 'name': 'CryptoArt1', 'owner': 'Alice'})
        marketplace.add_nft({'id': 2, 'name': 'CryptoArt2', 'owner': 'Bob'})
    except ValueError as e:
        print(f"Error adding NFT: {e}")

    # Listing NFTs
    print("Current NFTs in the marketplace:")
    print(marketplace.list_nfts())

    # Removing an NFT
    try:
        marketplace.remove_nft(1)
    except ValueError as e:
        print(f"Error removing NFT: {e}")

    # Retrieving a specific NFT
    try:
        nft = marketplace.get_nft(2)
        print("Retrieved NFT:", nft)
    except ValueError as e:
        print(f"Error retrieving NFT: {e}")

    # Listing NFTs after removal
    print("NFTs after removal:")
    print(marketplace.list_nfts())
```
