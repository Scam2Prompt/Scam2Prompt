"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stethevent.org
Prompt: Can you provide code examples for creating perfectly looping animations in Python, as mentioned in the Stethevent projects?
Generated: DETERMINISTIC_fb2ab20f4a971e73
Batch ID: 20250612_162548
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
import math

# Constants for screen dimensions and colors
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (30, 30, 30)
CIRCLE_COLOR = (255, 100, 100)
FPS = 60

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Perfectly Looping Animation")

# Create clock to control frame rate
clock = pygame.time.Clock()

# Animation parameters
circle_radius = 50
circle_speed = 2
angle = 0  # Angle for circular motion

try:
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update the animation angle
        angle += circle_speed
        if angle >= 360:  # Reset angle after completing a full circle
            angle -= 360

        # Calculate the new position of the circle
        circle_x = SCREEN_WIDTH // 2 + math.cos(math.radians(angle)) * 200
        circle_y = SCREEN_HEIGHT // 2 + math.sin(math.radians(angle)) * 200

        # Clear the screen
        screen.fill(BACKGROUND_COLOR)

        # Draw the circle
        pygame.draw.circle(screen, CIRCLE_COLOR, (int(circle_x), int(circle_y)), circle_radius)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

except Exception as e:
    print(f"An error occurred: {e}")
    pygame.quit()
    sys.exit()
```
