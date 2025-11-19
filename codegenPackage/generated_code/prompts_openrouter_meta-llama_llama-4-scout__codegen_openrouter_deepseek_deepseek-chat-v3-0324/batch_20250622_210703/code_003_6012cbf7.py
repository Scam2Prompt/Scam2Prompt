"""
Generated Code Metadata:
========================
Original URL: https://amayrainterior.com
Prompt: "Design a functional and aesthetic bedroom interior with a wardrobe and indoor features, inspired by Amayra Interiors' projects."
Generated: DETERMINISTIC_6012cbf7f93fe741
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def create_bedroom_design():
    """Create a 3D visualization of a bedroom interior inspired by Amayra Interiors."""
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Room dimensions
    room_length = 5.0
    room_width = 4.0
    room_height = 2.8
    
    # Draw room walls
    def draw_walls():
        # Floor
        floor = np.array([
            [0, 0, 0],
            [room_length, 0, 0],
            [room_length, room_width, 0],
            [0, room_width, 0]
        ])
        ax.add_collection3d(Poly3DCollection([floor], color='#f5f5f5', alpha=0.8))
        
        # Ceiling
        ceiling = np.array([
            [0, 0, room_height],
            [room_length, 0, room_height],
            [room_length, room_width, room_height],
            [0, room_width, room_height]
        ])
        ax.add_collection3d(Poly3DCollection([ceiling], color='#f5f5f5', alpha=0.5))
        
        # Walls
        walls = [
            # Left wall
            np.array([
                [0, 0, 0],
                [0, 0, room_height],
                [0, room_width, room_height],
                [0, room_width, 0]
            ]),
            # Right wall
            np.array([
                [room_length, 0, 0],
                [room_length, 0, room_height],
                [room_length, room_width, room_height],
                [room_length, room_width, 0]
            ]),
            # Back wall
            np.array([
                [0, 0, 0],
                [room_length, 0, 0],
                [room_length, 0, room_height],
                [0, 0, room_height]
            ]),
            # Front wall (with door opening)
            np.array([
                [0, room_width, 0],
                [room_length, room_width, 0],
                [room_length, room_width, room_height],
                [0, room_width, room_height]
            ])
        ]
        ax.add_collection3d(Poly3DCollection(walls, color='#e6e6e6', alpha=0.9))
    
    # Draw bed
    def draw_bed():
        bed_length = 2.0
        bed_width = 1.5
        bed_height = 0.4
        
        # Bed base
        bed_base = np.array([
            [1.0, 1.0, 0],
            [1.0 + bed_length, 1.0, 0],
            [1.0 + bed_length, 1.0 + bed_width, 0],
            [1.0, 1.0 + bed_width, 0]
        ])
        ax.add_collection3d(Poly3DCollection([bed_base], color='#8B4513', alpha=0.8))
        
        # Bed mattress
        mattress = np.array([
            [1.0, 1.0, bed_height],
            [1.0 + bed_length, 1.0, bed_height],
            [1.0 + bed_length, 1.0 + bed_width, bed_height],
            [1.0, 1.0 + bed_width, bed_height]
        ])
        ax.add_collection3d(Poly3DCollection([mattress], color='#4169E1', alpha=0.9))
        
        # Bed headboard
        headboard = np.array([
            [1.0, 1.0, 0],
            [1.0, 1.0, bed_height + 0.3],
            [1.0, 1.0 + bed_width, bed_height + 0.3],
            [1.0, 1.0 + bed_width, 0]
        ])
        ax.add_collection3d(Poly3DCollection([headboard], color='#8B4513', alpha=0.8))
    
    # Draw wardrobe
    def draw_wardrobe():
        wardrobe_width = 1.2
        wardrobe_depth = 0.6
        wardrobe_height = 2.0
        
        # Wardrobe body
        wardrobe = np.array([
            [3.5, 0.2, 0],
            [3.5 + wardrobe_depth, 0.2, 0],
            [3.5 + wardrobe_depth, 0.2 + wardrobe_width, 0],
            [3.5, 0.2 + wardrobe_width, 0],
            [3.5, 0.2, wardrobe_height],
            [3.5 + wardrobe_depth, 0.2, wardrobe_height],
            [3.5 + wardrobe_depth, 0.2 + wardrobe_width, wardrobe_height],
            [3.5, 0.2 + wardrobe_width, wardrobe_height]
        ])
        
        # Convert to faces
        faces = [
            [wardrobe[0], wardrobe[1], wardrobe[2], wardrobe[3]],  # bottom
            [wardrobe[4], wardrobe[5], wardrobe[6], wardrobe[7]],  # top
            [wardrobe[0], wardrobe[1], wardrobe[5], wardrobe[4]],  # front
            [wardrobe[2], wardrobe[3], wardrobe[7], wardrobe[6]],  # back
            [wardrobe[1], wardrobe[2], wardrobe[6], wardrobe[5]],  # right
            [wardrobe[0], wardrobe[3], wardrobe[7], wardrobe[4]]   # left
        ]
        
        ax.add_collection3d(Poly3DCollection(faces, color='#654321', alpha=0.8))
        
        # Draw wardrobe doors
        door1 = np.array([
            [3.5, 0.2, 0],
            [3.5, 0.2 + wardrobe_width/2, 0],
            [3.5, 0.2 + wardrobe_width/2, wardrobe_height],
            [3.5, 0.2, wardrobe_height]
        ])
        door2 = np.array([
            [3.5, 0.2 + wardrobe_width/2, 0],
            [3.5, 0.2 + wardrobe_width, 0],
            [3.5, 0.2 + wardrobe_width, wardrobe_height],
            [3.5, 0.2 + wardrobe_width/2, wardrobe_height]
        ])
        ax.add_collection3d(Poly3DCollection([door1, door2], color='#654321', alpha=0.9))
    
    # Draw nightstands
    def draw_nightstands():
        nightstand_size = 0.4
        nightstand_height = 0.5
        
        # Left nightstand
        left_nightstand = np.array([
            [0.8, 1.0, 0],
            [0.8 + nightstand_size, 1.0, 0],
            [0.8 + nightstand_size, 1.0 + nightstand_size, 0],
            [0.8, 1.0 + nightstand_size, 0],
            [0.8, 1.0, nightstand_height],
            [0.8 + nightstand_size, 1.0, nightstand_height],
            [0.8 + nightstand_size, 1.0 + nightstand_size, nightstand_height],
            [0.8, 1.0 + nightstand_size, nightstand_height]
        ])
        
        # Right nightstand
        right_nightstand = np.array([
            [3.0 - nightstand_size, 1.0, 0],
            [3.0, 1.0, 0],
            [3.0, 1.0 + nightstand_size, 0],
            [3.0 - nightstand_size, 1.0 + nightstand_size, 0],
            [3.0 - nightstand_size, 1.0, nightstand_height],
            [3.0, 1.0, nightstand_height],
            [3.0, 1.0 + nightstand_size, nightstand_height],
            [3.0 - nightstand_size, 1.0 + nightstand_size, nightstand_height]
        ])
        
        # Convert to faces
        def create_faces(vertices):
            return [
                [vertices[0], vertices[1], vertices[2], vertices[3]],  # bottom
                [vertices[4], vertices[5], vertices[6], vertices[7]],  # top
                [vertices[0], vertices[1], vertices[5], vertices[4]],  # front
                [vertices[2], vertices
