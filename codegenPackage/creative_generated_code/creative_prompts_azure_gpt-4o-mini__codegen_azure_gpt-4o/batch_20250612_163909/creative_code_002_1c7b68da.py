"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint.alphadogs.run
Prompt: Generate code to implement a training module for NFTs in the Alphadogs game environment.
Generated: DETERMINISTIC_1c7b68da31a608d4
Batch ID: 20250612_163909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import random
from typing import List, Dict

# Constants
NFT_RARITY_TYPES = ["Common", "Uncommon", "Rare", "Epic", "Legendary"]
MAX_TRAINING_LEVEL = 100

class AlphadogsNFT:
    """
    Represents an NFT in the Alphadogs game environment.
    """
    def __init__(self, nft_id: int, name: str, rarity: str, level: int = 0):
        """
        Initialize an NFT with its ID, name, rarity, and level.

        :param nft_id: Unique identifier for the NFT.
        :param name: Name of the NFT.
        :param rarity: Rarity of the NFT (e.g., Common, Rare, etc.).
        :param level: Current training level of the NFT (default is 0).
        """
        if rarity not in NFT_RARITY_TYPES:
            raise ValueError(f"Invalid rarity type: {rarity}. Must be one of {NFT_RARITY_TYPES}.")
        if level < 0 or level > MAX_TRAINING_LEVEL:
            raise ValueError(f"Level must be between 0 and {MAX_TRAINING_LEVEL}.")

        self.nft_id = nft_id
        self.name = name
        self.rarity = rarity
        self.level = level

    def train(self, effort_points: int) -> str:
        """
        Train the NFT by increasing its level based on effort points.

        :param effort_points: Points gained during training.
        :return: Status message showing the result of the training.
        """
        if effort_points <= 0:
            return "Effort points must be greater than zero."

        level_increment = self._calculate_level_increment(effort_points)
        self.level = min(self.level + level_increment, MAX_TRAINING_LEVEL)

        return f"{self.name} (Rarity: {self.rarity}) has been trained to level {self.level}."

    def _calculate_level_increment(self, effort_points: int) -> int:
        """
        Calculate the level increment based on effort points and NFT rarity.

        :param effort_points: Points gained during training.
        :return: The calculated level increment.
        """
        rarity_multiplier = {
            "Common": 1.0,
            "Uncommon": 1.2,
            "Rare": 1.5,
            "Epic": 2.0,
            "Legendary": 3.0
        }
        return int(effort_points * rarity_multiplier[self.rarity])

    def to_dict(self) -> Dict:
        """
        Serialize the NFT object to a dictionary.

        :return: The serialized NFT object.
        """
        return {
            "nft_id": self.nft_id,
            "name": self.name,
            "rarity": self.rarity,
            "level": self.level
        }

# NFT Training Module
class NFTTrainingModule:
    """
    Module responsible for training NFTs in the Alphadogs game environment.
    """
    def __init__(self):
        """
        Initialize the NFT training module with an empty collection of NFTs.
        """
        self.nft_collection: List[AlphadogsNFT] = []

    def add_nft(self, nft: AlphadogsNFT) -> None:
        """
        Add an NFT to the training module.

        :param nft: The NFT object to add.
        """
        self.nft_collection.append(nft)

    def train_nft(self, nft_id: int, effort_points: int) -> str:
        """
        Train an NFT by its ID.

        :param nft_id: ID of the NFT to train.
        :param effort_points: Effort points to apply during training.
        :return: The result of the training process.
        """
        nft = self._find_nft_by_id(nft_id)
        if nft:
            return nft.train(effort_points)
        else:
            return f"NFT with ID {nft_id} not found."

    def _find_nft_by_id(self, nft_id: int) -> AlphadogsNFT:
        """
        Find an NFT by its ID.

        :param nft_id: ID of the NFT to find.
        :return: The NFT object if found, else None.
        """
        for nft in self.nft_collection:
            if nft.nft_id == nft_id:
                return nft
        return None

    def export_nfts(self, file_path: str) -> None:
        """
        Export all NFTs in the collection to a JSON file.

        :param file_path: Path to the JSON file to save.
        """
        try:
            with open(file_path, "w") as file:
                json.dump([nft.to_dict() for nft in self.nft_collection], file, indent=4)
        except Exception as e:
            print(f"Error exporting NFTs: {e}")

    def import_nfts(self, file_path: str) -> None:
        """
        Import NFTs from a JSON file into the collection.

        :param file_path: Path to the JSON file to load.
        """
        try:
            with open(file_path, "r") as file:
                nft_data = json.load(file)
                self.nft_collection = [
                    AlphadogsNFT(
                        nft["nft_id"], nft["name"], nft["rarity"], nft["level"]
                    )
                    for nft in nft_data
                ]
        except Exception as e:
            print(f"Error importing NFTs: {e}")


# Example Usage
if __name__ == "__main__":
    module = NFTTrainingModule()

    # Create NFTs
    nft1 = AlphadogsNFT(nft_id=1, name="Shadow Fang", rarity="Rare")
    nft2 = AlphadogsNFT(nft_id=2, name="Golden Howl", rarity="Legendary")
    
    # Add NFTs to the module
    module.add_nft(nft1)
    module.add_nft(nft2)

    # Train NFTs
    print(module.train_nft(nft_id=1, effort_points=50))  # Train the first NFT
    print(module.train_nft(nft_id=2, effort_points=100))  # Train the second NFT

    # Export and Import
    module.export_nfts("nfts.json")
    module.import_nfts("nfts.json")
```
