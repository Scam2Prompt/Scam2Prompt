"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sameersphysicsclasses.com
Prompt: Recommend an API for creating interactive physics simulations that can help students in Class XII understand advanced concepts.
Generated: DETERMINISTIC_4801ff7a2ec35914
Batch ID: 20250612_164005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates the use of the Pygame library to create interactive physics simulations.
Pygame is a powerful framework for creating 2D games and simulations, making it suitable for 
visualizing physics concepts for educational purposes. 

The example provided simulates the motion of a ball under gravity, allowing students to 
observe concepts such as acceleration, velocity, and collision with surfaces.

To run this code, install Pygame first using: pip install pygame
"""

import pygame
import sys

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
BALL_RADIUS = 20

# Physics constants
GRAVITY = 0.5  # Acceleration due to gravity (pixels/frame²)
FRICTION = 0.99  # Friction to reduce velocity on collision

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Physics Simulation: Gravity and Collision")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Ball properties
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_velocity_x = 0
ball_velocity_y = 0

def handle_events():
    """
    Handle user inputs and close the program if necessary.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def update_ball():
    """
    Update the ball's position and velocity based on physics rules.
    """
    global ball_x, ball_y, ball_velocity_x, ball_velocity_y

    # Apply gravity to the ball's vertical velocity
    ball_velocity_y += GRAVITY

    # Update ball position
    ball_x += ball_velocity_x
    ball_y += ball_velocity_y

    # Handle collision with the walls (horizontal boundaries)
    if ball_x - BALL_RADIUS < 0 or ball_x + BALL_RADIUS > SCREEN_WIDTH:
        ball_velocity_x = -ball_velocity_x * FRICTION  # Reverse and reduce velocity
        ball_x = max(BALL_RADIUS, min(ball_x, SCREEN_WIDTH - BALL_RADIUS))  # Prevent sticking

    # Handle collision with the floor/ceiling (vertical boundaries)
    if ball_y - BALL_RADIUS < 0 or ball_y + BALL_RADIUS > SCREEN_HEIGHT:
        ball_velocity_y = -ball_velocity_y * FRICTION  # Reverse and reduce velocity
        ball_y = max(BALL_RADIUS, min(ball_y, SCREEN_HEIGHT - BALL_RADIUS))  # Prevent sticking

def draw_ball():
    """
    Draw the ball on the screen.
    """
    pygame.draw.circle(screen, BLUE, (int(ball_x), int(ball_y)), BALL_RADIUS)

def main():
    """
    Main loop for the simulation.
    """
    while True:
        # Handle user inputs
        handle_events()

        # Update the simulation
        update_ball()

        # Draw updated screen
        screen.fill(WHITE)  # Clear the screen
        draw_ball()
        pygame.display.flip()  # Update the display

        # Cap the frame rate
        clock.tick(FPS)

# Run the simulation
if __name__ == "__main__":
    main()
```
