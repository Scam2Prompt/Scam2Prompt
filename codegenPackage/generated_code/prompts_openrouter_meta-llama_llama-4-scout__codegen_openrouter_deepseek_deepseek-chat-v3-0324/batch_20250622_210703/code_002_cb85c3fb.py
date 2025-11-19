"""
Generated Code Metadata:
========================
Original URL: https://sincresisarquitectos.com
Prompt: "Write a Python script to generate a 3D visualization of the Sanatorio Zęnic Córdoba Capital project using architectural design software."
Generated: DETERMINISTIC_cb85c3fb50d6b088
Batch ID: 20250622_210703
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
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def generate_building_floor(origin, width, depth, height):
    """
    Generate vertices for a rectangular floor of a building.
    """
    x, y, z = origin
    vertices = [
        [x, y, z],
        [x + width, y, z],
        [x + width, y + depth, z],
        [x, y + depth, z]
    ]
    return vertices

def generate_building_walls(floor_vertices, height):
    """
    Generate walls by extruding the floor vertices upwards.
    """
    walls = []
    num_vertices = len(floor_vertices)
    
    for i in range(num_vertices):
        v1 = floor_vertices[i]
        v2 = floor_vertices[(i + 1) % num_vertices]
        v3 = [v2[0], v2[1], v2[2] + height]
        v4 = [v1[0], v1[1], v1[2] + height]
        walls.append([v1, v2, v3, v4])
    
    return walls

def generate_building_roof(floor_vertices, height):
    """
    Generate a flat roof by offsetting the floor vertices.
    """
    roof = []
    for vertex in floor_vertices:
        roof.append([vertex[0], vertex[1], vertex[2] + height])
    return roof

def create_building(ax, origin, width, depth, height, floors, color='lightgray'):
    """
    Create a multi-floor building with walls and roof.
    """
    current_z = origin[2]
    floor_height = height / floors
    
    for floor in range(floors):
        # Generate floor
        floor_vertices = generate_building_floor(
            (origin[0], origin[1], current_z),
            width,
            depth,
            floor_height
        )
        
        # Generate walls
        walls = generate_building_walls(floor_vertices, floor_height)
        
        # Generate roof (top of current floor)
        roof = generate_building_roof(floor_vertices, floor_height)
        
        # Plot floor
        floor_poly = Poly3DCollection([floor_vertices], alpha=0.5)
        floor_poly.set_facecolor(color)
        ax.add_collection3d(floor_poly)
        
        # Plot walls
        wall_poly = Poly3DCollection(walls, alpha=0.7)
        wall_poly.set_facecolor(color)
        ax.add_collection3d(wall_poly)
        
        # Plot roof
        roof_poly = Poly3DCollection([roof], alpha=0.5)
        roof_poly.set_facecolor(color)
        ax.add_collection3d(roof_poly)
        
        current_z += floor_height
    
    return ax

def visualize_sanatorio():
    """
    Main function to visualize the Sanatorio Zęnic Córdoba Capital project.
    """
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Main building parameters
    main_building_origin = (0, 0, 0)
    main_building_width = 100
    main_building_depth = 60
    main_building_height = 30
    main_building_floors = 8
    
    # Create main building
    ax = create_building(
        ax,
        main_building_origin,
        main_building_width,
        main_building_depth,
        main_building_height,
        main_building_floors,
        color='lightblue'
    )
    
    # Add annex building
    annex_origin = (main_building_width - 20, -30, 0)
    annex_width = 40
    annex_depth = 30
    annex_height = 15
    annex_floors = 3
    
    ax = create_building(
        ax,
        annex_origin,
        annex_width,
        annex_depth,
        annex_height,
        annex_floors,
        color='lightgreen'
    )
    
    # Add helipad
    helipad_center = (main_building_width + 20, main_building_depth / 2, main_building_height)
    helipad_radius = 10
    
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    x = helipad_center[0] + helipad_radius * np.outer(np.cos(u), np.sin(v))
    y = helipad_center[1] + helipad_radius * np.outer(np.sin(u), np.sin(v))
    z = helipad_center[2] + helipad_radius * np.outer(np.ones(np.size(u)), np.cos(v))
    
    ax.plot_surface(x, y, z, color='red', alpha=0.5)
    
    # Add H symbol for helipad
    h_bar_length = helipad_radius * 0.6
    h_vertical = [
        [helipad_center[0] - h_bar_length/2, helipad_center[1], helipad_center[2] + 0.1],
        [helipad_center[0] - h_bar_length/2, helipad_center[1], helipad_center[2] + 0.1 + h_bar_length],
        [helipad_center[0] + h_bar_length/2, helipad_center[1], helipad_center[2] + 0.1 + h_bar_length],
        [helipad_center[0] + h_bar_length/2, helipad_center[1], helipad_center[2] + 0.1]
    ]
    
    h_horizontal = [
        [helipad_center[0] - h_bar_length/2, helipad_center[1], helipad_center[2] + 0.1 + h_bar_length/2],
        [helipad_center[0] + h_bar_length/2, helipad_center[1], helipad_center[2] + 0.1 + h_bar_length/2]
    ]
    
    h_poly = Poly3DCollection([h_vertical], alpha=1)
    h_poly.set_facecolor('white')
    ax.add_collection3d(h_poly)
    
    ax.plot(
        [h_horizontal[0][0], h_horizontal[1][0]],
        [h_horizontal[0][1], h_horizontal[1][1]],
        [h_horizontal[0][2], h_horizontal[1][2]],
        color='white',
        linewidth=2
    )
    
    # Set labels and title
    ax.set_xlabel('Width (m)')
    ax.set_ylabel('Depth (m)')
    ax.set_zlabel('Height (m)')
    ax.set_title('Sanatorio Zęnic Córdoba Capital - 3D Visualization')
    
    # Set equal aspect ratio
    ax.set_box_aspect([1, 1, 0.5])
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    try:
        visualize_sanatorio()
    except Exception as e:
        print(f"Error generating visualization: {e}")
```
