"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shelterder.com
Prompt: Create a Python script to model water vapor fireplaces with 3D flame effects, including adjustable color and intensity settings.
Generated: DETERMINISTIC_4c97f57706bf73ac
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

# Define constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Initialize Pygame
pygame.init()

# Create the screen object
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Water Vapor Fireplace Simulation")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Flame:
    def __init__(self, x, y, color, intensity):
        """Initialize flame properties."""
        self.x = x
        self.y = y
        self.color = color
        self.intensity = intensity
        self.size = random.randint(15, 30)

    def update(self):
        """Update the flame properties to simulate flickering."""
        self.size = random.randint(15, 30) * self.intensity
        self.y -= 1 * self.intensity  # Simulate upward movement

        # Reset position and size for realism
        if self.y < 0:
            self.y = HEIGHT
            self.x = random.randint(300, 500)  # Flame should appear in fireplace area

    def draw(self, surface):
        """Draw the flame on the provided surface."""
        pygame.draw.circle(surface, self.color, (self.x, int(self.y)), self.size)

def main():
    # Set up a clock for controlling the frame rate
    clock = pygame.time.Clock()

    # Create a list of flames
    flames = [Flame(random.randint(300, 500), HEIGHT, (255, 165, 0), 1.0) for _ in range(50)]

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update flames
        for flame in flames:
            flame.update()

        # Clear the screen
        screen.fill(BLACK)

        # Draw flames
        for flame in flames:
            flame.draw(screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()
        sys.exit()
```
