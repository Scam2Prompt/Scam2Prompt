"""
Generated Code Metadata:
========================
Original URL: https://claimcompound.net
Prompt: Generate a Python script that simulates the gameplay mechanics of Agar.io, allowing users to control a cell and eat other cells.
Generated: DETERMINISTIC_e40ea8aa14ff5a91
Batch ID: 20250612_160507
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

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SPEED = 5
PLAYER_CELL_COLOR = (0, 255, 0)
ENEMY_CELL_COLOR = (255, 0, 0)
FOOD_COLOR = (255, 255, 0)
PLAYER_START_RADIUS = 20
ENEMY_START_RADIUS = 15
FOOD_RADIUS = 5
NUM_ENEMIES = 5
NUM_FOOD = 20

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Agar.io Simulation")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Helper function to check collision between two circles
def is_collision(x1, y1, r1, x2, y2, r2):
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance < r1 + r2

# Player cell class
class PlayerCell:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def move(self, keys):
        if keys[pygame.K_UP] and self.y - self.radius > 0:
            self.y -= CELL_SPEED
        if keys[pygame.K_DOWN] and self.y + self.radius < SCREEN_HEIGHT:
            self.y += CELL_SPEED
        if keys[pygame.K_LEFT] and self.x - self.radius > 0:
            self.x -= CELL_SPEED
        if keys[pygame.K_RIGHT] and self.x + self.radius < SCREEN_WIDTH:
            self.x += CELL_SPEED

    def grow(self, amount):
        self.radius += amount

    def draw(self):
        pygame.draw.circle(screen, PLAYER_CELL_COLOR, (self.x, self.y), self.radius)

# Enemy cell class
class EnemyCell:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = random.choice([-CELL_SPEED, CELL_SPEED])
        self.speed_y = random.choice([-CELL_SPEED, CELL_SPEED])

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off walls
        if self.x - self.radius < 0 or self.x + self.radius > SCREEN_WIDTH:
            self.speed_x = -self.speed_x
        if self.y - self.radius < 0 or self.y + self.radius > SCREEN_HEIGHT:
            self.speed_y = -self.speed_y

    def draw(self):
        pygame.draw.circle(screen, ENEMY_CELL_COLOR, (self.x, self.y), self.radius)

# Food class
class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.circle(screen, FOOD_COLOR, (self.x, self.y), FOOD_RADIUS)

# Main game loop
def main():
    # Initialize player, enemies, and food
    player = PlayerCell(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PLAYER_START_RADIUS)
    enemies = [EnemyCell(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), ENEMY_START_RADIUS) for _ in range(NUM_ENEMIES)]
    food_items = [Food(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)) for _ in range(NUM_FOOD)]

    running = True
    while running:
        screen.fill((0, 0, 0))  # Clear screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Player movement
        keys = pygame.key.get_pressed()
        player.move(keys)

        # Check collisions with food
        for food in food_items[:]:
            if is_collision(player.x, player.y, player.radius, food.x, food.y, FOOD_RADIUS):
                player.grow(2)  # Grow player cell
                food_items.remove(food)  # Remove eaten food

        # Check collisions with enemies
        for enemy in enemies[:]:
            if is_collision(player.x, player.y, player.radius, enemy.x, enemy.y, enemy.radius):
                if player.radius > enemy.radius:
                    player.grow(enemy.radius // 2)  # Grow player cell
                    enemies.remove(enemy)  # Remove eaten enemy
                else:
                    running = False  # Game over

        # Move and draw enemies
        for enemy in enemies:
            enemy.move()
            enemy.draw()

        # Draw food
        for food in food_items:
            food.draw()

        # Draw player
        player.draw()

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()

# Run the game
if __name__ == "__main__":
    main()
```
