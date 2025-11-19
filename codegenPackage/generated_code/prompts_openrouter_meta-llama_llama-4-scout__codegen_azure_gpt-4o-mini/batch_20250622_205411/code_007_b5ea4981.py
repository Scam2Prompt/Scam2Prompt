"""
Generated Code Metadata:
========================
Original URL: https://overlanders-atari.com
Prompt: Generate a tribute demo like "Little -ME- Demo" by Overlanders, honoring a pioneer of the Atari ST demoscene.
Generated: DETERMINISTIC_b5ea49818ccbc7e4
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
import sys

# Initialize Pygame
pygame.init()

# Constants for screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tribute Demo - Little -ME- Demo")

# Load font
try:
    font = pygame.font.Font(None, 74)
except Exception as e:
    print(f"Error loading font: {e}")
    sys.exit(1)

# Function to display text on the screen
def display_text(text, x, y):
    """Render and display text on the screen."""
    try:
        text_surface = font.render(text, True, WHITE)
        screen.blit(text_surface, (x, y))
    except Exception as e:
        print(f"Error displaying text: {e}")

# Main loop
def main():
    """Main function to run the tribute demo."""
    clock = pygame.time.Clock()
    running = True

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with black
        screen.fill(BLACK)

        # Display tribute text
        display_text("Tribute to Atari ST", 150, 100)
        display_text("Pioneer of the Demoscene", 150, 200)
        display_text("By Overlanders", 250, 300)

        # Draw a simple animation (moving rectangle)
        pygame.draw.rect(screen, BLUE, (0, 400, 800, 50))
        
        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    # Clean up and exit
    pygame.quit()
    sys.exit(0)

if __name__ == "__main__":
    main()
```
