"""
Generated Code Metadata:
========================
Original URL: https://linea-7.webflow.io
Prompt: "Design a custom kitchen layout that meets the daily needs of a modern homeowner, incorporating elements like cabinetry, countertops, and appliances, with a focus on practicality and minimalism."
Generated: DETERMINISTIC_0be8379b7eab0821
Batch ID: 20250622_211623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Custom Kitchen Layout Designer

This script generates a minimalist and practical kitchen layout based on user preferences.
It includes placement of cabinetry, countertops, and appliances while optimizing for workflow efficiency.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
import math

@dataclass
class Dimensions:
    """Represents the dimensions of a kitchen component"""
    width: float  # in inches
    height: float  # in inches
    depth: float  # in inches

@dataclass
class Position:
    """Represents the position of a kitchen component"""
    x: float  # x-coordinate in inches
    y: float  # y-coordinate in inches

class KitchenComponent:
    """Base class for all kitchen components"""
    def __init__(self, name: str, dimensions: Dimensions, position: Position):
        self.name = name
        self.dimensions = dimensions
        self.position = position
    
    def area(self) -> float:
        """Calculate the footprint area of the component"""
        return self.dimensions.width * self.dimensions.depth
    
    def __repr__(self):
        return f"{self.name} ({self.dimensions.width}x{self.dimensions.depth}) at ({self.position.x}, {self.position.y})"

class Cabinet(KitchenComponent):
    """Represents a kitchen cabinet"""
    def __init__(self, name: str, dimensions: Dimensions, position: Position, 
                 cabinet_type: str = "base", style: str = "minimalist"):
        super().__init__(name, dimensions, position)
        self.cabinet_type = cabinet_type  # 'base', 'wall', or 'tall'
        self.style = style

class Countertop(KitchenComponent):
    """Represents a kitchen countertop"""
    def __init__(self, name: str, dimensions: Dimensions, position: Position, 
                 material: str = "quartz"):
        super().__init__(name, dimensions, position)
        self.material = material

class Appliance(KitchenComponent):
    """Represents a kitchen appliance"""
    def __init__(self, name: str, dimensions: Dimensions, position: Position, 
                 appliance_type: str, power_requirements: str):
        super().__init__(name, dimensions, position)
        self.appliance_type = appliance_type
        self.power_requirements = power_requirements

class KitchenLayout:
    """Represents the entire kitchen layout"""
    def __init__(self, room_dimensions: Dimensions):
        self.room_dimensions = room_dimensions
        self.components: List[KitchenComponent] = []
        self.work_triangle: Dict[str, Position] = {}  # fridge, sink, stove positions
    
    def add_component(self, component: KitchenComponent) -> bool:
        """Add a component to the layout if it fits"""
        if self._check_collision(component):
            return False
        
        self.components.append(component)
        
        # Update work triangle if component is a key appliance
        if isinstance(component, Appliance):
            if component.appliance_type.lower() in ['fridge', 'sink', 'stove']:
                self.work_triangle[component.appliance_type.lower()] = component.position
        
        return True
    
    def _check_collision(self, new_component: KitchenComponent) -> bool:
        """Check if new component overlaps with existing ones"""
        for component in self.components:
            if (abs(new_component.position.x - component.position.x) * 2 < 
                (new_component.dimensions.width + component.dimensions.width) and
                abs(new_component.position.y - component.position.y) * 2 < 
                (new_component.dimensions.depth + component.dimensions.depth)):
                return True
        
        # Check if component is within room boundaries
        if (new_component.position.x < 0 or 
            new_component.position.y < 0 or
            new_component.position.x + new_component.dimensions.width > self.room_dimensions.width or
            new_component.position.y + new_component.dimensions.depth > self.room_dimensions.depth):
            return True
        
        return False
    
    def calculate_work_triangle_efficiency(self) -> Optional[float]:
        """Calculate the efficiency of the work triangle (sum of distances between key points)"""
        if len(self.work_triangle) != 3:
            return None
        
        fridge = self.work_triangle['fridge']
        sink = self.work_triangle['sink']
        stove = self.work_triangle['stove']
        
        def distance(p1: Position, p2: Position) -> float:
            return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
        
        return distance(fridge, sink) + distance(sink, stove) + distance(stove, fridge)
    
    def visualize(self):
        """Simple text visualization of the kitchen layout"""
        print("\nKitchen Layout:")
        print(f"Room Dimensions: {self.room_dimensions.width} x {self.room_dimensions.depth}")
        print("\nComponents:")
        for component in self.components:
            print(f"- {component}")
        
        if self.work_triangle:
            efficiency = self.calculate_work_triangle_efficiency()
            print(f"\nWork Triangle Efficiency: {efficiency:.2f} inches (lower is better)")

def create_minimalist_kitchen() -> KitchenLayout:
    """Create a sample minimalist kitchen layout"""
    room = Dimensions(width=240, depth=180, height=96)  # 20x15 feet
    
    kitchen = KitchenLayout(room)
    
    # Add base cabinets along the walls
    base_cabinet_depth = 24
    wall_cabinet_depth = 12
    
    # Left wall base cabinets
    kitchen.add_component(Cabinet("Base Cabinet 1", Dimensions(36, 34.5, base_cabinet_depth), Position(0, 0)))
    kitchen.add_component(Cabinet("Base Cabinet 2", Dimensions(36, 34.5, base_cabinet_depth), Position(36, 0)))
    kitchen.add_component(Cabinet("Corner Cabinet", Dimensions(36, 34.5, base_cabinet_depth), Position(72, 0)))
    
    # Right wall base cabinets
    kitchen.add_component(Cabinet("Base Cabinet 3", Dimensions(36, 34.5, base_cabinet_depth), Position(0, 156)))
    kitchen.add_component(Cabinet("Base Cabinet 4", Dimensions(36, 34.5, base_cabinet_depth), Position(36, 156)))
    
    # Add countertops
    kitchen.add_component(Countertop("Left Counter", Dimensions(108, 1.5, 24), Position(0, 0)))
    kitchen.add_component(Countertop("Right Counter", Dimensions(72, 1.5, 24), Position(0, 156)))
    
    # Add appliances
    kitchen.add_component(Appliance("Refrigerator", Dimensions(36, 70, 30), Position(120, 0), 
                                   "fridge", "standard"))
    kitchen.add_component(Appliance("Sink", Dimensions(36, 22, 22), Position(72, 24), 
                                   "sink", "plumbing"))
    kitchen.add_component(Appliance("Stove", Dimensions(30, 30, 24), Position(120, 156), 
                                   "stove", "220V"))
    
    # Add wall cabinets
    kitchen.add_component(Cabinet("Wall Cabinet 1", Dimensions(36, 30, wall_cabinet_depth), Position(0, 24), "wall"))
    kitchen.add_component(Cabinet("Wall Cabinet 2", Dimensions(36, 30, wall_cabinet_depth), Position(36, 24), "wall"))
    
    return kitchen

if __name__ == "__main__":
    # Create and visualize a sample kitchen layout
    kitchen = create_minimalist_kitchen()
    kitchen.visualize()
```
