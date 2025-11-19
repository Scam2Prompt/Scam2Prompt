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
# Import necessary modules
import uuid

class NFT:
    """
    A class representing an individual NFT.
    """
    def __init__(self, name, attributes, owner):
        """
        Initialize an NFT instance.

        :param name: Name of the NFT
        :param attributes: Dictionary of attributes describing the NFT
        :param owner: Owner of the NFT
        """
        self.id = str(uuid.uuid4())  # Unique identifier for the NFT
        self.name = name
        self.attributes = attributes
        self.owner = owner

    def __str__(self):
        """
        String representation of the NFT.
        """
        return f"NFT(ID: {self.id}, Name: {self.name}, Owner: {self.owner}, Attributes: {self.attributes})"


class NFTCollection:
    """
    A class to manage a collection of NFTs.
    """
    def __init__(self):
        """
        Initialize an empty NFT collection.
        """
        self.nfts = {}  # Dictionary to store NFTs with their unique ID as the key

    def add_nft(self, nft):
        """
        Add an NFT to the collection.

        :param nft: An instance of the NFT class
        """
        if nft.id in self.nfts:
            raise ValueError("NFT with this ID already exists in the collection.")
        self.nfts[nft.id] = nft

    def remove_nft(self, nft_id):
        """
        Remove an NFT from the collection by its ID.

        :param nft_id: The unique ID of the NFT to be removed
        """
        if nft_id not in self.nfts:
            raise KeyError("NFT with this ID does not exist in the collection.")
        del self.nfts[nft_id]

    def get_nft(self, nft_id):
        """
        Retrieve an NFT from the collection by its ID.

        :param nft_id: The unique ID of the NFT to be retrieved
        :return: The NFT instance
        """
        if nft_id not in self.nfts:
            raise KeyError("NFT with this ID does not exist in the collection.")
        return self.nfts[nft_id]

    def list_nfts(self):
        """
        List all NFTs in the collection.

        :return: A list of all NFT instances
        """
        return list(self.nfts.values())


# Example usage
if __name__ == "__main__":
    try:
        # Create an NFT collection
        collection = NFTCollection()

        # Create some NFTs
        nft1 = NFT(name="Lil Panda #1", attributes={"color": "black", "hat": "red cap"}, owner="Alice")
        nft2 = NFT(name="Lil Panda #2", attributes={"color": "white", "hat": "blue cap"}, owner="Bob")

        # Add NFTs to the collection
        collection.add_nft(nft1)
        collection.add_nft(nft2)

        # List all NFTs
        print("All NFTs in the collection:")
        for nft in collection.list_nfts():
            print(nft)

        # Retrieve a specific NFT
        print("\nRetrieving NFT with ID:", nft1.id)
        print(collection.get_nft(nft1.id))

        # Remove an NFT
        print("\nRemoving NFT with ID:", nft2.id)
        collection.remove_nft(nft2.id)

        # List all NFTs after removal
        print("\nAll NFTs in the collection after removal:")
        for nft in collection.list_nfts():
            print(nft)

    except Exception as e:
        print(f"Error: {e}")
```
