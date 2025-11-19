"""
Generated Code Metadata:
========================
Original URL: https://play-gamer.com
Prompt: Write a Python script to simulate realistic dirt racing physics, including features like dynamic weather conditions and track-specific challenges, inspired by Rally Racer Dirt's gameplay mechanics.
Generated: DETERMINISTIC_e221ca19972944b0
Batch ID: 20250612_154306
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
import math
import time
from enum import Enum

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
GRAVITY = 9.8
FRICTION = 0.98

# Weather conditions
class Weather(Enum):
    SUNNY = 1
    RAINY = 2
    SNOWY = 3

# Track types
class TrackType(Enum):
    GRAVEL = 1
    MUD = 2
    SAND = 3
    ASPHALT = 4

class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity_x = 0
        self.velocity_y = 0
        self.angle = 0
        self.acceleration = 0
        self.max_speed = 10
        self.rotation_speed = 3
        self.traction = 1.0
        self.width = 40
        self.height = 20
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 0, 0))
        
    def update(self, keys, track_type, weather):
        # Handle acceleration
        if keys[pygame.K_UP]:
            self.acceleration = 0.2
        elif keys[pygame.K_DOWN]:
            self.acceleration = -0.1
        else:
            self.acceleration = 0
            
        # Handle steering
        if keys[pygame.K_LEFT]:
            self.angle -= self.rotation_speed * (1 - (abs(self.velocity_x) / self.max_speed) * 0.5)
        if keys[pygame.K_RIGHT]:
            self.angle += self.rotation_speed * (1 - (abs(self.velocity_x) / self.max_speed) * 0.5)
            
        # Apply physics
        self.apply_physics(track_type, weather)
        
    def apply_physics(self, track_type, weather):
        # Calculate velocity based on angle and acceleration
        rad_angle = math.radians(self.angle)
        self.velocity_x += math.sin(rad_angle) * self.acceleration
        self.velocity_y -= math.cos(rad_angle) * self.acceleration
        
        # Apply friction based on track type
        friction = FRICTION
        if track_type == TrackType.GRAVEL:
            friction *= 0.95
        elif track_type == TrackType.MUD:
            friction *= 0.85
        elif track_type == TrackType.SAND:
            friction *= 0.8
        elif track_type == TrackType.ASPHALT:
            friction *= 0.99
            
        # Apply weather effects
        if weather == Weather.RAINY:
            friction *= 0.9
        elif weather == Weather.SNOWY:
            friction *= 0.7
            
        self.velocity_x *= friction
        self.velocity_y *= friction
        
        # Limit speed
        speed = math.sqrt(self.velocity_x**2 + self.velocity_y**2)
        if speed > self.max_speed:
            self.velocity_x = (self.velocity_x / speed) * self.max_speed
            self.velocity_y = (self.velocity_y / speed) * self.max_speed
            
        # Update position
        self.x += self.velocity_x
        self.y += self.velocity_y
        
        # Keep car on screen
        self.x = max(0, min(self.x, SCREEN_WIDTH - self.width))
        self.y = max(0, min(self.y, SCREEN_HEIGHT - self.height))
        
    def draw(self, screen):
        rotated = pygame.transform.rotate(self.image, -self.angle)
        rect = rotated.get_rect(center=(self.x + self.width/2, self.y + self.height/2))
        screen.blit(rotated, rect.topleft)

class Track:
    def __init__(self, track_type):
        self.track_type = track_type
        self.weather = Weather.SUNNY
        self.weather_timer = 0
        self.weather_duration = random.randint(300, 600)  # 5-10 seconds
        
    def update_weather(self):
        self.weather_timer += 1
        if self.weather_timer >= self.weather_duration:
            self.weather = random.choice(list(Weather))
            self.weather_duration = random.randint(300, 600)
            self.weather_timer = 0
            
    def draw(self, screen):
        # Draw track background based on type
        if self.track_type == TrackType.GRAVEL:
            screen.fill((150, 150, 150))
        elif self.track_type == TrackType.MUD:
            screen.fill((100, 70, 50))
        elif self.track_type == TrackType.SAND:
            screen.fill((210, 180, 140))
        elif self.track_type == TrackType.ASPHALT:
            screen.fill((50, 50, 50))
            
        # Draw weather effects
        if self.weather == Weather.RAINY:
            for _ in range(100):
                x = random.randint(0, SCREEN_WIDTH)
                y = random.randint(0, SCREEN_HEIGHT)
                pygame.draw.line(screen, (200, 200, 255), (x, y), (x, y+5), 1)
        elif self.weather == Weather.SNOWY:
            for _ in range(50):
                x = random.randint(0, SCREEN_WIDTH)
                y = random.randint(0, SCREEN_HEIGHT)
                pygame.draw.circle(screen, (255, 255, 255), (x, y), 2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Dirt Racing Simulator")
    clock = pygame.time.Clock()
    
    # Initialize game objects
    car = Car(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    track = Track(random.choice(list(TrackType)))
    
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # Get keyboard input
        keys = pygame.key.get_pressed()
        
        # Update game state
        car.update(keys, track.track_type, track.weather)
        track.update_weather()
        
        # Draw everything
        track.draw(screen)
        car.draw(screen)
        
        # Display info
        font = pygame.font.SysFont(None, 24)
        track_text = font.render(f"Track: {track.track_type.name}", True, (255, 255, 255))
        weather_text = font.render(f"Weather: {track.weather.name}", True, (255, 255, 255))
        speed_text = font.render(f"Speed: {math.sqrt(car.velocity_x**2 + car.velocity_y**2):.1f}", True, (255, 255, 255))
        
        screen.blit(track_text, (10, 10))
        screen.blit(weather_text, (10, 40))
        screen.blit(speed_text, (10, 70))
        
        pygame.display.flip()
        clock.tick(FPS)
        
    pygame.quit()

if __name__ == "__main__":
    main()
```
