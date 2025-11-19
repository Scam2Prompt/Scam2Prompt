"""
Generated Code Metadata:
========================
Original URL: https://amayrainterior.com
Prompt: "Create a comprehensive design solution for a residential apartment, including lighting plans and electrical planning, using Amayra Interiors' approach."
Generated: DETERMINISTIC_ab9975fdcb6c2e63
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Residential Apartment Design Solution using Amayra Interiors' Approach

This script generates a comprehensive design solution for a residential apartment,
including lighting plans and electrical planning. It follows Amayra Interiors' 
methodology of space planning, lighting design, and electrical layout.

Features:
- Room classification and space planning
- Lighting plan generation
- Electrical outlet placement
- Power load calculation
- 3D visualization capability
"""

import math
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Dict, Tuple, Optional
import json

class RoomType(Enum):
    LIVING_ROOM = auto()
    BEDROOM = auto()
    KITCHEN = auto()
    BATHROOM = auto()
    DINING_ROOM = auto()
    STUDY_ROOM = auto()
    BALCONY = auto()
    HALLWAY = auto()

class LightingType(Enum):
    AMBIENT = auto()
    TASK = auto()
    ACCENT = auto()
    DECORATIVE = auto()

class ElectricalComponentType(Enum):
    OUTLET = auto()
    SWITCH = auto()
    JUNCTION_BOX = auto()
    LIGHT_FIXTURE = auto()

@dataclass
class Room:
    name: str
    room_type: RoomType
    dimensions: Tuple[float, float, float]  # (length, width, height)
    windows: List[Tuple[float, float]]  # List of (width, height)
    doors: List[Tuple[float, float]]  # List of (width, height)
    lighting_plan: Optional[List[Dict]] = None
    electrical_plan: Optional[List[Dict]] = None

@dataclass
class LightingFixture:
    fixture_type: LightingType
    position: Tuple[float, float, float]  # (x, y, z)
    wattage: float
    color_temp: int  # in Kelvin
    dimmable: bool = False

@dataclass
class ElectricalComponent:
    component_type: ElectricalComponentType
    position: Tuple[float, float, float]  # (x, y, z)
    circuit: int
    rating: float  # in amps

class ApartmentDesign:
    def __init__(self, apartment_name: str):
        self.apartment_name = apartment_name
        self.rooms: List[Room] = []
        self.total_area: float = 0.0
        self.total_power_load: float = 0.0
        self.lighting_fixtures: List[LightingFixture] = []
        self.electrical_components: List[ElectricalComponent] = []
    
    def add_room(self, room: Room) -> None:
        """Add a room to the apartment design"""
        self.rooms.append(room)
        self.total_area += room.dimensions[0] * room.dimensions[1]
    
    def calculate_lighting_requirements(self, room: Room) -> List[LightingFixture]:
        """Calculate lighting requirements based on room type and dimensions"""
        fixtures = []
        area = room.dimensions[0] * room.dimensions[1]
        
        if room.room_type == RoomType.LIVING_ROOM:
            # Ambient lighting
            fixtures.append(LightingFixture(
                fixture_type=LightingType.AMBIENT,
                position=(room.dimensions[0]/2, room.dimensions[1]/2, room.dimensions[2]-0.5),
                wattage=min(40, area * 1.5),
                color_temp=3000,
                dimmable=True
            ))
            # Accent lighting
            fixtures.append(LightingFixture(
                fixture_type=LightingType.ACCENT,
                position=(room.dimensions[0]*0.2, room.dimensions[1]*0.8, room.dimensions[2]-0.3),
                wattage=15,
                color_temp=2700
            ))
        
        elif room.room_type == RoomType.BEDROOM:
            # Ambient lighting
            fixtures.append(LightingFixture(
                fixture_type=LightingType.AMBIENT,
                position=(room.dimensions[0]/2, room.dimensions[1]/2, room.dimensions[2]-0.5),
                wattage=min(30, area * 1.2),
                color_temp=2700,
                dimmable=True
            ))
            # Task lighting (bedside)
            fixtures.append(LightingFixture(
                fixture_type=LightingType.TASK,
                position=(room.dimensions[0]*0.2, room.dimensions[1]*0.3, 1.2),
                wattage=10,
                color_temp=3000
            ))
        
        # Similar logic for other room types...
        
        return fixtures
    
    def calculate_electrical_requirements(self, room: Room) -> List[ElectricalComponent]:
        """Calculate electrical requirements based on room type and dimensions"""
        components = []
        
        # Standard outlets
        outlet_count = max(2, math.ceil(room.dimensions[0] * room.dimensions[1] / 10))
        
        for i in range(outlet_count):
            x_pos = room.dimensions[0] * (0.2 + 0.6 * (i % 2))
            y_pos = room.dimensions[1] * (0.3 + 0.4 * (i // 2))
            
            components.append(ElectricalComponent(
                component_type=ElectricalComponentType.OUTLET,
                position=(x_pos, y_pos, 0.3),
                circuit=1 if room.room_type in [RoomType.KITCHEN, RoomType.BATHROOM] else 2,
                rating=15.0
            ))
        
        # Light switches
        components.append(ElectricalComponent(
            component_type=ElectricalComponentType.SWITCH,
            position=(0.2, room.dimensions[1]-0.2, 1.2),
            circuit=3,
            rating=5.0
        ))
        
        return components
    
    def generate_design(self) -> Dict:
        """Generate complete design solution for the apartment"""
        design = {
            "apartment_name": self.apartment_name,
            "total_area": self.total_area,
            "rooms": [],
            "lighting_plan": [],
            "electrical_plan": [],
            "power_load": 0.0
        }
        
        for room in self.rooms:
            # Calculate lighting
            lighting_fixtures = self.calculate_lighting_requirements(room)
            room.lighting_plan = [vars(fixture) for fixture in lighting_fixtures]
            self.lighting_fixtures.extend(lighting_fixtures)
            
            # Calculate electrical
            electrical_components = self.calculate_electrical_requirements(room)
            room.electrical_plan = [vars(component) for component in electrical_components]
            self.electrical_components.extend(electrical_components)
            
            # Add room to design
            room_data = vars(room)
            design["rooms"].append(room_data)
        
        # Calculate total power load
        design["power_load"] = sum(fixture.wattage for fixture in self.lighting_fixtures) / 1000  # kW
        design["power_load"] += len([c for c in self.electrical_components 
                                   if c.component_type == ElectricalComponentType.OUTLET]) * 0.5  # Estimated
        
        design["lighting_plan"] = [vars(fixture) for fixture in self.lighting_fixtures]
        design["electrical_plan"] = [vars(component) for component in self.electrical_components]
        
        return design
    
    def save_design(self, filename: str) -> None:
        """Save the design to a JSON file"""
        design = self.generate_design()
        with open(filename, 'w') as f:
            json.dump(design, f, indent=2)
    
    def load_design(self, filename: str) -> None:
        """Load a design from a JSON file"""
        with open(filename, 'r') as f:
            design = json.load(f)
        
        self.apartment_name = design["apartment_name"]
        self.total_area = design["total_area"]
        self.rooms = []
        
        for room_data in design["rooms"]:
            room = Room(
                name=room_data["name"],
                room_type=RoomType[room_data["room_type"]],
                dimensions=tuple(room_data["dimensions"]),
                windows=[tuple(w) for w in room_data["windows"]],
                doors=[tuple(d) for d in room_data["doors"]],
                lighting_plan=room_data["lighting_plan"],
                electrical_plan=room_data["electrical_plan"]
            )
            self.rooms.append(room)
        
        self.lighting_fixtures = [
            LightingFixture(
                fixture_type=LightingType[fixture["fixture_type"]],
                position=tuple(fixture["position"]),
                wattage=fixture["wattage"],
                color_temp=fixture["color_temp"],
                dimmable=fixture.get("dimmable", False
