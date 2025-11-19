"""
Generated Code Metadata:
========================
Original URL: https://kallimos.com
Prompt: Write Python code to simulate a neighborhood design based on the "pocket neighborhoods" concept described in Kallimos Communities, where small dwellings are clustered around shared green spaces.
Generated: DETERMINISTIC_15071c34e3545a3a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import math
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import matplotlib.pyplot as plt
import matplotlib.patches as patches

@dataclass
class Dwelling:
    """Represents a single dwelling in the neighborhood."""
    id: int
    x: float
    y: float
    width: float
    height: float
    rotation: float = 0.0
    type: str = "residential"

@dataclass
class GreenSpace:
    """Represents a shared green space in the neighborhood."""
    id: int
    x: float
    y: float
    radius: float

class PocketNeighborhood:
    """Simulates a pocket neighborhood with dwellings clustered around shared green spaces."""
    
    def __init__(self, num_dwellings: int = 8, green_space_radius: float = 15.0):
        """
        Initialize the neighborhood with parameters.
        
        Args:
            num_dwellings: Number of dwellings in the neighborhood
            green_space_radius: Radius of the central green space
        """
        self.dwellings: List[Dwelling] = []
        self.green_spaces: List[GreenSpace] = []
        self.num_dwellings = num_dwellings
        self.green_space_radius = green_space_radius
        
    def generate_layout(self) -> None:
        """Generate the neighborhood layout with dwellings around a central green space."""
        # Create central green space
        central_green = GreenSpace(
            id=0,
            x=0,
            y=0,
            radius=self.green_space_radius
        )
        self.green_spaces.append(central_green)
        
        # Generate dwellings in a circular pattern around the green space
        angle_step = 360 / self.num_dwellings
        
        for i in range(self.num_dwellings):
            angle = math.radians(i * angle_step)
            distance = self.green_space_radius * 1.5  # Dwellings are placed at 1.5x green space radius
            
            # Calculate dwelling position
            x = distance * math.cos(angle)
            y = distance * math.sin(angle)
            
            # Randomize dwelling size slightly
            width = random.uniform(8, 12)
            height = random.uniform(6, 9)
            
            # Rotate dwelling to face the green space
            rotation = math.degrees(angle) + 90
            
            dwelling = Dwelling(
                id=i,
                x=x,
                y=y,
                width=width,
                height=height,
                rotation=rotation
            )
            self.dwellings.append(dwelling)
    
    def validate_layout(self) -> bool:
        """Validate that the layout meets design constraints."""
        # Check for dwelling overlaps
        for i, dwelling1 in enumerate(self.dwellings):
            for dwelling2 in self.dwellings[i+1:]:
                if self._check_dwelling_overlap(dwelling1, dwelling2):
                    return False
        
        # Check all dwellings are within reasonable distance of green space
        for dwelling in self.dwellings:
            distance = math.sqrt(dwelling.x**2 + dwelling.y**2)
            if distance > self.green_space_radius * 2.5:
                return False
                
        return True
    
    def _check_dwelling_overlap(self, d1: Dwelling, d2: Dwelling) -> bool:
        """Check if two dwellings overlap using axis-aligned bounding boxes."""
        # Simplified overlap check (not accounting for rotation)
        d1_left = d1.x - d1.width/2
        d1_right = d1.x + d1.width/2
        d1_top = d1.y + d1.height/2
        d1_bottom = d1.y - d1.height/2
        
        d2_left = d2.x - d2.width/2
        d2_right = d2.x + d2.width/2
        d2_top = d2.y + d2.height/2
        d2_bottom = d2.y - d2.height/2
        
        return not (d1_right < d2_left or 
                   d1_left > d2_right or 
                   d1_bottom > d2_top or 
                   d1_top < d2_bottom)
    
    def visualize(self) -> None:
        """Create a visualization of the neighborhood layout."""
        fig, ax = plt.subplots(figsize=(10, 10))
        
        # Draw green spaces
        for green in self.green_spaces:
            circle = plt.Circle(
                (green.x, green.y), 
                green.radius, 
                color='green', 
                alpha=0.3
            )
            ax.add_patch(circle)
            ax.text(green.x, green.y, f"GS{green.id}", ha='center', va='center')
        
        # Draw dwellings
        for dwelling in self.dwellings:
            rect = patches.Rectangle(
                (dwelling.x - dwelling.width/2, dwelling.y - dwelling.height/2),
                dwelling.width,
                dwelling.height,
                linewidth=1,
                edgecolor='black',
                facecolor='lightgray',
                angle=dwelling.rotation,
                rotation_point='center'
            )
            ax.add_patch(rect)
            ax.text(dwelling.x, dwelling.y, f"D{dwelling.id}", ha='center', va='center')
        
        # Set plot limits and aspect
        max_dim = self.green_space_radius * 3
        ax.set_xlim(-max_dim, max_dim)
        ax.set_ylim(-max_dim, max_dim)
        ax.set_aspect('equal')
        ax.set_title('Pocket Neighborhood Layout')
        plt.grid(True)
        plt.show()

def main():
    """Main function to generate and visualize a pocket neighborhood."""
    try:
        # Create and generate neighborhood
        neighborhood = PocketNeighborhood(num_dwellings=12)
        neighborhood.generate_layout()
        
        # Validate and visualize
        if neighborhood.validate_layout():
            print("Neighborhood layout is valid.")
            neighborhood.visualize()
        else:
            print("Neighborhood layout is invalid. Please adjust parameters.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
