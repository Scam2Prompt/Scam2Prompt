"""
Generated Code Metadata:
========================
Original URL: https://taramediaworks.com
Prompt: Provide code examples for designing 2D animations or captivating visuals for marketing purposes, as highlighted in Tara Media Works' graphic designing services.
Generated: DETERMINISTIC_e427a933c70624a3
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Animation Example")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Class to represent a moving object
class MovingObject:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.speed = 5

    def move(self):
        # Move the object horizontally
        self.rect.x += self.speed
        # Reverse direction if it hits the screen edges
        if self.rect.x > SCREEN_WIDTH or self.rect.x < 0:
            self.speed = -self.speed

    def draw(self, surface):
        # Draw the object on the given surface
        pygame.draw.rect(surface, self.color, self.rect)

# Main function to run the animation
def main():
    # Create a moving object
    moving_object = MovingObject(100, 250, 50, 50, BLUE)

    # Main loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update the moving object
        moving_object.move()

        # Fill the screen with white
        screen.fill(WHITE)

        # Draw the moving object
        moving_object.draw(screen)

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
