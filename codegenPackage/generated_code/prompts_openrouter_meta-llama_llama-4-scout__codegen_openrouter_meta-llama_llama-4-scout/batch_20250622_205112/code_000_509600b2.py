"""
Generated Code Metadata:
========================
Original URL: https://rplanet-io.vercel.app
Prompt: Write a Python code snippet to create an NFT marketplace for a game like R-Planet, including categories for Land, Hero, Hero's Items, and Artifacts.
Generated: DETERMINISTIC_509600b2546fb116
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nft_marketplace.py

from enum import Enum
from typing import List, Dict

class NFTCategory(str, Enum):
    """NFT categories"""
    LAND = "Land"
    HERO = "Hero"
    HERO_ITEM = "Hero's Items"
    ARTIFACT = "Artifacts"

class NFT:
    """Base NFT class"""
    def __init__(self, id: int, name: str, category: NFTCategory, description: str, price: float):
        """
        Initialize an NFT.

        Args:
        - id (int): Unique identifier
        - name (str): NFT name
        - category (NFTCategory): NFT category
        - description (str): NFT description
        - price (float): NFT price
        """
        self.id = id
        self.name = name
        self.category = category
        self.description = description
        self.price = price

    def __repr__(self):
        return f"NFT(id={self.id}, name='{self.name}', category='{self.category.value}', description='{self.description}', price={self.price})"

class Land(NFT):
    """Land NFT class"""
    def __init__(self, id: int, name: str, description: str, price: float, size: int, location: str):
        """
        Initialize a Land NFT.

        Args:
        - id (int): Unique identifier
        - name (str): NFT name
        - description (str): NFT description
        - price (float): NFT price
        - size (int): Land size
        - location (str): Land location
        """
        super().__init__(id, name, NFTCategory.LAND, description, price)
        self.size = size
        self.location = location

    def __repr__(self):
        return f"Land(id={self.id}, name='{self.name}', description='{self.description}', price={self.price}, size={self.size}, location='{self.location}')"

class Hero(NFT):
    """Hero NFT class"""
    def __init__(self, id: int, name: str, description: str, price: float, level: int, experience: int):
        """
        Initialize a Hero NFT.

        Args:
        - id (int): Unique identifier
        - name (str): NFT name
        - description (str): NFT description
        - price (float): NFT price
        - level (int): Hero level
        - experience (int): Hero experience
        """
        super().__init__(id, name, NFTCategory.HERO, description, price)
        self.level = level
        self.experience = experience

    def __repr__(self):
        return f"Hero(id={self.id}, name='{self.name}', description='{self.description}', price={self.price}, level={self.level}, experience={self.experience})"

class HeroItem(NFT):
    """Hero's Item NFT class"""
    def __init__(self, id: int, name: str, description: str, price: float, item_type: str, stats: Dict[str, int]):
        """
        Initialize a Hero's Item NFT.

        Args:
        - id (int): Unique identifier
        - name (str): NFT name
        - description (str): NFT description
        - price (float): NFT price
        - item_type (str): Item type
        - stats (Dict[str, int]): Item stats
        """
        super().__init__(id, name, NFTCategory.HERO_ITEM, description, price)
        self.item_type = item_type
        self.stats = stats

    def __repr__(self):
        return f"HeroItem(id={self.id}, name='{self.name}', description='{self.description}', price={self.price}, item_type='{self.item_type}', stats={self.stats})"

class Artifact(NFT):
    """Artifact NFT class"""
    def __init__(self, id: int, name: str, description: str, price: float, artifact_type: str, effects: List[str]):
        """
        Initialize an Artifact NFT.

        Args:
        - id (int): Unique identifier
        - name (str): NFT name
        - description (str): NFT description
        - price (float): NFT price
        - artifact_type (str): Artifact type
        - effects (List[str]): Artifact effects
        """
        super().__init__(id, name, NFTCategory.ARTIFACT, description, price)
        self.artifact_type = artifact_type
        self.effects = effects

    def __repr__(self):
        return f"Artifact(id={self.id}, name='{self.name}', description='{self.description}', price={self.price}, artifact_type='{self.artifact_type}', effects={self.effects})"

class NFTMarketplace:
    """NFT marketplace class"""
    def __init__(self):
        self.nfts = []

    def add_nft(self, nft: NFT):
        """Add an NFT to the marketplace"""
        self.nfts.append(nft)

    def remove_nft(self, nft_id: int):
        """Remove an NFT from the marketplace"""
        self.nfts = [nft for nft in self.nfts if nft.id != nft_id]

    def get_nfts(self, category: NFTCategory = None):
        """Get NFTs from the marketplace"""
        if category:
            return [nft for nft in self.nfts if nft.category == category]
        return self.nfts

def main():
    marketplace = NFTMarketplace()

    land = Land(1, "My Land", "This is my land", 1000.0, 10, "R-Planet")
    hero = Hero(2, "My Hero", "This is my hero", 5000.0, 10, 1000)
    hero_item = HeroItem(3, "My Hero's Item", "This is my hero's item", 100.0, "Sword", {"attack": 10, "defense": 5})
    artifact = Artifact(4, "My Artifact", "This is my artifact", 500.0, "Ring", ["+10% attack", "+5% defense"])

    marketplace.add_nft(land)
    marketplace.add_nft(hero)
    marketplace.add_nft(hero_item)
    marketplace.add_nft(artifact)

    print("All NFTs:")
    for nft in marketplace.get_nfts():
        print(nft)

    print("\nLands:")
    for land in marketplace.get_nfts(NFTCategory.LAND):
        print(land)

if __name__ == "__main__":
    main()
```
