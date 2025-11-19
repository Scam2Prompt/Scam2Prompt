"""
Generated Code Metadata:
========================
Original URL: https://minerinde.com
Prompt: Create a simulation in Python to demonstrate the benefits of increasing click speed and multiplying coin earnings, as described in the "Verbessern Sie Ihr Tipperlebnis" section of the TG WebApp Euro Verdienen webpage.
Generated: DETERMINISTIC_1f899a11925cc0b0
Batch ID: 20250612_145712
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
import time
from pygame.locals import *

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
RED = (200, 0, 0)
GOLD = (255, 215, 0)

# Game variables
coins = 0
click_value = 1
click_speed = 1  # clicks per second
multiplier = 1.0
upgrades = {
    "click_power": {"cost": 10, "value": 1, "level": 0},
    "click_speed": {"cost": 25, "value": 0.1, "level": 0},
    "multiplier": {"cost": 50, "value": 0.1, "level": 0}
}
last_click_time = 0
auto_clickers = 0
auto_clicker_cost = 100

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Coin Clicker Simulation")
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 24)
small_font = pygame.font.SysFont('Arial', 18)

def draw_button(x, y, width, height, color, text, text_color=WHITE):
    """Draw a button with text"""
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surf = font.render(text, True, text_color)
    text_rect = text_surf.get_rect(center=(x + width/2, y + height/2))
    screen.blit(text_surf, text_rect)
    return pygame.Rect(x, y, width, height)

def draw_stats():
    """Draw game statistics on screen"""
    # Coin display
    coin_text = font.render(f"Coins: {coins:.2f}", True, GOLD)
    screen.blit(coin_text, (20, 20))
    
    # Stats display
    stats = [
        f"Click Value: {click_value}",
        f"Click Speed: {click_speed:.1f}/s",
        f"Multiplier: {multiplier:.1f}x",
        f"Auto Clickers: {auto_clickers}"
    ]
    
    for i, stat in enumerate(stats):
        stat_text = small_font.render(stat, True, WHITE)
        screen.blit(stat_text, (20, 60 + i * 30))

def draw_upgrades():
    """Draw upgrade buttons"""
    upgrades_text = font.render("Upgrades", True, WHITE)
    screen.blit(upgrades_text, (SCREEN_WIDTH - 200, 20))
    
    # Click power upgrade
    power_rect = draw_button(
        SCREEN_WIDTH - 220, 60, 180, 50, BLUE,
        f"Power (+1) - {upgrades['click_power']['cost']} coins"
    )
    
    # Click speed upgrade
    speed_rect = draw_button(
        SCREEN_WIDTH - 220, 120, 180, 50, GREEN,
        f"Speed (+0.1) - {upgrades['click_speed']['cost']} coins"
    )
    
    # Multiplier upgrade
    multi_rect = draw_button(
        SCREEN_WIDTH - 220, 180, 180, 50, RED,
        f"Multiplier (+0.1) - {upgrades['multiplier']['cost']} coins"
    )
    
    # Auto clicker
    auto_rect = draw_button(
        SCREEN_WIDTH - 220, 240, 180, 50, GOLD,
        f"Auto Clicker - {auto_clicker_cost} coins"
    )
    
    return power_rect, speed_rect, multi_rect, auto_rect

def handle_upgrade(upgrade_type):
    """Handle upgrade purchases"""
    global coins, click_value, click_speed, multiplier, auto_clickers, auto_clicker_cost
    
    if upgrade_type == "auto_clicker":
        if coins >= auto_clicker_cost:
            coins -= auto_clicker_cost
            auto_clickers += 1
            auto_clicker_cost = int(auto_clicker_cost * 1.5)
            return True
    else:
        upgrade = upgrades[upgrade_type]
        if coins >= upgrade["cost"]:
            coins -= upgrade["cost"]
            
            if upgrade_type == "click_power":
                click_value += upgrade["value"]
            elif upgrade_type == "click_speed":
                click_speed += upgrade["value"]
            elif upgrade_type == "multiplier":
                multiplier += upgrade["value"]
            
            upgrade["level"] += 1
            upgrade["cost"] = int(upgrade["cost"] * 1.5)
            return True
    
    return False

def main():
    global coins, last_click_time
    
    # Main game loop
    running = True
    coin_rect = pygame.Rect(SCREEN_WIDTH//2 - 50, SCREEN_HEIGHT//2 - 50, 100, 100)
    
    while running:
        current_time = time.time()
        
        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    mouse_pos = pygame.mouse.get_pos()
                    
                    # Check if clicked on coin
                    if coin_rect.collidepoint(mouse_pos):
                        coins += click_value * multiplier
                        last_click_time = current_time
                    
                    # Check upgrades
                    power_rect, speed_rect, multi_rect, auto_rect = draw_upgrades()
                    
                    if power_rect.collidepoint(mouse_pos):
                        handle_upgrade("click_power")
                    elif speed_rect.collidepoint(mouse_pos):
                        handle_upgrade("click_speed")
                    elif multi_rect.collidepoint(mouse_pos):
                        handle_upgrade("multiplier")
                    elif auto_rect.collidepoint(mouse_pos):
                        handle_upgrade("auto_clicker")
        
        # Auto clickers
        if auto_clickers > 0 and current_time - last_click_time >= 1.0 / click_speed:
            coins += (click_value * multiplier * auto_clickers)
            last_click_time = current_time
        
        # Draw everything
        screen.fill(BLACK)
        
        # Draw coin
        pygame.draw.ellipse(screen, GOLD, coin_rect)
        coin_text = font.render("Click!", True, BLACK)
        coin_text_rect = coin_text.get_rect(center=coin_rect.center)
        screen.blit(coin_text, coin_text_rect)
        
        # Draw stats and upgrades
        draw_stats()
        draw_upgrades()
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
```
