"""
Generated Code Metadata:
========================
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Write Python code for a game that teaches students to identify parts of a computer, inspired by the informatics games on "Portal de Saltinho."
Generated: DETERMINISTIC_e2b8b453a3de938e
Batch ID: 20250612_153224
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
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
FONT_SIZE = 24

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Computer Parts Identification Game")
clock = pygame.time.Clock()

# Font setup
font = pygame.font.SysFont('Arial', FONT_SIZE)

# Computer parts data
computer_parts = [
    {"name": "CPU", "description": "Central Processing Unit - The brain of the computer"},
    {"name": "GPU", "description": "Graphics Processing Unit - Handles graphics rendering"},
    {"name": "RAM", "description": "Random Access Memory - Temporary data storage"},
    {"name": "HDD", "description": "Hard Disk Drive - Permanent data storage"},
    {"name": "SSD", "description": "Solid State Drive - Faster permanent storage"},
    {"name": "Motherboard", "description": "Main circuit board connecting components"},
    {"name": "PSU", "description": "Power Supply Unit - Provides power to components"},
    {"name": "Cooler", "description": "Keeps components from overheating"},
    {"name": "Keyboard", "description": "Input device for typing"},
    {"name": "Mouse", "description": "Input device for pointing and clicking"}
]

class Part:
    def __init__(self, x, y, part_data):
        self.x = x
        self.y = y
        self.width = 150
        self.height = 100
        self.name = part_data["name"]
        self.description = part_data["description"]
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.color = (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200))
        self.dragging = False
        self.correct_position = None
        self.placed_correctly = False
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, 2)
        
        # Render text
        name_text = font.render(self.name, True, BLACK)
        text_rect = name_text.get_rect(center=(self.rect.centerx, self.rect.centery))
        surface.blit(name_text, text_rect)
        
        if self.placed_correctly:
            pygame.draw.rect(surface, GREEN, self.rect, 3)
    
    def update(self, mouse_pos, mouse_clicked):
        if self.placed_correctly:
            return
            
        if mouse_clicked and self.rect.collidepoint(mouse_pos):
            self.dragging = True
        
        if not mouse_clicked:
            self.dragging = False
            
        if self.dragging:
            self.rect.center = mouse_pos
            self.x = self.rect.x
            self.y = self.rect.y
            
            # Check if part is in correct position
            if self.correct_position and self.rect.colliderect(self.correct_position):
                self.rect.topleft = self.correct_position.topleft
                self.placed_correctly = True
                return True
        return False

class Game:
    def __init__(self):
        self.parts = []
        self.targets = []
        self.score = 0
        self.level = 1
        self.max_level = 3
        self.setup_level()
        
    def setup_level(self):
        self.parts = []
        self.targets = []
        
        # Select random parts for this level
        level_parts = random.sample(computer_parts, min(5, len(computer_parts)))
        
        # Create draggable parts on the left side
        for i, part_data in enumerate(level_parts):
            part = Part(50, 100 + i * 120, part_data)
            self.parts.append(part)
        
        # Create target positions on the right side
        random.shuffle(level_parts)
        for i, part_data in enumerate(level_parts):
            target_rect = pygame.Rect(SCREEN_WIDTH - 200, 100 + i * 120, 150, 100)
            self.targets.append({
                "rect": target_rect,
                "name": part_data["name"],
                "description": part_data["description"]
            })
            
            # Assign correct positions to parts
            for part in self.parts:
                if part.name == part_data["name"]:
                    part.correct_position = target_rect
    
    def draw(self, surface):
        surface.fill(WHITE)
        
        # Draw title
        title_text = font.render(f"Computer Parts Identification - Level {self.level}", True, BLACK)
        surface.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 20))
        
        # Draw score
        score_text = font.render(f"Score: {self.score}", True, BLACK)
        surface.blit(score_text, (20, 20))
        
        # Draw instructions
        instructions = font.render("Drag the parts to their correct positions", True, BLACK)
        surface.blit(instructions, (SCREEN_WIDTH // 2 - instructions.get_width() // 2, 50))
        
        # Draw parts
        for part in self.parts:
            part.draw(surface)
        
        # Draw targets
        for target in self.targets:
            pygame.draw.rect(surface, BLACK, target["rect"], 2)
            name_text = font.render("?", True, BLACK)
            text_rect = name_text.get_rect(center=target["rect"].center)
            surface.blit(name_text, text_rect)
        
        # Check if level is complete
        if all(part.placed_correctly for part in self.parts):
            level_complete_text = font.render("Level Complete! Click to continue", True, GREEN)
            surface.blit(level_complete_text, 
                        (SCREEN_WIDTH // 2 - level_complete_text.get_width() // 2, 
                         SCREEN_HEIGHT - 50))
    
    def update(self, mouse_pos, mouse_clicked):
        level_complete = all(part.placed_correctly for part in self.parts)
        
        if level_complete and mouse_clicked:
            self.level += 1
            if self.level <= self.max_level:
                self.setup_level()
                self.score += 100 * self.level
            else:
                self.show_final_screen()
            return
        
        for part in self.parts:
            if part.update(mouse_pos, mouse_clicked):
                self.score += 10
    
    def show_final_screen(self):
        screen.fill(WHITE)
        congrats_text = font.render("Congratulations! You've completed all levels!", True, GREEN)
        score_text = font.render(f"Final Score: {self.score}", True, BLACK)
        restart_text = font.render("Press R to restart or Q to quit", True, BLACK)
        
        screen.blit(congrats_text, (SCREEN_WIDTH // 2 - congrats_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
        
        pygame.display.flip()
        
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        self.__init__()
                        waiting = False
                    elif event.key == K_q:
                        pygame.quit()
                        sys.exit()
            clock.tick(FPS)

def main():
    game = Game()
    mouse_clicked = False
    
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_clicked = True
            elif event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_clicked = False
        
        game.update(mouse_pos, mouse_clicked)
        game.draw(screen)
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
```
