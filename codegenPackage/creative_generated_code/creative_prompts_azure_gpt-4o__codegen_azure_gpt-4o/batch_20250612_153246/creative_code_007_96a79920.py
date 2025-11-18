"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.rankraze.fr
Prompt: Develop a 2D animation for a digital marketing campaign, incorporating Rankraze's expertise in video production services.
Generated: DETERMINISTIC_96a79920ab6fae6c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

To create a 2D animation for a digital marketing campaign incorporating Rankraze's expertise, we typically use animation libraries or frameworks tailored for such tasks. Below is an example using Python with the `pygame` library to create a simple animation:

```python
import pygame
import sys

# Initialize pygame
pygame.init()

# Constants for screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors (RGB format)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 102, 204)

# FPS (Frames Per Second)
FPS = 60

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rankraze 2D Animation")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Load assets
try:
    logo = pygame.image.load("rankraze_logo.png")  # Placeholder for Rankraze logo
except pygame.error as e:
    print(f"Error loading image: {e}")
    pygame.quit()
    sys.exit()

# Resize the logo for animation
logo = pygame.transform.scale(logo, (150, 150))

# Animation variables
logo_x = SCREEN_WIDTH // 2 - 75  # Center position horizontally
logo_y = SCREEN_HEIGHT - 150     # Start position vertically
logo_speed = -3                  # Speed of movement (negative for upward motion)
text_font = pygame.font.Font(None, 48)

# Text for animation
marketing_text = "Rankraze - Your Video Production Experts"

def draw_text(screen, text, font, color, x, y):
    """Utility function to draw text on the screen."""
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Main game loop
def main():
    global logo_y

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear screen
        screen.fill(WHITE)

        # Animate the logo's vertical movement
        logo_y += logo_speed
        if logo_y <= 50:  # Bounce back when logo reaches the top
            logo_speed *= -1
        elif logo_y >= SCREEN_HEIGHT - 150:  # Bounce back when logo reaches the bottom
            logo_speed *= -1

        # Draw the logo
        screen.blit(logo, (logo_x, logo_y))

        # Draw marketing text
        draw_text(screen, marketing_text, text_font, BLUE, SCREEN_WIDTH // 2 - 250, 50)

        # Update the screen
        pygame.display.flip()

        # Maintain frame rate
        clock.tick(FPS)

# Run the program
if __name__ == "__main__":
    main()
```

### Notes:
1. Ensure that you have the file `rankraze_logo.png` in the same directory as the script or provide the correct path.
2. Install `pygame` before running the code: `pip install pygame`.
3. Enhance visuals and interactions based on specific campaign needs. The code above serves as a starting point for more complex animations.
