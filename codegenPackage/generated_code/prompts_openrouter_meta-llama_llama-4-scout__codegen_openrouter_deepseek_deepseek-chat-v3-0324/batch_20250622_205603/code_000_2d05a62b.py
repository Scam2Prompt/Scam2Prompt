"""
Generated Code Metadata:
========================
Original URL: https://panam.su
Prompt: "Generate a detailed plan and cost estimate for a turnkey apartment renovation in Russia, including design, materials, and labor costs, as per the services offered by ПАНАМ."
Generated: DETERMINISTIC_2d05a62b91b6703f
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Apartment Renovation Cost Estimator for ПАНАМ (Russia)

This script calculates a detailed plan and cost estimate for a turnkey apartment renovation
in Russia, including design, materials, and labor costs based on ПАНАМ's service offerings.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
import json

@dataclass
class Room:
    """Represents a room in the apartment with its dimensions and type."""
    name: str
    area: float  # in square meters
    type: str  # e.g., 'living', 'kitchen', 'bathroom'

@dataclass
class Material:
    """Represents a construction material with its cost per unit."""
    name: str
    unit: str  # e.g., 'sqm', 'piece', 'linear meter'
    cost_per_unit: float  # in RUB

@dataclass
class Service:
    """Represents a renovation service with its cost."""
    name: str
    cost_per_sqm: float  # in RUB per square meter
    is_design: bool = False

class RenovationEstimate:
    """Main class to calculate renovation costs for an apartment."""
    
    def __init__(self):
        self.rooms: List[Room] = []
        self.materials: Dict[str, Material] = {}
        self.services: Dict[str, Service] = {}
        self.design_cost: float = 0.0
        self._load_default_data()
    
    def _load_default_data(self) -> None:
        """Load default materials and services based on ПАНАМ's offerings."""
        # Default materials (prices are approximate as of 2023)
        self.materials = {
            'floor_tile': Material('Floor Tile', 'sqm', 1500),
            'wall_paint': Material('Wall Paint', 'sqm', 500),
            'wallpaper': Material('Wallpaper', 'sqm', 800),
            'kitchen_countertop': Material('Kitchen Countertop', 'linear meter', 10000),
            'bathroom_sanitary': Material('Bathroom Sanitary', 'piece', 20000),
        }
        
        # Default services
        self.services = {
            'demolition': Service('Demolition', 1000),
            'electrical': Service('Electrical Work', 1500),
            'plumbing': Service('Plumbing Work', 2000),
            'floor_installation': Service('Floor Installation', 1200),
            'wall_finishing': Service('Wall Finishing', 1000),
            'design': Service('Interior Design', 3000, is_design=True),
        }
        
        # Design cost is separate
        self.design_cost = 50000  # RUB
    
    def add_room(self, name: str, area: float, room_type: str) -> None:
        """Add a room to the apartment plan."""
        if area <= 0:
            raise ValueError("Room area must be positive")
        self.rooms.append(Room(name, area, room_type))
    
    def calculate_material_cost(self, room: Room) -> float:
        """Calculate material costs for a given room."""
        material_cost = 0.0
        
        if room.type == 'living':
            material_cost += room.area * self.materials['wall_paint'].cost_per_unit
            material_cost += room.area * self.materials['floor_tile'].cost_per_unit
        elif room.type == 'kitchen':
            material_cost += room.area * self.materials['wallpaper'].cost_per_unit
            material_cost += room.area * self.materials['floor_tile'].cost_per_unit
            material_cost += 3 * self.materials['kitchen_countertop'].cost_per_unit  # Approximate length
        elif room.type == 'bathroom':
            material_cost += room.area * self.materials['wall_paint'].cost_per_unit
            material_cost += room.area * self.materials['floor_tile'].cost_per_unit
            material_cost += 2 * self.materials['bathroom_sanitary'].cost_per_unit  # Toilet + sink
        
        return material_cost
    
    def calculate_service_cost(self, room: Room) -> float:
        """Calculate service costs for a given room."""
        service_cost = 0.0
        
        # Base services for all rooms
        service_cost += room.area * self.services['demolition'].cost_per_sqm
        service_cost += room.area * self.services['electrical'].cost_per_sqm
        service_cost += room.area * self.services['plumbing'].cost_per_sqm
        service_cost += room.area * self.services['floor_installation'].cost_per_sqm
        service_cost += room.area * self.services['wall_finishing'].cost_per_sqm
        
        return service_cost
    
    def generate_estimate(self) -> Dict:
        """Generate complete renovation estimate."""
        if not self.rooms:
            raise ValueError("No rooms added to the plan")
        
        total_area = sum(room.area for room in self.rooms)
        total_material_cost = 0.0
        total_service_cost = 0.0
        room_details = []
        
        for room in self.rooms:
            material_cost = self.calculate_material_cost(room)
            service_cost = self.calculate_service_cost(room)
            total_material_cost += material_cost
            total_service_cost += service_cost
            
            room_details.append({
                'name': room.name,
                'type': room.type,
                'area': room.area,
                'material_cost': material_cost,
                'service_cost': service_cost,
                'total_cost': material_cost + service_cost
            })
        
        total_cost = (
            total_material_cost + 
            total_service_cost + 
            self.design_cost
        )
        
        return {
            'total_area': total_area,
            'design_cost': self.design_cost,
            'total_material_cost': total_material_cost,
            'total_service_cost': total_service_cost,
            'total_cost': total_cost,
            'rooms': room_details,
            'currency': 'RUB'
        }
    
    def save_estimate_to_file(self, filename: str) -> None:
        """Save the estimate to a JSON file."""
        estimate = self.generate_estimate()
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(estimate, f, ensure_ascii=False, indent=2)

# Example usage
if __name__ == "__main__":
    estimator = RenovationEstimate()
    
    # Add rooms to the apartment
    estimator.add_room("Living Room", 20.5, "living")
    estimator.add_room("Kitchen", 12.0, "kitchen")
    estimator.add_room("Bathroom", 8.0, "bathroom")
    estimator.add_room("Bedroom", 15.0, "living")
    
    # Generate and print estimate
    estimate = estimator.generate_estimate()
    print(json.dumps(estimate, ensure_ascii=False, indent=2))
    
    # Save to file
    estimator.save_estimate_to_file("apartment_renovation_estimate.json")
```
