"""
Generated Code Metadata:
========================
Original URL: https://moontropica.pages.dev
Prompt: Create a build mode tool for a game like Moon Tropica, allowing players to create and share custom worlds and experiences.
Generated: DETERMINISTIC_44026efc4a0dde0d
Batch ID: 20250622_204603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pygame
import json
import os
import sys
from pygame.locals import *

# Constants
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
GRID_SIZE = 32
MAX_ITEMS = 100
SAVE_DIR = "user_worlds"
DEFAULT_THEME = "tropical"

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (200, 200, 200)

class BuildModeTool:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Moon Tropica Build Mode")
        
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 16)
        
        # Game state
        self.mode = "build"  # build, play, menu
        self.selected_item = None
        self.items = []
        self.camera_x = 0
        self.camera_y = 0
        self.grid_visible = True
        self.current_theme = DEFAULT_THEME
        
        # UI elements
        self.toolbar_rect = pygame.Rect(0, 0, SCREEN_WIDTH, 50)
        self.world_rect = pygame.Rect(0, 50, SCREEN_WIDTH, SCREEN_HEIGHT - 50)
        
        # Load assets
        self.load_assets()
        self.create_default_items()
        
        # Ensure save directory exists
        if not os.path.exists(SAVE_DIR):
            os.makedirs(SAVE_DIR)
    
    def load_assets(self):
        """Load game assets like sprites and themes"""
        # In a real implementation, this would load from files
        self.themes = {
            "tropical": {
                "background": (135, 206, 235),  # Sky blue
                "items": {
                    "palm_tree": {"color": GREEN, "size": (2, 3)},
                    "water": {"color": BLUE, "size": (1, 1)},
                    "rock": {"color": GRAY, "size": (1, 1)}
                }
            }
        }
    
    def create_default_items(self):
        """Create default items available for placement"""
        self.available_items = [
            {"name": "palm_tree", "display_name": "Palm Tree"},
            {"name": "water", "display_name": "Water"},
            {"name": "rock", "display_name": "Rock"}
        ]
    
    def handle_events(self):
        """Handle user input events"""
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.mode = "menu" if self.mode != "menu" else "build"
                elif event.key == K_g:
                    self.grid_visible = not self.grid_visible
                elif event.key == K_s and pygame.key.get_mods() & KMOD_CTRL:
                    self.save_world()
                elif event.key == K_l and pygame.key.get_mods() & KMOD_CTRL:
                    self.load_world()
            
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    self.handle_left_click(event.pos)
                elif event.button == 3:  # Right click
                    self.handle_right_click(event.pos)
                elif event.button == 4:  # Scroll up
                    self.camera_y += GRID_SIZE
                elif event.button == 5:  # Scroll down
                    self.camera_y -= GRID_SIZE
            
            if event.type == MOUSEMOTION:
                if pygame.mouse.get_pressed()[0] and self.selected_item:
                    self.handle_drag(event.pos)
    
    def handle_left_click(self, pos):
        """Handle left mouse click events"""
        if self.toolbar_rect.collidepoint(pos):
            self.handle_toolbar_click(pos)
        elif self.world_rect.collidepoint(pos):
            self.handle_world_click(pos)
    
    def handle_right_click(self, pos):
        """Handle right mouse click events"""
        if self.world_rect.collidepoint(pos):
            world_pos = self.screen_to_world(pos)
            self.remove_item_at(world_pos)
    
    def handle_drag(self, pos):
        """Handle mouse drag events"""
        if self.world_rect.collidepoint(pos):
            world_pos = self.screen_to_world(pos)
            self.place_item(world_pos)
    
    def handle_toolbar_click(self, pos):
        """Handle clicks on the toolbar"""
        item_width = SCREEN_WIDTH // len(self.available_items)
        item_index = pos[0] // item_width
        
        if 0 <= item_index < len(self.available_items):
            self.selected_item = self.available_items[item_index]["name"]
    
    def handle_world_click(self, pos):
        """Handle clicks in the world area"""
        if self.selected_item:
            world_pos = self.screen_to_world(pos)
            self.place_item(world_pos)
    
    def screen_to_world(self, screen_pos):
        """Convert screen coordinates to world coordinates"""
        x = (screen_pos[0] + self.camera_x) // GRID_SIZE
        y = (screen_pos[1] - self.toolbar_rect.height + self.camera_y) // GRID_SIZE
        return (x, y)
    
    def world_to_screen(self, world_pos):
        """Convert world coordinates to screen coordinates"""
        x = world_pos[0] * GRID_SIZE - self.camera_x
        y = world_pos[1] * GRID_SIZE + self.toolbar_rect.height - self.camera_y
        return (x, y)
    
    def place_item(self, world_pos):
        """Place an item at the specified world position"""
        if len(self.items) >= MAX_ITEMS:
            return
        
        # Check if position is already occupied
        for item in self.items:
            if item["x"] == world_pos[0] and item["y"] == world_pos[1]:
                return
        
        self.items.append({
            "type": self.selected_item,
            "x": world_pos[0],
            "y": world_pos[1]
        })
    
    def remove_item_at(self, world_pos):
        """Remove item at specified world position"""
        for i, item in enumerate(self.items):
            if item["x"] == world_pos[0] and item["y"] == world_pos[1]:
                del self.items[i]
                return
    
    def save_world(self):
        """Save the current world to a file"""
        try:
            filename = f"world_{len(os.listdir(SAVE_DIR)) + 1}.json"
            filepath = os.path.join(SAVE_DIR, filename)
            
            world_data = {
                "theme": self.current_theme,
                "items": self.items
            }
            
            with open(filepath, 'w') as f:
                json.dump(world_data, f, indent=4)
            
            print(f"World saved to {filepath}")
        except Exception as e:
            print(f"Error saving world: {e}")
    
    def load_world(self):
        """Load a world from file"""
        try:
            if not os.listdir(SAVE_DIR):
                print("No saved worlds found")
                return
            
            filename = sorted(os.listdir(SAVE_DIR))[-1]  # Load most recent
            filepath = os.path.join(SAVE_DIR, filename)
            
            with open(filepath, 'r') as f:
                world_data = json.load(f)
            
            self.current_theme = world_data.get("theme", DEFAULT_THEME)
            self.items = world_data.get("items", [])
            
            print(f"World loaded from {filepath}")
        except Exception as e:
            print(f"Error loading world: {e}")
    
    def draw(self):
        """Draw everything to the screen"""
        # Clear screen
        self.screen.fill(WHITE)
        
        # Draw toolbar
        pygame.draw.rect(self.screen, BLACK, self.toolbar_rect)
        
        # Draw toolbar items
        item_width = SCREEN_WIDTH // len(self.available_items)
        for i, item in enumerate(self.available_items):
            rect = pygame.Rect(i * item_width, 0, item_width, self.toolbar_rect.height)
            color = GREEN if item["name"] == self.selected_item else WHITE
            pygame.draw.rect(self.screen, color, rect, 2)
            
            text = self.font.render(item["display_name"], True, WHITE)
            text_rect = text.get_rect(center=rect.center)
            self.screen.blit(text, text_rect)
        
        # Draw world background
        pygame.draw.rect(self
