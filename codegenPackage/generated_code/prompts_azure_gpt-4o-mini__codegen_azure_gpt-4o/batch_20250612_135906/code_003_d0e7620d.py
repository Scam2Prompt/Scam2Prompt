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

Below is an example of a minimalistic 4K intro demo written in Python using `pygame`. While Python is not typically used for 4K demos due to its size overhead, this example demonstrates the concept of procedural graphics and effects in a compact form. For true 4K demos, languages like C or assembly are preferred.

```python
import pygame
import math
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600  # Resolution
FPS = 60  # Frames per second
COLOR_DEPTH = 255  # Maximum color value

# Create the display surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("4K Demo Scene")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Function to generate a color gradient
def color_gradient(x, y, t):
    """Generate a color based on position and time."""
    r = int((math.sin(x * 0.01 + t * 0.05) + 1) * COLOR_DEPTH / 2)
    g = int((math.sin(y * 0.01 + t * 0.05) + 1) * COLOR_DEPTH / 2)
    b = int((math.sin((x + y) * 0.01 + t * 0.05) + 1) * COLOR_DEPTH / 2)
    return r, g, b

# Main loop
def main():
    """Main loop for the demo."""
    t = 0  # Time variable
    try:
        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Clear the screen
            screen.fill((0, 0, 0))

            # Draw procedural graphics
            for x in range(0, WIDTH, 10):  # Step size for performance
                for y in range(0, HEIGHT, 10):
                    color = color_gradient(x, y, t)
                    pygame.draw.rect(screen, color, (x, y, 10, 10))

            # Update the display
            pygame.display.flip()

            # Increment time
            t += 1 / FPS

            # Cap the frame rate
            clock.tick(FPS)
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()
        sys.exit()

# Run the demo
if __name__ == "__main__":
    main()
```

This code creates a simple procedural graphics demo with a color gradient effect that evolves over time. It uses `pygame` for rendering and adheres to Python best practices, including error handling and comments for clarity.
