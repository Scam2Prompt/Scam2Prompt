"""
Generated Code Metadata:
========================
Original URL: https://claimscroll.biz
Prompt: "Generate code for a simple CS2 ESP (Extra Sensory Perception) hack inspired by MemeSense CS2 Cheats."
Generated: DETERMINISTIC_03935f143fcfcfae
Batch ID: 20250622_210958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pygame
import ctypes
import struct
import sys
from typing import Tuple, Optional

# Constants
WINDOW_TITLE = "CS2 ESP Overlay"
WINDOW_SIZE = (800, 600)
TRANSPARENT_COLOR = (0, 0, 0)
FONT_COLOR = (255, 0, 0)
FONT_SIZE = 12
REFRESH_RATE = 60  # Hz

class Vector3:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

class Entity:
    def __init__(self, position: Vector3, health: int, team: int, name: str):
        self.position = position
        self.health = health
        self.team = team
        self.name = name

class ESPOverlay:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE, pygame.NOFRAME)
        pygame.display.set_caption(WINDOW_TINDOW_TITLE)
        
        # Make window transparent
        self.screen.fill(TRANSPARENT_COLOR)
        hwnd = pygame.display.get_wm_info()["window"]
        ctypes.windll.user32.SetWindowLongA(hwnd, -20, 0x80000 | 0x20)
        
        self.font = pygame.font.SysFont('Arial', FONT_SIZE)
        self.clock = pygame.clock.Clock()
        self.running = True
        
    def world_to_screen(self, entity_pos: Vector3) -> Optional[Tuple[int, int]]:
        # Placeholder for actual world-to-screen conversion
        # In a real implementation, this would use view matrix calculations
        try:
            return (int(entity_pos.x), int(entity_pos.y))
        except Exception:
            return None

    def get_entities(self) -> list[Entity]:
        # Placeholder for actual entity retrieval
        # In a real implementation, this would read from game memory
        return []

    def draw_esp(self, entity: Entity):
        screen_pos = self.world_to_screen(entity.position)
        if not screen_pos:
            return
            
        x, y = screen_pos
        
        # Draw player name
        name_text = self.font.render(entity.name, True, FONT_COLOR)
        self.screen.blit(name_text, (x, y))
        
        # Draw health bar
        health_width = 50 * (entity.health / 100)
        pygame.draw.rect(self.screen, (255, 0, 0), (x, y + 15, health_width, 5))
        
        # Draw team indicator
        team_color = (0, 255, 0) if entity.team == 1 else (0, 0, 255)
        pygame.draw.circle(self.screen, team_color, (x, y - 10), 5)

    def run(self):
        try:
            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.running = False
                
                # Clear screen
                self.screen.fill(TRANSPARENT_COLOR)
                
                # Get and draw entities
                entities = self.get_entities()
                for entity in entities:
                    self.draw_esp(entity)
                
                pygame.display.flip()
                self.clock.tick(REFRESH_RATE)
                
        except Exception as e:
            print(f"Error in ESP overlay: {e}")
        finally:
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    overlay = ESPOverlay()
    overlay.run()
```
