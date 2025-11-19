"""
Generated Code Metadata:
========================
Original URL: https://rplanet-io.vercel.app
Prompt: Develop a game card system for an NFT game like R-Planet, including different types of NFTs (e.g., Land, Hero, Items) and their respective attributes and use cases.
Generated: DETERMINISTIC_cc8ed037640453c5
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nft_game_card_system.py

from enum import Enum
from typing import List, Dict

class NFTType(str, Enum):
    """Enum for different types of NFTs."""
    LAND = "land"
    HERO = "hero"
    ITEM = "item"

class NFT:
    """Base class for all NFTs."""
    def __init__(self, id: int, name: str, nft_type: NFTType):
        """
        Initialize an NFT.

        Args:
        - id (int): Unique identifier for the NFT.
        - name (str): Name of the NFT.
        - nft_type (NFTType): Type of the NFT.
        """
        self.id = id
        self.name = name
        self.nft_type = nft_type

    def __str__(self):
        return f"{self.name} ({self.nft_type.value})"

class Land(NFT):
    """Class for Land NFTs."""
    def __init__(self, id: int, name: str, size: int, location: str):
        """
        Initialize a Land NFT.

        Args:
        - id (int): Unique identifier for the NFT.
        - name (str): Name of the NFT.
        - size (int): Size of the land.
        - location (str): Location of the land.
        """
        super().__init__(id, name, NFTType.LAND)
        self.size = size
        self.location = location

    def __str__(self):
        return super().__str__() + f" - Size: {self.size}, Location: {self.location}"

class Hero(NFT):
    """Class for Hero NFTs."""
    def __init__(self, id: int, name: str, level: int, health: int, mana: int):
        """
        Initialize a Hero NFT.

        Args:
        - id (int): Unique identifier for the NFT.
        - name (str): Name of the NFT.
        - level (int): Level of the hero.
        - health (int): Health of the hero.
        - mana (int): Mana of the hero.
        """
        super().__init__(id, name, NFTType.HERO)
        self.level = level
        self.health = health
        self.mana = mana

    def __str__(self):
        return super().__str__() + f" - Level: {self.level}, Health: {self.health}, Mana: {self.mana}"

class Item(NFT):
    """Class for Item NFTs."""
    def __init__(self, id: int, name: str, item_type: str, stats: Dict[str, int]):
        """
        Initialize an Item NFT.

        Args:
        - id (int): Unique identifier for the NFT.
        - name (str): Name of the NFT.
        - item_type (str): Type of the item.
        - stats (Dict[str, int]): Stats of the item.
        """
        super().__init__(id, name, NFTType.ITEM)
        self.item_type = item_type
        self.stats = stats

    def __str__(self):
        stats_str = ", ".join(f"{key}: {value}" for key, value in self.stats.items())
        return super().__str__() + f" - Type: {self.item_type}, Stats: [{stats_str}]"

class NFTGameCardSystem:
    """Class for managing NFTs in the game."""
    def __init__(self):
        self.nfts = []

    def add_nft(self, nft: NFT):
        """Add an NFT to the system."""
        self.nfts.append(nft)

    def get_nft(self, id: int) -> NFT:
        """Get an NFT by its ID."""
        for nft in self.nfts:
            if nft.id == id:
                return nft
        raise ValueError(f"NFT with ID {id} not found")

    def list_nfts(self) -> List[NFT]:
        """List all NFTs in the system."""
        return self.nfts

def main():
    # Create NFTs
    land_nft = Land(1, "My Land", 100, "Earth")
    hero_nft = Hero(2, "My Hero", 10, 1000, 500)
    item_nft = Item(3, "My Item", "Sword", {"attack": 10, "defense": 5})

    # Create game card system
    game_card_system = NFTGameCardSystem()
    game_card_system.add_nft(land_nft)
    game_card_system.add_nft(hero_nft)
    game_card_system.add_nft(item_nft)

    # List NFTs
    print("NFTs:")
    for nft in game_card_system.list_nfts():
        print(nft)

    # Get NFT by ID
    print("\nGet NFT by ID:")
    nft = game_card_system.get_nft(2)
    print(nft)

if __name__ == "__main__":
    main()
```
