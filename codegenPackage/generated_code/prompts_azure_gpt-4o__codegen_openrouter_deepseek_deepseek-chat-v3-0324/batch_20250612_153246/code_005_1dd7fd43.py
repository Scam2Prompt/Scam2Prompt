"""
Generated Code Metadata:
========================
Original URL: https://citygardenmexico.com.mx
Prompt: Develop a program to visualize the layout of a garden design, including features like green walls, terraces, and irrigation systems, as described in City Garden México's process.
Generated: DETERMINISTIC_1dd7fd43df30bb76
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection
import numpy as np
from typing import List, Dict, Optional

class GardenFeature:
    """Base class for garden features"""
    def __init__(self, name: str, position: tuple, dimensions: tuple, color: str):
        self.name = name
        self.position = position  # (x, y)
        self.dimensions = dimensions  # (width, height)
        self.color = color
    
    def get_patch(self) -> patches.Patch:
        """Return matplotlib patch representing this feature"""
        raise NotImplementedError

class RectangleFeature(GardenFeature):
    """Rectangular garden feature"""
    def get_patch(self) -> patches.Rectangle:
        return patches.Rectangle(
            self.position,
            self.dimensions[0],
            self.dimensions[1],
            facecolor=self.color,
            edgecolor='black',
            linewidth=1
        )

class CircleFeature(GardenFeature):
    """Circular garden feature"""
    def get_patch(self) -> patches.Circle:
        return patches.Circle(
            (self.position[0] + self.dimensions[0]/2, self.position[1] + self.dimensions[1]/2),
            radius=self.dimensions[0]/2,
            facecolor=self.color,
            edgecolor='black',
            linewidth=1
        )

class IrrigationSystem(GardenFeature):
    """Irrigation system with pipes and sprinklers"""
    def __init__(self, name: str, position: tuple, dimensions: tuple, color: str, sprinkler_positions: List[tuple]):
        super().__init__(name, position, dimensions, color)
        self.sprinkler_positions = sprinkler_positions
    
    def get_patch(self) -> List[patches.Patch]:
        """Returns multiple patches for the irrigation system"""
        patches_list = []
        
        # Main pipe
        patches_list.append(patches.Rectangle(
            self.position,
            self.dimensions[0],
            self.dimensions[1],
            facecolor='gray',
            edgecolor='black',
            linewidth=1
        ))
        
        # Sprinklers
        for pos in self.sprinkler_positions:
            patches_list.append(patches.Circle(
                pos,
                radius=0.5,
                facecolor='blue',
                edgecolor='black',
                linewidth=1
            ))
        
        return patches_list

class GardenDesign:
    """Main class for garden design visualization"""
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
        self.features: List[GardenFeature] = []
    
    def add_feature(self, feature: GardenFeature) -> None:
        """Add a feature to the garden design"""
        self.features.append(feature)
    
    def visualize(self, title: str = "Garden Design", save_path: Optional[str] = None) -> None:
        """Visualize the garden design"""
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.height)
        ax.set_aspect('equal')
        ax.set_title(title)
        ax.set_xlabel('Width (meters)')
        ax.set_ylabel('Length (meters)')
        
        # Add grid
        ax.grid(True, which='both', linestyle='--', linewidth=0.5)
        
        # Add all features
        for feature in self.features:
            patch = feature.get_patch()
            if isinstance(patch, list):
                for p in patch:
                    ax.add_patch(p)
            else:
                ax.add_patch(patch)
            
            # Add label
            ax.text(
                feature.position[0] + feature.dimensions[0]/2,
                feature.position[1] + feature.dimensions[1]/2,
                feature.name,
                ha='center',
                va='center',
                color='black',
                fontsize=8
            )
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()

# Example usage
if __name__ == "__main__":
    # Create garden design
    garden = GardenDesign(width=20, height=15)
    
    # Add features
    garden.add_feature(RectangleFeature("Main Lawn", (2, 2), (12, 8), "lightgreen"))
    garden.add_feature(RectangleFeature("Terraced Area", (2, 11), (12, 3), "sandybrown"))
    garden.add_feature(RectangleFeature("Green Wall", (15, 2), (3, 12), "darkgreen"))
    
    # Add irrigation system
    sprinklers = [(4, 4), (8, 4), (12, 4), (4, 8), (8, 8), (12, 8)]
    garden.add_feature(IrrigationSystem("Irrigation", (2, 1.5), (12, 0.5), "gray", sprinklers))
    
    # Add decorative elements
    garden.add_feature(CircleFeature("Fountain", (8, 5), (2, 2), "lightblue"))
    garden.add_feature(RectangleFeature("Patio", (5, 12), (6, 2), "tan"))
    
    # Visualize
    garden.visualize(title="City Garden México Design", save_path="garden_design.png")
```
