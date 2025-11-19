"""
Generated Code Metadata:
========================
Original URL: https://play-gamer.com
Prompt: Generate code for implementing handbrake drifting mechanics in a racing game, using WASD or arrow keys for control, as described in Rally Racer Dirt's gameplay instructions.
Generated: DETERMINISTIC_2b63dcc8aa0adc38
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
import math
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rally Racer Dirt")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (100, 100, 100)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 20
        self.angle = 0  # in degrees
        self.speed = 0
        self.max_speed = 10
        self.acceleration = 0.1
        self.deceleration = 0.05
        self.turn_speed = 2
        self.drift_angle = 0
        self.drifting = False
        self.handbrake = False
        self.traction_fast = 0.1  # Normal traction
        self.traction_slow = 0.02  # Drift traction
        self.traction = self.traction_fast
        
    def update(self, keys):
        # Handle acceleration/deceleration
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.speed += self.acceleration
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.speed -= self.acceleration
        else:
            # Natural deceleration
            if self.speed > 0:
                self.speed = max(0, self.speed - self.deceleration)
            elif self.speed < 0:
                self.speed = min(0, self.speed + self.deceleration)
        
        # Limit speed
        self.speed = max(-self.max_speed/2, min(self.speed, self.max_speed))
        
        # Handle steering
        if self.speed != 0:
            turn_speed = self.turn_speed * (abs(self.speed) / self.max_speed)
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.angle -= turn_speed
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.angle += turn_speed
        
        # Handle handbrake for drifting
        self.handbrake = keys[pygame.K_SPACE]
        
        if self.handbrake and abs(self.speed) > 2:
            self.drifting = True
            self.traction = self.traction_slow
            # Add some drift angle based on steering
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.drift_angle -= 1
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.drift_angle += 1
        else:
            if self.drifting:
                # Gradually return to normal when not drifting
                self.drift_angle *= 0.95
                if abs(self.drift_angle) < 0.5:
                    self.drifting = False
                    self.drift_angle = 0
                    self.traction = self.traction_fast
        
        # Apply drift angle to movement
        effective_angle = self.angle + self.drift_angle
        
        # Calculate movement vector
        rad_angle = math.radians(effective_angle)
        self.x += self.speed * math.sin(rad_angle)
        self.y -= self.speed * math.cos(rad_angle)
        
        # Apply traction (gradually reduce drift angle)
        self.drift_angle *= (1 - self.traction)
        
        # Keep car on screen
        self.x = max(0, min(self.x, SCREEN_WIDTH))
        self.y = max(0, min(self.y, SCREEN_HEIGHT))
    
    def draw(self, surface):
        # Create car surface
        car_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.rect(car_surface, RED, (0, 0, self.width, self.height))
        
        # Add some details to show orientation
        pygame.draw.rect(car_surface, WHITE, (5, 5, 10, 10))  # Front
        pygame.draw.rect(car_surface, BLUE, (self.width-15, 5, 10, 10))  # Back
        
        # Rotate car surface
        rotated_car = pygame.transform.rotate(car_surface, -self.angle)
        rect = rotated_car.get_rect(center=(self.x, self.y))
        
        # Draw to screen
        surface.blit(rotated_car, rect.topleft)
        
        # Draw drift indicator
        if self.drifting:
            drift_pos = (
                self.x + 30 * math.sin(math.radians(self.angle + 90)),
                self.y - 30 * math.cos(math.radians(self.angle + 90))
            )
            pygame.draw.circle(surface, WHITE, (int(drift_pos[0]), int(drift_pos[1])), 5)

def main():
    running = True
    car = Car(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    
    # Track surface with some dirt
    track = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    track.fill(GRAY)
    pygame.draw.rect(track, GREEN, (100, 100, SCREEN_WIDTH-200, SCREEN_HEIGHT-200), 2)
    
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Get key states
        keys = pygame.key.get_pressed()
        
        # Update car
        car.update(keys)
        
        # Draw everything
        screen.blit(track, (0, 0))
        car.draw(screen)
        
        # Display info
        font = pygame.font.SysFont(None, 24)
        speed_text = font.render(f"Speed: {abs(car.speed):.1f}", True, WHITE)
        drift_text = font.render(f"Drifting: {'Yes' if car.drifting else 'No'}", True, WHITE)
        screen.blit(speed_text, (10, 10))
        screen.blit(drift_text, (10, 40))
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()
```
