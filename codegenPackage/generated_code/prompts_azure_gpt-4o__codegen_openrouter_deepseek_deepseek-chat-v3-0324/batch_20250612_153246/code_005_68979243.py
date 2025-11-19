"""
Generated Code Metadata:
========================
Original URL: https://greystoneinfra.in
Prompt: Create a step-by-step algorithm for automating the interior design process, including layout creation, moodboard generation, and material finalization, following the workflow outlined by Greystone Infra.
Generated: DETERMINISTIC_68979243416d2e1d
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Interior Design Automation Algorithm
Following Greystone Infra's workflow for:
1. Layout Creation
2. Moodboard Generation
3. Material Finalization
"""

import json
from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum, auto
import random
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class RoomType(Enum):
    LIVING = auto()
    BEDROOM = auto()
    KITCHEN = auto()
    BATHROOM = auto()
    OFFICE = auto()

@dataclass
class FurnitureItem:
    id: str
    name: str
    dimensions: Dict[str, float]
    category: str
    style: str

@dataclass
class Material:
    id: str
    name: str
    type: str
    color: str
    texture: str
    durability: float

@dataclass
class RoomSpecs:
    dimensions: Dict[str, float]
    room_type: RoomType
    windows: List[Dict[str, float]]
    doors: List[Dict[str, float]]

@dataclass
class DesignLayout:
    room_specs: RoomSpecs
    furniture_placement: List[Dict]
    traffic_flow: List[List[float]]

@dataclass
class Moodboard:
    color_palette: List[str]
    materials: List[Material]
    furniture_styles: List[str]
    inspiration_images: List[str]

class InteriorDesignAutomator:
    def __init__(self, furniture_catalog: List[FurnitureItem], material_catalog: List[Material]):
        self.furniture_catalog = furniture_catalog
        self.material_catalog = material_catalog
        self.design_rules = self._load_design_rules()

    def _load_design_rules(self) -> Dict:
        """Load design rules from JSON file"""
        try:
            with open('design_rules.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error("Design rules file not found")
            raise
        except json.JSONDecodeError:
            logger.error("Invalid design rules JSON")
            raise

    def create_layout(self, room_specs: RoomSpecs) -> DesignLayout:
        """Generate furniture layout based on room specifications"""
        try:
            logger.info(f"Creating layout for {room_specs.room_type.name} room")
            
            # Step 1: Apply design rules for the room type
            room_rules = self.design_rules.get(room_specs.room_type.name, {})
            
            # Step 2: Select appropriate furniture
            selected_furniture = self._select_furniture(room_specs.room_type)
            
            # Step 3: Optimize furniture placement
            placement = self._optimize_placement(selected_furniture, room_specs)
            
            # Step 4: Calculate traffic flow
            traffic_flow = self._calculate_traffic_flow(placement, room_specs)
            
            return DesignLayout(
                room_specs=room_specs,
                furniture_placement=placement,
                traffic_flow=traffic_flow
            )
        except Exception as e:
            logger.error(f"Error creating layout: {str(e)}")
            raise

    def _select_furniture(self, room_type: RoomType) -> List[FurnitureItem]:
        """Select furniture items based on room type"""
        return [item for item in self.furniture_catalog 
                if item.category.lower() == room_type.name.lower()]

    def _optimize_placement(self, furniture: List[FurnitureItem], 
                          room_specs: RoomSpecs) -> List[Dict]:
        """Optimize furniture placement using basic rules"""
        placements = []
        x_pos = 1.0
        y_pos = 1.0
        
        for item in furniture:
            placement = {
                "item_id": item.id,
                "position": {"x": x_pos, "y": y_pos},
                "rotation": 0,
                "dimensions": item.dimensions
            }
            placements.append(placement)
            
            # Simple placement logic - in production would use more sophisticated algorithm
            x_pos += item.dimensions["length"] + 0.5
            if x_pos > room_specs.dimensions["length"] - 2:
                x_pos = 1.0
                y_pos += item.dimensions["width"] + 0.5
                
        return placements

    def _calculate_traffic_flow(self, placements: List[Dict], 
                              room_specs: RoomSpecs) -> List[List[float]]:
        """Calculate optimal traffic flow paths"""
        # Simplified traffic flow calculation
        # In production would use pathfinding algorithm
        main_path = [
            [1.0, 1.0],
            [room_specs.dimensions["length"] / 2, 1.0],
            [room_specs.dimensions["length"] / 2, room_specs.dimensions["width"] / 2],
            [1.0, room_specs.dimensions["width"] / 2]
        ]
        return [main_path]

    def generate_moodboard(self, layout: DesignLayout, 
                         style_preferences: Optional[List[str]] = None) -> Moodboard:
        """Generate moodboard based on layout and optional style preferences"""
        try:
            logger.info("Generating moodboard")
            
            # Step 1: Determine color palette
            color_palette = self._select_color_palette(layout.room_specs.room_type, style_preferences)
            
            # Step 2: Select materials
            materials = self._select_materials(color_palette, layout.room_specs.room_type)
            
            # Step 3: Determine furniture styles
            furniture_styles = self._determine_furniture_styles(style_preferences)
            
            # Step 4: Select inspiration images
            inspiration_images = self._select_inspiration_images(
                layout.room_specs.room_type, 
                furniture_styles
            )
            
            return Moodboard(
                color_palette=color_palette,
                materials=materials,
                furniture_styles=furniture_styles,
                inspiration_images=inspiration_images
            )
        except Exception as e:
            logger.error(f"Error generating moodboard: {str(e)}")
            raise

    def _select_color_palette(self, room_type: RoomType, 
                            style_preferences: Optional[List[str]]) -> List[str]:
        """Select color palette based on room type and style"""
        palettes = {
            "LIVING": ["#E8E8E8", "#A0A0A0", "#606060", "#303030"],
            "BEDROOM": ["#F5F5F5", "#D8C4B8", "#B89B8C", "#8C7265"],
            "KITCHEN": ["#FFFFFF", "#F0F0F0", "#C0C0C0", "#808080"],
            "BATHROOM": ["#FFFFFF", "#E0F7FA", "#B2EBF2", "#80DEEA"],
            "OFFICE": ["#FFFFFF", "#E8F5E9", "#C8E6C9", "#A5D6A7"]
        }
        
        if style_preferences and "dark" in style_preferences:
            return ["#303030", "#404040", "#505050", "#606060"]
        
        return palettes.get(room_type.name, ["#FFFFFF", "#F0F0F0", "#E0E0E0", "#D0D0D0"])

    def _select_materials(self, color_palette: List[str], 
                        room_type: RoomType) -> List[Material]:
        """Select materials that match color palette and room type"""
        return random.sample(
            [m for m in self.material_catalog 
             if m.color in color_palette or room_type.name.lower() in m.type.lower()],
            min(5, len(self.material_catalog))
        )

    def _determine_furniture_styles(self, style_preferences: Optional[List[str]]) -> List[str]:
        """Determine furniture styles based on preferences or default"""
        if style_preferences:
            return style_preferences
        return ["Modern", "Minimalist"]

    def _select_inspiration_images(self, room_type: RoomType, 
                                 styles: List[str]) -> List[str]:
        """Select inspiration images based on room type and styles"""
        # In production would query a database or API
        base_path = f"inspiration/{room_type.name.lower()}"
        return [
            f"{base_path}/image1.jpg",
            f"{base_path}/image2.jpg",
            f"{base_path}/image3.jpg"
        ]

    def finalize_materials(self, moodboard: Moodboard, 
                         budget_constraints
