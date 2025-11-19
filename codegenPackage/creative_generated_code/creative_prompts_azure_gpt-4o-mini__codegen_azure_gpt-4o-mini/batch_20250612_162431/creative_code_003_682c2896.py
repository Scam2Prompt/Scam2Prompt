"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superrare.fr
Prompt: Describe the differences between NFTs and cryptocurrencies, referencing the unique characteristics highlighted on SuperRare.fr.
Generated: DETERMINISTIC_682c28967dddae35
Batch ID: 20250612_162431
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DigitalAsset:
    """A base class representing a digital asset."""

    def __init__(self, asset_id, owner):
        """
        Initialize a digital asset.

        :param asset_id: Unique identifier for the asset
        :param owner: Owner of the asset
        """
        self.asset_id = asset_id
        self.owner = owner


class NFT(DigitalAsset):
    """Class representing a Non-Fungible Token (NFT)."""

    def __init__(self, asset_id, owner, metadata):
        """
        Initialize an NFT.

        :param asset_id: Unique identifier for the NFT
        :param owner: Owner of the NFT
        :param metadata: Metadata associated with the NFT (e.g., title, description, image)
        """
        super().__init__(asset_id, owner)
        self.metadata = metadata

    def __str__(self):
        """Return a string representation of the NFT."""
        return f"NFT(ID: {self.asset_id}, Owner: {self.owner}, Metadata: {self.metadata})"


class Cryptocurrency(DigitalAsset):
    """Class representing a Cryptocurrency."""

    def __init__(self, asset_id, owner, amount):
        """
        Initialize a Cryptocurrency.

        :param asset_id: Unique identifier for the cryptocurrency
        :param owner: Owner of the cryptocurrency
        :param amount: Amount of cryptocurrency owned
        """
        super().__init__(asset_id, owner)
        self.amount = amount

    def __str__(self):
        """Return a string representation of the Cryptocurrency."""
        return f"Cryptocurrency(ID: {self.asset_id}, Owner: {self.owner}, Amount: {self.amount})"


def main():
    """Main function to demonstrate the differences between NFTs and Cryptocurrencies."""
    try:
        # Create an NFT instance
        nft = NFT(asset_id="1", owner="user123", metadata={"title": "Digital Art", "artist": "Artist A"})
        print(nft)

        # Create a Cryptocurrency instance
        crypto = Cryptocurrency(asset_id="2", owner="user123", amount=100.5)
        print(crypto)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
