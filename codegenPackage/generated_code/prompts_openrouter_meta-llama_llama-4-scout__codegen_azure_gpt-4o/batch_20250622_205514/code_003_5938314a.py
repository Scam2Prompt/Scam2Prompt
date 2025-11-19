"""
Generated Code Metadata:
========================
Original URL: https://solitairenetwork.com
Prompt: Design a simple Mahjong game using a Python library, allowing users to match tiles to eliminate all tiles from the layout.
Generated: DETERMINISTIC_5938314aef32bd1b
Batch ID: 20250622_205514
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

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 80
GRID_ROWS = 6
GRID_COLS = 8
FPS = 60
FONT_SIZE = 24

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Tile images (replace with actual images for production)
TILE_IMAGES = ["tile1", "tile2", "tile3", "tile4", "tile5", "tile6"]

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mahjong Game")
clock = pygame.time.Clock()

# Font for messages
font = pygame.font.Font(None, FONT_SIZE)

# Helper function to load tile images
def load_tile_images():
    # Replace with actual image loading in production
    return {name: pygame.Surface((TILE_SIZE, TILE_SIZE)) for name in TILE_IMAGES}

# Tile class
class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_type):
        super().__init__()
        self.image = tile_images[tile_type]
        self.image.fill(GRAY)  # Placeholder color
        self.rect = self.image.get_rect(topleft=(x, y))
        self.tile_type = tile_type
        self.selected = False

    def toggle_selection(self):
        self.selected = not self.selected
        self.image.fill(WHITE if self.selected else GRAY)

# Game class
class MahjongGame:
    def __init__(self):
        self.tiles = pygame.sprite.Group()
        self.selected_tiles = []
        self.create_layout()

    def create_layout(self):
        # Randomly generate a grid of tiles
        tile_types = TILE_IMAGES * (GRID_ROWS * GRID_COLS // len(TILE_IMAGES))
        random.shuffle(tile_types)

        for row in range(GRID_ROWS):
            for col in range(GRID_COLS):
                x = col * TILE_SIZE
                y = row * TILE_SIZE
                tile_type = tile_types.pop()
                tile = Tile(x, y, tile_type)
                self.tiles.add(tile)

    def handle_click(self, pos):
        # Check if a tile was clicked
        for tile in self.tiles:
            if tile.rect.collidepoint(pos):
                tile.toggle_selection()
                if tile.selected:
                    self.selected_tiles.append(tile)
                else:
                    self.selected_tiles.remove(tile)

                # Check for matching tiles
                if len(self.selected_tiles) == 2:
                    self.check_match()

    def check_match(self):
        tile1, tile2 = self.selected_tiles
        if tile1.tile_type == tile2.tile_type:
            self.tiles.remove(tile1, tile2)
        else:
            tile1.toggle_selection()
            tile2.toggle_selection()
        self.selected_tiles.clear()

    def is_game_over(self):
        return len(self.tiles) == 0

    def draw(self):
        self.tiles.draw(screen)

    def update(self):
        pass  # Placeholder for future updates

# Main game loop
def main():
    global tile_images
    tile_images = load_tile_images()
    game = MahjongGame()

    while True:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game.handle_click(event.pos)

        game.update()
        game.draw()

        if game.is_game_over():
            text = font.render("You Win!", True, WHITE)
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2))
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
```
