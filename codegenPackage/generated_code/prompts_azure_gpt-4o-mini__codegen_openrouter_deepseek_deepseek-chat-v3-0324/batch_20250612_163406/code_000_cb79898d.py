"""
Generated Code Metadata:
========================
Original URL: https://www.prointegrationfuture.asia
Prompt: Generate a code snippet that simulates a live demonstration of immersive technology for the Pro Integration Future Asia event, showcasing real-world applications in AV and lighting.
Generated: DETERMINISTIC_cb79898d44aa26d3
Batch ID: 20250612_163406
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
import time
import sys
from enum import Enum

# Constants for screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Lighting states
class LightingState(Enum):
    WARM = 1
    COOL = 2
    DYNAMIC = 3
    STROBE = 4

# AV effects
class AVEffect(Enum):
    FADE = 1
    ZOOM = 2
    PAN = 3
    ROTATE = 4

class ImmersiveTechDemo:
    def __init__(self):
        """Initialize the immersive technology demo."""
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pro Integration Future Asia - Immersive Tech Demo")
        
        # Load assets
        try:
            self.background = pygame.image.load("background.jpg").convert()
            self.logo = pygame.image.load("logo.png").convert_alpha()
        except pygame.error as e:
            print(f"Error loading assets: {e}")
            sys.exit(1)
            
        self.clock = pygame.time.Clock()
        self.running = True
        self.current_lighting = LightingState.WARM
        self.current_effect = AVEffect.FADE
        self.effect_progress = 0
        self.font = pygame.font.SysFont('Arial', 24)
        
    def handle_events(self):
        """Handle user input events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.current_lighting = LightingState.WARM
                elif event.key == pygame.K_2:
                    self.current_lighting = LightingState.COOL
                elif event.key == pygame.K_3:
                    self.current_lighting = LightingState.DYNAMIC
                elif event.key == pygame.K_4:
                    self.current_lighting = LightingState.STROBE
                elif event.key == pygame.K_q:
                    self.current_effect = AVEffect.FADE
                elif event.key == pygame.K_w:
                    self.current_effect = AVEffect.ZOOM
                elif event.key == pygame.K_e:
                    self.current_effect = AVEffect.PAN
                elif event.key == pygame.K_r:
                    self.current_effect = AVEffect.ROTATE
                elif event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self):
        """Update demo state."""
        self.effect_progress = (self.effect_progress + 0.01) % 1.0
        
        # Simulate lighting changes
        if self.current_lighting == LightingState.STROBE:
            if random.random() < 0.1:
                self.screen.fill((255, 255, 255))
                
    def apply_lighting(self):
        """Apply current lighting state to the scene."""
        if self.current_lighting == LightingState.WARM:
            self.screen.fill((255, 200, 150, 50), special_flags=pygame.BLEND_MULT)
        elif self.current_lighting == LightingState.COOL:
            self.screen.fill((150, 200, 255, 50), special_flags=pygame.BLEND_MULT)
        elif self.current_lighting == LightingState.DYNAMIC:
            hue = (time.time() % 10) / 10
            r, g, b = self.hsv_to_rgb(hue, 1, 1)
            self.screen.fill((r, g, b, 30), special_flags=pygame.BLEND_MULT)
            
    def apply_av_effect(self):
        """Apply current AV effect to the logo."""
        logo_rect = self.logo.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        
        if self.current_effect == AVEffect.FADE:
            alpha = int(255 * self.effect_progress)
            self.logo.set_alpha(alpha)
            self.screen.blit(self.logo, logo_rect)
        elif self.current_effect == AVEffect.ZOOM:
            scale = 0.5 + self.effect_progress
            scaled_logo = pygame.transform.scale(self.logo, 
                (int(self.logo.get_width() * scale), 
                 int(self.logo.get_height() * scale)))
            scaled_rect = scaled_logo.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            self.screen.blit(scaled_logo, scaled_rect)
        elif self.current_effect == AVEffect.PAN:
            x_pos = int(SCREEN_WIDTH * self.effect_progress)
            self.screen.blit(self.logo, (x_pos, SCREEN_HEIGHT//2 - self.logo.get_height()//2))
        elif self.current_effect == AVEffect.ROTATE:
            angle = 360 * self.effect_progress
            rotated_logo = pygame.transform.rotate(self.logo, angle)
            rotated_rect = rotated_logo.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            self.screen.blit(rotated_logo, rotated_rect)
            
    def hsv_to_rgb(self, h, s, v):
        """Convert HSV to RGB color."""
        if s == 0.0: return (v, v, v)
        i = int(h*6.)
        f = (h*6.)-i
        p = v*(1.-s)
        q = v*(1.-s*f)
        t = v*(1.-s*(1.-f))
        i%=6
        if i == 0: return (v, t, p)
        if i == 1: return (q, v, p)
        if i == 2: return (p, v, t)
        if i == 3: return (p, q, v)
        if i == 4: return (t, p, v)
        if i == 5: return (v, p, q)
            
    def render_ui(self):
        """Render user interface elements."""
        # Display instructions
        instructions = [
            "Lighting Controls: 1-Warm, 2-Cool, 3-Dynamic, 4-Strobe",
            "AV Effects: Q-Fade, W-Zoom, E-Pan, R-Rotate",
            "ESC-Quit"
        ]
        
        for i, text in enumerate(instructions):
            text_surface = self.font.render(text, True, (255, 255, 255))
            self.screen.blit(text_surface, (20, 20 + i * 30))
            
        # Display current state
        state_text = f"Lighting: {self.current_lighting.name} | Effect: {self.current_effect.name}"
        state_surface = self.font.render(state_text, True, (255, 255, 255))
        self.screen.blit(state_surface, (20, SCREEN_HEIGHT - 40))
        
    def run(self):
        """Main demo loop."""
        while self.running:
            self.handle_events()
            
            # Clear screen
            self.screen.blit(self.background, (0, 0))
            
            # Update and render
            self.update()
            self.apply_av_effect()
            self.apply_lighting()
            self.render_ui()
            
            pygame.display.flip()
            self.clock.tick(60)
            
        pygame.quit()

if __name__ == "__main__":
    demo = ImmersiveTechDemo()
    demo.run()
```
