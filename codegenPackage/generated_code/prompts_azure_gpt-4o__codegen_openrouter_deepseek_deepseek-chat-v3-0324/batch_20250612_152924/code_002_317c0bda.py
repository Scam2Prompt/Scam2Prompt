"""
Generated Code Metadata:
========================
Original URL: https://uaeinterior.com
Prompt: Create a script that automates space planning for interior design, optimizing layouts for small offices and kitchens, inspired by Amazing Interior's "making the best possible use of available space" philosophy.
Generated: DETERMINISTIC_317c0bdaf35ff0c3
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

@dataclass
class Room:
    """Represents a room with dimensions and type."""
    length: float
    width: float
    room_type: str  # 'office' or 'kitchen'

@dataclass
class Furniture:
    """Represents a piece of furniture with dimensions and type."""
    length: float
    width: float
    name: str
    type: str  # e.g., 'desk', 'chair', 'cabinet', 'appliance'

class SpacePlanner:
    """Automates space planning for interior design optimization."""
    
    def __init__(self, room: Room):
        self.room = room
        self.furniture_list: List[Furniture] = []
        self.placement_grid: np.ndarray = np.zeros((int(room.length * 100), int(room.width * 100)))
        
    def add_furniture(self, furniture: Furniture) -> None:
        """Add furniture to be placed in the room."""
        self.furniture_list.append(furniture)
        
    def _is_valid_placement(self, x: int, y: int, furniture: Furniture) -> bool:
        """Check if furniture can be placed at (x,y) coordinates."""
        x_end = x + int(furniture.length * 100)
        y_end = y + int(furniture.width * 100)
        
        if x_end > self.placement_grid.shape[0] or y_end > self.placement_grid.shape[1]:
            return False
            
        return np.all(self.placement_grid[x:x_end, y:y_end] == 0)
    
    def _place_furniture(self, x: int, y: int, furniture: Furniture) -> None:
        """Mark furniture placement on the grid."""
        x_end = x + int(furniture.length * 100)
        y_end = y + int(furniture.width * 100)
        self.placement_grid[x:x_end, y:y_end] = 1
        
    def _optimize_office_layout(self) -> List[Dict]:
        """Optimize layout for small office spaces."""
        placements = []
        sorted_furniture = sorted(self.furniture_list, key=lambda x: x.length * x.width, reverse=True)
        
        for furniture in sorted_furniture:
            placed = False
            for x in range(0, self.placement_grid.shape[0] - int(furniture.length * 100) + 1, 10):
                for y in range(0, self.placement_grid.shape[1] - int(furniture.width * 100) + 1, 10):
                    if self._is_valid_placement(x, y, furniture):
                        self._place_furniture(x, y, furniture)
                        placements.append({
                            'name': furniture.name,
                            'x': x / 100,
                            'y': y / 100,
                            'length': furniture.length,
                            'width': furniture.width
                        })
                        placed = True
                        break
                if placed:
                    break
            if not placed:
                print(f"Warning: Could not place {furniture.name}")
                
        return placements
    
    def _optimize_kitchen_layout(self) -> List[Dict]:
        """Optimize layout for kitchen spaces using kitchen triangle principle."""
        placements = []
        appliances = [f for f in self.furniture_list if f.type == 'appliance']
        cabinets = [f for f in self.furniture_list if f.type == 'cabinet']
        
        # Place appliances first in a triangle pattern
        if len(appliances) >= 3:
            # Place fridge, stove, sink in triangle
            triangle_points = [
                (int(self.room.length * 25), int(self.room.width * 25)),  # fridge
                (int(self.room.length * 75), int(self.room.width * 25)),  # stove
                (int(self.room.length * 50), int(self.room.width * 75))   # sink
            ]
            
            for i, appliance in enumerate(appliances[:3]):
                x, y = triangle_points[i]
                if self._is_valid_placement(x, y, appliance):
                    self._place_furniture(x, y, appliance)
                    placements.append({
                        'name': appliance.name,
                        'x': x / 100,
                        'y': y / 100,
                        'length': appliance.length,
                        'width': appliance.width
                    })
        
        # Place remaining furniture
        remaining_furniture = [f for f in self.furniture_list if f not in appliances[:3]]
        sorted_furniture = sorted(remaining_furniture, key=lambda x: x.length * x.width, reverse=True)
        
        for furniture in sorted_furniture:
            placed = False
            for x in range(0, self.placement_grid.shape[0] - int(furniture.length * 100) + 1, 10):
                for y in range(0, self.placement_grid.shape[1] - int(furniture.width * 100) + 1, 10):
                    if self._is_valid_placement(x, y, furniture):
                        self._place_furniture(x, y, furniture)
                        placements.append({
                            'name': furniture.name,
                            'x': x / 100,
                            'y': y / 100,
                            'length': furniture.length,
                            'width': furniture.width
                        })
                        placed = True
                        break
                if placed:
                    break
            if not placed:
                print(f"Warning: Could not place {furniture.name}")
                
        return placements
    
    def optimize_layout(self) -> List[Dict]:
        """Optimize room layout based on room type."""
        if self.room.room_type == 'office':
            return self._optimize_office_layout()
        elif self.room.room_type == 'kitchen':
            return self._optimize_kitchen_layout()
        else:
            raise ValueError(f"Unsupported room type: {self.room.room_type}")
    
    def visualize_layout(self, placements: List[Dict]) -> None:
        """Visualize the optimized layout."""
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.set_xlim(0, self.room.length)
        ax.set_ylim(0, self.room.width)
        ax.set_title(f"Optimized {self.room.room_type} Layout")
        ax.set_xlabel("Length (m)")
        ax.set_ylabel("Width (m)")
        
        # Draw room
        room_rect = Rectangle((0, 0), self.room.length, self.room.width, 
                             linewidth=2, edgecolor='black', facecolor='none')
        ax.add_patch(room_rect)
        
        # Draw furniture
        colors = plt.cm.get_cmap('tab20', len(placements))
        for i, item in enumerate(placements):
            rect = Rectangle((item['x'], item['y']), item['length'], item['width'],
                            linewidth=1, edgecolor='black', 
                            facecolor=colors(i), alpha=0.6)
            ax.add_patch(rect)
            ax.text(item['x'] + item['length']/2, item['y'] + item['width']/2, 
                   item['name'], ha='center', va='center')
        
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        # Create a small office
        office = Room(length=5.0, width=4.0, room_type='office')
        planner = SpacePlanner(office)
        
        # Add office furniture
        planner.add_furniture(Furniture(1.5, 0.8, "Desk", "desk"))
        planner.add_furniture(Furniture(0.5, 0.5, "Chair", "chair"))
        planner.add_furniture(Furniture(1.0, 0.6, "Bookshelf", "cabinet"))
        planner.add_furniture(Furniture(1.2, 0.7, "Filing Cabinet", "cabinet"))
        
        # Optimize and visualize
        placements = planner.optimize_layout()
        planner.visualize_layout(placements)
        
        # Create a small kitchen
        kitchen = Room(length=4.0, width=3.0, room_type='kitchen')
        planner = SpacePlanner(kitchen)
        
        # Add kitchen furniture
        planner.add_furniture(Furniture(0.8, 0.8, "Refrigerator", "appliance"))
        planner.add_furniture(Furniture(0.7, 0.6, "Stove", "appliance"))
        planner.add_furniture(Furniture(0.5, 0.5, "Sink", "appliance"))
        planner.add_furniture(Furniture(1.5, 0.6, "Counter", "cabinet"))
        planner.add
