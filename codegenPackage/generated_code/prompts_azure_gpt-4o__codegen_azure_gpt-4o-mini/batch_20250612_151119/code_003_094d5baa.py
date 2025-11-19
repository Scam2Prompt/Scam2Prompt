"""
Generated Code Metadata:
========================
Original URL: https://quilling.xii.jp
Prompt: Develop code using a graphics library to simulate the rolling and shaping of paper strips for quilling, incorporating adjustable parameters for width and length.
Generated: DETERMINISTIC_094d5baac6e0ccba
Batch ID: 20250612_151119
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
import random

# Initialize Pygame
pygame.init()

# Constants for the display
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
STRIP_COLOR = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quilling Paper Strips Simulation")

def draw_strip(x, y, width, length, angle):
    """
    Draws a paper strip on the screen.

    :param x: The x-coordinate of the strip's starting point.
    :param y: The y-coordinate of the strip's starting point.
    :param width: The width of the strip.
    :param length: The length of the strip.
    :param angle: The angle to rotate the strip.
    """
    # Create a surface for the strip
    strip_surface = pygame.Surface((length, width))
    strip_surface.fill(STRIP_COLOR)

    # Rotate the strip surface
    rotated_strip = pygame.transform.rotate(strip_surface, angle)

    # Get the rectangle of the rotated strip
    rect = rotated_strip.get_rect(center=(x, y))

    # Draw the rotated strip on the main screen
    screen.blit(rotated_strip, rect.topleft)

def main():
    """
    Main function to run the Pygame simulation.
    """
    # Parameters for the paper strips
    strip_width = 10
    strip_length = 200
    strip_angle = 0

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Adjust parameters with keyboard input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    strip_length += 10  # Increase length
                elif event.key == pygame.K_DOWN:
                    strip_length = max(10, strip_length - 10)  # Decrease length
                elif event.key == pygame.K_LEFT:
                    strip_width = max(1, strip_width - 1)  # Decrease width
                elif event.key == pygame.K_RIGHT:
                    strip_width += 1  # Increase width
                elif event.key == pygame.K_r:
                    strip_angle = random.randint(0, 360)  # Randomize angle

        # Fill the background
        screen.fill(BACKGROUND_COLOR)

        # Draw the paper strip
        draw_strip(WIDTH // 2, HEIGHT // 2, strip_width, strip_length, strip_angle)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main()
```
