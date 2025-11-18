"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quilling.xii.jp
Prompt: Develop code using a graphics library to simulate the rolling and shaping of paper strips for quilling, incorporating adjustable parameters for width and length.
Generated: DETERMINISTIC_094d5baac6e0ccba
Batch ID: 20250612_151119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for the display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (255, 255, 255)

# Strip properties
strip_length = 200  # Length of the strip in pixels
strip_width = 20    # Width of the strip in pixels
strip_color = (255, 0, 0)  # Color of the strip (Red)

def draw_strip(surface, start_pos, length, width, color):
    """
    Draw a rectangular strip (quilling strip) on the given surface.
    
    :param surface: The Pygame surface to draw on.
    :param start_pos: A tuple (x, y) representing the starting position.
    :param length: The length of the strip.
    :param width: The width of the strip.
    :param color: The color of the strip.
    """
    # Draw the strip as a rectangle
    pygame.draw.rect(surface, color, (start_pos[0], start_pos[1], length, width))

def main():
    """
    Main function to run the Pygame window and simulate the quilling strips.
    """
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Quilling Strip Simulator")
    
    # Clock to control the frame rate
    clock = pygame.time.Clock()
    
    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Fill the background
        screen.fill(BACKGROUND_COLOR)
        
        # Draw quilling strips
        draw_strip(screen, (100, 200), strip_length, strip_width, strip_color)
        
        # Update the display
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick(60)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        pygame.quit()
        sys.exit()
```
