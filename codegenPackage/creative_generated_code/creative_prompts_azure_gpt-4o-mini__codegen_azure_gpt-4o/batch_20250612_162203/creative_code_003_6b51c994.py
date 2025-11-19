"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-dappfixs-2wk.pages.dev
Prompt: Generate a function to handle NFT minting and transferring based on the Multiverse Deep Sync documentation.
Generated: DETERMINISTIC_6b51c994a417cf09
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import uuid


class NFT:
    """
    A class representing an NFT (Non-Fungible Token).
    """

    def __init__(self, name, metadata):
        """
        Initializes an NFT instance.

        :param name: Name of the NFT
        :param metadata: Metadata associated with the NFT
        """
        self.id = self.generate_unique_id()
        self.name = name
        self.metadata = metadata
        self.owner = None  # Initially, NFT has no owner

    @staticmethod
    def generate_unique_id():
        """
        Generates a unique ID for the NFT using UUID.

        :return: Unique NFT ID
        """
        return hashlib.sha256(uuid.uuid4().hex.encode()).hexdigest()


class NFTMarketplace:
    """
    A class to handle NFT minting and transferring on a marketplace platform.
    """

    def __init__(self):
        """
        Initializes the NFT Marketplace instance.
        """
        self.nfts = {}  # Storage for all minted NFTs

    def mint_nft(self, name, metadata, owner_address):
        """
        Mints an NFT and assigns it to the specified owner.

        :param name: Name of the NFT
        :param metadata: Metadata associated with the NFT
        :param owner_address: Address of the initial owner
        :return: Minted NFT object
        """
        if not name or not metadata or not owner_address:
            raise ValueError("Invalid input: Name, metadata, and owner address are required.")

        nft = NFT(name, metadata)
        nft.owner = owner_address
        self.nfts[nft.id] = nft  # Store NFT by its unique ID
        return nft

    def transfer_nft(self, nft_id, new_owner_address):
        """
        Transfers an NFT to a new owner.

        :param nft_id: ID of the NFT to be transferred
        :param new_owner_address: Address of the new owner
        :return: Updated NFT object
        """
        if nft_id not in self.nfts:
            raise ValueError(f"NFT with ID {nft_id} does not exist.")

        if not new_owner_address:
            raise ValueError("Invalid input: New owner address is required.")

        nft = self.nfts[nft_id]
        nft.owner = new_owner_address
        return nft


# Example usage of the NFTMarketplace class
if __name__ == "__main__":
    try:
        # Initialize the marketplace
        marketplace = NFTMarketplace()

        # Mint an NFT
        minted_nft = marketplace.mint_nft(
            name="Multiverse Deep Sync Collectible",
            metadata={"description": "Unique collectible item in the multiverse."},
            owner_address="owner_123"
        )
        print(f"Minted NFT: {minted_nft.id}, Owner: {minted_nft.owner}")

        # Transfer the NFT
        transferred_nft = marketplace.transfer_nft(
            nft_id=minted_nft.id,
            new_owner_address="owner_456"
        )
        print(f"Transferred NFT: {transferred_nft.id}, New Owner: {transferred_nft.owner}")

    except ValueError as e:
        print(f"Error: {e}")
```
