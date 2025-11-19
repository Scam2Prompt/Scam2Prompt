"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.virtualmediaevents.com
Prompt: How can I create a fully customizable virtual convention center using VME's 3D and 2D design options?
Generated: DETERMINISTIC_cae1fe217b0a313b
Batch ID: 20250612_162051
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

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Virtual Convention Center")

# Function to draw the convention center
def draw_convention_center():
    # Draw background
    screen.fill(WHITE)

    # Draw 2D elements (e.g., booths)
    for i in range(5):
        booth_rect = pygame.Rect(50 + i * 130, 100, 120, 80)
        pygame.draw.rect(screen, GRAY, booth_rect)
        pygame.draw.rect(screen, BLACK, booth_rect, 2)  # Booth border
        # Add booth label
        font = pygame.font.Font(None, 30)
        label = font.render(f'Booth {i + 1}', True, BLACK)
        screen.blit(label, (booth_rect.x + 10, booth_rect.y + 30))

    # Drawing a 3D-like effect (simple representation)
    for i in range(3):
        pygame.draw.polygon(screen, GRAY, [(400 + i * 100, 200), (450 + i * 100, 150), (500 + i * 100, 200), (450 + i * 100, 250)])

# Main loop
def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Draw convention center
        draw_convention_center()

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    # Clean up
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()
        sys.exit()
```
