"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miamigojesus.edu.pe
Prompt: Suggest tools or frameworks for designing visually appealing game graphics and a user-friendly interface, similar to SCATTER HITAM's design.
Generated: DETERMINISTIC_4dd4e86e2e0494c3
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for game development
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game Graphics and UI Example')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Function to draw a rectangle with border
def draw_button(surface, color, rect, border_color, border_thickness):
    # Draw button background
    pygame.draw.rect(surface, color, rect)
    # Draw button border
    pygame.draw.rect(surface, border_color, rect, border_thickness)

# Main function to run the game
def main():
    # Game loop flag
    running = True

    # Main game loop
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with white
        screen.fill(WHITE)

        # Draw a sample button
        button_rect = pygame.Rect(100, 100, 200, 50)
        draw_button(screen, GREEN, button_rect, BLACK, 2)

        # Update the display
        pygame.display.flip()

    # Quit Pygame properly
    pygame.quit()
    sys.exit()

# Entry point of the game
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()
        sys.exit(1)
```
