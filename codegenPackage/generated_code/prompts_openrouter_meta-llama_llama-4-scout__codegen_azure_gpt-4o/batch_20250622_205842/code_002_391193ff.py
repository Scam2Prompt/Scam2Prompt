"""
Generated Code Metadata:
========================
Original URL: https://mint.mythlcal.market
Prompt: Generate code to implement a random NFT rarity system, with rarity levels such as RARE, and LEGENDARY, as seen in the NFL Rivals blueprint minting event.
Generated: DETERMINISTIC_391193ff6a1f8b81
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class NFTRaritySystem:
    """
    A class to implement a random NFT rarity system.
    Rarity levels include COMMON, RARE, EPIC, and LEGENDARY.
    """

    def __init__(self):
        """
        Initialize the rarity system with predefined rarity levels and their probabilities.
        Probabilities should sum to 1.0.
        """
        self.rarity_levels = {
            "COMMON": 0.6,      # 60% chance
            "RARE": 0.25,       # 25% chance
            "EPIC": 0.1,        # 10% chance
            "LEGENDARY": 0.05   # 5% chance
        }

    def mint_nft(self):
        """
        Mint an NFT with a random rarity based on predefined probabilities.

        Returns:
            str: The rarity level of the minted NFT.
        """
        try:
            # Generate a random rarity based on probabilities
            rarity = random.choices(
                population=list(self.rarity_levels.keys()),
                weights=list(self.rarity_levels.values()),
                k=1
            )[0]
            return rarity
        except Exception as e:
            # Handle unexpected errors gracefully
            print(f"An error occurred while minting the NFT: {e}")
            return None

    def simulate_minting_event(self, num_mints):
        """
        Simulate a minting event where multiple NFTs are minted.

        Args:
            num_mints (int): The number of NFTs to mint.

        Returns:
            dict: A dictionary with counts of each rarity level.
        """
        try:
            # Validate input
            if num_mints <= 0:
                raise ValueError("Number of mints must be greater than zero.")

            # Initialize a counter for each rarity level
            rarity_counts = {rarity: 0 for rarity in self.rarity_levels.keys()}

            # Mint NFTs and count their rarities
            for _ in range(num_mints):
                minted_rarity = self.mint_nft()
                if minted_rarity:
                    rarity_counts[minted_rarity] += 1

            return rarity_counts
        except ValueError as ve:
            print(f"Input error: {ve}")
            return {}
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return {}

# Example usage
if __name__ == "__main__":
    nft_system = NFTRaritySystem()

    # Mint a single NFT
    print("Minted NFT Rarity:", nft_system.mint_nft())

    # Simulate a minting event with 100 NFTs
    num_mints = 100
    results = nft_system.simulate_minting_event(num_mints)
    print(f"Minting Event Results ({num_mints} NFTs):")
    for rarity, count in results.items():
        print(f"{rarity}: {count}")
```
