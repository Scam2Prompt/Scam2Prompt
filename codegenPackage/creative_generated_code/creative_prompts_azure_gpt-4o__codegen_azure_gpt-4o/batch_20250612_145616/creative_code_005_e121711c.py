"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://misterymigration.pages.dev
Prompt: Create a game feature in Python that mimics the old-school Mario-style gameplay described in the "Mistery Journey Chapter I" game, incorporating $MERY-themed storytelling.
Generated: DETERMINISTIC_e121711c93ec2f44
Batch ID: 20250612_145616
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
import random

# Initialize the pygame library
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Frames per second
FPS = 60

# Font for storytelling
pygame.font.init()
font = pygame.font.SysFont("Arial", 24)

# Game window setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mystery Journey Chapter I - MERY's Adventure")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Global game variables
gravity = 0.5
jump_strength = -10
ground_level = SCREEN_HEIGHT - 100

# Storytelling text
STORY_TEXT = [
    "Welcome to Mystery Journey Chapter I!",
    "MERY is on a quest to recover the lost artifacts of her world.",
    "Beware of enemies and obstacles along the way.",
    "Collect coins to unlock the secrets of MERY's journey.",
    "Let's begin!"
]

# Classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = ground_level - self.rect.height
        self.velocity_y = 0
        self.is_jumping = False

    def update(self):
        # Apply gravity
        self.velocity_y += gravity
        self.rect.y += self.velocity_y

        # Prevent falling through the ground
        if self.rect.y >= ground_level - self.rect.height:
            self.rect.y = ground_level - self.rect.height
            self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.velocity_y = jump_strength
            self.is_jumping = True


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # Move obstacle to the left
        self.rect.x -= 5
        # Respawn off-screen once it goes out of view
        if self.rect.right < 0:
            self.rect.x = SCREEN_WIDTH
            self.rect.y = ground_level - self.rect.height


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Game setup
player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

obstacles = pygame.sprite.Group()
for i in range(3):
    obstacle = Obstacle(SCREEN_WIDTH + i * 300, ground_level - 50)
    obstacles.add(obstacle)

coins = pygame.sprite.Group()
for i in range(5):
    coin = Coin(random.randint(600, 1200), ground_level - random.randint(150, 200))
    coins.add(coin)

# Gameplay variables
score = 0
game_over = False
story_index = 0

# Main game loop
def main():
    global score, game_over, story_index
    running = True
    display_story = True

    while running:
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if display_story:
                        # Advance story if still displaying
                        story_index += 1
                        if story_index >= len(STORY_TEXT):
                            display_story = False
                    else:
                        # Allow the player to jump if the game has started
                        player.jump()

        # Game logic
        if not display_story and not game_over:
            player_group.update()
            obstacles.update()
            coins.update()

            # Check for collisions with obstacles
            if pygame.sprite.spritecollide(player, obstacles, False):
                game_over = True

            # Check for collisions with coins
            collected_coins = pygame.sprite.spritecollide(player, coins, True)
            score += len(collected_coins)

        # Drawing
        if display_story:
            # Display story text
            story_surface = font.render(STORY_TEXT[story_index], True, BLACK)
            screen.blit(story_surface, (50, SCREEN_HEIGHT // 2 - 50))
        elif game_over:
            # Display game over screen
            game_over_surface = font.render("Game Over! Press ESC to quit.", True, RED)
            score_surface = font.render(f"Final Score: {score}", True, BLACK)
            screen.blit(game_over_surface, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50))
            screen.blit(score_surface, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
        else:
            # Normal gameplay
            player_group.draw(screen)
            obstacles.draw(screen)
            coins.draw(screen)

            # Display score
            score_surface = font.render(f"Score: {score}", True, BLACK)
            screen.blit(score_surface, (10, 10))

        # Update screen
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

# Run the game
if __name__ == "__main__":
    main()
```
