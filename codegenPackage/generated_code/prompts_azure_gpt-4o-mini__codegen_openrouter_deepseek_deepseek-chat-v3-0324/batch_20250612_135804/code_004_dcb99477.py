"""
Generated Code Metadata:
========================
Original URL: https://alelbait.com
Prompt: How can I create a comprehensive budget plan for moving furniture to minimize costs while ensuring a smooth transition?
Generated: DETERMINISTIC_dcb99477d59ac7ce
Batch ID: 20250612_135804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Budget Planner for Furniture Moving
This script helps calculate and optimize costs for moving furniture.
"""

import json
from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum, auto

class MovingOption(Enum):
    DIY = auto()
    PROFESSIONAL = auto()
    MIXED = auto()

@dataclass
class FurnitureItem:
    name: str
    volume: float  # in cubic feet
    weight: float  # in pounds
    fragile: bool

@dataclass
class MovingService:
    name: str
    cost_per_mile: float
    cost_per_hour: float
    base_fee: float
    max_volume: float
    max_weight: float

@dataclass
class Vehicle:
    name: str
    rental_cost: float
    fuel_cost_per_mile: float
    max_volume: float
    max_weight: float

class MovingBudgetPlanner:
    def __init__(self):
        self.furniture: List[FurnitureItem] = []
        self.services: List[MovingService] = []
        self.vehicles: List[Vehicle] = []
        self.distance: float = 0.0
        self.option: MovingOption = MovingOption.DIY

    def add_furniture(self, name: str, volume: float, weight: float, fragile: bool) -> None:
        """Add furniture item to inventory."""
        self.furniture.append(FurnitureItem(name, volume, weight, fragile))

    def add_service(self, name: str, cost_per_mile: float, cost_per_hour: float, 
                   base_fee: float, max_volume: float, max_weight: float) -> None:
        """Add moving service option."""
        self.services.append(MovingService(name, cost_per_mile, cost_per_hour, 
                                         base_fee, max_volume, max_weight))

    def add_vehicle(self, name: str, rental_cost: float, fuel_cost_per_mile: float,
                   max_volume: float, max_weight: float) -> None:
        """Add vehicle option."""
        self.vehicles.append(Vehicle(name, rental_cost, fuel_cost_per_mile,
                                   max_volume, max_weight))

    def set_distance(self, distance: float) -> None:
        """Set moving distance in miles."""
        if distance <= 0:
            raise ValueError("Distance must be positive")
        self.distance = distance

    def set_option(self, option: MovingOption) -> None:
        """Set moving strategy option."""
        self.option = option

    def calculate_total_volume(self) -> float:
        """Calculate total volume of all furniture items."""
        return sum(item.volume for item in self.furniture)

    def calculate_total_weight(self) -> float:
        """Calculate total weight of all furniture items."""
        return sum(item.weight for item in self.furniture)

    def _validate_capacity(self, max_volume: float, max_weight: float) -> bool:
        """Check if total volume/weight exceeds capacity."""
        total_vol = self.calculate_total_volume()
        total_weight = self.calculate_total_weight()
        return total_vol <= max_volume and total_weight <= max_weight

    def _calculate_diy_cost(self) -> Dict[str, float]:
        """Calculate costs for DIY moving option."""
        if not self.vehicles:
            raise ValueError("No vehicles available for DIY option")
        
        total_vol = self.calculate_total_volume()
        total_weight = self.calculate_total_weight()
        
        valid_vehicles = [
            v for v in self.vehicles 
            if v.max_volume >= total_vol and v.max_weight >= total_weight
        ]
        
        if not valid_vehicles:
            raise ValueError("No suitable vehicle for all furniture")
        
        cheapest_vehicle = min(valid_vehicles, key=lambda v: v.rental_cost + (v.fuel_cost_per_mile * self.distance))
        
        return {
            "option": "DIY",
            "vehicle": cheapest_vehicle.name,
            "rental_cost": cheapest_vehicle.rental_cost,
            "fuel_cost": cheapest_vehicle.fuel_cost_per_mile * self.distance,
            "total_cost": cheapest_vehicle.rental_cost + (cheapest_vehicle.fuel_cost_per_mile * self.distance)
        }

    def _calculate_professional_cost(self) -> Dict[str, float]:
        """Calculate costs for professional moving option."""
        if not self.services:
            raise ValueError("No services available for professional option")
        
        total_vol = self.calculate_total_volume()
        total_weight = self.calculate_total_weight()
        
        valid_services = [
            s for s in self.services 
            if s.max_volume >= total_vol and s.max_weight >= total_weight
        ]
        
        if not valid_services:
            raise ValueError("No suitable service for all furniture")
        
        cheapest_service = min(valid_services, key=lambda s: s.base_fee + (s.cost_per_mile * self.distance))
        
        return {
            "option": "Professional",
            "service": cheapest_service.name,
            "base_fee": cheapest_service.base_fee,
            "mileage_cost": cheapest_service.cost_per_mile * self.distance,
            "total_cost": cheapest_service.base_fee + (cheapest_service.cost_per_mile * self.distance)
        }

    def _calculate_mixed_cost(self) -> Dict[str, float]:
        """Calculate costs for mixed moving option (some DIY, some professional)."""
        fragile_items = [item for item in self.furniture if item.fragile]
        non_fragile_items = [item for item in self.furniture if not item.fragile]
        
        # Create temporary planners for each category
        fragile_planner = MovingBudgetPlanner()
        fragile_planner.furniture = fragile_items
        fragile_planner.services = self.services
        fragile_planner.distance = self.distance
        
        non_fragile_planner = MovingBudgetPlanner()
        non_fragile_planner.furniture = non_fragile_items
        non_fragile_planner.vehicles = self.vehicles
        non_fragile_planner.distance = self.distance
        
        try:
            fragile_cost = fragile_planner._calculate_professional_cost()
            non_fragile_cost = non_fragile_planner._calculate_diy_cost()
            
            return {
                "option": "Mixed",
                "fragile_items": {
                    "service": fragile_cost["service"],
                    "cost": fragile_cost["total_cost"]
                },
                "non_fragile_items": {
                    "vehicle": non_fragile_cost["vehicle"],
                    "cost": non_fragile_cost["total_cost"]
                },
                "total_cost": fragile_cost["total_cost"] + non_fragile_cost["total_cost"]
            }
        except ValueError as e:
            raise ValueError(f"Mixed option not feasible: {str(e)}")

    def calculate_best_option(self) -> Dict:
        """Calculate the most cost-effective moving option."""
        try:
            if self.option == MovingOption.DIY:
                return self._calculate_diy_cost()
            elif self.option == MovingOption.PROFESSIONAL:
                return self._calculate_professional_cost()
            elif self.option == MovingOption.MIXED:
                return self._calculate_mixed_cost()
            else:
                raise ValueError("Invalid moving option")
        except ValueError as e:
            return {"error": str(e)}

    def save_to_json(self, filename: str) -> None:
        """Save current configuration to JSON file."""
        data = {
            "furniture": [{"name": item.name, "volume": item.volume, 
                          "weight": item.weight, "fragile": item.fragile} 
                         for item in self.furniture],
            "services": [{"name": s.name, "cost_per_mile": s.cost_per_mile,
                         "cost_per_hour": s.cost_per_hour, "base_fee": s.base_fee,
                         "max_volume": s.max_volume, "max_weight": s.max_weight}
                        for s in self.services],
            "vehicles": [{"name": v.name, "rental_cost": v.rental_cost,
                         "fuel_cost_per_mile": v.fuel_cost_per_mile,
                         "max_volume": v.max_volume, "max_weight": v.max_weight}
                        for v in self.vehicles],
            "distance": self.distance,
            "option": self.option.name
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_from_json(self, filename: str) -> None:
        """Load configuration from JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        self.furniture = [
            FurnitureItem(item["name"], item["volume"], item["weight"], item["fragile"])
            for item in data["furniture"]
        ]
        
        self.services = [
            MovingService(s["name"], s["cost_per_mile"], s
