"""
Generated Code Metadata:
========================
Original URL: https://stellarcropgame.fun
Prompt: How can I create a procedural generation system for generating diverse, planetary environments in a game like Stellar Crop, and what are some techniques for ensuring that these environments remain engaging and balanced?
Generated: DETERMINISTIC_a84371dcab7d1889
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import math
import noise
from enum import Enum
from typing import Dict, List, Tuple, Optional

class BiomeType(Enum):
    """Enumeration of possible biome types for planetary environments."""
    DESERT = "Desert"
    TUNDRA = "Tundra"
    FOREST = "Forest"
    JUNGLE = "Jungle"
    OCEAN = "Ocean"
    MOUNTAIN = "Mountain"
    VOLCANIC = "Volcanic"
    CRYSTAL = "Crystal"
    SWAMP = "Swamp"
    SAVANNAH = "Savannah"

class ResourceType(Enum):
    """Enumeration of possible resource types available in biomes."""
    WATER = "Water"
    MINERALS = "Minerals"
    ORGANICS = "Organics"
    GAS = "Gas"
    CRYSTALS = "Crystals"
    METALS = "Metals"

class Planet:
    """Represents a procedurally generated planet with diverse environments."""
    
    def __init__(self, seed: Optional[int] = None):
        """Initialize the planet with optional seed for reproducibility."""
        self.seed = seed if seed is not None else random.randint(0, 1000000)
        random.seed(self.seed)
        self.biomes: Dict[Tuple[int, int], BiomeType] = {}
        self.resources: Dict[Tuple[int, int], Dict[ResourceType, float]] = {}
        self.temperature: float = random.uniform(-50, 50)
        self.humidity: float = random.uniform(0, 1)
        self._generate_terrain()
    
    def _generate_terrain(self, size: int = 100) -> None:
        """Generate terrain using Perlin noise for natural-looking biomes."""
        scale = 100.0
        octaves = 6
        persistence = 0.5
        lacunarity = 2.0
        
        for x in range(size):
            for y in range(size):
                nx = x / size - 0.5
                ny = y / size - 0.5
                
                # Generate elevation using Perlin noise
                elevation = noise.pnoise2(
                    nx * scale, 
                    ny * scale, 
                    octaves=octaves,
                    persistence=persistence,
                    lacunarity=lacunarity,
                    repeatx=1024,
                    repeaty=1024,
                    base=self.seed
                )
                
                # Generate moisture using different noise parameters
                moisture = noise.pnoise2(
                    (nx + 100) * scale, 
                    (ny + 100) * scale, 
                    octaves=octaves,
                    persistence=persistence,
                    lacunarity=lacunarity,
                    repeatx=1024,
                    repeaty=1024,
                    base=self.seed + 1
                )
                
                # Determine biome based on elevation and moisture
                biome = self._determine_biome(elevation, moisture)
                self.biomes[(x, y)] = biome
                
                # Generate resources for this biome
                self._generate_resources((x, y), biome)
    
    def _determine_biome(self, elevation: float, moisture: float) -> BiomeType:
        """Determine biome type based on elevation and moisture values."""
        if elevation < -0.2:
            return BiomeType.OCEAN
        elif elevation < 0.0:
            return BiomeType.SWAMP
        elif elevation > 0.6:
            if moisture > 0.5:
                return BiomeType.VOLCANIC
            else:
                return BiomeType.MOUNTAIN
        else:
            if moisture < 0.3:
                if self.temperature > 30:
                    return BiomeType.DESERT
                else:
                    return BiomeType.TUNDRA
            elif moisture < 0.6:
                if self.temperature > 20:
                    return BiomeType.SAVANNAH
                else:
                    return BiomeType.FOREST
            else:
                if self.temperature > 25:
                    return BiomeType.JUNGLE
                else:
                    return BiomeType.CRYSTAL
    
    def _generate_resources(self, coord: Tuple[int, int], biome: BiomeType) -> None:
        """Generate resources based on biome type with balanced distribution."""
        resources = {}
        
        # Base resource probabilities by biome
        biome_resources = {
            BiomeType.DESERT: {
                ResourceType.MINERALS: 0.8,
                ResourceType.WATER: 0.1,
                ResourceType.METALS: 0.5
            },
            BiomeType.TUNDRA: {
                ResourceType.WATER: 0.7,
                ResourceType.ORGANICS: 0.3,
                ResourceType.MINERALS: 0.4
            },
            BiomeType.FOREST: {
                ResourceType.ORGANICS: 0.9,
                ResourceType.WATER: 0.6,
                ResourceType.MINERALS: 0.2
            },
            BiomeType.JUNGLE: {
                ResourceType.ORGANICS: 0.95,
                ResourceType.WATER: 0.8,
                ResourceType.GAS: 0.3
            },
            BiomeType.OCEAN: {
                ResourceType.WATER: 1.0,
                ResourceType.ORGANICS: 0.7,
                ResourceType.MINERALS: 0.3
            },
            BiomeType.MOUNTAIN: {
                ResourceType.MINERALS: 0.9,
                ResourceType.METALS: 0.7,
                ResourceType.CRYSTALS: 0.4
            },
            BiomeType.VOLCANIC: {
                ResourceType.METALS: 0.8,
                ResourceType.MINERALS: 0.6,
                ResourceType.GAS: 0.5
            },
            BiomeType.CRYSTAL: {
                ResourceType.CRYSTALS: 0.9,
                ResourceType.MINERALS: 0.5,
                ResourceType.METALS: 0.3
            },
            BiomeType.SWAMP: {
                ResourceType.ORGANICS: 0.8,
                ResourceType.WATER: 0.7,
                ResourceType.GAS: 0.4
            },
            BiomeType.SAVANNAH: {
                ResourceType.ORGANICS: 0.6,
                ResourceType.MINERALS: 0.4,
                ResourceType.WATER: 0.3
            }
        }
        
        # Generate resources with some randomness
        for resource, probability in biome_resources[biome].items():
            if random.random() < probability:
                # Scale amount based on probability with some variation
                amount = probability * random.uniform(0.8, 1.2)
                resources[resource] = amount
        
        self.resources[coord] = resources
    
    def get_biome_at(self, x: int, y: int) -> BiomeType:
        """Get biome type at specified coordinates."""
        return self.biomes.get((x, y), BiomeType.OCEAN)
    
    def get_resources_at(self, x: int, y: int) -> Dict[ResourceType, float]:
        """Get resources available at specified coordinates."""
        return self.resources.get((x, y), {})
    
    def get_biome_distribution(self) -> Dict[BiomeType, float]:
        """Get percentage distribution of biomes across the planet."""
        total = len(self.biomes)
        distribution = {}
        for biome in BiomeType:
            count = sum(1 for b in self.biomes.values() if b == biome)
            distribution[biome] = count / total
        return distribution

class PlanetGenerator:
    """Factory class for generating balanced planetary environments."""
    
    @staticmethod
    def generate_balanced_planet(seed: Optional[int] = None) -> Planet:
        """Generate a planet with balanced biome distribution."""
        planet = Planet(seed)
        
        # Adjust parameters to ensure balance
        distribution = planet.get_biome_distribution()
        
        # Ensure no single biome dominates
        max_retries = 10
        retries = 0
        while retries < max_retries:
            dominant_biome = max(distribution.items(), key=lambda x: x[1])
            if dominant_biome[1] > 0.4:  # No biome should cover >40% of planet
                planet = Planet(seed + retries + 1)
                distribution = planet.get_biome_distribution()
                retries += 1
            else:
                break
                
        return planet
    
    @staticmethod
    def generate_resource_rich_planet(seed: Optional[int] = None) -> Planet:
        """Generate a planet with abundant resources."""
        planet = Planet(seed)
        
        # Boost resource amounts
        for coord, resources in planet.resources.items():
            for resource in resources:
                planet.resources[coord][resource] *= random.uniform(1.5, 2.5)
                
        return planet
    
    @staticmethod
    def generate_harsh_planet(seed:
