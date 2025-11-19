"""
Generated Code Metadata:
========================
Original URL: https://blurnft-blur.github.io
Prompt: Develop a use case for Blur NFTs in the art world, highlighting their potential to democratize access to art and redefine ownership.
Generated: DETERMINISTIC_021ce3a42447b421
Batch ID: 20250622_212302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from typing import Dict, List
from dataclasses import dataclass
from enum import Enum
import hashlib
import json

# Define an Enum for NFT types
class NFTType(Enum):
    """Enum for NFT types"""
    PAINTING = 1
    SCULPTURE = 2
    PHOTOGRAPHY = 3
    DIGITAL_ART = 4

# Define a data class for Artwork
@dataclass
class Artwork:
    """Data class for Artwork"""
    id: str
    title: str
    description: str
    nft_type: NFTType
    owner: str
    price: float

# Define a data class for NFT
@dataclass
class NFT:
    """Data class for NFT"""
    id: str
    artwork: Artwork
    token_id: str
    owner: str

# Define a class for BlurNFT
class BlurNFT:
    """Class for BlurNFT"""
    def __init__(self):
        self.artworks: Dict[str, Artwork] = {}
        self.nfts: Dict[str, NFT] = {}

    def create_artwork(self, artwork: Artwork):
        """Create a new artwork"""
        self.artworks[artwork.id] = artwork

    def create_nft(self, nft: NFT):
        """Create a new NFT"""
        self.nfts[nft.id] = nft

    def get_artwork(self, artwork_id: str) -> Artwork:
        """Get an artwork by ID"""
        return self.artworks.get(artwork_id)

    def get_nft(self, nft_id: str) -> NFT:
        """Get an NFT by ID"""
        return self.nfts.get(nft_id)

    def transfer_nft(self, nft_id: str, new_owner: str):
        """Transfer an NFT to a new owner"""
        nft = self.get_nft(nft_id)
        if nft:
            nft.owner = new_owner
        else:
            raise ValueError("NFT not found")

    def list_nfts(self) -> List[NFT]:
        """List all NFTs"""
        return list(self.nfts.values())

# Define a function to hash artwork metadata
def hash_artwork_metadata(artwork: Artwork) -> str:
    """Hash artwork metadata"""
    metadata = json.dumps({
        "title": artwork.title,
        "description": artwork.description,
        "nft_type": artwork.nft_type.value,
        "owner": artwork.owner,
        "price": artwork.price
    }, sort_keys=True)
    return hashlib.sha256(metadata.encode()).hexdigest()

# Example usage
if __name__ == "__main__":
    blur_nft = BlurNFT()

    # Create artworks
    artwork1 = Artwork(
        id="artwork1",
        title="Example Artwork",
        description="This is an example artwork",
        nft_type=NFTType.PAINTING,
        owner="Artist1",
        price=1000.0
    )
    blur_nft.create_artwork(artwork1)

    # Create NFTs
    nft1 = NFT(
        id="nft1",
        artwork=artwork1,
        token_id="token1",
        owner="Buyer1"
    )
    blur_nft.create_nft(nft1)

    # List NFTs
    nfts = blur_nft.list_nfts()
    for nft in nfts:
        print(f"NFT ID: {nft.id}, Owner: {nft.owner}")

    # Transfer NFT
    blur_nft.transfer_nft(nft1.id, "Buyer2")

    # Get artwork metadata hash
    artwork_hash = hash_artwork_metadata(artwork1)
    print(f"Artwork Hash: {artwork_hash}")
```
