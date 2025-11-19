"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anima.art.br
Prompt: Generate a Python script that uses digital painting techniques for beginners, inspired by the courses offered at Ânima Academia de Arte.
Generated: DETERMINISTIC_2e7cdaccc1bfbd7c
Batch ID: 20250612_164021
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

# Constants for the application
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (255, 255, 255)  # White background
BRUSH_COLOR = (0, 0, 0)  # Black brush
BRUSH_SIZE = 5  # Size of the brush

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Digital Painting for Beginners")

# Function to draw on the canvas
def draw_on_canvas(screen, position):
    pygame.draw.circle(screen, BRUSH_COLOR, position, BRUSH_SIZE)

def main():
    # Variable to track the drawing state
    drawing = False
    
    # Main event loop
    while True:
        for event in pygame.event.get():
            # Handle quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle mouse button down event
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    drawing = True
                    draw_on_canvas(screen, event.pos)

            # Handle mouse button up event
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    drawing = False

            # Handle mouse motion event
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    draw_on_canvas(screen, event.pos)

        # Update the display
        pygame.display.flip()

        # Fill the screen with the background color
        screen.fill(BACKGROUND_COLOR)

# Run the application
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()
        sys.exit()
```
