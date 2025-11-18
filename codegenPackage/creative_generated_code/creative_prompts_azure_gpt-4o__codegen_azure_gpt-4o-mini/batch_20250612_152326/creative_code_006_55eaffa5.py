"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mainnet-nobody.pages.dev
Prompt: Suggest best practices for designing an NFT project man
Generated: DETERMINISTIC_55eaffa50eefc514
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List, Dict

class NFTProject:
    """
    A class to represent an NFT project.

    Attributes:
    ----------
    name : str
        The name of the NFT project.
    description : str
        A brief description of the project.
    creators : List[str]
        A list of creators involved in the project.
    nfts : List[Dict]
        A list of NFTs represented by dictionaries.
    """

    def __init__(self, name: str, description: str, creators: List[str]):
        """
        Initializes the NFTProject instance with a name, description, and creators.

        Parameters:
        ----------
        name : str
            The name of the NFT project.
        description : str
            A brief description of the project.
        creators : List[str]
            A list of creators involved in the project.
        """
        self.name = name
        self.description = description
        self.creators = creators
        self.nfts = []

    def add_nft(self, nft_id: str, nft_metadata: Dict) -> None:
        """
        Adds a new NFT to the project.

        Parameters:
        ----------
        nft_id : str
            The unique identifier for the NFT.
        nft_metadata : Dict
            A dictionary containing metadata for the NFT.

        Raises:
        ------
        ValueError: If the NFT ID already exists in the project.
        """
        if any(nft['id'] == nft_id for nft in self.nfts):
            raise ValueError(f"NFT with ID {nft_id} already exists.")

        nft = {
            'id': nft_id,
            'metadata': nft_metadata
        }
        self.nfts.append(nft)

    def remove_nft(self, nft_id: str) -> None:
        """
        Removes an NFT from the project.

        Parameters:
        ----------
        nft_id : str
            The unique identifier for the NFT to remove.

        Raises:
        ------
        ValueError: If the NFT ID does not exist in the project.
        """
        for nft in self.nfts:
            if nft['id'] == nft_id:
                self.nfts.remove(nft)
                return

        raise ValueError(f"NFT with ID {nft_id} does not exist.")

    def get_nft(self, nft_id: str) -> Dict:
        """
        Retrieves an NFT's metadata by its ID.

        Parameters:
        ----------
        nft_id : str
            The unique identifier for the NFT.

        Returns:
        -------
        Dict
            The metadata of the NFT.

        Raises:
        ------
        ValueError: If the NFT ID does not exist in the project.
        """
        for nft in self.nfts:
            if nft['id'] == nft_id:
                return nft['metadata']

        raise ValueError(f"NFT with ID {nft_id} does not exist.")

    def list_nfts(self) -> List[Dict]:
        """
        Lists all NFTs in the project.

        Returns:
        -------
        List[Dict]
            A list of all NFTs in the project.
        """
        return self.nfts

# Example usage
if __name__ == "__main__":
    try:
        project = NFTProject("Art Collection", "A collection of digital art NFTs.", ["Alice", "Bob"])
        project.add_nft("1", {"title": "Sunset", "artist": "Alice", "year": 2022})
        project.add_nft("2", {"title": "Ocean Waves", "artist": "Bob", "year": 2023})

        print("List of NFTs:")
        print(project.list_nfts())

        print("Get NFT with ID 1:")
        print(project.get_nft("1"))

        project.remove_nft("1")
        print("NFTs after removal:")
        print(project.list_nfts())

    except ValueError as e:
        print(f"Error: {e}")
```
