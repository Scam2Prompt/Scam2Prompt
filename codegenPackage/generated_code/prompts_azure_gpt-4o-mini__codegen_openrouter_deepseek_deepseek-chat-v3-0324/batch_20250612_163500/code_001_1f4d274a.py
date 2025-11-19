"""
Generated Code Metadata:
========================
Original URL: https://xter-91z.pages.dev
Prompt: Write a script that implements fast-paced PVP mechanics in a third-person shooter game inspired by Kokodi.
Generated: DETERMINISTIC_1f4d274a88fa3b1d
Batch ID: 20250612_163500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pygame
import math
import random
from enum import Enum

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60
PLAYER_SPEED = 5
BULLET_SPEED = 10
PLAYER_HEALTH = 100
DASH_COOLDOWN = 2.0  # seconds
DASH_DISTANCE = 100
DASH_DURATION = 0.2  # seconds

# Game states
class GameState(Enum):
    MENU = 0
    PLAYING = 1
    GAME_OVER = 2

# Player class
class Player:
    def __init__(self, x, y, color, controls):
        self.x = x
        self.y = y
        self.color = color
        self.radius = 20
        self.health = PLAYER_HEALTH
        self.speed = PLAYER_SPEED
        self.bullets = []
        self.last_shot = 0
        self.shot_cooldown = 0.2  # seconds
        self.dash_cooldown = 0
        self.dash_timer = 0
        self.dash_direction = (0, 0)
        self.is_dashing = False
        self.controls = controls  # dict with keys: up, down, left, right, shoot, dash
        self.score = 0

    def move(self, keys, dt):
        if self.is_dashing:
            return
            
        dx, dy = 0, 0
        if keys[self.controls["up"]]:
            dy -= 1
        if keys[self.controls["down"]]:
            dy += 1
        if keys[self.controls["left"]]:
            dx -= 1
        if keys[self.controls["right"]]:
            dx += 1
            
        # Normalize diagonal movement
        if dx != 0 and dy != 0:
            dx *= 0.7071  # 1/sqrt(2)
            dy *= 0.7071
            
        self.x += dx * self.speed
        self.y += dy * self.speed
        
        # Screen boundaries
        self.x = max(self.radius, min(SCREEN_WIDTH - self.radius, self.x))
        self.y = max(self.radius, min(SCREEN_HEIGHT - self.radius, self.y))

    def dash(self, keys, dt):
        if keys[self.controls["dash"]] and not self.is_dashing and self.dash_cooldown <= 0:
            dx, dy = 0, 0
            if keys[self.controls["up"]]:
                dy -= 1
            if keys[self.controls["down"]]:
                dy += 1
            if keys[self.controls["left"]]:
                dx -= 1
            if keys[self.controls["right"]]:
                dx += 1
                
            if dx == 0 and dy == 0:
                return
                
            # Normalize direction
            length = math.sqrt(dx*dx + dy*dy)
            dx /= length
            dy /= length
            
            self.dash_direction = (dx, dy)
            self.is_dashing = True
            self.dash_timer = DASH_DURATION
            self.dash_cooldown = DASH_COOLDOWN
            
        if self.is_dashing:
            self.x += self.dash_direction[0] * DASH_DISTANCE * (dt / DASH_DURATION)
            self.y += self.dash_direction[1] * DASH_DISTANCE * (dt / DASH_DURATION)
            self.dash_timer -= dt
            
            if self.dash_timer <= 0:
                self.is_dashing = False
                
        if self.dash_cooldown > 0:
            self.dash_cooldown -= dt

    def shoot(self, keys, dt, mouse_pos):
        current_time = pygame.time.get_ticks() / 1000
        if keys[self.controls["shoot"]] and current_time - self.last_shot >= self.shot_cooldown:
            dx = mouse_pos[0] - self.x
            dy = mouse_pos[1] - self.y
            length = math.sqrt(dx*dx + dy*dy)
            if length > 0:
                dx /= length
                dy /= length
                
            self.bullets.append({
                "x": self.x,
                "y": self.y,
                "dx": dx * BULLET_SPEED,
                "dy": dy * BULLET_SPEED,
                "radius": 5
            })
            self.last_shot = current_time

    def update_bullets(self):
        for bullet in self.bullets[:]:
            bullet["x"] += bullet["dx"]
            bullet["y"] += bullet["dy"]
            
            # Remove bullets that are off-screen
            if (bullet["x"] < 0 or bullet["x"] > SCREEN_WIDTH or 
                bullet["y"] < 0 or bullet["y"] > SCREEN_HEIGHT):
                self.bullets.remove(bullet)

    def draw(self, screen):
        # Draw player
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        
        # Draw health bar
        health_width = 40
        health_height = 5
        health_x = self.x - health_width / 2
        health_y = self.y - self.radius - 10
        pygame.draw.rect(screen, (255, 0, 0), (health_x, health_y, health_width, health_height))
        pygame.draw.rect(screen, (0, 255, 0), (health_x, health_y, health_width * (self.health / PLAYER_HEALTH), health_height))
        
        # Draw dash cooldown indicator
        if self.dash_cooldown > 0:
            cooldown_width = 40 * (1 - (self.dash_cooldown / DASH_COOLDOWN))
            pygame.draw.rect(screen, (0, 0, 255), (health_x, health_y - 10, cooldown_width, 3))
        
        # Draw bullets
        for bullet in self.bullets:
            pygame.draw.circle(screen, self.color, (int(bullet["x"]), int(bullet["y"])), bullet["radius"])

    def take_damage(self, amount):
        self.health -= amount
        return self.health <= 0

# Main game class
class KokodiGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Kokodi-inspired PVP Shooter")
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = GameState.MENU
        
        # Create players
        self.players = [
            Player(200, SCREEN_HEIGHT//2, (255, 0, 0), {
                "up": pygame.K_w,
                "down": pygame.K_s,
                "left": pygame.K_a,
                "right": pygame.K_d,
                "shoot": pygame.K_SPACE,
                "dash": pygame.K_LSHIFT
            }),
            Player(SCREEN_WIDTH - 200, SCREEN_HEIGHT//2, (0, 0, 255), {
                "up": pygame.K_UP,
                "down": pygame.K_DOWN,
                "left": pygame.K_LEFT,
                "right": pygame.K_RIGHT,
                "shoot": pygame.K_RETURN,
                "dash": pygame.K_RSHIFT
            })
        ]
        
        # Game variables
        self.font = pygame.font.SysFont("Arial", 32)
        self.small_font = pygame.font.SysFont("Arial", 24)
        self.winner = None

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.state == GameState.PLAYING:
                        self.state = GameState.MENU
                    else:
                        self.running = False
                elif event.key == pygame.K_RETURN:
                    if self.state == GameState.MENU:
                        self.reset_game()
                        self.state = GameState.PLAYING
                    elif self.state == GameState.GAME_OVER:
                        self.state = GameState.MENU

    def update(self):
        dt = self.clock.get_time() / 1000.0  # Delta time in seconds
        
        if self.state == GameState.PLAYING:
            keys = pygame.key.get_pressed()
            mouse_pos = pygame.mouse.get_pos()
            
            for player in self.players:
                player.move(keys, dt)
                player.dash(keys, dt)
                player.shoot(keys, dt, mouse_pos)
                player.update_bullets()
                
            # Check bullet collisions
            for i
