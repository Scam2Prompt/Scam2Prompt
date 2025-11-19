"""
Generated Code Metadata:
========================
Original URL: https://wolfgames.pages.dev
Prompt: "List the key features and provide a code overview for implementing a game like Wolf Game's Cave Game Blast."
Generated: DETERMINISTIC_39dad46d7fa228ea
Batch ID: 20250622_205836
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
from enum import Enum

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
TILE_SIZE = 50
PLAYER_SPEED = 5
BLAST_RADIUS = 3
BLAST_DURATION = 30
GAME_DURATION = 180  # seconds

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (100, 100, 100)

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)

    def update_rect(self):
        self.rect.x = self.x * TILE_SIZE
        self.rect.y = self.y * TILE_SIZE

class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = BLUE
        self.blasts = []
        self.blast_cooldown = 0
        self.max_blasts = 3

    def move(self, direction, grid):
        new_x, new_y = self.x, self.y
        
        if direction == Direction.UP:
            new_y -= 1
        elif direction == Direction.DOWN:
            new_y += 1
        elif direction == Direction.LEFT:
            new_x -= 1
        elif direction == Direction.RIGHT:
            new_x += 1

        if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
            if grid[new_y][new_x] == 0:  # 0 represents walkable path
                self.x, self.y = new_x, new_y
                self.update_rect()

    def place_blast(self, grid):
        if self.blast_cooldown <= 0 and len(self.blasts) < self.max_blasts:
            self.blasts.append(Blast(self.x, self.y))
            self.blast_cooldown = 30
            return True
        return False

class Blast(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = RED
        self.timer = BLAST_DURATION
        self.exploded = False

    def update(self):
        self.timer -= 1
        if self.timer <= 0 and not self.exploded:
            self.explode()
            return True
        return False

    def explode(self):
        self.exploded = True
        self.color = WHITE

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Cave Game Blast")
        self.clock = pygame.time.Clock()
        self.running = True
        self.grid = self.generate_grid(16, 12)
        self.player = Player(1, 1)
        self.font = pygame.font.SysFont('Arial', 24)
        self.start_time = pygame.time.get_ticks()
        self.game_over = False

    def generate_grid(self, width, height):
        grid = [[1 if random.random() < 0.3 else 0 for _ in range(width)] for _ in range(height)]
        
        # Ensure player starting position is clear
        grid[1][1] = 0
        return grid

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_SPACE and not self.game_over:
                    self.player.place_blast(self.grid)

        if not self.game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.player.move(Direction.UP, self.grid)
            if keys[pygame.K_DOWN]:
                self.player.move(Direction.DOWN, self.grid)
            if keys[pygame.K_LEFT]:
                self.player.move(Direction.LEFT, self.grid)
            if keys[pygame.K_RIGHT]:
                self.player.move(Direction.RIGHT, self.grid)

    def update(self):
        if self.player.blast_cooldown > 0:
            self.player.blast_cooldown -= 1

        # Update blasts
        for blast in self.player.blasts[:]:
            if blast.update():
                self.player.blasts.remove(blast)

        # Check game time
        elapsed = (pygame.time.get_ticks() - self.start_time) / 1000
        if elapsed >= GAME_DURATION:
            self.game_over = True

    def draw(self):
        self.screen.fill(BLACK)

        # Draw grid
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                if cell == 1:  # Wall
                    pygame.draw.rect(self.screen, GRAY, rect)
                else:  # Path
                    pygame.draw.rect(self.screen, WHITE, rect, 1)

        # Draw player
        pygame.draw.rect(self.screen, self.player.color, self.player.rect)

        # Draw blasts
        for blast in self.player.blasts:
            pygame.draw.rect(self.screen, blast.color, blast.rect)
            if blast.exploded:
                # Draw explosion radius
                for dx in range(-BLAST_RADIUS, BLAST_RADIUS + 1):
                    for dy in range(-BLAST_RADIUS, BLAST_RADIUS + 1):
                        if abs(dx) + abs(dy) <= BLAST_RADIUS:
                            x, y = blast.x + dx, blast.y + dy
                            if 0 <= x < len(self.grid[0]) and 0 <= y < len(self.grid):
                                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                                pygame.draw.rect(self.screen, (255, 100, 100), rect, 2)

        # Draw UI
        elapsed = (pygame.time.get_ticks() - self.start_time) / 1000
        time_text = self.font.render(f"Time: {int(GAME_DURATION - elapsed)}", True, WHITE)
        self.screen.blit(time_text, (10, 10))

        if self.game_over:
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            self.screen.blit(overlay, (0, 0))
            game_over_text = self.font.render("GAME OVER", True, WHITE)
            self.screen.blit(game_over_text, (SCREEN_WIDTH//2 - game_over_text.get_width()//2, 
                                             SCREEN_HEIGHT//2 - game_over_text.get_height()//2))

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
```
