"""
Generated Code Metadata:
========================
Original URL: https://amayrainterior.com
Prompt: "Generate a tailored home lighting plan for a modern living room, using Amayra Interiors' design principles."
Generated: DETERMINISTIC_36fb9a6f43441d09
Batch ID: 20250622_210703
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
from enum import Enum, auto
from typing import List, Dict, Optional

class LightingType(Enum):
    AMBIENT = auto()
    TASK = auto()
    ACCENT = auto()
    DECORATIVE = auto()

@dataclass
class LightFixture:
    name: str
    type: LightingType
    position: str
    brightness: int  # in lumens
    color_temp: int  # in Kelvin
    dimmable: bool
    smart_control: bool

@dataclass
class LightingPlan:
    room: str
    style: str
    fixtures: List[LightFixture]
    total_lumens: int
    energy_efficient: bool

class LightingDesigner:
    """Creates tailored lighting plans following Amayra Interiors' principles."""
    
    def __init__(self):
        self.base_lighting_rules = {
            "modern": {
                "ambient": {"lumens_per_sqft": 20, "color_temp": 3000},
                "task": {"lumens_per_sqft": 30, "color_temp": 4000},
                "accent": {"lumens_per_sqft": 10, "color_temp": 2700},
                "decorative": {"lumens_per_sqft": 5, "color_temp": 2200}
            }
        }
    
    def calculate_lumens(self, area_sqft: float, fixture_type: LightingType, style: str) -> int:
        """Calculate recommended lumens for a fixture type."""
        try:
            rules = self.base_lighting_rules[style.lower()]
            type_str = fixture_type.name.lower()
            return int(area_sqft * rules[type_str]["lumens_per_sqft"])
        except KeyError as e:
            raise ValueError(f"Unsupported style or fixture type: {e}")

    def get_color_temp(self, fixture_type: LightingType, style: str) -> int:
        """Get recommended color temperature for a fixture type."""
        try:
            rules = self.base_lighting_rules[style.lower()]
            type_str = fixture_type.name.lower()
            return rules[type_str]["color_temp"]
        except KeyError as e:
            raise ValueError(f"Unsupported style or fixture type: {e}")

    def create_lighting_plan(self, room: str, style: str, area_sqft: float) -> LightingPlan:
        """
        Generate a complete lighting plan for a modern living room.
        
        Args:
            room: Name of the room
            style: Design style (e.g., 'modern')
            area_sqft: Area of the room in square feet
            
        Returns:
            LightingPlan: Complete lighting design
        """
        if area_sqft <= 0:
            raise ValueError("Room area must be positive")
            
        fixtures = []
        total_lumens = 0
        
        # Ambient lighting (main source)
        ambient_lumens = self.calculate_lumens(area_sqft, LightingType.AMBIENT, style)
        fixtures.append(LightFixture(
            name="Ceiling Recessed Lights",
            type=LightingType.AMBIENT,
            position="Ceiling (evenly spaced)",
            brightness=ambient_lumens,
            color_temp=self.get_color_temp(LightingType.AMBIENT, style),
            dimmable=True,
            smart_control=True
        ))
        total_lumens += ambient_lumens
        
        # Task lighting
        task_lumens = self.calculate_lumens(area_sqft, LightingType.TASK, style)
        fixtures.append(LightFixture(
            name="Floor Lamp",
            type=LightingType.TASK,
            position="Near seating area",
            brightness=task_lumens,
            color_temp=self.get_color_temp(LightingType.TASK, style),
            dimmable=True,
            smart_control=True
        ))
        total_lumens += task_lumens
        
        # Accent lighting
        accent_lumens = self.calculate_lumens(area_sqft, LightingType.ACCENT, style)
        fixtures.append(LightFixture(
            name="Wall Sconces",
            type=LightingType.ACCENT,
            position="On feature wall",
            brightness=accent_lumens,
            color_temp=self.get_color_temp(LightingType.ACCENT, style),
            dimmable=True,
            smart_control=False
        ))
        total_lumens += accent_lumens
        
        # Decorative lighting
        decorative_lumens = self.calculate_lumens(area_sqft, LightingType.DECORATIVE, style)
        fixtures.append(LightFixture(
            name="Pendant Light",
            type=LightingType.DECORATIVE,
            position="Above coffee table",
            brightness=decorative_lumens,
            color_temp=self.get_color_temp(LightingType.DECORATIVE, style),
            dimmable=False,
            smart_control=False
        ))
        total_lumens += decorative_lumens
        
        return LightingPlan(
            room=room,
            style=style,
            fixtures=fixtures,
            total_lumens=total_lumens,
            energy_efficient=True
        )

    def plan_to_json(self, plan: LightingPlan) -> str:
        """Convert lighting plan to JSON format."""
        return json.dumps({
            "room": plan.room,
            "style": plan.style,
            "total_lumens": plan.total_lumens,
            "energy_efficient": plan.energy_efficient,
            "fixtures": [{
                "name": f.name,
                "type": f.type.name,
                "position": f.position,
                "brightness": f.brightness,
                "color_temp": f.color_temp,
                "dimmable": f.dimmable,
                "smart_control": f.smart_control
            } for f in plan.fixtures]
        }, indent=2)

# Example usage
if __name__ == "__main__":
    try:
        designer = LightingDesigner()
        plan = designer.create_lighting_plan(
            room="Living Room",
            style="modern",
            area_sqft=250
        )
        print(designer.plan_to_json(plan))
    except ValueError as e:
        print(f"Error generating lighting plan: {e}")
```
