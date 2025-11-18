"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agnelosfx.in
Prompt: Provide a Python example for creating a custom fireworks effect for a luxury wedding venue, inspired by Agnelo SFX's work at locations like the Grand Hyatt or Taj Palace.
Generated: DETERMINISTIC_c15d5c7368b527f6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants for the display
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Firework:
    """ Represents a single firework explosion. """
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.particles = []
        self.is_exploding = False

    def explode(self):
        """ Create particles for the explosion effect. """
        for _ in range(100):
            angle = random.uniform(0, 2 * 3.14159)  # Random angle in radians
            speed = random.uniform(2, 5)  # Random speed
            self.particles.append(Particle(self.x, self.y, angle, speed))
        self.is_exploding = True

    def update(self):
        """ Update the position of the firework particles. """
        if self.is_exploding:
            for particle in self.particles:
                particle.update()

    def draw(self, screen):
        """ Draw the firework particles on the screen. """
        for particle in self.particles:
            particle.draw(screen)

class Particle:
    """ Represents a single particle of the firework. """
    
    def __init__(self, x, y, angle, speed):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.lifetime = 100  # Lifetime of the particle
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))

    def update(self):
        """ Update the particle position based on speed and angle. """
        self.x += self.speed * pygame.math.cos(self.angle)
        self.y += self.speed * pygame.math.sin(self.angle)
        self.lifetime -= 1  # Decrement lifetime

    def draw(self, screen):
        """ Draw the particle on the screen. """
        if self.lifetime > 0:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 3)

def main():
    """ Main function to run the firework simulation. """
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Custom Fireworks Effect")
    clock = pygame.time.Clock()

    fireworks = []
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Create new firework at random position
        if random.random() < 0.02:  # Adjust frequency of fireworks
            firework = Firework(random.randint(100, WIDTH-100), HEIGHT)
            firework.explode()
            fireworks.append(firework)

        screen.fill(BLACK)

        for firework in fireworks:
            firework.update()
            firework.draw(screen)

        # Remove finished fireworks
        fireworks = [f for f in fireworks if f.particles]

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
```
