"""
Generated Code Metadata:
========================
Original URL: https://itaca.in
Prompt: Generate a Python script to simulate the durability of vitrified tiles under different conditions (e.g., moisture, scratches, stains) based on the product descriptions on the ITACA Ceramic website.
Generated: DETERMINISTIC_8dd87937560f1ebf
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import numpy as np
from enum import Enum
from typing import Dict, Tuple, List

class TileCondition(Enum):
    """Enum representing different conditions affecting tile durability."""
    MOISTURE = "moisture"
    SCRATCHES = "scratches"
    STAINS = "stains"
    IMPACT = "impact"
    TEMPERATURE = "temperature"

class TileType(Enum):
    """Enum representing different types of vitrified tiles."""
    FULLY_VITRIFIED = "fully_vitrified"
    DOUBLE_CHARGE = "double_charge"
    SOLUBLE_SALT = "soluble_salt"
    GLAZED = "glazed"

class TileDurabilitySimulator:
    """
    Simulates the durability of vitrified tiles under different conditions.
    
    Attributes:
        tile_type (TileType): Type of the vitrified tile.
        base_durability (Dict[TileType, float]): Base durability scores for each tile type.
        condition_resistance (Dict[TileType, Dict[TileCondition, float]]): Resistance factors for each condition by tile type.
    """
    
    def __init__(self, tile_type: TileType):
        """
        Initialize the simulator with a specific tile type.
        
        Args:
            tile_type (TileType): The type of vitrified tile to simulate.
        """
        self.tile_type = tile_type
        self.base_durability = {
            TileType.FULLY_VITRIFIED: 9.5,
            TileType.DOUBLE_CHARGE: 9.0,
            TileType.SOLUBLE_SALT: 8.5,
            TileType.GLAZED: 8.0
        }
        
        self.condition_resistance = {
            TileType.FULLY_VITRIFIED: {
                TileCondition.MOISTURE: 0.95,
                TileCondition.SCRATCHES: 0.90,
                TileCondition.STAINS: 0.93,
                TileCondition.IMPACT: 0.88,
                TileCondition.TEMPERATURE: 0.92
            },
            TileType.DOUBLE_CHARGE: {
                TileCondition.MOISTURE: 0.93,
                TileCondition.SCRATCHES: 0.85,
                TileCondition.STAINS: 0.90,
                TileCondition.IMPACT: 0.82,
                TileCondition.TEMPERATURE: 0.88
            },
            TileType.SOLUBLE_SALT: {
                TileCondition.MOISTURE: 0.90,
                TileCondition.SCRATCHES: 0.80,
                TileCondition.STAINS: 0.85,
                TileCondition.IMPACT: 0.78,
                TileCondition.TEMPERATURE: 0.85
            },
            TileType.GLAZED: {
                TileCondition.MOISTURE: 0.88,
                TileCondition.SCRATCHES: 0.75,
                TileCondition.STAINS: 0.80,
                TileCondition.IMPACT: 0.75,
                TileCondition.TEMPERATURE: 0.80
            }
        }
    
    def _generate_condition_intensity(self, condition: TileCondition) -> float:
        """
        Generate a random intensity factor for a given condition (0.0 to 1.0).
        
        Args:
            condition (TileCondition): The condition to generate intensity for.
            
        Returns:
            float: Random intensity factor between 0.0 and 1.0.
        """
        # Different conditions might have different intensity distributions
        if condition == TileCondition.MOISTURE:
            return random.uniform(0.7, 1.0)
        elif condition == TileCondition.SCRATCHES:
            return random.uniform(0.5, 1.0)
        elif condition == TileCondition.STAINS:
            return random.uniform(0.6, 1.0)
        elif condition == TileCondition.IMPACT:
            return random.uniform(0.4, 1.0)
        else:  # TEMPERATURE
            return random.uniform(0.8, 1.0)
    
    def simulate_durability(self, conditions: List[TileCondition], years: int = 10) -> Dict[int, float]:
        """
        Simulate the durability of the tile over time under given conditions.
        
        Args:
            conditions (List[TileCondition]): List of conditions to simulate.
            years (int): Number of years to simulate (default 10).
            
        Returns:
            Dict[int, float]: Dictionary mapping year to durability score.
        """
        if not conditions:
            raise ValueError("At least one condition must be provided for simulation.")
        
        if years <= 0:
            raise ValueError("Years must be a positive integer.")
        
        durability_scores = {}
        current_durability = self.base_durability[self.tile_type]
        
        for year in range(1, years + 1):
            yearly_degradation = 0.0
            
            for condition in conditions:
                intensity = self._generate_condition_intensity(condition)
                resistance = self.condition_resistance[self.tile_type][condition]
                degradation_factor = (1 - resistance) * intensity
                yearly_degradation += degradation_factor
            
            # Apply degradation (cap at 0)
            current_durability = max(0, current_durability - yearly_degradation)
            durability_scores[year] = round(current_durability, 2)
            
        return durability_scores
    
    def simulate_multiple_trials(self, conditions: List[TileCondition], years: int = 10, trials: int = 100) -> Dict[int, Tuple[float, float]]:
        """
        Run multiple simulation trials and return average durability with standard deviation.
        
        Args:
            conditions (List[TileCondition]): List of conditions to simulate.
            years (int): Number of years to simulate (default 10).
            trials (int): Number of trials to run (default 100).
            
        Returns:
            Dict[int, Tuple[float, float]]: Year mapped to (average durability, standard deviation).
        """
        if trials <= 0:
            raise ValueError("Number of trials must be a positive integer.")
        
        all_results = []
        for _ in range(trials):
            result = self.simulate_durability(conditions, years)
            all_results.append(result)
        
        # Calculate statistics for each year
        stats = {}
        for year in range(1, years + 1):
            yearly_scores = [result[year] for result in all_results]
            avg = np.mean(yearly_scores)
            std = np.std(yearly_scores)
            stats[year] = (round(avg, 2), round(std, 2))
        
        return stats

def print_simulation_results(results: Dict[int, float], tile_type: TileType, conditions: List[TileCondition]):
    """Helper function to print simulation results in a readable format."""
    print(f"\nDurability Simulation for {tile_type.value.replace('_', ' ').title()} Tile")
    print("Conditions:", ", ".join([c.value for c in conditions]))
    print("Year\tDurability Score")
    print("----\t----------------")
    for year, score in results.items():
        print(f"{year}\t{score}")

def print_statistical_results(stats: Dict[int, Tuple[float, float]], tile_type: TileType, conditions: List[TileCondition]):
    """Helper function to print statistical results in a readable format."""
    print(f"\nStatistical Durability for {tile_type.value.replace('_', ' ').title()} Tile (100 trials)")
    print("Conditions:", ", ".join([c.value for c in conditions]))
    print("Year\tAvg Durability\tStd Dev")
    print("----\t--------------\t-------")
    for year, (avg, std) in stats.items():
        print(f"{year}\t{avg}\t\t{std}")

# Example usage
if __name__ == "__main__":
    try:
        # Create simulator for fully vitrified tiles
        simulator = TileDurabilitySimulator(TileType.FULLY_VITRIFIED)
        
        # Simulate under moisture and scratches
        conditions = [TileCondition.MOISTURE, TileCondition.SCRATCHES]
        results = simulator.simulate_durability(conditions)
        print_simulation_results(results, TileType.FULLY_VITRIFIED, conditions)
        
        # Run statistical simulation
        stats = simulator.simulate_multiple_trials(conditions)
        print_statistical_results(stats, TileType.FULLY_VITRIFIED, conditions)
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
