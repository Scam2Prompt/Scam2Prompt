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

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Vehicle properties
VEHICLE_MASS = 1500  # kg
ENGINE_POWER = 500  # horsepower
FRICTION_COEFFICIENT = 0.7
HAND_BRAKE_FRICTION_COEFFICIENT = 0.95

class Vehicle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity_x = 0
        self.velocity_y = 0
        self.angle = 0
        self.handbrake = False

    def update(self, acceleration, steering, delta_time):
        # Update velocity
        self.velocity_x += acceleration * math.cos(self.angle) * delta_time
        self.velocity_y += acceleration * math.sin(self.angle) * delta_time

        # Apply friction
        if self.handbrake:
            friction = HAND_BRAKE_FRICTION_COEFFICIENT
        else:
            friction = FRICTION_COEFFICIENT

        self.velocity_x *= (1 - friction * delta_time)
        self.velocity_y *= (1 - friction * delta_time)

        # Update position
        self.x += self.velocity_x * delta_time
        self.y += self.velocity_y * delta_time

        # Update angle
        self.angle += steering * delta_time

    def apply_handbrake(self, handbrake):
        self.handbrake = handbrake

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    vehicle = Vehicle(WIDTH / 2, HEIGHT / 2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    vehicle.apply_handbrake(True)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    vehicle.apply_handbrake(False)

        keys = pygame.key.get_pressed()
        acceleration = 0
        steering = 0

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            acceleration = 10
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            acceleration = -5
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            steering = -5
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            steering = 5

        vehicle.update(acceleration, steering / 10, 1 / 60)

        screen.fill(WHITE)

        # Draw vehicle
        vehicle_x_on_screen = int(vehicle.x)
        vehicle_y_on_screen = int(vehicle.y)
        pygame.draw.polygon(screen, RED, (
            (vehicle_x_on_screen + 20 * math.cos(vehicle.angle), vehicle_y_on_screen + 20 * math.sin(vehicle.angle)),
            (vehicle_x_on_screen + 10 * math.cos(vehicle.angle + math.pi * 2 / 3), vehicle_y_on_screen + 10 * math.sin(vehicle.angle + math.pi * 2 / 3)),
            (vehicle_x_on_screen + 10 * math.cos(vehicle.angle - math.pi * 2 / 3), vehicle_y_on_screen + 10 * math.sin(vehicle.angle - math.pi * 2 / 3))
        ))

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
```
