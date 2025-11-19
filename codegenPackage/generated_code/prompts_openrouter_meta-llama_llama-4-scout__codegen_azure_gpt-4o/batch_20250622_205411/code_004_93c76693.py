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

Below is a Python program using the `pygame` library to create a flat-shaded 3D cube with rotations. Ensure you have `pygame` installed (`pip install pygame`) before running the code.

```python
import pygame
import math
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flat Shaded 3D Cube")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Vertices of a cube
vertices = [
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1],
]

# Faces of the cube (each face is a list of vertex indices)
faces = [
    (0, 1, 2, 3, RED),
    (4, 5, 6, 7, GREEN),
    (0, 1, 5, 4, BLUE),
    (2, 3, 7, 6, YELLOW),
    (0, 3, 7, 4, CYAN),
    (1, 2, 6, 5, MAGENTA),
]

# Function to project 3D points to 2D
def project(point, width, height, scale=200):
    x = int(point[0] * scale + width / 2)
    y = int(-point[1] * scale + height / 2)
    return (x, y)

# Function to rotate a point around the X axis
def rotate_x(point, angle):
    x, y, z = point
    y_new = y * math.cos(angle) - z * math.sin(angle)
    z_new = y * math.sin(angle) + z * math.cos(angle)
    return (x, y_new, z_new)

# Function to rotate a point around the Y axis
def rotate_y(point, angle):
    x, y, z = point
    x_new = x * math.cos(angle) + z * math.sin(angle)
    z_new = -x * math.sin(angle) + z * math.cos(angle)
    return (x_new, y, z)

# Function to rotate a point around the Z axis
def rotate_z(point, angle):
    x, y, z = point
    x_new = x * math.cos(angle) - y * math.sin(angle)
    y_new = x * math.sin(angle) + y * math.cos(angle)
    return (x_new, y_new, z)

# Main loop
def main():
    angle_x = 0
    angle_y = 0
    angle_z = 0

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear screen
        screen.fill(BLACK)

        # Rotate cube
        rotated_vertices = []
        for vertex in vertices:
            rotated = rotate_x(vertex, angle_x)
            rotated = rotate_y(rotated, angle_y)
            rotated = rotate_z(rotated, angle_z)
            rotated_vertices.append(rotated)

        # Draw faces
        for face in faces:
            points = [project(rotated_vertices[i], WIDTH, HEIGHT) for i in face[:-1]]
            pygame.draw.polygon(screen, face[-1], points)

        # Update angles for rotation
        angle_x += 0.01
        angle_y += 0.01
        angle_z += 0.01

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

# Run the program
if __name__ == "__main__":
    main()
```

This program creates a rotating 3D cube with flat shading. Each face of the cube is drawn with a solid color. The cube rotates continuously around the X, Y, and Z axes.
