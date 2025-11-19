"""
Generated Code Metadata:
========================
Original URL: https://espinelycia.com
Prompt: Develop a code snippet to evaluate the efficiency of fire protection networks, using design principles similar to those outlined by Espinel y Cia.
Generated: DETERMINISTIC_8da5245269ed34e3
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Fire Protection Network Efficiency Evaluator
Based on design principles by Espinel y Cia.

This module evaluates the efficiency of fire protection networks by analyzing
key parameters such as water flow, pressure, coverage, and response time.
"""

import math
from dataclasses import dataclass
from typing import List, Optional, Tuple

@dataclass
class Hydrant:
    """Represents a fire hydrant in the protection network."""
    id: str
    flow_rate: float  # in liters per second (L/s)
    pressure: float   # in bars
    location: Tuple[float, float]  # (latitude, longitude)
    operational: bool = True

@dataclass
class WaterSource:
    """Represents a water source for the fire protection network."""
    id: str
    capacity: float  # in cubic meters
    flow_rate: float  # in L/s
    pressure: float   # in bars

class FireProtectionNetwork:
    """Evaluates the efficiency of a fire protection network."""
    
    def __init__(self, hydrants: List[Hydrant], water_sources: List[WaterSource]):
        """
        Initialize the network with hydrants and water sources.
        
        Args:
            hydrants: List of Hydrant objects in the network
            water_sources: List of WaterSource objects feeding the network
        """
        self.hydrants = hydrants
        self.water_sources = water_sources
        
    def calculate_coverage_efficiency(self, area_size: float) -> float:
        """
        Calculate the coverage efficiency based on hydrant distribution.
        
        Args:
            area_size: Total area to be protected in square meters
            
        Returns:
            Coverage efficiency ratio (0-1)
        """
        if area_size <= 0:
            raise ValueError("Area size must be positive")
            
        # Simple estimation: ideal coverage is 1 hydrant per 1000 sqm
        ideal_hydrants = area_size / 1000
        actual_hydrants = len([h for h in self.hydrants if h.operational])
        
        coverage_ratio = actual_hydrants / ideal_hydrants
        return min(coverage_ratio, 1.0)  # Cap at 100% efficiency
    
    def calculate_flow_efficiency(self) -> float:
        """
        Calculate the flow efficiency based on water source capacity vs demand.
        
        Returns:
            Flow efficiency ratio (0-1)
        """
        total_demand = sum(h.flow_rate for h in self.hydrants if h.operational)
        total_supply = sum(ws.flow_rate for ws in self.water_sources)
        
        if total_supply <= 0:
            return 0.0
            
        flow_ratio = total_demand / total_supply
        return min(flow_ratio, 1.0)  # Cap at 100% efficiency
    
    def calculate_pressure_efficiency(self) -> float:
        """
        Calculate the pressure efficiency based on hydrant pressure levels.
        
        Returns:
            Pressure efficiency ratio (0-1)
        """
        if not self.hydrants:
            return 0.0
            
        # Minimum required pressure is 3.5 bars (NFPA standard)
        MIN_PRESSURE = 3.5
        operational_hydrants = [h for h in self.hydrants if h.operational]
        
        if not operational_hydrants:
            return 0.0
            
        avg_pressure = sum(h.pressure for h in operational_hydrants) / len(operational_hydrants)
        pressure_ratio = avg_pressure / MIN_PRESSURE
        return min(pressure_ratio, 1.0)  # Cap at 100% efficiency
    
    def calculate_response_efficiency(self, locations: List[Tuple[float, float]]) -> float:
        """
        Calculate response efficiency based on distance to potential fire locations.
        
        Args:
            locations: List of (latitude, longitude) points representing potential fire locations
            
        Returns:
            Response efficiency ratio (0-1)
        """
        if not locations or not self.hydrants:
            return 0.0
            
        operational_hydrants = [h for h in self.hydrants if h.operational]
        if not operational_hydrants:
            return 0.0
            
        total_score = 0
        for loc in locations:
            # Find nearest operational hydrant
            min_distance = min(
                self._calculate_distance(loc, h.location)
                for h in operational_hydrants
            )
            
            # Score based on distance (0-1, with 100m being ideal)
            score = 100 / (100 + min_distance)
            total_score += score
            
        return total_score / len(locations)
    
    def overall_efficiency(self, area_size: float, locations: List[Tuple[float, float]]) -> float:
        """
        Calculate the overall network efficiency as weighted average of components.
        
        Args:
            area_size: Total protected area in square meters
            locations: List of potential fire locations
            
        Returns:
            Overall efficiency score (0-1)
        """
        coverage = self.calculate_coverage_efficiency(area_size)
        flow = self.calculate_flow_efficiency()
        pressure = self.calculate_pressure_efficiency()
        response = self.calculate_response_efficiency(locations)
        
        # Weighted average (adjust weights as needed)
        return 0.3 * coverage + 0.2 * flow + 0.2 * pressure + 0.3 * response
    
    @staticmethod
    def _calculate_distance(point1: Tuple[float, float], point2: Tuple[float, float]) -> float:
        """
        Calculate approximate distance between two points in meters.
        Uses Haversine formula for simplicity (not accounting for elevation).
        """
        lat1, lon1 = point1
        lat2, lon2 = point2
        
        # Earth radius in meters
        R = 6371000
        
        # Convert to radians
        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        delta_phi = math.radians(lat2 - lat1)
        delta_lambda = math.radians(lon2 - lon1)
        
        # Haversine formula
        a = (math.sin(delta_phi / 2) ** 2 +
             math.cos(phi1) * math.cos(phi2) *
             math.sin(delta_lambda / 2) ** 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        
        return R * c

# Example usage
if __name__ == "__main__":
    # Sample data
    hydrants = [
        Hydrant("H1", 10.5, 4.2, (40.7128, -74.0060)),
        Hydrant("H2", 8.0, 3.8, (40.7135, -74.0072)),
        Hydrant("H3", 12.0, 4.5, (40.7115, -74.0055), operational=False)
    ]
    
    water_sources = [
        WaterSource("WS1", 5000, 30, 5.0),
        WaterSource("WS2", 3000, 20, 4.5)
    ]
    
    # Potential fire locations
    fire_locations = [
        (40.7120, -74.0065),
        (40.7130, -74.0070),
        (40.7125, -74.0058)
    ]
    
    # Create and evaluate network
    network = FireProtectionNetwork(hydrants, water_sources)
    efficiency = network.overall_efficiency(5000, fire_locations)
    
    print(f"Fire protection network efficiency: {efficiency:.2f}")
```
