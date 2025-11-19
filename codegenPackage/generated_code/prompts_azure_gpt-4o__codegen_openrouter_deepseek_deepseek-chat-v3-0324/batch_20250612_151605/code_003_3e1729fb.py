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
import json
from typing import Dict, List, Optional, Tuple

class NFTMiner:
    """
    Represents an NFT miner with attributes for evolution and merging.
    """
    def __init__(self, miner_id: str, level: int, power: float, is_evolving: bool = False):
        self.miner_id = miner_id
        self.level = level
        self.power = power
        self.is_evolving = is_evolving

    def to_dict(self) -> Dict:
        """Convert NFTMiner instance to dictionary."""
        return {
            "miner_id": self.miner_id,
            "level": self.level,
            "power": self.power,
            "is_evolving": self.is_evolving
        }

class NFTMinerManager:
    """
    Manages the evolution and merging of NFT miners on the GetFit Mining platform.
    """
    def __init__(self):
        self.miners: Dict[str, NFTMiner] = {}
        self.evolution_cost_multiplier = 1.5
        self.merge_power_boost = 0.2

    def add_miner(self, miner: NFTMiner) -> None:
        """Add a new miner to the manager."""
        if miner.miner_id in self.miners:
            raise ValueError(f"Miner with ID {miner.miner_id} already exists")
        self.miners[miner.miner_id] = miner

    def evolve_miner(self, miner_id: str) -> NFTMiner:
        """
        Evolve a miner to the next level.
        Returns the evolved miner or raises an exception if evolution fails.
        """
        if miner_id not in self.miners:
            raise ValueError(f"Miner with ID {miner_id} not found")
        
        miner = self.miners[miner_id]
        
        if miner.is_evolving:
            raise ValueError(f"Miner {miner_id} is already evolving")
        
        miner.is_evolving = True
        miner.level += 1
        miner.power *= self.evolution_cost_multiplier
        miner.is_evolving = False
        
        return miner

    def can_merge(self, miner1: NFTMiner, miner2: NFTMiner) -> bool:
        """
        Check if two miners can be merged.
        Miners can be merged if they are:
        - Not currently evolving
        - Of the same level
        """
        return (
            not miner1.is_evolving and
            not miner2.is_evolving and
            miner1.level == miner2.level
        )

    def merge_miners(self, miner1_id: str, miner2_id: str, keep_miner1: bool = True) -> Tuple[NFTMiner, Optional[NFTMiner]]:
        """
        Merge two miners of the same level.
        Returns the merged miner and the remaining miner (if any).
        If keep_miner1 is True, miner1 will be upgraded and miner2 will be destroyed.
        """
        if miner1_id not in self.miners or miner2_id not in self.miners:
            raise ValueError("One or both miners not found")
        
        miner1 = self.miners[miner1_id]
        miner2 = self.miners[miner2_id]
        
        if not self.can_merge(miner1, miner2):
            raise ValueError("Miners cannot be merged")
        
        if keep_miner1:
            # Upgrade miner1 and destroy miner2
            miner1.level += 1
            miner1.power += miner2.power * self.merge_power_boost
            del self.miners[miner2_id]
            return miner1, None
        else:
            # Upgrade miner2 and destroy miner1
            miner2.level += 1
            miner2.power += miner1.power * self.merge_power_boost
            del self.miners[miner1_id]
            return miner2, None

    def batch_evolve(self, miner_ids: List[str]) -> List[NFTMiner]:
        """
        Evolve multiple miners in a batch.
        Returns list of successfully evolved miners.
        """
        evolved_miners = []
        for miner_id in miner_ids:
            try:
                evolved_miner = self.evolve_miner(miner_id)
                evolved_miners.append(evolved_miner)
            except ValueError as e:
                print(f"Failed to evolve miner {miner_id}: {str(e)}")
                continue
        return evolved_miners

    def save_state(self, file_path: str) -> None:
        """Save current state of all miners to a JSON file."""
        state = {mid: miner.to_dict() for mid, miner in self.miners.items()}
        with open(file_path, 'w') as f:
            json.dump(state, f, indent=2)

    def load_state(self, file_path: str) -> None:
        """Load miners from a JSON file."""
        with open(file_path, 'r') as f:
            state = json.load(f)
        
        self.miners = {}
        for miner_id, miner_data in state.items():
            self.miners[miner_id] = NFTMiner(
                miner_id=miner_data['miner_id'],
                level=miner_data['level'],
                power=miner_data['power'],
                is_evolving=miner_data['is_evolving']
            )
```
