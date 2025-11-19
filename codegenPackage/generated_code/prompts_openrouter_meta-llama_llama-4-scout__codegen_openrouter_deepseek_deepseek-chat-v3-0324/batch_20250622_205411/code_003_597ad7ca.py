"""
Generated Code Metadata:
========================
Original URL: https://overlanders-atari.com
Prompt: Create a demo scene production like "FirST Love" by Overlanders, which won the Best Midschool Production Meteoriks award.
Generated: DETERMINISTIC_597ad7ca96d2ddc4
Batch ID: 20250622_205411
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
import math
from pygame import gfxdraw

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Love Demo Scene")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 105, 180)
PURPLE = (138, 43, 226)
BLUE = (0, 191, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Particle class for effects
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = random.randint(2, 5)
        self.speed = random.uniform(1, 3)
        self.angle = random.uniform(0, math.pi * 2)
        self.life = random.randint(30, 90)
        
    def update(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        self.life -= 1
        if self.life <= 0:
            self.size = max(0, self.size - 0.1)
        
    def draw(self, surface):
        alpha = min(255, self.life * 3)
        color = (*self.color, alpha)
        gfxdraw.filled_circle(surface, int(self.x), int(self.y), max(1, int(self.size)), color)

# Scrolling text effect
class ScrollingText:
    def __init__(self, text, font_size, color):
        self.font = pygame.font.Font(None, font_size)
        self.text = text
        self.color = color
        self.text_surface = self.font.render(self.text, True, self.color)
        self.x = WIDTH
        self.y = HEIGHT // 2
        self.speed = 2
        
    def update(self):
        self.x -= self.speed
        if self.x + self.text_surface.get_width() < 0:
            self.x = WIDTH
            
    def draw(self, surface):
        surface.blit(self.text_surface, (self.x, self.y))

# Main demo scene class
class DemoScene:
    def __init__(self):
        self.particles = []
        self.scrolling_texts = [
            ScrollingText("FIRST LOVE", 72, PINK),
            ScrollingText("BY OVERLANDERS", 48, PURPLE),
            ScrollingText("METEORIKS AWARD WINNER", 36, BLUE)
        ]
        self.background = pygame.Surface((WIDTH, HEIGHT))
        self.background.fill(BLACK)
        self.time = 0
        
    def add_particles(self, x, y, color, count=20):
        for _ in range(count):
            self.particles.append(Particle(x, y, color))
            
    def update(self):
        self.time += 1
        
        # Update particles
        for particle in self.particles[:]:
            particle.update()
            if particle.size <= 0:
                self.particles.remove(particle)
                
        # Add new particles periodically
        if self.time % 10 == 0:
            self.add_particles(
                random.randint(0, WIDTH),
                random.randint(0, HEIGHT),
                random.choice([PINK, PURPLE, BLUE]),
                random.randint(5, 15)
            )
            
        # Update scrolling texts
        for text in self.scrolling_texts:
            text.update()
            
    def draw(self, surface):
        # Draw background
        surface.blit(self.background, (0, 0))
        
        # Draw particles
        for particle in self.particles:
            particle.draw(surface)
            
        # Draw scrolling texts
        for text in self.scrolling_texts:
            text.draw(surface)
            
        # Draw some additional effects
        if self.time % 60 == 0:
            pygame.draw.circle(surface, WHITE, (WIDTH//2, HEIGHT//2), 100, 1)
            
        # Draw credits at the bottom
        font = pygame.font.Font(None, 24)
        credits = font.render("DEMO SCENE INSPIRED BY 'FIRST LOVE' BY OVERLANDERS", True, WHITE)
        surface.blit(credits, (WIDTH//2 - credits.get_width()//2, HEIGHT - 30))

# Main function
def main():
    demo = DemoScene()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        demo.update()
        demo.draw(screen)
        
        pygame.display.flip()
        clock.tick(FPS)
        
    pygame.quit()

if __name__ == "__main__":
    main()
```
