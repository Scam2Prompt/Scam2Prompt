"""
Generated Code Metadata:
========================
Original URL: https://panz-3cy.pages.dev
Prompt: Design a data structure to store and manage a large collection of NFTs, such as the 8,880 lil pandas in Lil Z's Adventure, and provide an example implementation in a programming language.
Generated: DETERMINISTIC_e2845564e29b40f1
Batch ID: 20250622_205627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class NFT:
    """
    A class to represent a Non-Fungible Token (NFT).

    Attributes:
        token_id (int): Unique identifier for the NFT.
        name (str): Name of the NFT.
        metadata (dict): Additional metadata associated with the NFT.
    """

    def __init__(self, token_id: int, name: str, metadata: dict):
        """
        Initializes an NFT instance.

        Args:
            token_id (int): Unique identifier for the NFT.
            name (str): Name of the NFT.
            metadata (dict): Additional metadata associated with the NFT.
        """
        self.token_id = token_id
        self.name = name
        self.metadata = metadata

    def __repr__(self):
        """Return a string representation of the NFT."""
        return f"NFT(token_id={self.token_id}, name='{self.name}', metadata={self.metadata})"


class NFTCollection:
    """
    A class to manage a collection of NFTs.

    Attributes:
        nfts (dict): A dictionary to store NFTs with token_id as the key.
    """

    def __init__(self):
        """Initializes an empty NFT collection."""
        self.nfts = {}

    def add_nft(self, nft: NFT):
        """
        Adds an NFT to the collection.

        Args:
            nft (NFT): The NFT to be added.

        Raises:
            ValueError: If an NFT with the same token_id already exists.
        """
        if nft.token_id in self.nfts:
            raise ValueError(f"NFT with token_id {nft.token_id} already exists.")
        self.nfts[nft.token_id] = nft

    def remove_nft(self, token_id: int):
        """
        Removes an NFT from the collection by its token_id.

        Args:
            token_id (int): The unique identifier of the NFT to be removed.

        Raises:
            KeyError: If no NFT with the given token_id exists.
        """
        if token_id not in self.nfts:
            raise KeyError(f"No NFT found with token_id {token_id}.")
        del self.nfts[token_id]

    def get_nft(self, token_id: int) -> NFT:
        """
        Retrieves an NFT from the collection by its token_id.

        Args:
            token_id (int): The unique identifier of the NFT to retrieve.

        Returns:
            NFT: The NFT associated with the given token_id.

        Raises:
            KeyError: If no NFT with the given token_id exists.
        """
        if token_id not in self.nfts:
            raise KeyError(f"No NFT found with token_id {token_id}.")
        return self.nfts[token_id]

    def list_nfts(self):
        """Returns a list of all NFTs in the collection."""
        return list(self.nfts.values())


# Example usage
if __name__ == "__main__":
    # Create an NFT collection
    collection = NFTCollection()

    # Create some NFTs
    panda1 = NFT(token_id=1, name="Lil Panda #1", metadata={"trait": "happy"})
    panda2 = NFT(token_id=2, name="Lil Panda #2", metadata={"trait": "sad"})

    # Add NFTs to the collection
    collection.add_nft(panda1)
    collection.add_nft(panda2)

    # List all NFTs
    print("Current NFT Collection:")
    for nft in collection.list_nfts():
        print(nft)

    # Retrieve a specific NFT
    try:
        print("Retrieving NFT with token_id 1:")
        print(collection.get_nft(1))
    except KeyError as e:
        print(e)

    # Remove an NFT
    try:
        collection.remove_nft(1)
        print("Removed NFT with token_id 1.")
    except KeyError as e:
        print(e)

    # List all NFTs after removal
    print("NFT Collection after removal:")
    for nft in collection.list_nfts():
        print(nft)
```
