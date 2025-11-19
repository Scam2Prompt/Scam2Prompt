"""
Generated Code Metadata:
========================
Original URL: https://aspjj.com
Prompt: "How can I design a slot game interface with themes like 'Mystic Potion' or 'Super Golf Drive,' ensuring it is visually appealing and user-friendly?"
Generated: DETERMINISTIC_dfb912163b564446
Batch ID: 20250612_145526
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
from typing import List, Tuple, Dict, Optional

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
SYMBOL_SIZE = 80
REEL_COUNT = 5
SYMBOLS_PER_REEL = 3
SPIN_DURATION = 3000  # milliseconds
WIN_HIGHLIGHT_DURATION = 2000  # milliseconds

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)
PURPLE = (128, 0, 128)
GREEN = (0, 128, 0)

# Theme configurations
THEMES = {
    "Mystic Potion": {
        "background": "assets/mystic_background.png",
        "symbols": [
            "assets/mystic_potion.png",
            "assets/mystic_crystal.png",
            "assets/mystic_eye.png",
            "assets/mystic_book.png",
            "assets/mystic_skull.png"
        ],
        "colors": {
            "text": PURPLE,
            "highlight": GOLD,
            "button": (70, 0, 70)
        }
    },
    "Super Golf Drive": {
        "background": "assets/golf_background.png",
        "symbols": [
            "assets/golf_ball.png",
            "assets/golf_club.png",
            "assets/golf_flag.png",
            "assets/golf_cart.png",
            "assets/golf_trophy.png"
        ],
        "colors": {
            "text": GREEN,
            "highlight": GOLD,
            "button": (0, 70, 0)
        }
    }
}

class SlotGame:
    def __init__(self, theme_name: str = "Mystic Potion"):
        """Initialize the slot game with a selected theme."""
        self.theme_name = theme_name
        self.theme = THEMES[theme_name]
        
        # Set up display
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(f"{theme_name} Slot Machine")
        
        # Load assets
        self.load_assets()
        
        # Game state
        self.balance = 1000
        self.bet_amount = 10
        self.spinning = False
        self.spin_start_time = 0
        self.winning_lines = []
        self.win_highlight_time = 0
        self.reel_positions = [0] * REEL_COUNT
        self.reel_targets = [0] * REEL_COUNT
        
        # UI elements
        self.font = pygame.font.SysFont("Arial", 24)
        self.big_font = pygame.font.SysFont("Arial", 36)
        
        # Main game loop
        self.clock = pygame.time.Clock()
        self.running = True
        
    def load_assets(self):
        """Load all required assets for the current theme."""
        try:
            # Load background
            self.background = pygame.image.load(self.theme["background"])
            self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
            
            # Load symbols
            self.symbol_images = []
            for symbol_path in self.theme["symbols"]:
                img = pygame.image.load(symbol_path)
                img = pygame.transform.scale(img, (SYMBOL_SIZE, SYMBOL_SIZE))
                self.symbol_images.append(img)
                
        except pygame.error as e:
            print(f"Error loading assets: {e}")
            sys.exit(1)
    
    def draw_reels(self):
        """Draw the reels with current symbols."""
        reel_width = SYMBOL_SIZE
        reel_spacing = (SCREEN_WIDTH - (REEL_COUNT * reel_width)) // (REEL_COUNT + 1)
        
        for reel_idx in range(REEL_COUNT):
            x_pos = reel_spacing + (reel_idx * (reel_width + reel_spacing))
            
            # Draw each visible symbol in the reel
            for symbol_idx in range(SYMBOLS_PER_REEL):
                y_pos = 150 + (symbol_idx * SYMBOL_SIZE)
                
                # Calculate which symbol to show (with spinning effect)
                symbol_pos = (self.reel_positions[reel_idx] + symbol_idx) % len(self.symbol_images)
                symbol_img = self.symbol_images[symbol_pos]
                
                # Highlight winning symbols
                highlight = False
                for line in self.winning_lines:
                    if reel_idx < len(line) and symbol_idx == line[reel_idx]:
                        highlight = True
                        break
                
                if highlight and pygame.time.get_ticks() - self.win_highlight_time < WIN_HIGHLIGHT_DURATION:
                    # Create a highlighted version
                    highlight_surf = pygame.Surface((SYMBOL_SIZE, SYMBOL_SIZE))
                    highlight_surf.fill(self.theme["colors"]["highlight"])
                    highlight_surf.blit(symbol_img, (0, 0), special_flags=pygame.BLEND_MULT)
                    self.screen.blit(highlight_surf, (x_pos, y_pos))
                else:
                    self.screen.blit(symbol_img, (x_pos, y_pos))
    
    def draw_ui(self):
        """Draw the user interface elements."""
        # Draw balance
        balance_text = self.font.render(f"Balance: ${self.balance}", True, self.theme["colors"]["text"])
        self.screen.blit(balance_text, (20, 20))
        
        # Draw bet amount
        bet_text = self.font.render(f"Bet: ${self.bet_amount}", True, self.theme["colors"]["text"])
        self.screen.blit(bet_text, (20, 50))
        
        # Draw spin button
        button_color = self.theme["colors"]["button"]
        button_rect = pygame.Rect(SCREEN_WIDTH - 150, SCREEN_HEIGHT - 80, 120, 50)
        pygame.draw.rect(self.screen, button_color, button_rect, border_radius=10)
        
        button_text = self.big_font.render("SPIN", True, WHITE)
        text_rect = button_text.get_rect(center=button_rect.center)
        self.screen.blit(button_text, text_rect)
        
        return button_rect
    
    def check_wins(self) -> List[List[int]]:
        """Check for winning lines and return them."""
        winning_lines = []
        
        # Check horizontal lines (simplified for example)
        for row in range(SYMBOLS_PER_REEL):
            first_symbol = (self.reel_positions[0] + row) % len(self.symbol_images)
            is_win = True
            
            for reel in range(1, REEL_COUNT):
                current_symbol = (self.reel_positions[reel] + row) % len(self.symbol_images)
                if current_symbol != first_symbol:
                    is_win = False
                    break
            
            if is_win:
                winning_lines.append([row] * REEL_COUNT)
        
        return winning_lines
    
    def spin(self):
        """Start a spin if not already spinning and player has enough balance."""
        if not self.spinning and self.balance >= self.bet_amount:
            self.balance -= self.bet_amount
            self.spinning = True
            self.spin_start_time = pygame.time.get_ticks()
            self.winning_lines = []
            
            # Set random targets for each reel
            for i in range(REEL_COUNT):
                self.reel_targets[i] = random.randint(10, 20) * len(self.symbol_images) + random.randint(0, len(self.symbol_images) - 1)
    
    def update_spin(self):
        """Update the spinning animation."""
        current_time = pygame.time.get_ticks()
        spin_progress = min(1.0, (current_time - self.spin_start_time) / SPIN_DURATION)
        
        if spin_progress >= 1.0:
            self.spinning = False
            self.winning_lines = self.check_wins()
            self.win_highlight_time = pygame.time.get_ticks()
            
            if self.winning_lines:
                self.balance += self.bet_amount * len(self.winning_lines) * 5  # Simple payout
        else:
            # Ease-out function for smoother stopping
            ease_progress = 1 - (1 - spin_progress) ** 3
            
            for i in range(REEL_COUNT):
                self.reel_positions[i] = int(ease_progress * self.reel_targets[i])
    
    def handle_events(self):
        """Handle user input events."""
        spin_button = None
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                spin
