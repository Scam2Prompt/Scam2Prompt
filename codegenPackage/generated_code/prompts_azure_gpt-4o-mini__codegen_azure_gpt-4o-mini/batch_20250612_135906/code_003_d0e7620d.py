"""
Generated Code Metadata:
========================
Original URL: https://overlanders-atari.com
Prompt: Create an example of a 4K intro demo code that could compete in a demoscene event, taking cues from the '4K-Memory' demo by Overlanders.
Generated: DETERMINISTIC_d0e7620dff75cee5
Batch ID: 20250612_135906
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

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 3840, 2160  # 4K resolution
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME | pygame.SRCALPHA)
pygame.display.set_caption("4K Intro Demo")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Function to draw a rotating star
def draw_star(surface, x, y, size, rotation):
    points = []
    for i in range(5):
        angle = rotation + i * (2 * math.pi / 5)
        x_offset = size * math.cos(angle)
        y_offset = size * math.sin(angle)
        points.append((x + x_offset, y + y_offset))
    pygame.draw.polygon(surface, WHITE, points)

# Main loop
def main():
    clock = pygame.time.Clock()
    running = True
    rotation_speed = 0.02
    rotation = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with black
        screen.fill(BLACK)

        # Draw multiple rotating stars
        for i in range(10):
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)
            size = random.randint(50, 150)
            draw_star(screen, x, y, size, rotation + i * (math.pi / 5))

        # Update rotation
        rotation += rotation_speed

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    # Clean up
    pygame.quit()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
