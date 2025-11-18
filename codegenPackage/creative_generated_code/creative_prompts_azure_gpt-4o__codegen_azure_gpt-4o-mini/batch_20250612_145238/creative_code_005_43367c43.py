"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.chibiheadnft.com
Prompt: Write code to create a "sold-out" indicator for NFTs in a collection, referencing the functionality described for "Chibi Head NFT."
Generated: DETERMINISTIC_43367c4386e7c558
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# nft_collection.py

class NFT:
    """
    A class to represent a Non-Fungible Token (NFT) in a collection.

    Attributes:
        name (str): The name of the NFT.
        id (int): Unique identifier for the NFT.
        is_sold (bool): Indicator of whether the NFT is sold or not.
    """

    def __init__(self, name: str, id: int):
        """
        Initializes an NFT instance.

        Parameters:
            name (str): The name of the NFT.
            id (int): Unique identifier for the NFT.
        """
        self.name = name
        self.id = id
        self.is_sold = False

    def sell(self):
        """
        Mark the NFT as sold.
        """
        if self.is_sold:
            raise ValueError(f"The NFT '{self.name}' (ID: {self.id}) is already sold.")
        self.is_sold = True

    def is_sold_out(self) -> bool:
        """
        Check if the NFT is sold out.

        Returns:
            bool: True if the NFT is sold, False otherwise.
        """
        return self.is_sold


class NFTCollection:
    """
    A class to represent a collection of NFTs.

    Attributes:
        nfts (list): A list to hold NFT instances in the collection.
    """

    def __init__(self):
        """
        Initializes an empty NFT collection.
        """
        self.nfts = []

    def add_nft(self, nft: NFT):
        """
        Add an NFT to the collection.

        Parameters:
            nft (NFT): The NFT instance to be added to the collection.
        """
        if not isinstance(nft, NFT):
            raise TypeError("Expected an instance of NFT.")
        self.nfts.append(nft)

    def check_sold_out(self, nft_id: int) -> bool:
        """
        Check if a specific NFT in the collection is sold out.

        Parameters:
            nft_id (int): The unique identifier of the NFT to check.

        Returns:
            bool: True if the NFT is sold out, False if it exists and is not sold.
            Raises ValueError if the NFT is not found in the collection.
        """
        for nft in self.nfts:
            if nft.id == nft_id:
                return nft.is_sold_out()
        raise ValueError(f"NFT with ID {nft_id} not found in the collection.")

# Example usage
if __name__ == "__main__":
    try:
        # Create a new NFT collection
        collection = NFTCollection()

        # Create and add NFTs to the collection
        chibi_nft1 = NFT("Chibi Head NFT #1", 1)
        collection.add_nft(chibi_nft1)

        chibi_nft2 = NFT("Chibi Head NFT #2", 2)
        collection.add_nft(chibi_nft2)

        # Sell the first NFT
        chibi_nft1.sell()

        # Check if NFTs are sold out
        print(f"Is 'Chibi Head NFT #1' sold out? {collection.check_sold_out(1)}")  # Should return True
        print(f"Is 'Chibi Head NFT #2' sold out? {collection.check_sold_out(2)}")  # Should return False

    except Exception as e:
        print(f"An error occurred: {e}")
```
