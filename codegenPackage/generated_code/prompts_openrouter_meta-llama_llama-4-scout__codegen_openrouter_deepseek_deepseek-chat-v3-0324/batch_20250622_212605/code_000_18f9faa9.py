"""
Generated Code Metadata:
========================
Original URL: https://uiriocabrabrazzz.blogspot.com
Prompt: Write a Python code snippet to create a simple window display simulation, considering factors like lighting, color palette, and product placement, as discussed in the context of vitrinismo.
Generated: DETERMINISTIC_18f9faa9c5d70cef
Batch ID: 20250622_212605
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
from typing import List, Tuple, Dict

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
BACKGROUND_COLOR = (240, 240, 240)  # Light gray background
LIGHT_COLORS = [(255, 255, 200), (200, 255, 255), (255, 200, 255)]  # Soft light colors
PRODUCT_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]  # Vibrant product colors

class Product:
    def __init__(self, x: int, y: int, width: int, height: int, color: Tuple[int, int, int]):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.original_color = color
        self.highlighted = False
    
    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, self.color, self.rect)
        # Add a border to make products stand out
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 2)
    
    def highlight(self, light_color: Tuple[int, int, int]) -> None:
        """Apply lighting effect to the product"""
        self.highlighted = True
        r = min(255, self.original_color[0] + light_color[0] // 3)
        g = min(255, self.original_color[1] + light_color[1] // 3)
        b = min(255, self.original_color[2] + light_color[2] // 3)
        self.color = (r, g, b)
    
    def reset_highlight(self) -> None:
        """Reset product to original color"""
        self.highlighted = False
        self.color = self.original_color

class Light:
    def __init__(self, x: int, y: int, radius: int, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.active = True
    
    def draw(self, surface: pygame.Surface) -> None:
        if self.active:
            # Create a surface for the light with per-pixel alpha
            light_surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
            # Draw a gradient circle
            for r in range(self.radius, 0, -1):
                alpha = int(200 * (r / self.radius))
                pygame.draw.circle(light_surface, (*self.color, alpha), (self.radius, self.radius), r)
            surface.blit(light_surface, (self.x - self.radius, self.y - self.radius))

class WindowDisplay:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Window Display Simulation")
        self.clock = pygame.time.Clock()
        self.products: List[Product] = []
        self.lights: List[Light] = []
        self.font = pygame.font.SysFont('Arial', 16)
        
        self.setup_display()
    
    def setup_display(self) -> None:
        """Initialize products and lights with a balanced arrangement"""
        # Create products with a visually pleasing arrangement
        product_width = 80
        product_height = 120
        spacing = 20
        
        # Center products horizontally
        total_width = (3 * product_width) + (2 * spacing)
        start_x = (SCREEN_WIDTH - total_width) // 2
        
        for i in range(3):
            x = start_x + i * (product_width + spacing)
            y = SCREEN_HEIGHT // 2 - product_height // 2
            color = random.choice(PRODUCT_COLORS)
            self.products.append(Product(x, y, product_width, product_height, color))
        
        # Add accent products
        self.products.append(Product(start_x - spacing - product_width, 
                                    SCREEN_HEIGHT // 2 - product_height // 4, 
                                    product_width, product_height // 2, 
                                    random.choice(PRODUCT_COLORS)))
        
        self.products.append(Product(start_x + total_width + spacing, 
                                    SCREEN_HEIGHT // 2 - product_height // 4, 
                                    product_width, product_height // 2, 
                                    random.choice(PRODUCT_COLORS)))
        
        # Add lights
        self.lights.append(Light(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4, 150, random.choice(LIGHT_COLORS)))
        self.lights.append(Light(3 * SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4, 150, random.choice(LIGHT_COLORS)))
        self.lights.append(Light(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3, 100, random.choice(LIGHT_COLORS)))
    
    def handle_events(self) -> bool:
        """Handle user input and return False if the application should quit"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_SPACE:
                    # Toggle lights
                    for light in self.lights:
                        light.active = not light.active
                elif event.key == pygame.K_r:
                    # Randomize colors
                    for product in self.products:
                        product.color = random.choice(PRODUCT_COLORS)
                        product.original_color = product.color
                    for light in self.lights:
                        light.color = random.choice(LIGHT_COLORS)
        return True
    
    def update(self) -> None:
        """Update display elements"""
        # Reset all product highlights
        for product in self.products:
            product.reset_highlight()
        
        # Apply lighting effects
        for light in self.lights:
            if light.active:
                for product in self.products:
                    # Simple distance-based highlighting
                    product_center = (product.rect.x + product.rect.width // 2, 
                                     product.rect.y + product.rect.height // 2)
                    distance = ((light.x - product_center[0]) ** 2 + 
                               (light.y - product_center[1]) ** 2) ** 0.5
                    if distance < light.radius:
                        product.highlight(light.color)
    
    def draw(self) -> None:
        """Draw all elements to the screen"""
        self.screen.fill(BACKGROUND_COLOR)
        
        # Draw products
        for product in self.products:
            product.draw(self.screen)
        
        # Draw lights
        for light in self.lights:
            light.draw(self.screen)
        
        # Draw instructions
        instructions = [
            "SPACE: Toggle lights",
            "R: Randomize colors",
            "ESC: Quit"
        ]
        for i, text in enumerate(instructions):
            text_surface = self.font.render(text, True, (0, 0, 0))
            self.screen.blit(text_surface, (10, 10 + i * 20))
        
        pygame.display.flip()
    
    def run(self) -> None:
        """Main game loop"""
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    display = WindowDisplay()
    display.run()
```
