"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rascalsnft.web.app
Prompt: What are the best practices for creating a rarity system for NFTs, based on the utilities described in the Rascals NFT project?
Generated: DETERMINISTIC_2aab6d45ac9cbd32
Batch ID: 20250612_155351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json

class NFT:
    """
    A class to represent an individual NFT with its associated traits and rarity.
    """

    def __init__(self, id, traits, utilities):
        """
        Initialize the NFT instance.

        :param id: Unique identifier for the NFT.
        :param traits: Dictionary containing traits and their values.
        :param utilities: Dictionary containing utilities and their assigned rarity weight.
        """
        self.id = id
        self.traits = traits
        self.utilities = utilities
        self.rarity_score = self.calculate_rarity()

    def calculate_rarity(self):
        """
        Calculate the rarity score of the NFT based on its utilities.

        :return: A rarity score (float) for the NFT.
        """
        rarity_score = 0
        for utility, weight in self.utilities.items():
            rarity_score += weight
        return rarity_score


class RaritySystem:
    """
    A class to manage the rarity system for NFTs.
    """

    def __init__(self):
        """
        Initialize the RaritySystem instance.
        """
        self.nfts = []

    def generate_nft(self, id, traits, utilities):
        """
        Generate and add a new NFT to the system.

        :param id: Unique identifier for the NFT.
        :param traits: Dictionary containing traits and their values.
        :param utilities: Dictionary containing utilities and their assigned rarity weight.
        """
        nft = NFT(id, traits, utilities)
        self.nfts.append(nft)

    def list_nfts(self):
        """
        List all NFTs.

        :return: A list of dictionaries representing NFTs and their rarity scores.
        """
        return [
            {"id": nft.id, "traits": nft.traits, "utilities": nft.utilities, "rarity_score": nft.rarity_score}
            for nft in self.nfts
        ]

    def sort_by_rarity(self):
        """
        Sort the NFTs by their rarity scores in descending order.

        :return: A list of NFTs sorted by rarity.
        """
        return sorted(self.nfts, key=lambda x: x.rarity_score, reverse=True)

    def save_nfts_to_file(self, filename):
        """
        Save all NFTs to a JSON file.

        :param filename: Name of the file where NFTs will be saved.
        """
        try:
            nfts_data = [
                {"id": nft.id, "traits": nft.traits, "utilities": nft.utilities, "rarity_score": nft.rarity_score}
                for nft in self.nfts
            ]
            with open(filename, 'w') as file:
                json.dump(nfts_data, file, indent=4)
            print(f"NFTs successfully saved to {filename}.")
        except Exception as e:
            print(f"Error saving NFTs to file: {e}")

    def load_nfts_from_file(self, filename):
        """
        Load NFTs from a JSON file.

        :param filename: Name of the file from which NFTs will be loaded.
        """
        try:
            with open(filename, 'r') as file:
                nfts_data = json.load(file)
            self.nfts = [NFT(data['id'], data['traits'], data['utilities']) for data in nfts_data]
            print(f"NFTs successfully loaded from {filename}.")
        except Exception as e:
            print(f"Error loading NFTs from file: {e}")


# Example usage
if __name__ == "__main__":
    # Initialize the rarity system
    rarity_system = RaritySystem()

    # Define traits and utilities for some sample NFTs
    traits1 = {"background": "blue", "accessory": "hat"}
    utilities1 = {"staking_reward": 1.5, "game_boost": 2.0}

    traits2 = {"background": "red", "accessory": "glasses"}
    utilities2 = {"staking_reward": 2.0, "game_boost": 3.0}

    # Generate NFTs
    rarity_system.generate_nft(id=1, traits=traits1, utilities=utilities1)
    rarity_system.generate_nft(id=2, traits=traits2, utilities=utilities2)

    # List NFTs
    print("List of NFTs:")
    print(rarity_system.list_nfts())

    # Sort NFTs by rarity
    print("\nSorted NFTs by rarity:")
    sorted_nfts = rarity_system.sort_by_rarity()
    for nft in sorted_nfts:
        print(f"ID: {nft.id}, Rarity Score: {nft.rarity_score}")

    # Save NFTs to file
    rarity_system.save_nfts_to_file("nfts.json")

    # Load NFTs from file
    rarity_system.load_nfts_from_file("nfts.json")
```
