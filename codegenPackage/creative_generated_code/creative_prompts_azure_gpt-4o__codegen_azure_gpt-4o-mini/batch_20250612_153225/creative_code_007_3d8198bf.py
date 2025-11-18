"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sdbondindia.com
Prompt: Write code to design a digital display for commercial signage, incorporating SD BOND India's emphasis on high-quality prints and innovative technology.
Generated: DETERMINISTIC_3d8198bf74dd00a4
Batch ID: 20250612_153225
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

# Constants for display settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)  # Black background

# Initialize the Pygame library
pygame.init()

# Create a display window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("SD BOND India Digital Signage")

# Font settings
FONT_SIZE = 48
FONT_COLOR = (255, 255, 255)  # White text
FONT_NAME = "Arial"

# Load font
try:
    font = pygame.font.Font(pygame.font.get_default_font(), FONT_SIZE)
except Exception as e:
    print(f"Error loading font: {e}")
    pygame.quit()
    sys.exit()

# Function to render text on the screen
def render_text(text, position):
    """Renders text on the display at the specified position."""
    text_surface = font.render(text, True, FONT_COLOR)
    screen.blit(text_surface, position)

# Main function to run the digital display
def run_display():
    """Main loop to run the digital signage display."""
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fill the background with color
        screen.fill(BACKGROUND_COLOR)

        # Display the signage message
        render_text("Welcome to SD BOND India", (100, 250))
        render_text("High-Quality Prints & Innovative Technology", (100, 350))

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        pygame.time.Clock().tick(60)

# Entry point of the program
if __name__ == "__main__":
    try:
        run_display()
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()
        sys.exit()
```
