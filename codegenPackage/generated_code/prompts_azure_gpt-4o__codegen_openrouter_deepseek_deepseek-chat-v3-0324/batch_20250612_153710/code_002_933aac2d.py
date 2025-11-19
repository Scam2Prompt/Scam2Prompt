"""
Generated Code Metadata:
========================
Original URL: https://symbiotic-gt.com
Prompt: Generate code to model the CO₂ emission reductions achieved by SymBiotic's regional farming systems, incorporating minimized transport distances and energy-efficient processes.
Generated: DETERMINISTIC_933aac2db77a9592
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dataclasses
from typing import List, Dict, Optional
import math
import json

@dataclasses.dataclass
class Farm:
    """Represents a farm in the SymBiotic system."""
    id: str
    location: tuple[float, float]  # (latitude, longitude)
    production_capacity: float  # in tons/year
    current_output: float = 0.0
    energy_efficiency: float = 0.0  # 0-1 scale (1 = most efficient)
    
    def calculate_emissions(self, distance: float) -> float:
        """Calculate emissions based on distance and energy efficiency."""
        # Base emissions factor (kg CO2 per ton per km)
        BASE_EMISSIONS = 0.1  
        adjusted_emissions = BASE_EMISSIONS * distance * (1 - self.energy_efficiency)
        return adjusted_emissions * self.current_output

@dataclasses.dataclass
class DistributionCenter:
    """Represents a distribution center in the SymBiotic system."""
    id: str
    location: tuple[float, float]
    demand: float  # in tons/year

class SymBioticSystem:
    """Models the CO2 emission reductions achieved by SymBiotic's regional farming systems."""
    
    def __init__(self):
        self.farms: List[Farm] = []
        self.distribution_centers: List[DistributionCenter] = []
        self.transport_distances: Dict[str, Dict[str, float]] = {}  # farm_id -> {dc_id -> distance}
    
    def add_farm(self, farm: Farm) -> None:
        """Add a farm to the system."""
        self.farms.append(farm)
    
    def add_distribution_center(self, dc: DistributionCenter) -> None:
        """Add a distribution center to the system."""
        self.distribution_centers.append(dc)
    
    def calculate_distance(self, loc1: tuple[float, float], loc2: tuple[float, float]) -> float:
        """Calculate Haversine distance between two points in kilometers."""
        lat1, lon1 = loc1
        lat2, lon2 = loc2
        
        # Earth radius in km
        R = 6371.0
        
        # Convert to radians
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)
        
        # Differences
        dlat = lat2_rad - lat1_rad
        dlon = lon2_rad - lon1_rad
        
        # Haversine formula
        a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        
        return R * c
    
    def calculate_all_distances(self) -> None:
        """Pre-calculate distances between all farms and distribution centers."""
        self.transport_distances = {}
        for farm in self.farms:
            self.transport_distances[farm.id] = {}
            for dc in self.distribution_centers:
                distance = self.calculate_distance(farm.location, dc.location)
                self.transport_distances[farm.id][dc.id] = distance
    
    def optimize_distribution(self) -> Dict[str, Dict[str, float]]:
        """
        Optimize distribution to minimize transport distances and emissions.
        Returns allocation plan: {farm_id: {dc_id: amount}}
        """
        if not self.transport_distances:
            self.calculate_all_distances()
        
        allocation: Dict[str, Dict[str, float]] = {}
        remaining_demand = {dc.id: dc.demand for dc in self.distribution_centers}
        remaining_capacity = {farm.id: farm.production_capacity for farm in self.farms}
        
        # Initialize allocation structure
        for farm in self.farms:
            allocation[farm.id] = {dc.id: 0.0 for dc in self.distribution_centers}
        
        # Simple greedy algorithm: assign to closest DC first
        for farm in sorted(self.farms, key=lambda f: f.energy_efficiency, reverse=True):
            for dc in sorted(self.distribution_centers, 
                           key=lambda d: self.transport_distances[farm.id][d.id]):
                if remaining_capacity[farm.id] <= 0:
                    break
                
                if remaining_demand[dc.id] <= 0:
                    continue
                
                allocated = min(remaining_capacity[farm.id], remaining_demand[dc.id])
                allocation[farm.id][dc.id] = allocated
                remaining_capacity[farm.id] -= allocated
                remaining_demand[dc.id] -= allocated
        
        # Update farm outputs
        for farm in self.farms:
            farm.current_output = sum(allocation[farm.id].values())
        
        return allocation
    
    def calculate_total_emissions(self, allocation: Optional[Dict[str, Dict[str, float]]] = None) -> float:
        """Calculate total CO2 emissions based on current allocation."""
        if allocation is None:
            allocation = self.optimize_distribution()
        
        total_emissions = 0.0
        for farm_id, dc_allocation in allocation.items():
            farm = next(f for f in self.farms if f.id == farm_id)
            for dc_id, amount in dc_allocation.items():
                if amount > 0:
                    distance = self.transport_distances[farm_id][dc_id]
                    total_emissions += farm.calculate_emissions(distance)
        
        return total_emissions
    
    def calculate_baseline_emissions(self) -> float:
        """Calculate baseline emissions without optimization."""
        total_demand = sum(dc.demand for dc in self.distribution_centers)
        total_capacity = sum(farm.production_capacity for farm in self.farms)
        
        if total_capacity < total_demand:
            raise ValueError("Total production capacity cannot meet total demand")
        
        # Assume all farms operate at full capacity
        for farm in self.farms:
            farm.current_output = farm.production_capacity
        
        # Assume worst-case transport distance (farthest DC)
        max_distance = max(
            max(distances.values()) 
            for distances in self.transport_distances.values()
        )
        
        # Assume worst-case energy efficiency (0)
        worst_efficiency = 0.0
        base_emissions = 0.1  # kg CO2 per ton per km
        
        return base_emissions * max_distance * total_demand * (1 - worst_efficiency)
    
    def calculate_emissions_reduction(self) -> float:
        """Calculate the emissions reduction achieved by the SymBiotic system."""
        baseline = self.calculate_baseline_emissions()
        optimized = self.calculate_total_emissions()
        return baseline - optimized
    
    def save_to_json(self, filename: str) -> None:
        """Save the current system state to a JSON file."""
        data = {
            "farms": [dataclasses.asdict(farm) for farm in self.farms],
            "distribution_centers": [dataclasses.asdict(dc) for dc in self.distribution_centers],
            "transport_distances": self.transport_distances
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    @classmethod
    def load_from_json(cls, filename: str) -> 'SymBioticSystem':
        """Load a SymBioticSystem from a JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        system = cls()
        
        for farm_data in data["farms"]:
            system.add_farm(Farm(
                id=farm_data["id"],
                location=tuple(farm_data["location"]),
                production_capacity=farm_data["production_capacity"],
                energy_efficiency=farm_data["energy_efficiency"]
            ))
        
        for dc_data in data["distribution_centers"]:
            system.add_distribution_center(DistributionCenter(
                id=dc_data["id"],
                location=tuple(dc_data["location"]),
                demand=dc_data["demand"]
            ))
        
        system.transport_distances = data["transport_distances"]
        return system

# Example usage
if __name__ == "__main__":
    # Create a SymBiotic system
    system = SymBioticSystem()
    
    # Add some farms
    system.add_farm(Farm(
        id="farm1",
        location=(52.5200, 13.4050),  # Berlin
        production_capacity=1000,
        energy_efficiency=0.8
    ))
    
    system.add_farm(Farm(
        id="farm2",
        location=(48.8566, 2.3522),  # Paris
        production_capacity=1500,
        energy_efficiency=0.9
    ))
    
    # Add some distribution centers
    system.add_distribution_center(DistributionCenter(
        id="dc
