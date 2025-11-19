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

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Rotation angles
angle_x, angle_y = 0, 0

# Cube vertices
vertices = [
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1]
]

# Cube edges
edges = [
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 0],
    [4, 5],
    [5, 6],
    [6, 7],
    [7, 4],
    [0, 4],
    [1, 5],
    [2, 6],
    [3, 7]
]

def rotate_x(vertex, angle):
    """Rotate vertex around X axis"""
    return [vertex[0], vertex[1] * math.cos(angle) - vertex[2] * math.sin(angle), vertex[1] * math.sin(angle) + vertex[2] * math.cos(angle)]

def rotate_y(vertex, angle):
    """Rotate vertex around Y axis"""
    return [vertex[0] * math.cos(angle) + vertex[2] * math.sin(angle), vertex[1], -vertex[0] * math.sin(angle) + vertex[2] * math.cos(angle)]

def project(vertex):
    """Project 3D vertex to 2D screen"""
    z_distance = 5
    factor = 200 / (z_distance - vertex[2])
    return [vertex[0] * factor + WIDTH // 2, -vertex[1] * factor + HEIGHT // 2]

def draw_cube(screen, vertices, edges):
    """Draw cube on screen"""
    for edge in edges:
        start = project(vertices[edge[0]])
        end = project(vertices[edge[1]])
        pygame.draw.line(screen, (255, 255, 255), start, end, 2)

def main():
    global angle_x, angle_y
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        rotated_vertices = []
        for vertex in vertices:
            rotated_x = rotate_x(vertex, angle_x)
            rotated_xy = rotate_y(rotated_x, angle_y)
            rotated_vertices.append(rotated_xy)

        draw_cube(screen, rotated_vertices, edges)

        angle_x += 0.01
        angle_y += 0.01

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
```
