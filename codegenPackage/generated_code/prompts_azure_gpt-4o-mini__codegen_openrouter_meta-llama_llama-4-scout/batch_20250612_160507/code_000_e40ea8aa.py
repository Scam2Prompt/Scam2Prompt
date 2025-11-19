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
import sys

# Window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Cell properties
CELL_COLOR = (255, 255, 255)
CELL_MIN_RADIUS = 5
CELL_MAX_RADIUS = 20

# Game properties
GAME_SPEED = 60  # FPS

class Cell:
    """Represents a cell in the game."""
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self, window):
        """Draws the cell on the window."""
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    def update(self):
        """Updates the cell's position."""
        # Randomly move the cell
        self.x += random.uniform(-1, 1)
        self.y += random.uniform(-1, 1)

        # Boundary checking
        if self.x - self.radius < 0 or self.x + self.radius > WINDOW_WIDTH:
            self.x = max(self.radius, min(self.x, WINDOW_WIDTH - self.radius))
        if self.y - self.radius < 0 or self.y + self.radius > WINDOW_HEIGHT:
            self.y = max(self.radius, min(self.y, WINDOW_HEIGHT - self.radius))

class PlayerCell(Cell):
    """Represents the player's cell."""
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, mouse_x, mouse_y):
        """Updates the player's cell position to follow the mouse."""
        dx = mouse_x - self.x
        dy = mouse_y - self.y
        dist = (dx ** 2 + dy ** 2) ** 0.5
        if dist > 0:
            self.x += dx / dist * 5
            self.y += dy / dist * 5

        # Boundary checking
        if self.x - self.radius < 0 or self.x + self.radius > WINDOW_WIDTH:
            self.x = max(self.radius, min(self.x, WINDOW_WIDTH - self.radius))
        if self.y - self.radius < 0 or self.y + self.radius > WINDOW_HEIGHT:
            self.y = max(self.radius, min(self.y, WINDOW_HEIGHT - self.radius))

def main():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    player_cell = PlayerCell(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, 10)
    cells = [Cell(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT), random.randint(CELL_MIN_RADIUS, CELL_MAX_RADIUS)) for _ in range(100)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        mouse_x, mouse_y = pygame.mouse.get_pos()
        player_cell.update(mouse_x, mouse_y)

        window.fill((0, 0, 0))

        player_cell.draw(window)

        for cell in cells:
            cell.update()
            cell.draw(window)

            # Check for collision with player cell
            dx = player_cell.x - cell.x
            dy = player_cell.y - cell.y
            dist = (dx ** 2 + dy ** 2) ** 0.5
            if dist < player_cell.radius + cell.radius:
                if player_cell.radius > cell.radius:
                    player_cell.radius += cell.radius * 0.1
                    cells.remove(cell)
                    cells.append(Cell(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT), random.randint(CELL_MIN_RADIUS, CELL_MAX_RADIUS)))

        pygame.display.flip()
        clock.tick(GAME_SPEED)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
```
