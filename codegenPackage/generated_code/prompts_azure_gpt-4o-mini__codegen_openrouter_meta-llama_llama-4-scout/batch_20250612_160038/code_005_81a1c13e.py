"""
Generated Code Metadata:
========================
Original URL: https://sonicgame.pages.dev
Prompt: Describe how to use Sonic's composable gaming primitives to build a sandbox environment for game development, including a code example.
Generated: DETERMINISTIC_81a1c13e276e2c55
Batch ID: 20250612_160038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pygame
import random

# Initialize Pygame
pygame.init()

# Define constants for the environment
ENVIRONMENT_WIDTH = 800
ENVIRONMENT_HEIGHT = 600
OBJECT_SIZE = 50

# Define a base class for game objects
class GameObject:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, OBJECT_SIZE, OBJECT_SIZE)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

# Define a player class that inherits from GameObject
class Player(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = 5

    def move(self, dx, dy):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

        # Boundary checking
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > ENVIRONMENT_WIDTH:
            self.rect.right = ENVIRONMENT_WIDTH

        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > ENVIRONMENT_HEIGHT:
            self.rect.bottom = ENVIRONMENT_HEIGHT

# Define an enemy class that inherits from GameObject
class Enemy(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = 2

    def move(self):
        self.rect.x += random.choice([-self.speed, self.speed])
        self.rect.y += random.choice([-self.speed, self.speed])

        # Boundary checking
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > ENVIRONMENT_WIDTH:
            self.rect.right = ENVIRONMENT_WIDTH

        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > ENVIRONMENT_HEIGHT:
            self.rect.bottom = ENVIRONMENT_HEIGHT

# Define a sandbox environment class
class SandboxEnvironment:
    def __init__(self):
        self.screen = pygame.display.set_mode((ENVIRONMENT_WIDTH, ENVIRONMENT_HEIGHT))
        self.clock = pygame.time.Clock()
        self.player = Player(ENVIRONMENT_WIDTH / 2, ENVIRONMENT_HEIGHT / 2)
        self.enemies = [Enemy(random.randint(0, ENVIRONMENT_WIDTH), random.randint(0, ENVIRONMENT_HEIGHT)) for _ in range(10)]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player.move(0, -1)
        if keys[pygame.K_s]:
            self.player.move(0, 1)
        if keys[pygame.K_a]:
            self.player.move(-1, 0)
        if keys[pygame.K_d]:
            self.player.move(1, 0)

    def update(self):
        for enemy in self.enemies:
            enemy.move()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)
        pygame.display.flip()

    def run(self):
        try:
            while True:
                self.handle_events()
                self.update()
                self.draw()
                self.clock.tick(60)
        except Exception as e:
            print(f"An error occurred: {e}")
            pygame.quit()

# Create and run the sandbox environment
if __name__ == "__main__":
    environment = SandboxEnvironment()
    environment.run()
```
