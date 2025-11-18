"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taramediaworks.com
Prompt: Provide code examples for designing 2D animations or captivating visuals for marketing purposes, as highlighted in Tara Media Works' graphic designing services.
Generated: DETERMINISTIC_e427a933c70624a3
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python script using the `pygame` library to create a simple, captivating 2D animation suitable for marketing purposes.

```python
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tara Media Works Animation")

# Colors (RGB tuples)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
COLORS = [RED, BLUE, YELLOW]

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Circle properties
circle_radius = 50
circle_position = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
circle_velocity = [4, 4]
circle_color = random.choice(COLORS)

# Function to create animated text
def render_animated_text(screen, text, font, position, color, scale_factor):
    """
    Renders animated text with scaling effect.

    :param screen: Pygame surface to draw on
    :param text: Text to display
    :param font: Pygame font object
    :param position: Position tuple (x, y)
    :param color: Color tuple (R, G, B)
    :param scale_factor: Scaling factor for animation
    """
    scaled_font = pygame.font.Font(font, int(scale_factor))
    text_surface = scaled_font.render(text, True, color)
    text_rect = text_surface.get_rect(center=position)
    screen.blit(text_surface, text_rect)

# Main loop
def main():
    font_path = pygame.font.match_font("arial")  # Use a generic font
    base_font_size = 30  # Base font size for text scaling
    text_scale_factor = base_font_size
    scaling_up = True

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear screen
        screen.fill(BLACK)

        # Bounce circle off walls
        if circle_position[0] + circle_radius >= SCREEN_WIDTH or circle_position[0] - circle_radius <= 0:
            circle_velocity[0] = -circle_velocity[0]
            circle_color = random.choice(COLORS)  # Change color on bounce
        if circle_position[1] + circle_radius >= SCREEN_HEIGHT or circle_position[1] - circle_radius <= 0:
            circle_velocity[1] = -circle_velocity[1]
            circle_color = random.choice(COLORS)  # Change color on bounce

        # Update circle position
        circle_position[0] += circle_velocity[0]
        circle_position[1] += circle_velocity[1]

        # Draw circle
        pygame.draw.circle(screen, circle_color, circle_position, circle_radius)

        # Animate text scaling
        if scaling_up:
            text_scale_factor += 1
            if text_scale_factor >= base_font_size + 10:
                scaling_up = False
        else:
            text_scale_factor -= 1
            if text_scale_factor <= base_font_size - 10:
                scaling_up = True

        # Render animated text
        render_animated_text(screen, "Tara Media Works", font_path, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), WHITE, text_scale_factor)

        # Update display
        pygame.display.flip()

        # Cap the frame rate to 60 FPS
        clock.tick(60)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()
        sys.exit()
```

**Requirements**:
- Install `pygame`: `pip install pygame`
- Run the script in a Python environment that supports `pygame`.

This code produces a bouncing circle with color changes and a scaling animated text at the center of the screen. Custom animations and visuals can be added upon request.
