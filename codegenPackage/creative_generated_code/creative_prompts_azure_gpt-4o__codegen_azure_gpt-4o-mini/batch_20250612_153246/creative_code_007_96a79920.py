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

```python
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Frame rate
FPS = 60

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rankraze Animation")

# Load assets
try:
    # Assuming 'logo.png' is a logo for Rankraze
    logo = pygame.image.load('logo.png').convert_alpha()
    logo_rect = logo.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
except pygame.error as e:
    print("Error loading image: ", e)
    pygame.quit()
    sys.exit()

# Animation variables
animation_speed = 5  # Speed of logo movement
direction = 1  # 1 for right, -1 for left

# Main loop
def main():
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            # Handle quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)

        # Update the logo position
        logo_rect.x += animation_speed * direction
        
        # Bounce the logo off the screen edges
        if logo_rect.left < 0 or logo_rect.right > SCREEN_WIDTH:
            direction *= -1  # Reverse direction

        # Draw the logo onto the screen
        screen.blit(logo, logo_rect)

        # Update the display
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick(FPS)

# Run the animation
if __name__ == '__main__':
    main()
```
