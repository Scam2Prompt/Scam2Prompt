"""
Generated Code Metadata:
========================
Original URL: https://stellarcropgame.fun
Prompt: Create a Python program to simulate planetary exploration in Stellar Crop, generating random "keşfedilmemiş gezegen türleri" with unique resources and challenges.
Generated: DETERMINISTIC_a6192ebc62143d72
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from enum import Enum
from typing import Dict, List, NamedTuple, Optional
from dataclasses import dataclass
import json

class PlanetType(Enum):
    """Enumeration of possible planet types."""
    TERRESTRIAL = "Terrestrial"
    GAS_GIANT = "Gas Giant"
    ICE_GIANT = "Ice Giant"
    LAVA = "Lava"
    OCEAN = "Ocean"
    DESERT = "Desert"
    TOXIC = "Toxic"
    RADIOACTIVE = "Radioactive"
    CRYSTALLINE = "Crystalline"
    ARTIFICIAL = "Artificial"

class ResourceType(Enum):
    """Enumeration of possible resource types."""
    MINERALS = "Minerals"
    GASES = "Gases"
    ORGANICS = "Organics"
    CRYSTALS = "Crystals"
    METALS = "Metals"
    ENERGY = "Energy"
    WATER = "Water"
    RARE_ELEMENTS = "Rare Elements"
    BIOMASS = "Biomass"
    TECH_ARTIFACTS = "Technology Artifacts"

class ChallengeType(Enum):
    """Enumeration of possible challenge types."""
    EXTREME_TEMPERATURE = "Extreme Temperature"
    HIGH_RADIATION = "High Radiation"
    TOXIC_ATMOSPHERE = "Toxic Atmosphere"
    STRONG_GRAVITY = "Strong Gravity"
    LOW_GRAVITY = "Low Gravity"
    ELECTROMAGNETIC_STORMS = "Electromagnetic Storms"
    PREDATORY_LIFE = "Predatory Life Forms"
    UNSTABLE_TERRAIN = "Unstable Terrain"
    LIMITED_RESOURCES = "Limited Resources"
    HOSTILE_NATIVES = "Hostile Natives"

@dataclass
class Planet:
    """Class representing a planet with its properties."""
    name: str
    planet_type: PlanetType
    resources: Dict[ResourceType, int]
    challenges: List[ChallengeType]
    habitability_score: float
    description: str

class PlanetGenerator:
    """Generates random unexplored planets with unique properties."""
    
    def __init__(self):
        self._load_name_parts()
        self._load_descriptions()
    
    def _load_name_parts(self) -> None:
        """Load name parts for planet name generation."""
        self.prefixes = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta"]
        self.suffixes = ["Prime", "Secundus", "Tertius", "Quartus", "Quintus"]
        self.middle_parts = ["Vega", "Orion", "Sirius", "Andromeda", "Persei"]
    
    def _load_descriptions(self) -> None:
        """Load planet descriptions templates."""
        self.descriptions = {
            PlanetType.TERRESTRIAL: "A rocky planet with potential for colonization.",
            PlanetType.GAS_GIANT: "A massive planet composed mainly of hydrogen and helium.",
            PlanetType.ICE_GIANT: "A cold planet with icy surface and atmosphere rich in volatiles.",
            PlanetType.LAVA: "A planet with molten surface and extreme volcanic activity.",
            PlanetType.OCEAN: "A water-covered world with deep oceans and possible aquatic life.",
            PlanetType.DESERT: "A dry world with vast deserts and minimal water sources.",
            PlanetType.TOXIC: "A planet with poisonous atmosphere and hazardous environment.",
            PlanetType.RADIOACTIVE: "A world with high radiation levels from its core or nearby star.",
            PlanetType.CRYSTALLINE: "A planet with surface covered in giant crystal formations.",
            PlanetType.ARTIFICIAL: "A mysterious planet showing signs of artificial construction."
        }
    
    def generate_planet_name(self) -> str:
        """Generate a random planet name."""
        return f"{random.choice(self.prefixes)}-{random.choice(self.middle_parts)} {random.choice(self.suffixes)}"
    
    def generate_planet_type(self) -> PlanetType:
        """Generate a random planet type."""
        return random.choice(list(PlanetType))
    
    def generate_resources(self, planet_type: PlanetType) -> Dict[ResourceType, int]:
        """Generate random resources based on planet type."""
        resources = {}
        num_resources = random.randint(2, 5)
        
        # Base resource probabilities by planet type
        resource_pool = {
            PlanetType.TERRESTRIAL: [ResourceType.MINERALS, ResourceType.METALS, ResourceType.WATER],
            PlanetType.GAS_GIANT: [ResourceType.GASES, ResourceType.ENERGY, ResourceType.RARE_ELEMENTS],
            PlanetType.ICE_GIANT: [ResourceType.WATER, ResourceType.GASES, ResourceType.ORGANICS],
            PlanetType.LAVA: [ResourceType.MINERALS, ResourceType.METALS, ResourceType.ENERGY],
            PlanetType.OCEAN: [ResourceType.WATER, ResourceType.ORGANICS, ResourceType.BIOMASS],
            PlanetType.DESERT: [ResourceType.MINERALS, ResourceType.METALS, ResourceType.RARE_ELEMENTS],
            PlanetType.TOXIC: [ResourceType.ORGANICS, ResourceType.BIOMASS, ResourceType.TECH_ARTIFACTS],
            PlanetType.RADIOACTIVE: [ResourceType.ENERGY, ResourceType.RARE_ELEMENTS, ResourceType.TECH_ARTIFACTS],
            PlanetType.CRYSTALLINE: [ResourceType.CRYSTALS, ResourceType.MINERALS, ResourceType.ENERGY],
            PlanetType.ARTIFICIAL: [ResourceType.TECH_ARTIFACTS, ResourceType.METALS, ResourceType.ENERGY]
        }
        
        # Add common resources
        base_resources = resource_pool.get(planet_type, [])
        for resource in random.sample(base_resources, min(num_resources, len(base_resources))):
            resources[resource] = random.randint(1, 100)
        
        # Add possible rare resources
        if random.random() < 0.3:
            rare_resource = random.choice(list(ResourceType))
            if rare_resource not in resources:
                resources[rare_resource] = random.randint(1, 50)
        
        return resources
    
    def generate_challenges(self, planet_type: PlanetType) -> List[ChallengeType]:
        """Generate random challenges based on planet type."""
        challenges = []
        num_challenges = random.randint(1, 3)
        
        # Base challenge probabilities by planet type
        challenge_pool = {
            PlanetType.TERRESTRIAL: [ChallengeType.UNSTABLE_TERRAIN, ChallengeType.PREDATORY_LIFE],
            PlanetType.GAS_GIANT: [ChallengeType.STRONG_GRAVITY, ChallengeType.ELECTROMAGNETIC_STORMS],
            PlanetType.ICE_GIANT: [ChallengeType.EXTREME_TEMPERATURE, ChallengeType.LOW_GRAVITY],
            PlanetType.LAVA: [ChallengeType.EXTREME_TEMPERATURE, ChallengeType.TOXIC_ATMOSPHERE],
            PlanetType.OCEAN: [ChallengeType.HIGH_RADIATION, ChallengeType.PREDATORY_LIFE],
            PlanetType.DESERT: [ChallengeType.EXTREME_TEMPERATURE, ChallengeType.LIMITED_RESOURCES],
            PlanetType.TOXIC: [ChallengeType.TOXIC_ATMOSPHERE, ChallengeType.HOSTILE_NATIVES],
            PlanetType.RADIOACTIVE: [ChallengeType.HIGH_RADIATION, ChallengeType.ELECTROMAGNETIC_STORMS],
            PlanetType.CRYSTALLINE: [ChallengeType.UNSTABLE_TERRAIN, ChallengeType.HIGH_RADIATION],
            PlanetType.ARTIFICIAL: [ChallengeType.HOSTILE_NATIVES, ChallengeType.TECH_ARTIFACTS]
        }
        
        base_challenges = challenge_pool.get(planet_type, [])
        for challenge in random.sample(base_challenges, min(num_challenges, len(base_challenges))):
            challenges.append(challenge)
        
        return challenges
    
    def calculate_habitability(self, planet_type: PlanetType, challenges: List[ChallengeType]) -> float:
        """Calculate habitability score based on planet type and challenges."""
        base_scores = {
            PlanetType.TERRESTRIAL: 0.7,
            PlanetType.GAS_GIANT: 0.1,
            PlanetType.ICE_GIANT: 0.2,
            PlanetType.LAVA: 0.05,
            PlanetType.OCEAN: 0.6,
            PlanetType.DESERT: 0.4,
            PlanetType.TOXIC: 0.1,
            PlanetType.RADIOACTIVE: 0.05,
            PlanetType.CRYSTALLINE: 0.3,
            PlanetType.ARTIFICIAL: 0.5
        }
        
        score = base_scores.get(planet_type, 0.5)
        
        # Adjust score based on challenges
        for challenge in challenges:
            if challenge in [
