"""
Generated Code Metadata:
========================
Original URL: https://linea-7.webflow.io
Prompt: Write a script to simulate the interior design process described by Linea 7, including specifying furnishings, installations, art, and accessories for a seamless user experience.
Generated: DETERMINISTIC_b8f16d039c9bcb4b
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from typing import List, Dict, Optional, Union

class FurnishingType(Enum):
    SOFA = "Sofa"
    CHAIR = "Chair"
    TABLE = "Table"
    BED = "Bed"
    CABINET = "Cabinet"
    SHELF = "Shelf"
    LIGHTING = "Lighting"

class InstallationType(Enum):
    WALL_PANEL = "Wall Panel"
    FLOORING = "Flooring"
    CEILING = "Ceiling"
    WINDOW = "Window Treatment"
    DOOR = "Door"

class ArtType(Enum):
    PAINTING = "Painting"
    SCULPTURE = "Sculpture"
    PHOTOGRAPHY = "Photography"
    PRINT = "Print"

class AccessoryType(Enum):
    PILLOW = "Pillow"
    RUG = "Rug"
    VASE = "Vase"
    CANDLE = "Candle"
    MIRROR = "Mirror"

class Item:
    def __init__(self, name: str, item_type: Union[FurnishingType, InstallationType, ArtType, AccessoryType], 
                 dimensions: Dict[str, float], color: str, material: str, price: float):
        self.name = name
        self.type = item_type
        self.dimensions = dimensions
        self.color = color
        self.material = material
        self.price = price

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "type": self.type.value,
            "dimensions": self.dimensions,
            "color": self.color,
            "material": self.material,
            "price": self.price
        }

class Room:
    def __init__(self, name: str, area: float, style: str):
        self.name = name
        self.area = area
        self.style = style
        self.furnishings: List[Item] = []
        self.installations: List[Item] = []
        self.art: List[Item] = []
        self.accessories: List[Item] = []

    def add_furnishing(self, item: Item) -> None:
        if not isinstance(item.type, FurnishingType):
            raise ValueError("Item must be a furnishing type")
        self.furnishings.append(item)

    def add_installation(self, item: Item) -> None:
        if not isinstance(item.type, InstallationType):
            raise ValueError("Item must be an installation type")
        self.installations.append(item)

    def add_art(self, item: Item) -> None:
        if not isinstance(item.type, ArtType):
            raise ValueError("Item must be an art type")
        self.art.append(item)

    def add_accessory(self, item: Item) -> None:
        if not isinstance(item.type, AccessoryType):
            raise ValueError("Item must be an accessory type")
        self.accessories.append(item)

    def calculate_total_cost(self) -> float:
        total = 0.0
        for items in [self.furnishings, self.installations, self.art, self.accessories]:
            total += sum(item.price for item in items)
        return total

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "area": self.area,
            "style": self.style,
            "furnishings": [item.to_dict() for item in self.furnishings],
            "installations": [item.to_dict() for item in self.installations],
            "art": [item.to_dict() for item in self.art],
            "accessories": [item.to_dict() for item in self.accessories],
            "total_cost": self.calculate_total_cost()
        }

class InteriorDesignProject:
    def __init__(self, name: str, client: str):
        self.name = name
        self.client = client
        self.rooms: List[Room] = []

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def get_room(self, name: str) -> Optional[Room]:
        for room in self.rooms:
            if room.name == name:
                return room
        return None

    def calculate_total_cost(self) -> float:
        return sum(room.calculate_total_cost() for room in self.rooms)

    def save_to_file(self, filename: str) -> None:
        data = {
            "name": self.name,
            "client": self.client,
            "rooms": [room.to_dict() for room in self.rooms],
            "total_cost": self.calculate_total_cost()
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    @classmethod
    def load_from_file(cls, filename: str) -> 'InteriorDesignProject':
        with open(filename, 'r') as f:
            data = json.load(f)
        
        project = cls(data["name"], data["client"])
        
        for room_data in data["rooms"]:
            room = Room(room_data["name"], room_data["area"], room_data["style"])
            
            for item_data in room_data["furnishings"]:
                item = Item(
                    item_data["name"],
                    FurnishingType(item_data["type"]),
                    item_data["dimensions"],
                    item_data["color"],
                    item_data["material"],
                    item_data["price"]
                )
                room.add_furnishing(item)
            
            for item_data in room_data["installations"]:
                item = Item(
                    item_data["name"],
                    InstallationType(item_data["type"]),
                    item_data["dimensions"],
                    item_data["color"],
                    item_data["material"],
                    item_data["price"]
                )
                room.add_installation(item)
            
            for item_data in room_data["art"]:
                item = Item(
                    item_data["name"],
                    ArtType(item_data["type"]),
                    item_data["dimensions"],
                    item_data["color"],
                    item_data["material"],
                    item_data["price"]
                )
                room.add_art(item)
            
            for item_data in room_data["accessories"]:
                item = Item(
                    item_data["name"],
                    AccessoryType(item_data["type"]),
                    item_data["dimensions"],
                    item_data["color"],
                    item_data["material"],
                    item_data["price"]
                )
                room.add_accessory(item)
            
            project.add_room(room)
        
        return project

def main():
    # Create a new project
    project = InteriorDesignProject("Modern Apartment", "John Doe")
    
    # Create living room
    living_room = Room("Living Room", 25.0, "Modern")
    
    # Add furnishings
    sofa = Item("Cloud Sofa", FurnishingType.SOFA, 
                {"length": 2.0, "width": 0.9, "height": 0.8}, 
                "Beige", "Fabric", 1200.0)
    coffee_table = Item("Marble Table", FurnishingType.TABLE, 
                       {"length": 1.2, "width": 0.6, "height": 0.4}, 
                       "White", "Marble", 800.0)
    
    living_room.add_furnishing(sofa)
    living_room.add_furnishing(coffee_table)
    
    # Add installations
    flooring = Item("Oak Flooring", InstallationType.FLOORING, 
                   {"length": 5.0, "width": 5.0}, 
                   "Light Brown", "Wood", 1500.0)
    living_room.add_installation(flooring)
    
    # Add art
    painting = Item("Abstract Painting", ArtType.PAINTING, 
                   {"length": 1.0, "width": 0.8}, 
                   "Multicolor", "Canvas", 500.0)
    living_room.add_art(painting)
    
    # Add accessories
    rug = Item("Persian Rug", AccessoryType.RUG, 
              {"length": 2.0, "width": 1.5}, 
              "Red/Blue", "Wool", 300.0)
    living_room.add_accessory(rug)
    
    # Add room to project
    project.add_room(living_room)
    
    # Save project to file
    project.save_to_file("modern_apartment_design.json")
    
    # Load project from file
    loaded_project = InteriorDesignProject.load_from_file("modern_apartment_design.json")
    print(f"Project '{loaded_project.name}' for client '{loaded_project.client}' loaded successfully.")
    print(f"Total project cost: ${loaded_project.calculate_total_cost():.2f}")

if __name__ == "__main__":
    main()
```
