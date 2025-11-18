"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getfitmining.pages.dev
Prompt: Write a function to evolve and merge NFT miners on the GetFit Mining platform, incorporating the optional merging process described.
Generated: DETERMINISTIC_3e1729fbf4de3c8a
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class NFTMiner:
    """Represents a miner NFT with attributes for evolution and merging."""

    def __init__(self, miner_id, level, rarity):
        self.miner_id = miner_id  # Unique identifier for the miner
        self.level = level        # Current evolution level of the miner
        self.rarity = rarity      # Rarity level of the miner (e.g., common, rare, epic)

    def evolve(self):
        """Evolves the miner to the next level if conditions are met."""
        if self.level < 5:  # Assuming max evolution level is 5
            self.level += 1
            print(f"Miner {self.miner_id} evolved to level {self.level}.")
        else:
            raise ValueError("Miner is already at maximum evolution level.")


def merge_miners(miner1: NFTMiner, miner2: NFTMiner) -> NFTMiner:
    """Merges two NFT miners into a new NFT miner.
    
    Args:
        miner1 (NFTMiner): The first miner to merge.
        miner2 (NFTMiner): The second miner to merge.

    Returns:
        NFTMiner: A new miner created from merging the two miners.
    
    Raises:
        ValueError: If the miners have different rarity levels or if any miner is already at max level.
    """
    # Check if miners have the same rarity
    if miner1.rarity != miner2.rarity:
        raise ValueError("Miners must have the same rarity to merge.")
    
    # Check if either miner is at max level
    if miner1.level >= 5 or miner2.level >= 5:
        raise ValueError("Cannot merge miners that are already at maximum level.")
    
    # Create a new miner based on the merged attributes
    new_miner_id = f"{miner1.miner_id}-{miner2.miner_id}-merged"
    new_level = max(miner1.level, miner2.level) + 1  # New level is one higher than the highest level
    new_rarity = miner1.rarity  # Rarity is the same as the other miners

    # Create and return the new miner
    merged_miner = NFTMiner(new_miner_id, new_level, new_rarity)
    print(f"Merged miner created with ID: {merged_miner.miner_id}, Level: {merged_miner.level}, Rarity: {merged_miner.rarity}.")
    return merged_miner


# Example Usage
if __name__ == "__main__":
    # Create two miners
    miner_a = NFTMiner("miner1", 3, "rare")
    miner_b = NFTMiner("miner2", 4, "rare")

    try:
        # Evolve the first miner
        miner_a.evolve()

        # Merge the two miners
        merged_miner = merge_miners(miner_a, miner_b)
    except ValueError as e:
        print(f"Error: {e}")
```
