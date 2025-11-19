"""
Generated Code Metadata:
========================
Original URL: https://graffian.com
Prompt: Write a short program to calculate the environmental impact of sourcing cooking oils from various regions, considering factors like carbon footprint and fair trade practices.
Generated: DETERMINISTIC_c67920ad605f2b25
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class OilSource:
    """Represents a source of cooking oil with environmental and trade attributes."""
    region: str
    carbon_footprint_kg_per_liter: float  # CO2 equivalent per liter of oil
    is_fair_trade: bool
    transport_distance_km: float  # Average distance to transport to market

class OilImpactCalculator:
    """Calculates environmental impact of cooking oil sources."""
    
    def __init__(self, oil_sources: List[OilSource]):
        self.oil_sources = oil_sources
    
    def calculate_impact(self, oil_volume_liters: float) -> Dict[str, Dict[str, float]]:
        """
        Calculates environmental impact for each oil source.
        
        Args:
            oil_volume_liters: Total volume of oil in liters to calculate impact for.
            
        Returns:
            Dictionary with region as key and impact metrics as values.
        """
        if oil_volume_liters <= 0:
            raise ValueError("Oil volume must be positive")
            
        results = {}
        for source in self.oil_sources:
            total_carbon = source.carbon_footprint_kg_per_liter * oil_volume_liters
            transport_carbon = self._calculate_transport_carbon(source.transport_distance_km, oil_volume_liters)
            
            results[source.region] = {
                "total_carbon_kg": total_carbon + transport_carbon,
                "carbon_per_liter_kg": source.carbon_footprint_kg_per_liter,
                "transport_carbon_kg": transport_carbon,
                "fair_trade": source.is_fair_trade
            }
        
        return results
    
    def _calculate_transport_carbon(self, distance_km: float, volume_liters: float) -> float:
        """
        Calculates transport carbon footprint using average values for freight transport.
        
        Args:
            distance_km: Transport distance in kilometers
            volume_liters: Volume being transported in liters
            
        Returns:
            Carbon footprint in kg CO2 equivalent
        """
        # Average carbon footprint for freight transport (kg CO2 per ton-km)
        CARBON_PER_TON_KM = 0.1
        # Average density of cooking oil (kg/liter)
        OIL_DENSITY_KG_PER_LITER = 0.92
        
        weight_kg = volume_liters * OIL_DENSITY_KG_PER_LITER
        weight_tons = weight_kg / 1000
        return distance_km * weight_tons * CARBON_PER_TON_KM
    
    def find_lowest_impact(self, oil_volume_liters: float) -> Dict[str, Optional[str]]:
        """
        Identifies the source with lowest carbon impact.
        
        Args:
            oil_volume_liters: Volume to base calculation on
            
        Returns:
            Dictionary with best region and its carbon impact
        """
        impacts = self.calculate_impact(oil_volume_liters)
        if not impacts:
            return {"region": None, "total_carbon_kg": None}
            
        best_region = min(impacts.items(), key=lambda x: x[1]["total_carbon_kg"])
        return {
            "region": best_region[0],
            "total_carbon_kg": best_region[1]["total_carbon_kg"]
        }

def load_sources_from_json(filepath: str) -> List[OilSource]:
    """
    Loads oil source data from JSON file.
    
    Args:
        filepath: Path to JSON file containing source data
        
    Returns:
        List of OilSource objects
        
    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If file is malformed
    """
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return [OilSource(**item) for item in data]
    except FileNotFoundError:
        raise FileNotFoundError(f"Source file not found: {filepath}")
    except (json.JSONDecodeError, TypeError) as e:
        raise ValueError(f"Invalid source data format: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Load sample data (in production, this would be from a config file)
        sources = [
            OilSource("Southeast Asia", 2.5, False, 8000),
            OilSource("Mediterranean", 1.8, True, 2000),
            OilSource("South America", 2.2, True, 6000)
        ]
        
        calculator = OilImpactCalculator(sources)
        
        # Calculate impact for 1000 liters
        impacts = calculator.calculate_impact(1000)
        print("Environmental Impact for 1000 liters:")
        for region, data in impacts.items():
            print(f"{region}: {data}")
        
        # Find best option
        best = calculator.find_lowest_impact(1000)
        print(f"\nBest option: {best['region']} with {best['total_carbon_kg']:.2f} kg CO2")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
