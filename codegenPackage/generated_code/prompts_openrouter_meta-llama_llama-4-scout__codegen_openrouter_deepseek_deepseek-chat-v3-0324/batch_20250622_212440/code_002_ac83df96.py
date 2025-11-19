"""
Generated Code Metadata:
========================
Original URL: https://dev-x-studios.com
Prompt: "Design a gaming experience that transports players to new worlds and tells unforgettable stories, inspired by Dev-X-Studios' approach."
Generated: DETERMINISTIC_ac83df96d5c7f8fa
Batch ID: 20250622_212440
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
import json
import os
import sys
from enum import Enum

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60
ASSET_PATH = "assets/"
SAVE_PATH = "saves/"

# Game states
class GameState(Enum):
    MAIN_MENU = 0
    PLAYING = 1
    PAUSED = 2
    GAME_OVER = 3
    CUTSCENE = 4

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.health = 100
        self.inventory = []
        self.story_progress = 0
        
    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            
        # Boundary checking
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))
    
    def add_to_inventory(self, item):
        self.inventory.append(item)
        
    def take_damage(self, amount):
        self.health -= amount
        return self.health <= 0

# World class
class World:
    def __init__(self, name, background_color, story_segments):
        self.name = name
        self.background_color = background_color
        self.story_segments = story_segments
        self.current_segment = 0
        self.enemies = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        
    def load_segment(self, segment_index):
        if segment_index < len(self.story_segments):
            self.current_segment = segment_index
            return self.story_segments[segment_index]
        return None
    
    def next_segment(self):
        return self.load_segment(self.current_segment + 1)
    
    def spawn_enemies(self, count):
        for _ in range(count):
            enemy = pygame.sprite.Sprite()
            enemy.image = pygame.Surface((40, 40))
            enemy.image.fill((255, 0, 0))
            enemy.rect = enemy.image.get_rect()
            enemy.rect.x = random.randint(0, SCREEN_WIDTH - 40)
            enemy.rect.y = random.randint(0, SCREEN_HEIGHT - 40)
            self.enemies.add(enemy)
    
    def spawn_items(self, count):
        for _ in range(count):
            item = pygame.sprite.Sprite()
            item.image = pygame.Surface((20, 20))
            item.image.fill((0, 0, 255))
            item.rect = item.image.get_rect()
            item.rect.x = random.randint(0, SCREEN_WIDTH - 20)
            item.rect.y = random.randint(0, SCREEN_HEIGHT - 20)
            self.items.add(item)

# Game class
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("World Explorer")
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = GameState.MAIN_MENU
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.worlds = []
        self.current_world_index = 0
        self.font = pygame.font.SysFont("Arial", 24)
        
        # Load game data
        self.load_worlds()
        self.load_save_data()
        
    def load_worlds(self):
        # In a real game, this would load from files
        story_segments = [
            "Welcome to the Forgotten Realm...",
            "The ancient ruins hold secrets...",
            "Beware the guardians of this world..."
        ]
        world1 = World("Forgotten Realm", (50, 50, 100), story_segments)
        world1.spawn_enemies(5)
        world1.spawn_items(3)
        self.worlds.append(world1)
        
        story_segments = [
            "The Crystal Desert stretches before you...",
            "The shifting sands reveal hidden paths...",
            "The desert holds its treasures close..."
        ]
        world2 = World("Crystal Desert", (200, 180, 100), story_segments)
        world2.spawn_enemies(8)
        world2.spawn_items(5)
        self.worlds.append(world2)
    
    def load_save_data(self):
        if not os.path.exists(SAVE_PATH):
            os.makedirs(SAVE_PATH)
            
        try:
            save_file = os.path.join(SAVE_PATH, "save.json")
            if os.path.exists(save_file):
                with open(save_file, "r") as f:
                    data = json.load(f)
                    self.player.story_progress = data.get("story_progress", 0)
                    self.current_world_index = data.get("world_index", 0)
        except Exception as e:
            print(f"Error loading save: {e}")
    
    def save_game(self):
        try:
            data = {
                "story_progress": self.player.story_progress,
                "world_index": self.current_world_index
            }
            save_file = os.path.join(SAVE_PATH, "save.json")
            with open(save_file, "w") as f:
                json.dump(data, f)
        except Exception as e:
            print(f"Error saving game: {e}")
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.state == GameState.PLAYING:
                        self.state = GameState.PAUSED
                    elif self.state == GameState.PAUSED:
                        self.state = GameState.PLAYING
                
                if self.state == GameState.MAIN_MENU:
                    if event.key == pygame.K_RETURN:
                        self.state = GameState.PLAYING
                
                if self.state == GameState.GAME_OVER:
                    if event.key == pygame.K_r:
                        self.reset_game()
                
                if self.state == GameState.CUTSCENE:
                    if event.key == pygame.K_SPACE:
                        self.state = GameState.PLAYING
    
    def update(self):
        if self.state == GameState.PLAYING:
            keys = pygame.key.get_pressed()
            self.player.update(keys)
            
            current_world = self.worlds[self.current_world_index]
            
            # Check collisions with enemies
            enemy_hits = pygame.sprite.spritecollide(self.player, current_world.enemies, False)
            for enemy in enemy_hits:
                if self.player.take_damage(10):
                    self.state = GameState.GAME_OVER
            
            # Check collisions with items
            item_hits = pygame.sprite.spritecollide(self.player, current_world.items, True)
            for item in item_hits:
                self.player.add_to_inventory("Item")
                
            # Progress story if all items collected
            if len(current_world.items) == 0:
                self.player.story_progress += 1
                if not current_world.next_segment():
                    # Move to next world
                    self.current_world_index = (self.current_world_index + 1) % len(self.worlds)
                    current_world = self.worlds[self.current_world_index]
                    current_world.load_segment(0)
                    self.state = GameState.CUTSCENE
                self.save_game()
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        
        if self.state == GameState.MAIN_MENU:
            title = self.font.render("WORLD EXPLORER", True, (255, 255, 255))
            instruction = self.font.render("Press ENTER to begin", True, (200, 200, 200))
            self.screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, SCREEN_HEIGHT // 3))
            self.screen.blit(instruction, (SCREEN_WIDTH // 2 - instruction.get_width() // 2, SCREEN_HEIGHT // 2))
        
        elif self.state == GameState.PLAYING or self.state == GameState.PAUSED:
            current_world = self.worlds[self.current_world_index]
