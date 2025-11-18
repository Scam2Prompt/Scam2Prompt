"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://play-gamer.com
Prompt: Generate code for implementing handbrake drifting mechanics in a racing game, using WASD or arrow keys for control, as described in Rally Racer Dirt's gameplay instructions.
Generated: DETERMINISTIC_2b63dcc8aa0adc38
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pygame
import math

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game clock
clock = pygame.time.Clock()

# Car configuration
CAR_WIDTH = 50
CAR_HEIGHT = 30
CAR_COLOR = (0, 255, 0)
MAX_SPEED = 10
ACCELERATION = 0.2
DECELERATION = 0.1
HAND_BRAKE_DECELERATION = 0.5
TURN_SPEED = 5

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Handbrake Drifting Mechanic")

# Car class
class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0  # Initial angle
        self.speed = 0  # Initial speed

    def draw(self):
        # Rotate the car surface around its center
        car_surface = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
        car_surface.fill(CAR_COLOR)
        rotated_car = pygame.transform.rotate(car_surface, -self.angle)
        rect = rotated_car.get_rect(center=(self.x, self.y))
        screen.blit(rotated_car, rect.topleft)

    def update(self, keys):
        global MAX_SPEED

        # Accelerate or decelerate based on key input
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.speed += ACCELERATION
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.speed -= DECELERATION
        else:
            # Gradual speed decay
            self.speed *= 0.98

        # Apply handbrake if space is pressed
        if keys[pygame.K_SPACE]:
            self.speed -= HAND_BRAKE_DECELERATION
            if self.speed < 0:
                self.speed = 0

        # Cap the speed to max speed
        if self.speed > MAX_SPEED:
            self.speed = MAX_SPEED
        elif self.speed < -MAX_SPEED / 2:  # Allow reverse speed, but limited
            self.speed = -MAX_SPEED / 2

        # Turn the car based on key input
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.angle += TURN_SPEED * (self.speed / MAX_SPEED)  # Smooth turning based on speed
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.angle -= TURN_SPEED * (self.speed / MAX_SPEED)

        # Calculate movement
        radians = math.radians(self.angle)
        self.x += self.speed * math.cos(radians)
        self.y -= self.speed * math.sin(radians)

        # Screen boundary handling
        if self.x < 0:
            self.x = 0
            self.speed = 0
        elif self.x > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH
            self.speed = 0

        if self.y < 0:
            self.y = 0
            self.speed = 0
        elif self.y > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT
            self.speed = 0


# Main game loop
def main():
    car = Car(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    running = True

    while running:
        screen.fill(WHITE)
        keys = pygame.key.get_pressed()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update car mechanics
        car.update(keys)

        # Draw the car
        car.draw()

        # Update the display
        pygame.display.flip()

        # Limit the frame rate
        clock.tick(60)

    # Quit pygame
    pygame.quit()


# Run the game
if __name__ == "__main__":
    main()
```
