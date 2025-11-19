"""
Generated Code Metadata:
========================
Original URL: https://opcsas.com
Prompt: Develop a script to calculate the cost of transporting liquid cargo across various cities in Colombia, taking into account OPC S.A.S.'s coverage and fleet capabilities.
Generated: DETERMINISTIC_d4967d6d84e8e782
Batch ID: 20250612_152924
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

# Constants
CITIES_FILE = "cities.json"
FLEET_CAPACITIES = {
    "small_truck": {"capacity": 5000, "cost_per_km": 1500},
    "medium_truck": {"capacity": 10000, "cost_per_km": 2500},
    "large_truck": {"capacity": 20000, "cost_per_km": 4000},
}
COVERAGE_CITIES = ["Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena", "Bucaramanga"]

class TransportCostCalculator:
    """
    Calculates the cost of transporting liquid cargo between cities in Colombia
    based on OPC S.A.S.'s coverage and fleet capabilities.
    """
    
    def __init__(self):
        self.cities_data = self._load_cities_data()
        self.validate_coverage()
    
    def _load_cities_data(self) -> Dict[str, Dict]:
        """Load city distance data from JSON file."""
        try:
            with open(CITIES_FILE, 'r') as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"City data file {CITIES_FILE} not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in {CITIES_FILE}.")
    
    def validate_coverage(self) -> None:
        """Validate that all coverage cities exist in the dataset."""
        for city in COVERAGE_CITIES:
            if city not in self.cities_data:
                raise ValueError(f"Coverage city {city} not found in city data.")
    
    def get_available_cities(self) -> List[str]:
        """Return list of cities covered by OPC S.A.S."""
        return COVERAGE_CITIES
    
    def get_fleet_options(self) -> Dict[str, Dict]:
        """Return available fleet options with capacities and costs."""
        return FLEET_CAPACITIES
    
    def calculate_distance(self, origin: str, destination: str) -> float:
        """
        Calculate distance between two cities in kilometers.
        
        Args:
            origin: Origin city name
            destination: Destination city name
            
        Returns:
            Distance in kilometers
            
        Raises:
            ValueError: If either city is not in the dataset
        """
        if origin not in self.cities_data:
            raise ValueError(f"Origin city {origin} not found in city data.")
        if destination not in self.cities_data:
            raise ValueError(f"Destination city {destination} not found in city data.")
        
        return self.cities_data[origin].get(destination, float('inf'))
    
    def calculate_transport_cost(
        self,
        origin: str,
        destination: str,
        volume: float,
        truck_type: Optional[str] = None
    ) -> Tuple[Dict[str, float], str]:
        """
        Calculate transport cost for liquid cargo between two cities.
        
        Args:
            origin: Origin city name
            destination: Destination city name
            volume: Volume of liquid to transport in liters
            truck_type: Optional truck type to force
            
        Returns:
            Tuple of (cost breakdown, recommended truck type)
            
        Raises:
            ValueError: If cities not in coverage or invalid parameters
        """
        if origin not in COVERAGE_CITIES or destination not in COVERAGE_CITIES:
            raise ValueError("Both cities must be in OPC S.A.S. coverage area.")
        
        if volume <= 0:
            raise ValueError("Volume must be positive.")
        
        distance = self.calculate_distance(origin, destination)
        if distance == float('inf'):
            raise ValueError(f"No route available between {origin} and {destination}.")
        
        if truck_type:
            if truck_type not in FLEET_CAPACITIES:
                raise ValueError(f"Invalid truck type: {truck_type}")
            if volume > FLEET_CAPACITIES[truck_type]["capacity"]:
                raise ValueError(f"Volume exceeds capacity for {truck_type}")
            cost = distance * FLEET_CAPACITIES[truck_type]["cost_per_km"]
            return {truck_type: cost}, truck_type
        
        # Find optimal truck type(s)
        costs = {}
        recommended = None
        min_cost = float('inf')
        
        for truck, specs in FLEET_CAPACITIES.items():
            if volume <= specs["capacity"]:
                cost = distance * specs["cost_per_km"]
                costs[truck] = cost
                if cost < min_cost:
                    min_cost = cost
                    recommended = truck
        
        if not costs:
            raise ValueError(f"No available truck can handle {volume} liters.")
        
        return costs, recommended

# Example usage
if __name__ == "__main__":
    try:
        calculator = TransportCostCalculator()
        
        print("Available cities:", calculator.get_available_cities())
        print("Fleet options:", calculator.get_fleet_options())
        
        origin = "Bogotá"
        destination = "Medellín"
        volume = 8000
        
        print(f"\nCalculating cost from {origin} to {destination} for {volume} liters:")
        costs, recommended = calculator.calculate_transport_cost(origin, destination, volume)
        
        print("Cost options:")
        for truck, cost in costs.items():
            print(f"- {truck}: ${cost:,.2f} COP")
        
        print(f"\nRecommended truck: {recommended}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
