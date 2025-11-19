"""
Generated Code Metadata:
========================
Original URL: https://remas.ae
Prompt: Create a Python function to generate structured interior design plans based on client preferences, referencing the structure interior designing services provided by Remas Engineering Consultants.
Generated: DETERMINISTIC_14f6801e6ac7413b
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Union
from dataclasses import dataclass, asdict
from enum import Enum, auto

class DesignStyle(Enum):
    MODERN = auto()
    CONTEMPORARY = auto()
    MINIMALIST = auto()
    INDUSTRIAL = auto()
    MID_CENTURY_MODERN = auto()
    SCANDINAVIAN = auto()
    TRADITIONAL = auto()
    TRANSITIONAL = auto()
    RUSTIC = auto()
    BOHEMIAN = auto()
    COASTAL = auto()
    FARMHOUSE = auto()

class RoomType(Enum):
    LIVING_ROOM = auto()
    BEDROOM = auto()
    KITCHEN = auto()
    BATHROOM = auto()
    DINING_ROOM = auto()
    HOME_OFFICE = auto()
    GAME_ROOM = auto()
    GYM = auto()
    LIBRARY = auto()
    GARAGE = auto()

@dataclass
class ClientPreferences:
    name: str
    contact_info: str
    preferred_styles: List[DesignStyle]
    room_types: List[RoomType]
    budget: float
    special_requirements: Optional[str] = None
    color_palette: Optional[List[str]] = None
    must_have_items: Optional[List[str]] = None

@dataclass
class RoomDesign:
    room_type: RoomType
    style: DesignStyle
    color_scheme: List[str]
    furniture_items: List[str]
    layout_plan: str
    estimated_cost: float

@dataclass
class InteriorDesignPlan:
    client: ClientPreferences
    rooms: List[RoomDesign]
    total_estimated_cost: float
    project_timeline: str
    additional_notes: Optional[str] = None

class InteriorDesignGenerator:
    def __init__(self):
        self._style_furniture_map = {
            DesignStyle.MODERN: ["Sleek sofa", "Glass coffee table", "Minimalist shelving"],
            DesignStyle.CONTEMPORARY: ["Modular furniture", "Statement lighting", "Neutral palette"],
            DesignStyle.MINIMALIST: ["Essential furniture only", "Clean lines", "Monochrome colors"],
            DesignStyle.INDUSTRIAL: ["Metal accents", "Exposed brick", "Reclaimed wood"],
            DesignStyle.MID_CENTURY_MODERN: ["Tapered legs", "Organic shapes", "Bold colors"],
            DesignStyle.SCANDINAVIAN: ["Light wood", "Functional furniture", "Cozy textiles"],
            DesignStyle.TRADITIONAL: ["Ornate details", "Classic patterns", "Wood finishes"],
            DesignStyle.TRANSITIONAL: ["Mix of traditional and modern", "Neutral palette", "Comfortable fabrics"],
            DesignStyle.RUSTIC: ["Natural materials", "Vintage pieces", "Earthy tones"],
            DesignStyle.BOHEMIAN: ["Eclectic mix", "Vibrant colors", "Patterned textiles"],
            DesignStyle.COASTAL: ["Light colors", "Nautical elements", "Natural textures"],
            DesignStyle.FARMHOUSE: ["Shiplap walls", "Apron sinks", "Vintage decor"]
        }
        
        self._room_furniture_map = {
            RoomType.LIVING_ROOM: ["Sofa", "Coffee table", "TV stand"],
            RoomType.BEDROOM: ["Bed", "Nightstands", "Dresser"],
            RoomType.KITCHEN: ["Cabinets", "Countertops", "Appliances"],
            RoomType.BATHROOM: ["Vanity", "Shower", "Toilet"],
            RoomType.DINING_ROOM: ["Dining table", "Chairs", "Buffet"],
            RoomType.HOME_OFFICE: ["Desk", "Chair", "Shelving"],
            RoomType.GAME_ROOM: ["Gaming table", "Seating", "Storage"],
            RoomType.GYM: ["Exercise equipment", "Mirrors", "Storage"],
            RoomType.LIBRARY: ["Bookshelves", "Reading chair", "Desk"],
            RoomType.GARAGE: ["Storage systems", "Workbench", "Tool organization"]
        }
        
        self._color_palettes = {
            DesignStyle.MODERN: ["#FFFFFF", "#000000", "#808080"],
            DesignStyle.CONTEMPORARY: ["#F5F5F5", "#333333", "#E0E0E0"],
            DesignStyle.MINIMALIST: ["#FFFFFF", "#000000", "#CCCCCC"],
            DesignStyle.INDUSTRIAL: ["#3E3E3E", "#A19D94", "#6B6B6B"],
            DesignStyle.MID_CENTURY_MODERN: ["#E68364", "#4A8FE7", "#F9F9F9"],
            DesignStyle.SCANDINAVIAN: ["#F3F3F3", "#D8D8D8", "#A5A5A5"],
            DesignStyle.TRADITIONAL: ["#8B4513", "#D2B48C", "#F5DEB3"],
            DesignStyle.TRANSITIONAL: ["#E5E5E5", "#C0C0C0", "#A9A9A9"],
            DesignStyle.RUSTIC: ["#8B5A2B", "#CD853F", "#D2B48C"],
            DesignStyle.BOHEMIAN: ["#FF6B6B", "#4ECDC4", "#FFE66D"],
            DesignStyle.COASTAL: ["#5F9EA0", "#F0F8FF", "#B0E0E6"],
            DesignStyle.FARMHOUSE: ["#F5F5DC", "#8B4513", "#D2B48C"]
        }

    def _generate_room_design(self, room_type: RoomType, style: DesignStyle, budget: float) -> RoomDesign:
        base_items = self._room_furniture_map.get(room_type, [])
        style_items = self._style_furniture_map.get(style, [])
        color_scheme = self._color_palettes.get(style, ["#FFFFFF", "#000000"])
        
        combined_items = base_items + style_items
        if len(combined_items) > 5:
            combined_items = combined_items[:5]
            
        cost_per_item = budget * 0.7 / len(combined_items) if combined_items else 0
        estimated_cost = cost_per_item * len(combined_items)
        
        layout_plan = f"Open layout with {style.name.lower()} elements focusing on {room_type.name.replace('_', ' ').lower()} functionality"
        
        return RoomDesign(
            room_type=room_type,
            style=style,
            color_scheme=color_scheme,
            furniture_items=combined_items,
            layout_plan=layout_plan,
            estimated_cost=estimated_cost
        )

    def generate_design_plan(self, client_prefs: ClientPreferences) -> InteriorDesignPlan:
        if not client_prefs.preferred_styles:
            raise ValueError("At least one design style must be specified")
            
        if not client_prefs.room_types:
            raise ValueError("At least one room type must be specified")
            
        if client_prefs.budget <= 0:
            raise ValueError("Budget must be a positive number")
            
        room_designs = []
        budget_per_room = client_prefs.budget / len(client_prefs.room_types)
        
        for room_type in client_prefs.room_types:
            style = client_prefs.preferred_styles[0]  # Use first preferred style
            room_design = self._generate_room_design(room_type, style, budget_per_room)
            room_designs.append(room_design)
            
        total_cost = sum(room.estimated_cost for room in room_designs)
        timeline = f"{len(room_designs) * 2} weeks"  # 2 weeks per room
        
        return InteriorDesignPlan(
            client=client_prefs,
            rooms=room_designs,
            total_estimated_cost=total_cost,
            project_timeline=timeline,
            additional_notes=client_prefs.special_requirements
        )

    def save_design_to_json(self, design_plan: InteriorDesignPlan, filename: str) -> None:
        try:
            with open(filename, 'w') as f:
                json.dump(asdict(design_plan), f, indent=4, default=str)
        except IOError as e:
            raise IOError(f"Failed to save design plan: {str(e)}")

    def load_design_from_json(self, filename: str) -> InteriorDesignPlan:
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                
            client_data = data['client']
            client_prefs = ClientPreferences(
                name=client_data['name'],
                contact_info=client_data['contact_info'],
                preferred_styles=[DesignStyle[style] for style in client_data['preferred_styles']],
                room_types=[RoomType[room
