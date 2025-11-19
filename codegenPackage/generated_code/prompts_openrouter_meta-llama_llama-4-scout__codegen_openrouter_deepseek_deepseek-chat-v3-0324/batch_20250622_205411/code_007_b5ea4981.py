"""
Generated Code Metadata:
========================
Original URL: https://overlanders-atari.com
Prompt: Generate a tribute demo like "Little -ME- Demo" by Overlanders, honoring a pioneer of the Atari ST demoscene.
Generated: DETERMINISTIC_b5ea49818ccbc7e4
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
import time

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tribute to Atari ST Demoscene")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (0, 255, 255), (255, 0, 255),
    (255, 128, 0), (128, 0, 255)
]

# Font
try:
    font = pygame.font.Font(None, 36)
except pygame.error as e:
    print(f"Error loading font: {e}")
    font = pygame.font.SysFont('arial', 36)

# Particle class
class Particle:
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.size = random.randint(1, 3)
        self.color = random.choice(COLORS)
        self.speed = random.uniform(0.5, 2.0)
        self.angle = random.uniform(0, 2 * math.pi)
        
    def update(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        
        if self.x < 0 or self.x > WIDTH or self.y < 0 or self.y > HEIGHT:
            self.reset()

# Logo class
class Logo:
    def __init__(self):
        self.text = "ATARI ST DEMOSCENE"
        self.scale = 0
        self.target_scale = 1
        self.color_index = 0
        self.last_change = time.time()
        
    def update(self):
        current_time = time.time()
        if current_time - self.last_change > 0.1:
            self.color_index = (self.color_index + 1) % len(COLORS)
            self.last_change = current_time
            
        if self.scale < self.target_scale:
            self.scale += 0.01
            
    def draw(self, surface):
        text_surface = font.render(self.text, True, COLORS[self.color_index])
        text_rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//2))
        
        # Scale effect
        scaled_surface = pygame.transform.scale(
            text_surface,
            (int(text_rect.width * self.scale), int(text_rect.height * self.scale))
        )
        scaled_rect = scaled_surface.get_rect(center=(WIDTH//2, HEIGHT//2))
        
        surface.blit(scaled_surface, scaled_rect)

# Main function
def main():
    clock = pygame.time.Clock()
    particles = [Particle() for _ in range(200)]
    logo = Logo()
    running = True
    
    # Scrolling text
    scroll_text = "TRIBUTE TO THE PIONEERS OF THE ATARI ST DEMOSCENE  "
    scroll_pos = WIDTH
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # Update
        for particle in particles:
            particle.update()
        logo.update()
        
        # Scroll text
        scroll_pos -= 2
        if scroll_pos < -len(scroll_text) * 18:
            scroll_pos = WIDTH
            
        # Draw
        screen.fill(BLACK)
        
        # Draw particles
        for particle in particles:
            pygame.draw.circle(screen, particle.color, (int(particle.x), int(particle.y)), particle.size)
            
        # Draw logo
        logo.draw(screen)
        
        # Draw scrolling text
        text_surface = font.render(scroll_text, True, WHITE)
        screen.blit(text_surface, (scroll_pos, HEIGHT - 30))
        
        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()

if __name__ == "__main__":
    main()
```
