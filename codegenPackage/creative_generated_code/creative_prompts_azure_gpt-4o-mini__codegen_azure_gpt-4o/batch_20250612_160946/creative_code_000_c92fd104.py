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

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Game settings
FPS = 60
TARGET_RADIUS = 25
TARGET_SPEED = 3
SCORE_FONT_SIZE = 30

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Clay Pigeon: Tap and Shoot")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Load assets (e.g., sounds)
try:
    shot_sound = pygame.mixer.Sound("shot.wav")
except FileNotFoundError:
    print("Sound file 'shot.wav' not found. Continuing without sound.")
    shot_sound = None

# Function to generate a random target position
def generate_target():
    x = random.randint(TARGET_RADIUS, SCREEN_WIDTH - TARGET_RADIUS)
    y = random.randint(TARGET_RADIUS, SCREEN_HEIGHT - TARGET_RADIUS)
    return x, y

# Main game function
def main():
    # Game variables
    score = 0
    target_pos = generate_target()
    game_running = True

    # Font for displaying the score
    font = pygame.font.Font(None, SCORE_FONT_SIZE)

    while game_running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the player clicked on the target
                mouse_x, mouse_y = event.pos
                distance = ((mouse_x - target_pos[0])**2 + (mouse_y - target_pos[1])**2)**0.5
                if distance <= TARGET_RADIUS:
                    score += 1
                    target_pos = generate_target()
                    # Play shot sound
                    if shot_sound:
                        shot_sound.play()

        # Move target (optional: add movement mechanics)
        target_pos = (
            target_pos[0] + random.choice([-TARGET_SPEED, TARGET_SPEED]),
            target_pos[1] + random.choice([-TARGET_SPEED, TARGET_SPEED]),
        )
        # Ensure target stays within screen bounds
        target_pos = (
            max(TARGET_RADIUS, min(SCREEN_WIDTH - TARGET_RADIUS, target_pos[0])),
            max(TARGET_RADIUS, min(SCREEN_HEIGHT - TARGET_RADIUS, target_pos[1])),
        )

        # Clear the screen
        screen.fill(WHITE)

        # Draw the target
        pygame.draw.circle(screen, RED, target_pos, TARGET_RADIUS)

        # Draw the score
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        # Update the screen
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    # Quit Pygame properly
    pygame.quit()
    sys.exit()

# Run the game
if __name__ == "__main__":
    main()
```
