"""
Generated Code Metadata:
========================
Original URL: https://quilling.xii.jp
Prompt: Develop code using a graphics library to simulate the rolling and shaping of paper strips for quilling, incorporating adjustable parameters for width and length.
Generated: DETERMINISTIC_094d5baac6e0ccba
Batch ID: 20250612_151119
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
import math
from pygame.locals import *

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Magenta
    (0, 255, 255),  # Cyan
]

class QuillingStrip:
    def __init__(self, x, y, length=200, width=10, color=None):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.color = color if color else COLORS[0]
        self.angle = 0
        self.roll_speed = 0.05
        self.rolled_length = 0
        self.coils = []
        self.shape = "circle"  # Can be "circle", "teardrop", "marquis", etc.
        
    def update(self):
        # Simulate rolling the strip
        if self.rolled_length < self.length:
            self.angle += self.roll_speed
            self.rolled_length += self.width * self.roll_speed
            
            # Calculate the position of the new coil
            radius = self.width * (1 + self.rolled_length / self.length)
            if self.shape == "circle":
                coil_x = self.x + radius * math.cos(self.angle)
                coil_y = self.y + radius * math.sin(self.angle)
            elif self.shape == "teardrop":
                coil_x = self.x + radius * math.cos(self.angle) * 0.7
                coil_y = self.y + radius * math.sin(self.angle) * 1.3
            elif self.shape == "marquis":
                coil_x = self.x + radius * math.cos(self.angle) * 1.5
                coil_y = self.y + radius * math.sin(self.angle) * 0.7
            
            self.coils.append((coil_x, coil_y))
    
    def draw(self, surface):
        # Draw the unrolled part of the strip
        if self.rolled_length < self.length:
            end_x = self.x + (self.length - self.rolled_length) * math.cos(self.angle + math.pi)
            end_y = self.y + (self.length - self.rolled_length) * math.sin(self.angle + math.pi)
            pygame.draw.line(surface, self.color, (self.x, self.y), (end_x, end_y), self.width)
        
        # Draw the rolled part
        if len(self.coils) > 1:
            pygame.draw.lines(surface, self.color, False, self.coils, self.width)

def main():
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Quilling Simulation")
    clock = pygame.time.Clock()
    
    # Create a quilling strip
    strip = QuillingStrip(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    
    # UI elements
    font = pygame.font.SysFont('Arial', 16)
    length_label = font.render("Length: " + str(strip.length), True, BLACK)
    width_label = font.render("Width: " + str(strip.width), True, BLACK)
    shape_label = font.render("Shape: " + strip.shape, True, BLACK)
    
    running = True
    while running:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_UP:
                    strip.length += 10
                    length_label = font.render("Length: " + str(strip.length), True, BLACK)
                elif event.key == K_DOWN and strip.length > 20:
                    strip.length -= 10
                    length_label = font.render("Length: " + str(strip.length), True, BLACK)
                elif event.key == K_RIGHT and strip.width < 30:
                    strip.width += 2
                    width_label = font.render("Width: " + str(strip.width), True, BLACK)
                elif event.key == K_LEFT and strip.width > 2:
                    strip.width -= 2
                    width_label = font.render("Width: " + str(strip.width), True, BLACK)
                elif event.key == K_1:
                    strip.shape = "circle"
                    shape_label = font.render("Shape: " + strip.shape, True, BLACK)
                elif event.key == K_2:
                    strip.shape = "teardrop"
                    shape_label = font.render("Shape: " + strip.shape, True, BLACK)
                elif event.key == K_3:
                    strip.shape = "marquis"
                    shape_label = font.render("Shape: " + strip.shape, True, BLACK)
                elif event.key == K_r:
                    # Reset the strip
                    strip = QuillingStrip(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, strip.length, strip.width)
                    length_label = font.render("Length: " + str(strip.length), True, BLACK)
                    width_label = font.render("Width: " + str(strip.width), True, BLACK)
                    shape_label = font.render("Shape: " + strip.shape, True, BLACK)
                elif event.key == K_c:
                    # Change color
                    current_color_index = COLORS.index(strip.color)
                    next_color_index = (current_color_index + 1) % len(COLORS)
                    strip.color = COLORS[next_color_index]
        
        # Update and draw the strip
        strip.update()
        strip.draw(screen)
        
        # Draw UI
        screen.blit(length_label, (10, 10))
        screen.blit(width_label, (10, 30))
        screen.blit(shape_label, (10, 50))
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
```
