"""
Generated Code Metadata:
========================
Original URL: https://simonscat.pages.dev
Prompt: Design a mobile game inspired by Simon's Cat, with gameplay mechanics and level design.
Generated: DETERMINISTIC_bcfc41c4affd0829
Batch ID: 20250622_204621
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Simon's Cat Mobile Game**
==========================

### Game Description

A mobile game inspired by Simon's Cat, where the player must tap on falling cat toys in the correct sequence to progress through levels.

### Code

```python
import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
CAT_TOYS = ['ball', 'mouse', 'laser']
LEVELS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class CatToy:
    def __init__(self, x, y, toy_type):
        self.x = x
        self.y = y
        self.toy_type = toy_type
        self.width = 50
        self.height = 50

    def draw(self, screen):
        if self.toy_type == 'ball':
            pygame.draw.circle(screen, WHITE, (self.x, self.y), self.width // 2)
        elif self.toy_type == 'mouse':
            pygame.draw.rect(screen, WHITE, (self.x - self.width // 2, self.y - self.height // 2, self.width, self.height))
            pygame.draw.circle(screen, WHITE, (self.x - self.width // 4, self.y), self.width // 4)
        elif self.toy_type == 'laser':
            pygame.draw.line(screen, WHITE, (self.x - self.width // 2, self.y), (self.x + self.width // 2, self.y), 5)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = 1
        self.sequence = []
        self.player_sequence = []
        self.cat_toys = []

    def generate_sequence(self):
        self.sequence.append(random.choice(CAT_TOYS))

    def generate_cat_toys(self):
        self.cat_toys = []
        for toy_type in self.sequence:
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(-100, 0)
            self.cat_toys.append(CatToy(x, y, toy_type))

    def draw_cat_toys(self):
        for toy in self.cat_toys:
            toy.draw(self.screen)

    def update_cat_toys(self):
        for toy in self.cat_toys:
            toy.y += 5
            if toy.y > SCREEN_HEIGHT:
                self.cat_toys.remove(toy)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for toy in self.cat_toys:
                    if toy.x - toy.width // 2 < event.pos[0] < toy.x + toy.width // 2 and toy.y - toy.height // 2 < event.pos[1] < toy.y + toy.height // 2:
                        self.player_sequence.append(toy.toy_type)
                        self.cat_toys.remove(toy)

    def check_sequence(self):
        if self.player_sequence != self.sequence[:len(self.player_sequence)]:
            return False
        if len(self.player_sequence) == len(self.sequence):
            self.player_sequence = []
            self.level += 1
            self.generate_sequence()
            self.generate_cat_toys()
            return True
        return None

    def run(self):
        self.generate_sequence()
        self.generate_cat_toys()
        running = True
        while running:
            self.clock.tick(60)
            self.screen.fill(BLACK)
            self.handle_events()
            self.update_cat_toys()
            self.draw_cat_toys()
            if not self.cat_toys:
                self.generate_cat_toys()
            result = self.check_sequence()
            if result is False:
                print("Game Over")
                running = False
            elif result is True:
                print(f"Level {self.level}")
            pygame.display.flip()
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
```

### Requirements

* Python 3.x
* Pygame 2.x

### Installation

```bash
pip install pygame
```

### Running the Game

```bash
python game.py
```
