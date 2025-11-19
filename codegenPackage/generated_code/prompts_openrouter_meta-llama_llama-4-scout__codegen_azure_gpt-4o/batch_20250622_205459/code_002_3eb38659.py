"""
Generated Code Metadata:
========================
Original URL: https://claimcompound.net
Prompt: Generate a simple Agar.io game clone using a game development API, with a focus on player cell growth and eating smaller cells.
Generated: DETERMINISTIC_3eb38659d3ed51c7
Batch ID: 20250622_205459
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

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5
PLAYER_INITIAL_RADIUS = 15
FOOD_RADIUS = 5
FOOD_COUNT = 50
GROWTH_RATE = 0.5
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Agar.io Clone")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Player class
class Player:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def move(self, keys):
        # Move player based on key inputs
        if keys[pygame.K_UP] and self.y - self.radius > 0:
            self.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN] and self.y + self.radius < SCREEN_HEIGHT:
            self.y += PLAYER_SPEED
        if keys[pygame.K_LEFT] and self.x - self.radius > 0:
            self.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and self.x + self.radius < SCREEN_WIDTH:
            self.x += PLAYER_SPEED

    def grow(self, amount):
        # Increase player radius
        self.radius += amount

    def draw(self):
        # Draw player on screen
        pygame.draw.circle(screen, GREEN, (self.x, self.y), self.radius)

# Food class
class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        # Draw food on screen
        pygame.draw.circle(screen, RED, (self.x, self.y), FOOD_RADIUS)

# Function to check collision between player and food
def check_collision(player, food):
    distance = ((player.x - food.x) ** 2 + (player.y - food.y) ** 2) ** 0.5
    return distance < player.radius + FOOD_RADIUS

# Main game loop
def main():
    # Create player
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PLAYER_INITIAL_RADIUS)

    # Generate food
    food_list = [Food(random.randint(FOOD_RADIUS, SCREEN_WIDTH - FOOD_RADIUS),
                      random.randint(FOOD_RADIUS, SCREEN_HEIGHT - FOOD_RADIUS)) for _ in range(FOOD_COUNT)]

    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get key inputs
        keys = pygame.key.get_pressed()

        # Move player
        player.move(keys)

        # Check collisions and grow player
        for food in food_list[:]:
            if check_collision(player, food):
                player.grow(GROWTH_RATE)
                food_list.remove(food)

        # Clear screen
        screen.fill(WHITE)

        # Draw player and food
        player.draw()
        for food in food_list:
            food.draw()

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    # Quit Pygame
    pygame.quit()

# Run the game
if __name__ == "__main__":
    main()
```
