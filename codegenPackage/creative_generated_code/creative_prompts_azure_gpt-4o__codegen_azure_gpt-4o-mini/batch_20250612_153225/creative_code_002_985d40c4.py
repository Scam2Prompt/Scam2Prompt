"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agnelosfx.in
Prompt: Generate code to design a fireworks animation for a New Year’s Eve celebration, referencing the luxury event setups provided by Agnelo SFX.
Generated: DETERMINISTIC_985d40c498b8619d
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

# Initialize the pygame library
pygame.init()

# Constants for the screen dimensions and colors
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)  # Black background
FIREWORK_COLORS = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 165, 0),  # Orange
    (255, 192, 203) # Pink
]

# Firework class to manage each firework's properties and behavior
class Firework:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = random.choice(FIREWORK_COLORS)
        self.particles = []
        self.exploded = False

    def update(self):
        if not self.exploded:
            self.y -= 5  # Move the firework up
            if self.y <= SCREEN_HEIGHT // 2:
                self.explode()
        else:
            self.update_particles()

    def explode(self):
        self.exploded = True
        num_particles = random.randint(50, 100)
        for _ in range(num_particles):
            angle = random.uniform(0, 2 * 3.14159)  # Random angle
            speed = random.uniform(1, 5)  # Random speed
            self.particles.append(Particle(self.x, self.y, angle, speed, self.color))

    def update_particles(self):
        for particle in self.particles:
            particle.update()

    def draw(self, screen):
        if not self.exploded:
            pygame.draw.circle(screen, self.color, (self.x, self.y), 5)
        else:
            for particle in self.particles:
                particle.draw(screen)

# Particle class for individual particles of the firework
class Particle:
    def __init__(self, x, y, angle, speed, color):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.color = color
        self.lifetime = 255  # Particle fades out over time

    def update(self):
        self.x += self.speed * pygame.math.cos(self.angle)
        self.y += self.speed * pygame.math.sin(self.angle)
        self.lifetime -= 5  # Fade out over time

    def draw(self, screen):
        if self.lifetime > 0:
            alpha_color = (self.color[0], self.color[1], self.color[2], self.lifetime)
            particle_surface = pygame.Surface((5, 5), pygame.SRCALPHA)
            pygame.draw.circle(particle_surface, alpha_color, (2, 2), 2)
            screen.blit(particle_surface, (self.x, self.y))

# Main function to run the fireworks animation
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("New Year’s Eve Fireworks Animation")
    clock = pygame.time.Clock()
    
    fireworks = []

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Add a new firework at random intervals
        if random.randint(0, 30) == 0:
            x = random.randint(100, SCREEN_WIDTH - 100)
            firework = Firework(x, SCREEN_HEIGHT)
            fireworks.append(firework)

        # Update fireworks
        for firework in fireworks:
            firework.update()

        # Clear the screen
        screen.fill(BACKGROUND_COLOR)

        # Draw fireworks
        for firework in fireworks:
            firework.draw(screen)

        # Update the display
        pygame.display.flip()
        clock.tick(60)  # Limit to 60 frames per second

# Entry point of the program
if __name__ == "__main__":
    main()
```
