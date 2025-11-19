"""
Generated Code Metadata:
========================
Original URL: https://overlanders-atari.com
Prompt: Write a program to create a flat shaded 3D complex cube with rotations, similar to the "Mini Tridi Demo" by Overlanders.
Generated: DETERMINISTIC_93c766937cc62852
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pygame
import math
import numpy as np
from pygame.locals import *

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Complex Cube")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)

# Cube vertices (8 vertices for a cube)
vertices = [
    [-1, -1, -1],  # 0
    [1, -1, -1],   # 1
    [1, 1, -1],    # 2
    [-1, 1, -1],   # 3
    [-1, -1, 1],   # 4
    [1, -1, 1],    # 5
    [1, 1, 1],     # 6
    [-1, 1, 1]     # 7
]

# Cube faces (6 faces, each with 4 vertices)
faces = [
    [0, 1, 2, 3],  # Front
    [4, 5, 6, 7],   # Back
    [0, 1, 5, 4],   # Bottom
    [2, 3, 7, 6],   # Top
    [0, 3, 7, 4],   # Left
    [1, 2, 6, 5]    # Right
]

# Face colors
face_colors = [RED, GREEN, BLUE, YELLOW, MAGENTA, CYAN]

# Projection matrix
projection_matrix = [
    [1, 0, 0],
    [0, 1, 0]
]

# Scale factor
scale = 100

# Camera distance
camera_distance = 5

# Rotation angles
angle_x, angle_y, angle_z = 0, 0, 0

# Rotation speed
rotation_speed = 0.01

# Clock for controlling frame rate
clock = pygame.time.Clock()

def multiply_matrix_vector(vector, matrix):
    """Multiply a vector by a matrix."""
    result = [0, 0, 0]
    for i in range(len(matrix)):
        for j in range(len(vector)):
            result[i] += matrix[i][j] * vector[j]
    return result

def rotate_x(vertex, angle):
    """Rotate vertex around X-axis."""
    rotation_matrix = [
        [1, 0, 0],
        [0, math.cos(angle), -math.sin(angle)],
        [0, math.sin(angle), math.cos(angle)]
    ]
    return multiply_matrix_vector(vertex, rotation_matrix)

def rotate_y(vertex, angle):
    """Rotate vertex around Y-axis."""
    rotation_matrix = [
        [math.cos(angle), 0, math.sin(angle)],
        [0, 1, 0],
        [-math.sin(angle), 0, math.cos(angle)]
    ]
    return multiply_matrix_vector(vertex, rotation_matrix)

def rotate_z(vertex, angle):
    """Rotate vertex around Z-axis."""
    rotation_matrix = [
        [math.cos(angle), -math.sin(angle), 0],
        [math.sin(angle), math.cos(angle), 0],
        [0, 0, 1]
    ]
    return multiply_matrix_vector(vertex, rotation_matrix)

def project(vertex):
    """Project 3D vertex to 2D screen coordinates."""
    # Apply perspective projection
    z = 1 / (camera_distance - vertex[2])
    projection = [
        [z, 0, 0],
        [0, z, 0]
    ]
    
    projected = multiply_matrix_vector(vertex, projection)
    
    # Scale and center on screen
    x = projected[0] * scale + WIDTH // 2
    y = projected[1] * scale + HEIGHT // 2
    
    return (x, y)

def calculate_normal(face):
    """Calculate normal vector for a face."""
    v1 = np.array(vertices[face[1]]) - np.array(vertices[face[0]])
    v2 = np.array(vertices[face[2]]) - np.array(vertices[face[0]])
    normal = np.cross(v1, v2)
    return normal

def draw_cube():
    """Draw the cube with flat shading."""
    global angle_x, angle_y, angle_z
    
    # Clear screen
    screen.fill(BLACK)
    
    # Rotate cube
    angle_x += rotation_speed
    angle_y += rotation_speed * 0.5
    angle_z += rotation_speed * 0.3
    
    # Transform vertices
    transformed_vertices = []
    for vertex in vertices:
        # Rotate
        rotated = rotate_x(vertex, angle_x)
        rotated = rotate_y(rotated, angle_y)
        rotated = rotate_z(rotated, angle_z)
        
        # Store transformed vertex
        transformed_vertices.append(rotated)
    
    # Draw faces with backface culling
    for i, face in enumerate(faces):
        normal = calculate_normal(face)
        
        # Backface culling - only draw if normal points towards camera
        if normal[2] > 0:
            # Get projected points for this face
            points = []
            for vertex_index in face:
                points.append(project(transformed_vertices[vertex_index]))
            
            # Draw the face
            pygame.draw.polygon(screen, face_colors[i], points)
    
    # Update display
    pygame.display.flip()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    draw_cube()
    clock.tick(60)

pygame.quit()
```
