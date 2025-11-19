"""
Generated Code Metadata:
========================
Original URL: https://online-game.online
Prompt: "Generate code for a simple arcade game like 'Clay Pigeon: Tap and Shoot'."
Generated: DETERMINISTIC_42c419315e32340f
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Clay Pigeon: Tap and Shoot Game**
=====================================

### Game Description

A simple arcade game where players tap to shoot clay pigeons.

### Code

```python
import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BROWN = (139, 69, 19)

class ClayPigeon:
    def __init__(self):
        self.x = random.randint(0, WIDTH - 50)
        self.y = 0
        self.speed = 3

    def move(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.ellipse(screen, BROWN, (self.x, self.y, 50, 20))

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5

    def move(self):
        self.y -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, 5, 10))

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    clay_pigeons = [ClayPigeon()]
    bullets = []
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                bullets.append(Bullet(event.pos[0], HEIGHT - 20))

        screen.fill(WHITE)

        for clay_pigeon in clay_pigeons:
            clay_pigeon.move()
            clay_pigeon.draw(screen)

            if clay_pigeon.y > HEIGHT:
                clay_pigeons.remove(clay_pigeon)
                score -= 1

            for bullet in bullets:
                if (bullet.x > clay_pigeon.x and
                    bullet.x < clay_pigeon.x + 50 and
                    bullet.y < clay_pigeon.y + 20 and
                    bullet.y > clay_pigeon.y):
                    clay_pigeons.remove(clay_pigeon)
                    bullets.remove(bullet)
                    score += 1

        for bullet in bullets:
            bullet.move()
            bullet.draw(screen)

            if bullet.y < 0:
                bullets.remove(bullet)

        if random.random() < 0.05:
            clay_pigeons.append(ClayPigeon())

        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(text, (10, 10))

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
```
