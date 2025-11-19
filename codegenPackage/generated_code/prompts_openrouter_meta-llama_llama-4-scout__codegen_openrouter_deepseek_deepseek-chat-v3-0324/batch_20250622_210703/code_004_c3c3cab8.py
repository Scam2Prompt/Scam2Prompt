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

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Game settings
PLAYER_SPEED = 5
TARGET_SCORE = 100
BONUS_SCORE = 20
BONUS_SPAWN_RATE = 0.02

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Collection Game")
clock = pygame.time.Clock()

# Load fonts
font = pygame.font.SysFont('Arial', 24)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.score = 0
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += PLAYER_SPEED

class Collectible(pygame.sprite.Sprite):
    def __init__(self, is_bonus=False):
        super().__init__()
        self.is_bonus = is_bonus
        if is_bonus:
            self.image = pygame.Surface((20, 20))
            self.image.fill(YELLOW)
            self.value = BONUS_SCORE
        else:
            self.image = pygame.Surface((30, 30))
            self.image.fill(GREEN)
            self.value = 10
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)

def show_game_over(score):
    screen.fill(BLACK)
    game_over_text = font.render(f"Game Over! Final Score: {score}", True, WHITE)
    restart_text = font.render("Press R to restart or Q to quit", True, WHITE)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
    screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 10))
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False
                    return True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        clock.tick(FPS)
    return False

def main():
    running = True
    
    while running:
        # Initialize game
        player = Player()
        all_sprites = pygame.sprite.Group(player)
        collectibles = pygame.sprite.Group()
        
        # Spawn initial collectibles
        for _ in range(10):
            collectible = Collectible()
            collectibles.add(collectible)
            all_sprites.add(collectible)
        
        game_over = False
        
        # Game loop
        while not game_over:
            # Process events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # Update
            all_sprites.update()
            
            # Check for collisions
            hits = pygame.sprite.spritecollide(player, collectibles, True)
            for hit in hits:
                player.score += hit.value
                # Randomly spawn bonus collectible
                if random.random() < BONUS_SPAWN_RATE:
                    bonus = Collectible(is_bonus=True)
                    collectibles.add(bonus)
                    all_sprites.add(bonus)
                # Spawn regular collectible
                collectible = Collectible()
                collectibles.add(collectible)
                all_sprites.add(collectible)
            
            # Check win condition
            if player.score >= TARGET_SCORE:
                game_over = True
            
            # Render
            screen.fill(BLACK)
            all_sprites.draw(screen)
            
            # Display score
            score_text = font.render(f"Score: {player.score}", True, WHITE)
            screen.blit(score_text, (10, 10))
            
            pygame.display.flip()
            clock.tick(FPS)
        
        # Game over screen
        if not show_game_over(player.score):
            running = False

if __name__ == "__main__":
    main()
```
