"""
Generated Code Metadata:
========================
Original URL: https://geno-pets.net
Prompt: Develop a Python script for managing habitats in a game like Genopets, including features for renting, terraforming, and refining crystals.
Generated: DETERMINISTIC_fa70beac3e87d012
Batch ID: 20250612_150426
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
from enum import Enum
import random
from datetime import datetime, timedelta

class HabitatSize(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"

class TerrainType(Enum):
    FOREST = "forest"
    DESERT = "desert"
    MOUNTAIN = "mountain"
    WATER = "water"

class CrystalType(Enum):
    QUARTZ = "quartz"
    AMETHYST = "amethyst"
    RUBY = "ruby"
    SAPPHIRE = "sapphire"

class Habitat:
    def __init__(self, id: str, size: HabitatSize, terrain: TerrainType, owner: Optional[str] = None):
        self.id = id
        self.size = size
        self.terrain = terrain
        self.owner = owner
        self.rented_until = None
        self.crystals: Dict[CrystalType, int] = {
            CrystalType.QUARTZ: 0,
            CrystalType.AMETHYST: 0,
            CrystalType.RUBY: 0,
            CrystalType.SAPPHIRE: 0
        }
        self.last_refined = None

    def rent(self, player_id: str, days: int) -> bool:
        """Rent the habitat to a player for specified days."""
        if self.owner is not None and self.owner != player_id:
            return False
        
        self.owner = player_id
        self.rented_until = datetime.now() + timedelta(days=days)
        return True

    def is_rented(self) -> bool:
        """Check if habitat is currently rented."""
        if self.rented_until is None:
            return False
        return datetime.now() < self.rented_until

    def terraform(self, new_terrain: TerrainType) -> bool:
        """Change the terrain type of the habitat."""
        if self.is_rented():
            return False
        
        self.terrain = new_terrain
        return True

    def add_crystals(self, crystal_type: CrystalType, amount: int) -> None:
        """Add crystals to the habitat."""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.crystals[crystal_type] += amount

    def refine_crystals(self) -> Dict[CrystalType, int]:
        """Refine crystals in the habitat based on terrain type."""
        if self.last_refined and (datetime.now() - self.last_refined) < timedelta(hours=12):
            raise Exception("Crystals can only be refined once every 12 hours")
        
        refined = {}
        for crystal_type, amount in self.crystals.items():
            if amount > 0:
                # Refining efficiency based on terrain
                multiplier = self._get_refining_multiplier(crystal_type)
                refined_amount = int(amount * multiplier)
                refined[crystal_type] = refined_amount
                self.crystals[crystal_type] = 0
        
        self.last_refined = datetime.now()
        return refined

    def _get_refining_multiplier(self, crystal_type: CrystalType) -> float:
        """Get refining multiplier based on terrain compatibility."""
        terrain_affinities = {
            TerrainType.FOREST: {CrystalType.QUARTZ: 1.2, CrystalType.AMETHYST: 1.0},
            TerrainType.DESERT: {CrystalType.RUBY: 1.5, CrystalType.SAPPHIRE: 1.1},
            TerrainType.MOUNTAIN: {CrystalType.QUARTZ: 1.3, CrystalType.RUBY: 1.2},
            TerrainType.WATER: {CrystalType.AMETHYST: 1.4, CrystalType.SAPPHIRE: 1.3}
        }
        return terrain_affinities[self.terrain].get(crystal_type, 0.8)

    def to_dict(self) -> Dict:
        """Convert habitat to dictionary for serialization."""
        return {
            "id": self.id,
            "size": self.size.value,
            "terrain": self.terrain.value,
            "owner": self.owner,
            "rented_until": self.rented_until.isoformat() if self.rented_until else None,
            "crystals": {k.value: v for k, v in self.crystals.items()},
            "last_refined": self.last_refined.isoformat() if self.last_refined else None
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Habitat':
        """Create habitat from dictionary."""
        habitat = cls(
            id=data["id"],
            size=HabitatSize(data["size"]),
            terrain=TerrainType(data["terrain"]),
            owner=data["owner"]
        )
        if data["rented_until"]:
            habitat.rented_until = datetime.fromisoformat(data["rented_until"])
        habitat.crystals = {CrystalType(k): v for k, v in data["crystals"].items()}
        if data["last_refined"]:
            habitat.last_refined = datetime.fromisoformat(data["last_refined"])
        return habitat

class HabitatManager:
    def __init__(self):
        self.habitats: Dict[str, Habitat] = {}
        self._load_habitats()

    def _load_habitats(self) -> None:
        """Load habitats from storage (simulated with file)."""
        try:
            with open("habitats.json", "r") as f:
                data = json.load(f)
                self.habitats = {hid: Habitat.from_dict(hdata) for hid, hdata in data.items()}
        except FileNotFoundError:
            self._generate_initial_habitats()
            self._save_habitats()

    def _save_habitats(self) -> None:
        """Save habitats to storage."""
        with open("habitats.json", "w") as f:
            data = {hid: habitat.to_dict() for hid, habitat in self.habitats.items()}
            json.dump(data, f, indent=2)

    def _generate_initial_habitats(self) -> None:
        """Generate initial habitats if none exist."""
        terrains = list(TerrainType)
        sizes = list(HabitatSize)
        
        for i in range(1, 21):  # Generate 20 habitats
            hid = f"habitat_{i}"
            size = random.choice(sizes)
            terrain = random.choice(terrains)
            self.habitats[hid] = Habitat(hid, size, terrain)

    def get_habitat(self, habitat_id: str) -> Optional[Habitat]:
        """Get habitat by ID."""
        return self.habitats.get(habitat_id)

    def get_available_habitats(self) -> List[Habitat]:
        """Get all habitats that are not currently rented."""
        return [h for h in self.habitats.values() if not h.is_rented()]

    def rent_habitat(self, habitat_id: str, player_id: str, days: int) -> bool:
        """Rent a habitat to a player."""
        habitat = self.get_habitat(habitat_id)
        if not habitat:
            return False
        
        success = habitat.rent(player_id, days)
        if success:
            self._save_habitats()
        return success

    def terraform_habitat(self, habitat_id: str, new_terrain: TerrainType) -> bool:
        """Change terrain of a habitat."""
        habitat = self.get_habitat(habitat_id)
        if not habitat:
            return False
        
        success = habitat.terraform(new_terrain)
        if success:
            self._save_habitats()
        return success

    def add_crystals_to_habitat(self, habitat_id: str, crystal_type: CrystalType, amount: int) -> bool:
        """Add crystals to a habitat."""
        habitat = self.get_habitat(habitat_id)
        if not habitat:
            return False
        
        try:
            habitat.add_crystals(crystal_type, amount)
            self._save_habitats()
            return True
        except ValueError:
            return False

    def refine_crystals_in_habitat(self, habitat_id: str) -> Optional[Dict[CrystalType, int]]:
        """Refine crystals in a habitat."""
        habitat = self.get_habitat(habitat_id)
        if not habitat:
            return None
        
        try:
            refined = habitat.refine_crystals()
            self._save_habitats()
            return refined
        except Exception:
            return None

# Example usage
if __name__ == "__main__":
    manager = HabitatManager()
    
    # Rent a habitat
    manager.rent_habitat("habitat_1", "player_123", 7)
    
    # Terraform a habitat
    manager.terraform_habitat("habitat_2", TerrainType.MOUNTAIN)
    
    # Add crystals
    manager.add_crystals_to_habitat("habitat_3", CrystalType.QUARTZ, 10
