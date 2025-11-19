"""
Generated Code Metadata:
========================
Original URL: https://metaforce360.com
Prompt: "Design a motion graphics animation for a marketing campaign that transforms ideas into motion and makes the message impossible to ignore."
Generated: DETERMINISTIC_b5c4ce9cb69abe51
Batch ID: 20250622_210655
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
import math
from pygame import gfxdraw

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Idea Motion Graphics")

# Colors
BACKGROUND = (10, 10, 20)
WHITE = (255, 255, 255)
COLORS = [
    (255, 50, 50),
    (50, 255, 50),
    (50, 50, 255),
    (255, 255, 50),
    (255, 50, 255),
    (50, 255, 255)
]

# Font
font = pygame.font.Font(None, 60)
small_font = pygame.font.Font(None, 36)

# Particle class
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = random.randint(2, 5)
        self.speed = random.uniform(0.5, 2.0)
        self.angle = random.uniform(0, math.pi * 2)
        self.life = random.randint(50, 150)
        self.max_life = self.life
        
    def update(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        self.life -= 1
        self.size = max(0, self.size * 0.98)
        
    def draw(self, surface):
        alpha = int(255 * (self.life / self.max_life))
        color = (*self.color[:3], alpha)
        pygame.gfxdraw.filled_circle(
            surface, 
            int(self.x), 
            int(self.y), 
            int(self.size), 
            color
        )

# Idea class
class Idea:
    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y
        self.target_x = x
        self.target_y = y
        self.particles = []
        self.color = random.choice(COLORS)
        self.size = 0
        self.max_size = 100
        self.growing = True
        
    def update(self):
        # Move towards target
        self.x += (self.target_x - self.x) * 0.1
        self.y += (self.target_y - self.y) * 0.1
        
        # Handle size animation
        if self.growing:
            self.size += 2
            if self.size >= self.max_size:
                self.growing = False
        else:
            self.size -= 1
            if self.size <= 0:
                self.growing = True
        
        # Create particles
        if random.random() < 0.3:
            self.particles.append(
                Particle(self.x, self.y, self.color)
            )
        
        # Update particles
        for particle in self.particles[:]:
            particle.update()
            if particle.life <= 0:
                self.particles.remove(particle)
                
    def draw(self, surface):
        # Draw particles
        for particle in self.particles:
            particle.draw(surface)
        
        # Draw idea text
        text_surface = font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=(self.x, self.y))
        
        # Draw animated circle
        alpha = 100 if self.growing else 50
        pygame.gfxdraw.filled_circle(
            surface, 
            int(self.x), 
            int(self.y), 
            int(self.size), 
            (*self.color, alpha)
        )
        
        surface.blit(text_surface, text_rect)

# Main animation class
class MotionGraphics:
    def __init__(self):
        self.ideas = []
        self.messages = [
            "Innovate",
            "Create",
            "Inspire",
            "Transform",
            "Engage",
            "Imagine"
        ]
        self.clock = pygame.time.Clock()
        self.timer = 0
        self.current_message = 0
        self.message_surface = None
        self.message_alpha = 0
        
    def add_idea(self):
        if len(self.ideas) < 6:
            text = random.choice(self.messages)
            x = random.randint(100, WIDTH - 100)
            y = random.randint(100, HEIGHT - 100)
            self.ideas.append(Idea(text, x, y))
            
    def update_message(self):
        self.timer += 1
        if self.timer % 180 == 0:
            self.current_message = (self.current_message + 1) % len(self.messages)
            self.message_alpha = 0
            
        if self.message_alpha < 255:
            self.message_alpha = min(255, self.message_alpha + 5)
            
        self.message_surface = small_font.render(
            "Transforming ideas into motion...", 
            True, 
            (*WHITE, self.message_alpha)
        )
        
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_SPACE:
                        self.add_idea()
            
            # Update
            self.update_message()
            for idea in self.ideas:
                idea.update()
                
            # Draw
            screen.fill(BACKGROUND)
            
            for idea in self.ideas:
                idea.draw(screen)
                
            if self.message_surface:
                msg_rect = self.message_surface.get_rect(
                    center=(WIDTH // 2, HEIGHT - 50)
                )
                screen.blit(self.message_surface, msg_rect)
            
            pygame.display.flip()
            self.clock.tick(60)
            
        pygame.quit()
        sys.exit()

# Run the animation
if __name__ == "__main__":
    animation = MotionGraphics()
    animation.add_idea()  # Start with one idea
    animation.run()
```
