"""
Generated Code Metadata:
========================
Original URL: https://pablo-defi.pages.dev
Prompt: Write a Python script to simulate gameplay mechanics for Narcos Land, including territory control, alliances, and NFT rewards, based on the Pablo ecosystem description.
Generated: DETERMINISTIC_2c058385a46c371a
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Set
from enum import Enum, auto
import hashlib
import time

class TerritoryType(Enum):
    """Types of territories in the game."""
    URBAN = auto()
    RURAL = auto()
    BORDER = auto()
    PORT = auto()

class ResourceType(Enum):
    """Types of resources in the game."""
    CASH = auto()
    WEAPONS = auto()
    INFLUENCE = auto()
    INTEL = auto()

class NFTType(Enum):
    """Types of NFTs that can be earned."""
    CHARACTER = auto()
    WEAPON = auto()
    VEHICLE = auto()
    PROPERTY = auto()

@dataclass
class NFT:
    """Represents an NFT asset."""
    nft_id: str
    nft_type: NFTType
    name: str
    rarity: float
    attributes: Dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> Dict:
        """Convert NFT to dictionary for serialization."""
        return {
            "nft_id": self.nft_id,
            "nft_type": self.nft_type.name,
            "name": self.name,
            "rarity": self.rarity,
            "attributes": self.attributes
        }

@dataclass
class Player:
    """Represents a player in the game."""
    player_id: str
    name: str
    resources: Dict[ResourceType, int] = field(default_factory=dict)
    territories: Set[str] = field(default_factory=set)
    nfts: List[NFT] = field(default_factory=list)
    alliance_id: Optional[str] = None

    def add_resource(self, resource_type: ResourceType, amount: int) -> None:
        """Add resources to player's inventory."""
        self.resources[resource_type] = self.resources.get(resource_type, 0) + amount

    def remove_resource(self, resource_type: ResourceType, amount: int) -> bool:
        """Remove resources from player's inventory if available."""
        if self.resources.get(resource_type, 0) >= amount:
            self.resources[resource_type] -= amount
            return True
        return False

    def add_territory(self, territory_id: str) -> None:
        """Add territory to player's control."""
        self.territories.add(territory_id)

    def remove_territory(self, territory_id: str) -> None:
        """Remove territory from player's control."""
        self.territories.discard(territory_id)

    def add_nft(self, nft: NFT) -> None:
        """Add NFT to player's collection."""
        self.nfts.append(nft)

    def to_dict(self) -> Dict:
        """Convert player to dictionary for serialization."""
        return {
            "player_id": self.player_id,
            "name": self.name,
            "resources": {rt.name: amount for rt, amount in self.resources.items()},
            "territories": list(self.territories),
            "nfts": [nft.to_dict() for nft in self.nfts],
            "alliance_id": self.alliance_id
        }

@dataclass
class Territory:
    """Represents a territory in the game."""
    territory_id: str
    name: str
    territory_type: TerritoryType
    base_value: int
    controlled_by: Optional[str] = None
    defense_level: int = 1

    def to_dict(self) -> Dict:
        """Convert territory to dictionary for serialization."""
        return {
            "territory_id": self.territory_id,
            "name": self.name,
            "territory_type": self.territory_type.name,
            "base_value": self.base_value,
            "controlled_by": self.controlled_by,
            "defense_level": self.defense_level
        }

@dataclass
class Alliance:
    """Represents an alliance of players."""
    alliance_id: str
    name: str
    members: Set[str] = field(default_factory=set)
    shared_resources: Dict[ResourceType, int] = field(default_factory=dict)
    controlled_territories: Set[str] = field(default_factory=set)

    def add_member(self, player_id: str) -> None:
        """Add a player to the alliance."""
        self.members.add(player_id)

    def remove_member(self, player_id: str) -> None:
        """Remove a player from the alliance."""
        self.members.discard(player_id)

    def add_shared_resource(self, resource_type: ResourceType, amount: int) -> None:
        """Add resources to alliance's shared pool."""
        self.shared_resources[resource_type] = self.shared_resources.get(resource_type, 0) + amount

    def remove_shared_resource(self, resource_type: ResourceType, amount: int) -> bool:
        """Remove resources from alliance's shared pool if available."""
        if self.shared_resources.get(resource_type, 0) >= amount:
            self.shared_resources[resource_type] -= amount
            return True
        return False

    def add_territory(self, territory_id: str) -> None:
        """Add territory to alliance's control."""
        self.controlled_territories.add(territory_id)

    def remove_territory(self, territory_id: str) -> None:
        """Remove territory from alliance's control."""
        self.controlled_territories.discard(territory_id)

    def to_dict(self) -> Dict:
        """Convert alliance to dictionary for serialization."""
        return {
            "alliance_id": self.alliance_id,
            "name": self.name,
            "members": list(self.members),
            "shared_resources": {rt.name: amount for rt, amount in self.shared_resources.items()},
            "controlled_territories": list(self.controlled_territories)
        }

class NarcosLandGame:
    """Main game class handling all gameplay mechanics."""
    
    def __init__(self):
        self.players: Dict[str, Player] = {}
        self.territories: Dict[str, Territory] = {}
        self.alliances: Dict[str, Alliance] = {}
        self.nft_counter: int = 0
        self._initialize_default_territories()
    
    def _initialize_default_territories(self) -> None:
        """Initialize the game with default territories."""
        territory_types = list(TerritoryType)
        for i in range(1, 21):  # 20 territories
            territory_id = f"territory_{i}"
            territory_type = random.choice(territory_types)
            base_value = random.randint(100, 1000)
            self.territories[territory_id] = Territory(
                territory_id=territory_id,
                name=f"{territory_type.name.capitalize()} Territory {i}",
                territory_type=territory_type,
                base_value=base_value
            )
    
    def register_player(self, name: str) -> str:
        """Register a new player and return their ID."""
        player_id = hashlib.sha256(f"{name}{time.time()}".encode()).hexdigest()[:16]
        self.players[player_id] = Player(player_id=player_id, name=name)
        # Give new player some starting resources
        self.players[player_id].add_resource(ResourceType.CASH, 500)
        self.players[player_id].add_resource(ResourceType.WEAPONS, 100)
        return player_id
    
    def create_alliance(self, creator_id: str, name: str) -> str:
        """Create a new alliance and return its ID."""
        if creator_id not in self.players:
            raise ValueError("Player does not exist")
        
        alliance_id = hashlib.sha256(f"{name}{time.time()}".encode()).hexdigest()[:16]
        self.alliances[alliance_id] = Alliance(alliance_id=alliance_id, name=name)
        self.alliances[alliance_id].add_member(creator_id)
        self.players[creator_id].alliance_id = alliance_id
        return alliance_id
    
    def join_alliance(self, player_id: str, alliance_id: str) -> None:
        """Add a player to an alliance."""
        if player_id not in self.players:
            raise ValueError("Player does not exist")
        if alliance_id not in self.alliances:
            raise ValueError("Alliance does not exist")
        
        # Leave current alliance if any
        current_alliance = self.players[player_id].alliance_id
        if current_alliance:
            self.leave_alliance(player_id)
        
        self.alliances[alliance_id].add_member(player_id)
        self.players[player_id].alliance_id = alliance_id
    
    def leave_alliance(self, player_id: str) -> None:
        """Remove a player from their alliance."""
        if player_id not in self.players:
            raise ValueError("Player does not exist")
        
        alliance_id = self.players[player_id
