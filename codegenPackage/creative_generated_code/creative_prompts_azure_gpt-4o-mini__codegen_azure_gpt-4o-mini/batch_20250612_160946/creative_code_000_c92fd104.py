"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://online-game.online
Prompt: Generate a code snippet for a simple online game that allows users to play an arcade-style shooting game similar to "Clay Pigeon: Tap and Shoot."
Generated: DETERMINISTIC_c92fd1044ef32e71
Batch ID: 20250612_160946
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

# Initialize the pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
CIRCLE_RADIUS = 30
TARGET_COLOR = (255, 0, 0)  # Red
BACKGROUND_COLOR = (0, 0, 0)  # Black
SCORE_FONT_SIZE = 36

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Clay Pigeon: Tap and Shoot")

# Setup the clock
clock = pygame.time.Clock()

# Score variable
score = 0

# Function to generate a random target position
def get_random_target():
    x = random.randint(CIRCLE_RADIUS, SCREEN_WIDTH - CIRCLE_RADIUS)
    y = random.randint(CIRCLE_RADIUS, SCREEN_HEIGHT - CIRCLE_RADIUS)
    return x, y

# Main game loop
def main():
    global score
    target_position = get_random_target()
    
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                # Check if the target was hit
                if (mouse_x - target_position[0]) ** 2 + (mouse_y - target_position[1]) ** 2 <= CIRCLE_RADIUS ** 2:
                    score += 1
                    target_position = get_random_target()

        # Drawing
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.circle(screen, TARGET_COLOR, target_position, CIRCLE_RADIUS)
        
        # Render score
        score_font = pygame.font.Font(None, SCORE_FONT_SIZE)
        score_text = score_font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        # Update the display
        pygame.display.flip()
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
