"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://overlanders-atari.com
Prompt: Create an example of a 4K intro demo code that could compete in a demoscene event, taking cues from the '4K-Memory' demo by Overlanders.
Generated: DETERMINISTIC_d0e7620dff75cee5
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a simple example of a 4K intro demo written in Python using the Pygame library. Please ensure you have Pygame installed (`pip install pygame`) before running this code.

```python
import pygame
import random
import sys
import math

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("4K Intro Demo")
clock = pygame.time.Clock()

def draw_square(x, y, size, color):
    """Draw a square on the screen."""
    pygame.draw.rect(screen, color, (x, y, size, size))

def main():
    """Main function to run the demo."""
    # Set the background color
    bg_color = (0, 0, 0)

    # Main loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(bg_color)

        # Animate squares
        for i in range(100):
            # Calculate random position and size
            size = random.randint(10, 50)
            x = random.randint(0, WIDTH - size)
            y = random.randint(0, HEIGHT - size)
            # Change color over time
            color = (
                int((math.sin(pygame.time.get_ticks() * 0.001 + i) + 1) * 127),
                int((math.sin(pygame.time.get_ticks() * 0.001 + i + 2) + 1) * 127),
                int((math.sin(pygame.time.get_ticks() * 0.001 + i + 4) + 1) * 127)
            )
            draw_square(x, y, size, color)

        # Update the display
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick(FPS)

if __name__ == "__main__":
    main()
```

This code creates a simple animated square demo using Pygame. You can modify the parameters and shapes to create more complex visuals typical of the demoscene. Make sure to run this code in an environment where Pygame is supported for optimal performance.
