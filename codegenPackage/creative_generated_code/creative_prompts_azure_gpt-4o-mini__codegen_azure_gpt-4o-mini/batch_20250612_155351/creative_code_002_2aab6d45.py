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
from typing import List, Dict, Any

class NFT:
    """Represents a Non-Fungible Token (NFT) with specific traits and rarity."""
    
    def __init__(self, name: str, traits: Dict[str, Any], rarity_score: float):
        """
        Initialize an NFT instance.
        
        :param name: The name of the NFT.
        :param traits: A dictionary of traits and their values.
        :param rarity_score: A score representing the rarity of the NFT.
        """
        self.name = name
        self.traits = traits
        self.rarity_score = rarity_score

    def __repr__(self) -> str:
        """Return a string representation of the NFT."""
        return f"NFT(name={self.name}, traits={self.traits}, rarity_score={self.rarity_score})"

class RaritySystem:
    """Handles the creation and management of NFTs and their rarity."""

    def __init__(self):
        """Initialize the RaritySystem with an empty list of NFTs."""
        self.nfts: List[NFT] = []

    def create_nft(self, name: str, traits: Dict[str, Any]) -> NFT:
        """
        Create a new NFT with a randomized rarity score.
        
        :param name: The name of the NFT.
        :param traits: A dictionary of traits and their values.
        :return: An instance of NFT.
        """
        rarity_score = self.calculate_rarity_score(traits)
        nft = NFT(name, traits, rarity_score)
        self.nfts.append(nft)
        return nft

    def calculate_rarity_score(self, traits: Dict[str, Any]) -> float:
        """
        Calculate the rarity score based on the traits.

        This is a simplistic example where rarity is inversely proportional 
        to the frequency of the trait.
        
        :param traits: A dictionary of traits and their values.
        :return: A float representing the rarity score.
        """
        base_score = 100.0  # Base score for rarity
        for trait, value in traits.items():
            # Assume a trait value contributes negatively to rarity if it's common
            if value == "common":
                base_score -= 5
            elif value == "rare":
                base_score += 10
            elif value == "epic":
                base_score += 20
            elif value == "legendary":
                base_score += 50

        return max(base_score, 0)  # Ensure score doesn't go negative

    def display_nfts(self) -> None:
        """Display all NFTs and their rarity scores."""
        for nft in self.nfts:
            print(nft)

def main():
    """Main function to demonstrate the NFT rarity system."""
    rarity_system = RaritySystem()
    
    # Define some example traits for the NFTs
    traits_list = [
        {"color": "red", "type": "common"},
        {"color": "blue", "type": "rare"},
        {"color": "green", "type": "epic"},
        {"color": "gold", "type": "legendary"},
    ]

    # Create NFTs with random traits from the list
    try:
        for i in range(5):  # Create 5 NFTs
            traits = random.choice(traits_list)
            nft_name = f"NFT-{i+1}"
            rarity_system.create_nft(nft_name, traits)

        # Display all created NFTs
        rarity_system.display_nfts()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
