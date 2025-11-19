"""
Generated Code Metadata:
========================
Original URL: https://sproutstudios.in
Prompt: "Write a code snippet to create a motion graphics animation similar to the ones showcased in Sprout Studios' work for TV series like Dream Street and Jinnie and friends."
Generated: DETERMINISTIC_52f95aed0bd5d219
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pygame
import random
import math
from pygame import gfxdraw

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Motion Graphics Animation")

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Colors
BACKGROUND = (20, 20, 30)
PRIMARY = (255, 215, 0)
SECONDARY = (100, 200, 255)
ACCENT = (255, 100, 150)

# Particle class for animated elements
class Particle:
    def __init__(self, x, y, color, size, velocity, lifespan):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.velocity = velocity
        self.lifespan = lifespan
        self.age = 0
        
    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.age += 1
        self.size = max(0, self.size - 0.1)
        
    def draw(self, surface):
        alpha = min(255, int(255 * (1 - self.age / self.lifespan)))
        color = (*self.color[:3], alpha)
        gfxdraw.filled_circle(surface, int(self.x), int(self.y), int(self.size), color)

# Shape animation class
class ShapeAnimation:
    def __init__(self):
        self.particles = []
        self.shapes = []
        self.time = 0
        self.create_initial_shapes()
        
    def create_initial_shapes(self):
        # Create some initial geometric shapes
        for _ in range(5):
            shape = {
                'type': random.choice(['circle', 'square', 'triangle']),
                'pos': [random.randint(100, WIDTH-100), random.randint(100, HEIGHT-100)],
                'size': random.randint(30, 80),
                'color': random.choice([PRIMARY, SECONDARY, ACCENT]),
                'velocity': [random.uniform(-1, 1), random.uniform(-1, 1)],
                'rotation': 0,
                'rotation_speed': random.uniform(-2, 2)
            }
            self.shapes.append(shape)
            
    def update(self):
        self.time += 1
        
        # Update shapes
        for shape in self.shapes:
            shape['pos'][0] += shape['velocity'][0]
            shape['pos'][1] += shape['velocity'][1]
            shape['rotation'] += shape['rotation_speed']
            
            # Bounce off edges
            if shape['pos'][0] < shape['size'] or shape['pos'][0] > WIDTH - shape['size']:
                shape['velocity'][0] *= -1
            if shape['pos'][1] < shape['size'] or shape['pos'][1] > HEIGHT - shape['size']:
                shape['velocity'][1] *= -1
                
            # Occasionally emit particles
            if random.random() < 0.02:
                for _ in range(3):
                    angle = random.uniform(0, math.pi * 2)
                    speed = random.uniform(0.5, 2)
                    self.particles.append(
                        Particle(
                            shape['pos'][0], shape['pos'][1],
                            (*shape['color'], 150),
                            random.randint(2, 5),
                            [math.cos(angle) * speed, math.sin(angle) * speed],
                            random.randint(30, 60)
                        )
                    )
        
        # Update particles
        for particle in self.particles[:]:
            particle.update()
            if particle.age >= particle.lifespan:
                self.particles.remove(particle)
                
        # Occasionally add new shapes
        if self.time % 120 == 0 and len(self.shapes) < 10:
            self.shapes.append({
                'type': random.choice(['circle', 'square', 'triangle']),
                'pos': [random.randint(100, WIDTH-100), random.randint(100, HEIGHT-100)],
                'size': random.randint(30, 80),
                'color': random.choice([PRIMARY, SECONDARY, ACCENT]),
                'velocity': [random.uniform(-1, 1), random.uniform(-1, 1)],
                'rotation': 0,
                'rotation_speed': random.uniform(-2, 2)
            })
            
    def draw(self, surface):
        surface.fill(BACKGROUND)
        
        # Draw particles
        for particle in self.particles:
            particle.draw(surface)
            
        # Draw shapes
        for shape in self.shapes:
            if shape['type'] == 'circle':
                pygame.draw.circle(
                    surface, shape['color'],
                    (int(shape['pos'][0]), int(shape['pos'][1])),
                    shape['size'], 2
                )
            elif shape['type'] == 'square':
                points = [
                    (shape['pos'][0] - shape['size'], shape['pos'][1] - shape['size']),
                    (shape['pos'][0] + shape['size'], shape['pos'][1] - shape['size']),
                    (shape['pos'][0] + shape['size'], shape['pos'][1] + shape['size']),
                    (shape['pos'][0] - shape['size'], shape['pos'][1] + shape['size'])
                ]
                pygame.draw.polygon(surface, shape['color'], points, 2)
            elif shape['type'] == 'triangle':
                points = [
                    (shape['pos'][0], shape['pos'][1] - shape['size']),
                    (shape['pos'][0] - shape['size'], shape['pos'][1] + shape['size']),
                    (shape['pos'][0] + shape['size'], shape['pos'][1] + shape['size'])
                ]
                pygame.draw.polygon(surface, shape['color'], points, 2)

# Main animation loop
def main():
    animation = ShapeAnimation()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        animation.update()
        animation.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
        
    pygame.quit()

if __name__ == "__main__":
    main()
```
