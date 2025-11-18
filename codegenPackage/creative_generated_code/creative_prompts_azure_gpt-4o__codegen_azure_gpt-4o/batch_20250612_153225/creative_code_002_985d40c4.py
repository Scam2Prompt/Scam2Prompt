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

# Initialize Pygame
pygame.init()

# Screen setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("New Year's Eve Fireworks Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLOR_PALETTE = [
    (255, 69, 0),  # Orange Red
    (255, 105, 180),  # Hot Pink
    (75, 0, 130),  # Indigo
    (0, 255, 255),  # Cyan
    (255, 255, 0),  # Yellow
    (144, 238, 144),  # Light Green
]

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Firework particle class
class FireworkParticle:
    def __init__(self, x, y, color, life, velocity):
        self.x = x
        self.y = y
        self.color = color
        self.radius = random.randint(2, 5)
        self.life = life
        self.velocity = velocity

    def update(self):
        """Update particle position and reduce life."""
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.life -= 1

    def draw(self, surface):
        """Draw particle on the screen."""
        if self.life > 0:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)


# Firework class
class Firework:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.particles = []
        self.create_particles()

    def create_particles(self):
        """Generate particles for the firework explosion."""
        for _ in range(random.randint(50, 100)):
            velocity = (
                random.uniform(-3, 3),  # Horizontal velocity
                random.uniform(-3, 3),  # Vertical velocity
            )
            life = random.randint(40, 100)  # Particle lifespan
            particle = FireworkParticle(self.x, self.y, self.color, life, velocity)
            self.particles.append(particle)

    def update(self):
        """Update all particles in the firework."""
        for particle in self.particles:
            particle.update()

    def draw(self, surface):
        """Draw all particles on the screen."""
        for particle in self.particles:
            particle.draw(surface)


# Main game loop
def main():
    fireworks = []

    try:
        while True:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Create new fireworks on mouse click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    color = random.choice(COLOR_PALETTE)
                    fireworks.append(Firework(x, y, color))

            # Clear the screen
            screen.fill(BLACK)

            # Update and draw fireworks
            for firework in fireworks:
                firework.update()
                firework.draw(screen)

            # Remove expired fireworks
            fireworks = [fw for fw in fireworks if any(p.life > 0 for p in fw.particles)]

            # Update the display
            pygame.display.flip()

            # Control the frame rate
            clock.tick(60)
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    main()
```
