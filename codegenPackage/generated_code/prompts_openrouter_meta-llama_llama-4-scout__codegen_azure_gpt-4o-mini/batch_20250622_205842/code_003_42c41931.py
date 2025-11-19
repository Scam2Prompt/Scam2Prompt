"""
Generated Code Metadata:
========================
Original URL: https://online-game.online
Prompt: "Generate code for a simple arcade game like 'Clay Pigeon: Tap and Shoot'."
Generated: DETERMINISTIC_42c419315e32340f
Batch ID: 20250622_205842
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
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
CIRCLE_RADIUS = 20
CIRCLE_COLOR = (255, 0, 0)  # Red color for the clay pigeon
BACKGROUND_COLOR = (255, 255, 255)  # White background

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Clay Pigeon: Tap and Shoot")

# Game variables
score = 0
clock = pygame.time.Clock()

def draw_circle(x, y):
    """Draws a clay pigeon (circle) on the screen."""
    pygame.draw.circle(screen, CIRCLE_COLOR, (x, y), CIRCLE_RADIUS)

def main():
    global score
    # Main game loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                # Check if the click is within the circle
                if (mouse_x - circle_x) ** 2 + (mouse_y - circle_y) ** 2 <= CIRCLE_RADIUS ** 2:
                    score += 1
                    print(f"Score: {score}")
                    # Move the circle to a new random position
                    move_circle()

        # Fill the background
        screen.fill(BACKGROUND_COLOR)
        # Draw the clay pigeon
        draw_circle(circle_x, circle_y)
        # Update the display
        pygame.display.flip()
        # Cap the frame rate
        clock.tick(FPS)

def move_circle():
    """Moves the clay pigeon to a random position on the screen."""
    global circle_x, circle_y
    circle_x = random.randint(CIRCLE_RADIUS, SCREEN_WIDTH - CIRCLE_RADIUS)
    circle_y = random.randint(CIRCLE_RADIUS, SCREEN_HEIGHT - CIRCLE_RADIUS)

# Initialize the position of the clay pigeon
move_circle()

# Start the game
if __name__ == "__main__":
    main()
```
