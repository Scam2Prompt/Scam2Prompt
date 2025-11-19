"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-93--quirky-shannon-80b532.netlify.app
Prompt: Develop a simple game using Python, incorporating insights from Aidan Kahrs, a game design and development student at FOSS@RIT.
Generated: DETERMINISTIC_f03b08c1d17150f2
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
A simple 2D platformer game inspired by insights from Aidan Kahrs, game design student at FOSS@RIT.

Features:
- Player movement (left, right, jump)
- Basic collision detection
- Simple enemy AI
- Collectible items
- Score tracking
"""

import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRAVITY = 1
JUMP_STRENGTH = 15
PLAYER_SPEED = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Platformer")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    """Player character class handling movement and collisions."""
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = SCREEN_HEIGHT - 100
        self.velocity_y = 0
        self.on_ground = False
        self.score = 0

    def update(self, platforms):
        """Update player position and handle collisions."""
        # Handle horizontal movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED

        # Apply gravity
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        # Keep player on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.on_ground = True
            self.velocity_y = 0

        # Check for platform collisions
        self.on_ground = False
        for platform in platforms:
            if (self.rect.colliderect(platform.rect) and 
                self.velocity_y > 0 and 
                self.rect.bottom < platform.rect.centery):
                self.rect.bottom = platform.rect.top
                self.on_ground = True
                self.velocity_y = 0

    def jump(self):
        """Make the player jump if on ground."""
        if self.on_ground:
            self.velocity_y = -JUMP_STRENGTH
            self.on_ground = False

class Platform(pygame.sprite.Sprite):
    """Platform class for the player to stand on."""
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Enemy(pygame.sprite.Sprite):
    """Simple enemy class with basic AI."""
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 1
        self.speed = 2

    def update(self, platforms):
        """Move enemy back and forth between platforms."""
        self.rect.x += self.speed * self.direction
        
        # Change direction if at edge of platform
        on_platform = False
        for platform in platforms:
            if (self.rect.colliderect(platform.rect) and 
                self.rect.bottom == platform.rect.top):
                on_platform = True
                if (self.rect.left <= platform.rect.left or 
                    self.rect.right >= platform.rect.right):
                    self.direction *= -1
                    break
        
        if not on_platform:
            self.direction *= -1

class Collectible(pygame.sprite.Sprite):
    """Item that player can collect for points."""
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def create_level():
    """Create platforms, enemies, and collectibles for the level."""
    platforms = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    collectibles = pygame.sprite.Group()
    
    # Ground platform
    platforms.add(Platform(0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50))
    
    # Other platforms
    platform_data = [
        (100, 400, 200, 20),
        (400, 300, 200, 20),
        (200, 200, 200, 20),
    ]
    
    for x, y, w, h in platform_data:
        platforms.add(Platform(x, y, w, h))
    
    # Enemies
    enemy_data = [
        (150, 370),
        (450, 270),
    ]
    
    for x, y in enemy_data:
        enemies.add(Enemy(x, y))
    
    # Collectibles
    for _ in range(5):
        x = random.randint(50, SCREEN_WIDTH - 50)
        y = random.randint(50, SCREEN_HEIGHT - 100)
        collectibles.add(Collectible(x, y))
    
    return platforms, enemies, collectibles

def show_score(screen, score, font):
    """Display the player's score on screen."""
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def game_over_screen(screen, score):
    """Display game over screen with final score."""
    screen.fill(BLACK)
    font = pygame.font.Font(None, 74)
    game_over_text = font.render("GAME OVER", True, WHITE)
    score_text = font.render(f"Final Score: {score}", True, WHITE)
    restart_text = font.render("Press R to restart", True, WHITE)
    
    screen.blit(game_over_text, (SCREEN_WIDTH//2 - 140, SCREEN_HEIGHT//2 - 100))
    screen.blit(score_text, (SCREEN_WIDTH//2 - 180, SCREEN_HEIGHT//2))
    screen.blit(restart_text, (SCREEN_WIDTH//2 - 180, SCREEN_HEIGHT//2 + 100))
    
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
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def main():
    """Main game loop."""
    # Create game objects
    player = Player()
    platforms, enemies, collectibles = create_level()
    all_sprites = pygame.sprite.Group()
    
    # Add objects to sprite groups
    all_sprites.add(player)
    all_sprites.add(platforms)
    all_sprites.add(enemies)
    all_sprites.add(collectibles)
    
    # Game font
    font = pygame.font.Font(None, 36)
    
    # Game state
    running = True
    game_active = True
    
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE and game_active:
                    player.jump()
                if not game_active and event.key == pygame.K_r:
                    # Reset game
                    player = Player()
                    platforms, enemies, collectibles = create_level()
                    all_sprites = pygame.sprite.Group()
                    all_sprites.add(player)
                    all_sprites.add(platforms)
                    all_sprites.add(enemies)
                    all_sprites.add(collectibles)
                    game_active = True
        
        if game_active:
            # Update
            player.update(platforms)
            enemies.update(platforms)
            
            # Check for collisions
            # Player-enemy collisions
            enemy_hits = pygame.sprite.spritecollide(player, enemies, False)
            if enemy_hits:
                game_active = False
            
            # Player-col
