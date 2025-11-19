"""
Generated Code Metadata:
========================
Original URL: https://jellydrop.web.app
Prompt: Write code for a "Jelly Flip" game or utility, referencing the interactive tools mentioned on the JellyDrop site.
Generated: DETERMINISTIC_a77a6483a00cb879
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pygame
import sys
import random
from pygame.locals import *

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
JELLY_COLORS = [
    (255, 105, 180),  # Pink
    (255, 165, 0),    # Orange
    (138, 43, 226),   # Purple
    (0, 191, 255),    # Sky Blue
    (50, 205, 50)     # Lime Green
]

class Jelly:
    def __init__(self, x, y, size=50):
        self.x = x
        self.y = y
        self.size = size
        self.color = random.choice(JELLY_COLORS)
        self.angle = 0
        self.flipping = False
        self.flip_speed = 5
        self.target_angle = 180
    
    def update(self):
        if self.flipping:
            self.angle += self.flip_speed
            if self.angle >= self.target_angle:
                self.angle = 0
                self.flipping = False
                self.color = random.choice(JELLY_COLORS)  # Change color after flip
    
    def draw(self, surface):
        # Draw jelly as a rounded rectangle with a "flipping" effect
        jelly_rect = pygame.Rect(self.x - self.size//2, self.y - self.size//2, self.size, self.size)
        
        if self.flipping:
            # Create a surface for the jelly with per-pixel alpha
            jelly_surface = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
            
            # Draw the jelly at an angle
            pygame.draw.rect(jelly_surface, (*self.color, 200), 
                            (0, 0, self.size, self.size), 
                            border_radius=10)
            
            # Rotate the surface
            rotated_jelly = pygame.transform.rotate(jelly_surface, self.angle)
            rotated_rect = rotated_jelly.get_rect(center=jelly_rect.center)
            
            surface.blit(rotated_jelly, rotated_rect.topleft)
        else:
            pygame.draw.rect(surface, self.color, jelly_rect, border_radius=10)
    
    def flip(self):
        if not self.flipping:
            self.flipping = True

class JellyFlipGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Jelly Flip Game")
        self.clock = pygame.time.Clock()
        self.jellies = []
        self.font = pygame.font.Font(None, 36)
        self.score = 0
        self.initialize_jellies()
    
    def initialize_jellies(self):
        # Create a grid of jellies
        grid_size = 5
        spacing = 80
        start_x = (SCREEN_WIDTH - (grid_size - 1) * spacing) // 2
        start_y = (SCREEN_HEIGHT - (grid_size - 1) * spacing) // 2
        
        for i in range(grid_size):
            for j in range(grid_size):
                x = start_x + i * spacing
                y = start_y + j * spacing
                self.jellies.append(Jelly(x, y))
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    self.check_jelly_click(mouse_pos)
    
    def check_jelly_click(self, pos):
        for jelly in self.jellies:
            jelly_rect = pygame.Rect(
                jelly.x - jelly.size//2,
                jelly.y - jelly.size//2,
                jelly.size,
                jelly.size
            )
            if jelly_rect.collidepoint(pos):
                jelly.flip()
                self.score += 1
    
    def update(self):
        for jelly in self.jellies:
            jelly.update()
    
    def draw(self):
        self.screen.fill(WHITE)
        
        # Draw jellies
        for jelly in self.jellies:
            jelly.draw(self.screen)
        
        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, BLACK)
        self.screen.blit(score_text, (20, 20))
        
        pygame.display.flip()
    
    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

if __name__ == "__main__":
    try:
        game = JellyFlipGame()
        game.run()
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()
        sys.exit(1)
```
