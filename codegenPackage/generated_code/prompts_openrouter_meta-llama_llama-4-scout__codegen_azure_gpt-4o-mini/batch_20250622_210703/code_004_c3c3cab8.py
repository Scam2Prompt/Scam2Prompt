"""
Generated Code Metadata:
========================
Original URL: https://blogdotrabalhadordigital.com
Prompt: Develop a simple game using Python and a library like Pygame that demonstrates a basic implementation of a game with winning conditions and bonuses, similar to those found on Pelangi189.
Generated: DETERMINISTIC_c3c3cab85638d144
Batch ID: 20250622_210703
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
PLAYER_SIZE = 50
BONUS_SIZE = 30
BONUS_SCORE = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Game settings
score = 0
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
bonus_pos = [random.randint(0, SCREEN_WIDTH - BONUS_SIZE), random.randint(0, SCREEN_HEIGHT - BONUS_SIZE)]

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Game")

# Clock to control the frame rate
clock = pygame.time.Clock()

def draw_player(position):
    """Draw the player on the screen."""
    pygame.draw.rect(screen, GREEN, (position[0], position[1], PLAYER_SIZE, PLAYER_SIZE))

def draw_bonus(position):
    """Draw the bonus item on the screen."""
    pygame.draw.rect(screen, RED, (position[0], position[1], BONUS_SIZE, BONUS_SIZE))

def check_collision(player_pos, bonus_pos):
    """Check for collision between player and bonus."""
    return (player_pos[0] < bonus_pos[0] + BONUS_SIZE and
            player_pos[0] + PLAYER_SIZE > bonus_pos[0] and
            player_pos[1] < bonus_pos[1] + BONUS_SIZE and
            player_pos[1] + PLAYER_SIZE > bonus_pos[1])

def display_score(score):
    """Display the current score on the screen."""
    font = pygame.font.Font(None, 36)
    text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(text, (10, 10))

def main():
    global score, bonus_pos

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Get the keys pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            player_pos[0] -= 5
        if keys[pygame.K_RIGHT] and player_pos[0] < SCREEN_WIDTH - PLAYER_SIZE:
            player_pos[0] += 5
        if keys[pygame.K_UP] and player_pos[1] > 0:
            player_pos[1] -= 5
        if keys[pygame.K_DOWN] and player_pos[1] < SCREEN_HEIGHT - PLAYER_SIZE:
            player_pos[1] += 5

        # Check for collision with bonus
        if check_collision(player_pos, bonus_pos):
            score += BONUS_SCORE
            bonus_pos = [random.randint(0, SCREEN_WIDTH - BONUS_SIZE), random.randint(0, SCREEN_HEIGHT - BONUS_SIZE)]

        # Fill the screen with white
        screen.fill(WHITE)

        # Draw player and bonus
        draw_player(player_pos)
        draw_bonus(bonus_pos)

        # Display the score
        display_score(score)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

if __name__ == "__main__":
    main()
```
