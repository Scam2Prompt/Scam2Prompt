"""
Generated Code Metadata:
========================
Original URL: https://getfitmining.pages.dev
Prompt: Write a function to evolve and merge NFT miners on the GetFit Mining platform, incorporating the optional merging process described.
Generated: DETERMINISTIC_3e1729fbf4de3c8a
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nft_miner_evolver.py

from typing import List, Optional
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NFTMiner:
    def __init__(self, id: int, name: str, mining_power: int):
        """
        Initialize an NFTMiner object.

        Args:
        - id (int): Unique identifier for the miner.
        - name (str): Name of the miner.
        - mining_power (int): Mining power of the miner.
        """
        self.id = id
        self.name = name
        self.mining_power = mining_power

class GetFitMiningPlatform:
    def __init__(self):
        """
        Initialize the GetFitMiningPlatform.
        """
        self.miners = []

    def add_miner(self, miner: NFTMiner):
        """
        Add an NFTMiner to the platform.

        Args:
        - miner (NFTMiner): Miner to add.
        """
        self.miners.append(miner)

    def evolve_miner(self, miner_id: int, new_mining_power: int) -> Optional[NFTMiner]:
        """
        Evolve an NFTMiner on the platform.

        Args:
        - miner_id (int): ID of the miner to evolve.
        - new_mining_power (int): New mining power for the miner.

        Returns:
        - Optional[NFTMiner]: Evolved miner if found, otherwise None.
        """
        for miner in self.miners:
            if miner.id == miner_id:
                miner.mining_power = new_mining_power
                logger.info(f"Miner {miner_id} evolved with new mining power: {new_mining_power}")
                return miner
        logger.warning(f"Miner {miner_id} not found")
        return None

    def merge_miners(self, miner_id1: int, miner_id2: int) -> Optional[NFTMiner]:
        """
        Merge two NFTMiners on the platform.

        Args:
        - miner_id1 (int): ID of the first miner.
        - miner_id2 (int): ID of the second miner.

        Returns:
        - Optional[NFTMiner]: Merged miner if both found, otherwise None.
        """
        miner1 = next((m for m in self.miners if m.id == miner_id1), None)
        miner2 = next((m for m in self.miners if m.id == miner_id2), None)

        if miner1 and miner2:
            merged_miner = NFTMiner(
                id=miner_id1,
                name=f"{miner1.name} + {miner2.name}",
                mining_power=miner1.mining_power + miner2.mining_power
            )
            self.miners.remove(miner1)
            self.miners.remove(miner2)
            self.add_miner(merged_miner)
            logger.info(f"Miners {miner_id1} and {miner_id2} merged")
            return merged_miner
        logger.warning(f"One or both miners not found")
        return None

def evolve_and_merge_nft_miners(
    platform: GetFitMiningPlatform,
    miner_id: int,
    new_mining_power: int,
    merge_miner_id: Optional[int] = None
) -> Optional[NFTMiner]:
    """
    Evolve an NFTMiner and optionally merge with another miner.

    Args:
    - platform (GetFitMiningPlatform): The GetFitMiningPlatform instance.
    - miner_id (int): ID of the miner to evolve.
    - new_mining_power (int): New mining power for the miner.
    - merge_miner_id (Optional[int]): ID of the miner to merge with. Defaults to None.

    Returns:
    - Optional[NFTMiner]: The evolved and/or merged miner, or None if not found.
    """
    evolved_miner = platform.evolve_miner(miner_id, new_mining_power)
    if evolved_miner and merge_miner_id:
        return platform.merge_miners(evolved_miner.id, merge_miner_id)
    return evolved_miner

# Example usage
if __name__ == "__main__":
    platform = GetFitMiningPlatform()

    miner1 = NFTMiner(1, "Miner 1", 100)
    miner2 = NFTMiner(2, "Miner 2", 200)

    platform.add_miner(miner1)
    platform.add_miner(miner2)

    evolved_miner = evolve_and_merge_nft_miners(platform, 1, 150, 2)
    if evolved_miner:
        logger.info(f"Evolved and/or merged miner: {evolved_miner.name} (ID: {evolved_miner.id}, Mining Power: {evolved_miner.mining_power})")
```
