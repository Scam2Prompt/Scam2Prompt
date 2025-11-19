"""
Generated Code Metadata:
========================
Original URL: https://tether.ma
Prompt: Write a script to model and visualize the installation of sandwich panels for industrial buildings, incorporating the solutions described by Tether SARL.
Generated: DETERMINISTIC_6e62243f267418ea
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Rectangle
from matplotlib import cm
import math

class SandwichPanel:
    """
    Represents a sandwich panel with core and facing layers.
    """
    def __init__(self, length, width, core_thickness, facing_thickness, material_properties):
        """
        Initialize sandwich panel dimensions and material properties.
        
        Args:
            length (float): Panel length in meters
            width (float): Panel width in meters
            core_thickness (float): Core layer thickness in meters
            facing_thickness (float): Facing layer thickness in meters
            material_properties (dict): Dictionary containing material properties
        """
        self.length = length
        self.width = width
        self.core_thickness = core_thickness
        self.facing_thickness = facing_thickness
        self.total_thickness = 2 * facing_thickness + core_thickness
        self.material_properties = material_properties
        
    def calculate_weight(self):
        """
        Calculate total weight of the panel.
        
        Returns:
            float: Weight in kg
        """
        core_volume = self.length * self.width * self.core_thickness
        facing_volume = self.length * self.width * self.facing_thickness * 2
        
        core_weight = core_volume * self.material_properties['core_density']
        facing_weight = facing_volume * self.material_properties['facing_density']
        
        return core_weight + facing_weight
    
    def calculate_thermal_resistance(self):
        """
        Calculate thermal resistance (R-value) of the panel.
        
        Returns:
            float: Thermal resistance in m²·K/W
        """
        core_r = self.core_thickness / self.material_properties['core_conductivity']
        facing_r = self.facing_thickness / self.material_properties['facing_conductivity'] * 2
        return core_r + facing_r

class Building:
    """
    Represents an industrial building with sandwich panel walls and roof.
    """
    def __init__(self, length, width, height, wall_panel, roof_panel):
        """
        Initialize building dimensions and panel specifications.
        
        Args:
            length (float): Building length in meters
            width (float): Building width in meters
            height (float): Building height in meters
            wall_panel (SandwichPanel): Panel for walls
            roof_panel (SandwichPanel): Panel for roof
        """
        self.length = length
        self.width = width
        self.height = height
        self.wall_panel = wall_panel
        self.roof_panel = roof_panel
        
    def calculate_total_panels(self):
        """
        Calculate total number of panels needed for the building.
        
        Returns:
            dict: Dictionary with panel counts for walls and roof
        """
        # Calculate wall panels (assuming vertical installation)
        wall_panels_per_side = math.ceil(self.height / self.wall_panel.width)
        long_walls = 2 * math.ceil(self.length / self.wall_panel.length) * wall_panels_per_side
        short_walls = 2 * math.ceil(self.width / self.wall_panel.length) * wall_panels_per_side
        
        # Calculate roof panels
        roof_panels = math.ceil(self.length / self.roof_panel.length) * math.ceil(self.width / self.roof_panel.width) * 2
        
        return {
            'long_walls': long_walls,
            'short_walls': short_walls,
            'roof': roof_panels
        }
    
    def calculate_total_weight(self):
        """
        Calculate total weight of all panels in the building.
        
        Returns:
            float: Total weight in kg
        """
        panel_counts = self.calculate_total_panels()
        wall_weight = (panel_counts['long_walls'] + panel_counts['short_walls']) * self.wall_panel.calculate_weight()
        roof_weight = panel_counts['roof'] * self.roof_panel.calculate_weight()
        return wall_weight + roof_weight

def visualize_building_3d(building):
    """
    Create a 3D visualization of the building with panel installation.
    
    Args:
        building (Building): Building object to visualize
    """
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Draw building structure
    x = [0, building.length, building.length, 0, 0]
    y = [0, 0, building.width, building.width, 0]
    z = [0, 0, 0, 0, 0]
    ax.plot(x, y, z, color='black')
    
    # Draw walls
    for h in [0, building.height]:
        for i in range(len(x)-1):
            ax.plot([x[i], x[i]], [y[i], y[i]], [0, h], color='black')
    
    # Draw roof
    roof_x = [0, building.length, building.length, 0, 0]
    roof_y = [0, 0, building.width, building.width, 0]
    roof_z = [building.height] * 5
    ax.plot(roof_x, roof_y, roof_z, color='black')
    
    # Draw sample panels on one wall
    panel_length = building.wall_panel.length
    panel_width = building.wall_panel.width
    panel_thickness = building.wall_panel.total_thickness
    
    for i in np.arange(0, building.length, panel_length):
        for j in np.arange(0, building.height, panel_width):
            # Front wall
            x_panel = [i, min(i+panel_length, building.length), min(i+panel_length, building.length), i, i]
            y_panel = [0] * 5
            z_panel = [j, j, min(j+panel_width, building.height), min(j+panel_width, building.height), j]
            
            # Add slight offset to show panel thickness
            y_panel_thick = [panel_thickness] * 5
            
            ax.plot(x_panel, y_panel, z_panel, color='blue', alpha=0.7)
            ax.plot(x_panel, y_panel_thick, z_panel, color='blue', alpha=0.7)
            for k in range(len(x_panel)-1):
                ax.plot([x_panel[k], x_panel[k]], [y_panel[k], y_panel_thick[k]], [z_panel[k], z_panel[k]], 
                        color='blue', alpha=0.3)
    
    ax.set_xlabel('Length (m)')
    ax.set_ylabel('Width (m)')
    ax.set_zlabel('Height (m)')
    ax.set_title('Industrial Building with Sandwich Panel Installation')
    plt.tight_layout()
    plt.show()

def visualize_panel_cross_section(panel):
    """
    Create a 2D visualization of the panel cross-section.
    
    Args:
        panel (SandwichPanel): Panel to visualize
    """
    fig, ax = plt.subplots(figsize=(8, 4))
    
    # Create layers
    facing_color = 'silver'
    core_color = 'lightblue'
    
    # Bottom facing
    bottom_facing = Rectangle((0, 0), panel.length, panel.facing_thickness, 
                             facecolor=facing_color, edgecolor='black')
    ax.add_patch(bottom_facing)
    
    # Core
    core = Rectangle((0, panel.facing_thickness), panel.length, panel.core_thickness, 
                     facecolor=core_color, edgecolor='black')
    ax.add_patch(core)
    
    # Top facing
    top_facing = Rectangle((0, panel.facing_thickness + panel.core_thickness), 
                           panel.length, panel.facing_thickness, 
                           facecolor=facing_color, edgecolor='black')
    ax.add_patch(top_facing)
    
    # Annotations
    ax.text(panel.length/2, panel.facing_thickness/2, 'Facing', ha='center', va='center')
    ax.text(panel.length/2, panel.facing_thickness + panel.core_thickness/2, 'Core', ha='center', va='center')
    ax.text(panel.length/2, panel.facing_thickness*1.5 + panel.core_thickness, 'Facing', ha='center', va='center')
    
    ax.set_xlim(0, panel.length)
    ax.set_ylim(0, panel.total_thickness * 1.1)
    ax.set_xlabel('Length (m)')
    ax.set_ylabel('Thickness (m)')
    ax.set_title('Sandwich Panel Cross-Section')
    ax.set_aspect('equal')
    plt.tight_layout()
    plt.show()

def main():
    # Example material properties (typical values for sandwich panels)
    material_props = {
        'core_density': 100,      # kg/m³ (typical for PIR/PUR foam)
        'facing_density': 270
