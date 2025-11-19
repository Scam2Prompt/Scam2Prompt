"""
Generated Code Metadata:
========================
Original URL: https://overlanders-atari.com
Prompt: Create a demo scene production like "FirST Love" by Overlanders, which won the Best Midschool Production Meteoriks award.
Generated: DETERMINISTIC_597ad7ca96d2ddc4
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
import random
import sys

# Initialize Pygame
pygame.init()

# Constants for the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Demo Scene: FirST Love Inspired")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Class to represent a moving star
class Star:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.speed = random.uniform(1, 3)

    def move(self):
        self.y += self.speed
        if self.y > SCREEN_HEIGHT:
            self.y = 0
            self.x = random.randint(0, SCREEN_WIDTH)

    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), self.size)

# Function to create a list of stars
def create_stars(num_stars):
    return [Star(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), random.randint(2, 5)) for _ in range(num_stars)]

# Main function to run the demo scene
def main():
    stars = create_stars(100)  # Create 100 stars

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fill the background
        screen.fill(BLACK)

        # Update and draw stars
        for star in stars:
            star.move()
            star.draw(screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

# Entry point of the program
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()
        sys.exit()
```
