"""
Generated Code Metadata:
========================
Original URL: https://taramediaworks.com
Prompt: Provide code examples for designing 2D animations or captivating visuals for marketing purposes, as highlighted in Tara Media Works' graphic designing services.
Generated: DETERMINISTIC_e427a933c70624a3
Batch ID: 20250612_153225
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
from pygame.locals import *

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BACKGROUND_COLOR = (5, 5, 25)
PARTICLE_COUNT = 100
LOGO_PATH = "logo.png"  # Replace with actual logo path

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tara Media Works - Marketing Visuals")
clock = pygame.time.Clock()

# Particle class for animated background
class Particle:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.size = random.randint(1, 3)
        self.speed = random.uniform(0.5, 2)
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        self.angle = random.uniform(0, 2 * math.pi)
        
    def update(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        
        # Wrap around screen edges
        if self.x < 0: self.x = WIDTH
        if self.x > WIDTH: self.x = 0
        if self.y < 0: self.y = HEIGHT
        if self.y > HEIGHT: self.y = 0
        
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)

# Text animation class
class TextAnimation:
    def __init__(self, text, font_size, color):
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.color = color
        self.alpha = 0
        self.fade_in = True
        self.position = (WIDTH // 2, HEIGHT // 2)
        
    def update(self):
        if self.fade_in:
            self.alpha = min(255, self.alpha + 3)
            if self.alpha == 255:
                self.fade_in = False
        else:
            self.alpha = max(0, self.alpha - 3)
            if self.alpha == 0:
                self.fade_in = True
                
    def draw(self, surface):
        text_surface = self.font.render(self.text, True, self.color)
        text_surface.set_alpha(self.alpha)
        text_rect = text_surface.get_rect(center=self.position)
        surface.blit(text_surface, text_rect)

# Logo animation class
class LogoAnimation:
    def __init__(self, image_path):
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        self.scale = 0.1
        self.scale_direction = 1
        self.angle = 0
        
    def update(self):
        # Pulsing effect
        self.scale += 0.005 * self.scale_direction
        if self.scale > 1.2:
            self.scale_direction = -1
        elif self.scale < 0.8:
            self.scale_direction = 1
            
        # Rotation
        self.angle = (self.angle + 0.5) % 360
        
        # Transform the image
        scaled_width = int(self.original_image.get_width() * self.scale)
        scaled_height = int(self.original_image.get_height() * self.scale)
        scaled_image = pygame.transform.scale(self.original_image, (scaled_width, scaled_height))
        self.image = pygame.transform.rotate(scaled_image, self.angle)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Main function
def main():
    # Create particles
    particles = [Particle() for _ in range(PARTICLE_COUNT)]
    
    # Create text animation
    text_anim = TextAnimation("Tara Media Works - Creative Marketing Solutions", 36, (255, 255, 255))
    
    # Create logo animation
    try:
        logo_anim = LogoAnimation(LOGO_PATH)
    except pygame.error:
        print(f"Error: Could not load logo image from {LOGO_PATH}")
        return
    
    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        # Update animations
        for particle in particles:
            particle.update()
        text_anim.update()
        logo_anim.update()
        
        # Draw everything
        screen.fill(BACKGROUND_COLOR)
        
        for particle in particles:
            particle.draw(screen)
            
        logo_anim.draw(screen)
        text_anim.draw(screen)
        
        # Display FPS (for debugging)
        fps_text = pygame.font.Font(None, 24).render(f"FPS: {int(clock.get_fps())}", True, (255, 255, 255))
        screen.blit(fps_text, (10, 10))
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
```
