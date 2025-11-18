"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swap.depillama.com
Prompt: Create a visualization of a cosmic battle scene using Python and libraries like Matplotlib or Pygame, inspired by Captain J. Visser's leadership in "War in the Space Odyssey."
Generated: DETERMINISTIC_9da635cbbaff452e
Batch ID: 20250612_154115
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

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cosmic Battle Scene")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Load spaceship images
try:
    player_ship = pygame.image.load("player_ship.png")
    enemy_ship = pygame.image.load("enemy_ship.png")
except pygame.error as e:
    print(f"Error loading images: {e}")
    pygame.quit()
    sys.exit()

# Scale images
player_ship = pygame.transform.scale(player_ship, (50, 50))
enemy_ship = pygame.transform.scale(enemy_ship, (50, 50))

# Define classes for Spaceship and Bullet
class Spaceship(pygame.sprite.Sprite):
    """Class representing a spaceship."""
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=position)

    def update(self):
        """Update spaceship position - can be implemented for movement."""
        pass

class Bullet(pygame.sprite.Sprite):
    """Class representing a bullet."""
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=position)

    def update(self):
        """Move the bullet upwards."""
        self.rect.y -= 10
        if self.rect.bottom < 0:
            self.kill()

# Create sprite groups
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Create player spaceship
player = Spaceship(player_ship, (WIDTH // 2, HEIGHT - 50))
all_sprites.add(player)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Fire a bullet
                bullet = Bullet(player.rect.center)
                all_sprites.add(bullet)
                bullets.add(bullet)

    # Update all sprites
    all_sprites.update()

    # Draw everything
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Display the current frame
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Clean up
pygame.quit()
``` 

**Note**: Ensure you have `player_ship.png` and `enemy_ship.png` in the same directory as the script for it to run successfully.
