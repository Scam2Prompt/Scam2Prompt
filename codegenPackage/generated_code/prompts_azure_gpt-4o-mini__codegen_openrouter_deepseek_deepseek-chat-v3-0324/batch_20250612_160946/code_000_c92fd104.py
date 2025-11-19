"""
Generated Code Metadata:
========================
Original URL: https://online-game.online
Prompt: Generate a code snippet for a simple online game that allows users to play an arcade-style shooting game similar to "Clay Pigeon: Tap and Shoot."
Generated: DETERMINISTIC_c92fd1044ef32e71
Batch ID: 20250612_160946
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
import math
from pygame.locals import *

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
TARGET_RADIUS = 30
TARGET_SPEED = 3
TARGET_SPAWN_RATE = 60  # frames
SHOT_COOLDOWN = 15  # frames
MAX_TARGETS = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BACKGROUND_COLOR = (135, 206, 235)

class Target:
    def __init__(self):
        self.radius = TARGET_RADIUS
        self.x = random.randint(self.radius, SCREEN_WIDTH - self.radius)
        self.y = SCREEN_HEIGHT + self.radius
        angle = random.uniform(math.pi/4, 3*math.pi/4)
        self.dx = math.cos(angle) * TARGET_SPEED
        self.dy = -math.sin(angle) * TARGET_SPEED
        self.active = True
    
    def update(self):
        self.x += self.dx
        self.y += self.dy
        
        # Bounce off walls
        if self.x <= self.radius or self.x >= SCREEN_WIDTH - self.radius:
            self.dx *= -1
        
        # Deactivate if off screen
        if self.y < -self.radius:
            self.active = False
    
    def draw(self, surface):
        pygame.draw.circle(surface, RED, (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), self.radius - 10)
        pygame.draw.circle(surface, RED, (int(self.x), int(self.y)), self.radius - 20)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Clay Pigeon Shooter")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 32)
        
        self.targets = []
        self.score = 0
        self.shots_fired = 0
        self.shot_cooldown = 0
        self.frame_count = 0
    
    def spawn_target(self):
        if len(self.targets) < MAX_TARGETS:
            self.targets.append(Target())
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and self.shot_cooldown <= 0:
                self.shoot(event.pos)
                self.shot_cooldown = SHOT_COOLDOWN
    
    def shoot(self, pos):
        self.shots_fired += 1
        hit = False
        
        for target in self.targets:
            if target.active:
                distance = math.sqrt((pos[0] - target.x)**2 + (pos[1] - target.y)**2)
                if distance <= target.radius:
                    target.active = False
                    self.score += 1
                    hit = True
        
        if hit:
            # Visual feedback for hit
            pygame.draw.circle(self.screen, GREEN, pos, 10)
        else:
            # Visual feedback for miss
            pygame.draw.circle(self.screen, BLUE, pos, 5)
        
        pygame.display.flip()
    
    def update(self):
        self.frame_count += 1
        if self.frame_count % TARGET_SPAWN_RATE == 0:
            self.spawn_target()
        
        if self.shot_cooldown > 0:
            self.shot_cooldown -= 1
        
        for target in self.targets[:]:
            target.update()
            if not target.active:
                self.targets.remove(target)
    
    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        
        # Draw targets
        for target in self.targets:
            target.draw(self.screen)
        
        # Draw UI
        score_text = self.font.render(f"Score: {self.score}", True, BLACK)
        accuracy = 0 if self.shots_fired == 0 else (self.score / self.shots_fired) * 100
        accuracy_text = self.font.render(f"Accuracy: {accuracy:.1f}%", True, BLACK)
        
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(accuracy_text, (10, 50))
        
        pygame.display.flip()
    
    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()
```
