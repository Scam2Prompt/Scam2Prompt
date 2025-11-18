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
import math

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60
BACKGROUND_COLOR = (255, 255, 255)  # White background
PAPER_COLOR = (200, 0, 0)  # Red paper strip
DEFAULT_STRIP_WIDTH = 20  # Default width of paper strip in pixels
DEFAULT_STRIP_LENGTH = 400  # Default length of paper strip in pixels
ROLL_SPEED = 2  # Rolling speed of the paper strip

# Initialize the Pygame window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Quilling Simulation")
clock = pygame.time.Clock()

# Function to draw a paper strip
def draw_paper_strip(x, y, width, length, surface):
    """
    Draws a paper strip on the given surface.

    :param x: X-coordinate of the strip's starting position
    :param y: Y-coordinate of the strip's starting position
    :param width: Width of the paper strip in pixels
    :param length: Length of the paper strip in pixels
    :param surface: Pygame surface to draw on
    """
    pygame.draw.rect(surface, PAPER_COLOR, (x, y, width, length))

# Function to simulate rolling the paper strip
def roll_paper_strip(center_x, center_y, radius, angle, surface):
    """
    Simulates rolling a paper strip by drawing concentric arcs.

    :param center_x: X-coordinate of the rolling center
    :param center_y: Y-coordinate of the rolling center
    :param radius: Radius of the current roll
    :param angle: Angle of the roll in degrees
    :param surface: Pygame surface to draw on
    """
    for i in range(0, radius, 2):  # Draw arcs with step size 2 for smooth rolling effect
        pygame.draw.arc(
            surface, PAPER_COLOR,
            (center_x - i, center_y - i, i * 2, i * 2),
            math.radians(0), math.radians(angle), 2
        )

# Main function
def main():
    # Initial settings
    strip_width = DEFAULT_STRIP_WIDTH
    strip_length = DEFAULT_STRIP_LENGTH
    rolling = False
    roll_radius = 0
    roll_angle = 0

    # Start simulation loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Key controls for adjustable parameters
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:  # Increase strip width
                    strip_width += 2
                elif event.key == pygame.K_DOWN:  # Decrease strip width
                    strip_width = max(2, strip_width - 2)
                elif event.key == pygame.K_RIGHT:  # Increase strip length
                    strip_length += 10
                elif event.key == pygame.K_LEFT:  # Decrease strip length
                    strip_length = max(10, strip_length - 10)
                elif event.key == pygame.K_SPACE:  # Toggle rolling
                    rolling = not rolling

        # Clear screen
        screen.fill(BACKGROUND_COLOR)

        # Draw the paper strip
        if not rolling:
            draw_paper_strip((WINDOW_WIDTH - strip_width) // 2, (WINDOW_HEIGHT - strip_length) // 2, strip_width, strip_length, screen)
        else:
            # Simulate rolling
            roll_radius += ROLL_SPEED
            roll_angle += ROLL_SPEED
            roll_paper_strip(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, roll_radius, roll_angle, screen)

            # Reset rolling if radius exceeds a limit
            if roll_radius > min(WINDOW_WIDTH, WINDOW_HEIGHT) // 2:
                roll_radius = 0
                roll_angle = 0

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

# Entry point
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()
        sys.exit()
```
