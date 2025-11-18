"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://klar-sehen.ch
Prompt: Write Python code to simulate a visual perception training exercise inspired by the holistic eye training methods described on the Klar Sehen website. Include features like dynamic visual stimuli and user interaction.
Generated: DETERMINISTIC_d2f1cad218e5c14e
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
import random
import sys

# Initialize Pygame
pygame.init()

# Constants for the screen dimensions and colors
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Visual Perception Training Exercise")

# Font for text rendering
font = pygame.font.Font(None, 36)

def draw_stimulus(shape, x, y, size):
    """Draws a random shape on the screen at the specified position."""
    if shape == 'circle':
        pygame.draw.circle(screen, TEXT_COLOR, (x, y), size)
    elif shape == 'square':
        pygame.draw.rect(screen, TEXT_COLOR, (x - size//2, y - size//2, size, size))
    elif shape == 'triangle':
        points = [(x, y - size), (x - size, y + size), (x + size, y + size)]
        pygame.draw.polygon(screen, TEXT_COLOR, points)

def display_message(message):
    """Displays a message on the screen."""
    text = font.render(message, True, TEXT_COLOR)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)

def main():
    """Main function to run the visual perception training exercise."""
    # List of shapes to be drawn
    shapes = ['circle', 'square', 'triangle']
    
    # Game loop
    run = True
    while run:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Fill the background
        screen.fill(BACKGROUND_COLOR)

        # Randomly select a shape and its position
        shape = random.choice(shapes)
        x = random.randint(100, SCREEN_WIDTH - 100)
        y = random.randint(100, SCREEN_HEIGHT - 100)
        size = random.randint(20, 50)

        # Draw the visual stimulus
        draw_stimulus(shape, x, y, size)

        # Display instructions to the user
        display_message("Press any key when you see the shape!")

        # Update the display
        pygame.display.flip()

        # Wait for a short duration before clearing the screen
        pygame.time.delay(2000)

    # Clean up and exit
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
```
