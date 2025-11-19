"""
Generated Code Metadata:
========================
Original URL: https://bafybeicojev2iwj2ru47t7xqdl7lnbfh734z2kpnoieoo5jd2zqtdelche.ipfs.dweb.link
Prompt: "Write a library for handling NFT ownership in a gaming context, inspired by Planet Mojo's use cases."
Generated: DETERMINISTIC_6bc9fe4101edbfdf
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nft_ownership.py

class NFT:
    """
    A class to represent a Non-Fungible Token (NFT) in a gaming context.
    """

    def __init__(self, token_id: str, owner: str):
        """
        Initializes an NFT instance.

        :param token_id: Unique identifier for the NFT.
        :param owner: The current owner of the NFT.
        """
        self.token_id = token_id
        self.owner = owner

    def transfer_ownership(self, new_owner: str):
        """
        Transfers ownership of the NFT to a new owner.

        :param new_owner: The address of the new owner.
        :raises ValueError: If the new owner is the same as the current owner.
        """
        if new_owner == self.owner:
            raise ValueError("New owner must be different from the current owner.")
        self.owner = new_owner


class NFTMarketplace:
    """
    A class to represent a marketplace for trading NFTs.
    """

    def __init__(self):
        """
        Initializes an empty marketplace.
        """
        self.nfts = {}

    def create_nft(self, token_id: str, owner: str):
        """
        Creates a new NFT and adds it to the marketplace.

        :param token_id: Unique identifier for the NFT.
        :param owner: The current owner of the NFT.
        :raises ValueError: If the NFT with the same token_id already exists.
        """
        if token_id in self.nfts:
            raise ValueError("NFT with this token_id already exists.")
        self.nfts[token_id] = NFT(token_id, owner)

    def transfer_nft(self, token_id: str, new_owner: str):
        """
        Transfers ownership of an NFT in the marketplace.

        :param token_id: Unique identifier for the NFT.
        :param new_owner: The address of the new owner.
        :raises KeyError: If the NFT does not exist in the marketplace.
        :raises ValueError: If the new owner is the same as the current owner.
        """
        if token_id not in self.nfts:
            raise KeyError("NFT not found in the marketplace.")
        
        nft = self.nfts[token_id]
        nft.transfer_ownership(new_owner)

    def get_nft_owner(self, token_id: str) -> str:
        """
        Retrieves the owner of a specific NFT.

        :param token_id: Unique identifier for the NFT.
        :raises KeyError: If the NFT does not exist in the marketplace.
        :return: The owner of the NFT.
        """
        if token_id not in self.nfts:
            raise KeyError("NFT not found in the marketplace.")
        
        return self.nfts[token_id].owner

    def list_nfts(self):
        """
        Lists all NFTs in the marketplace along with their owners.

        :return: A dictionary of token_ids and their respective owners.
        """
        return {token_id: nft.owner for token_id, nft in self.nfts.items()}


# Example usage (commented out for production readiness)
# if __name__ == "__main__":
#     marketplace = NFTMarketplace()
#     marketplace.create_nft("nft1", "owner1")
#     print(marketplace.get_nft_owner("nft1"))  # Output: owner1
#     marketplace.transfer_nft("nft1", "owner2")
#     print(marketplace.get_nft_owner("nft1"))  # Output: owner2
```
