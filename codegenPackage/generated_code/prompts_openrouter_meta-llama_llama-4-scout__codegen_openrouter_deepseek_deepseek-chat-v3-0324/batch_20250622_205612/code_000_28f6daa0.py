"""
Generated Code Metadata:
========================
Original URL: https://delsolmontessorihn.com
Prompt: "Write a Python code snippet to implement a simple robotics simulation for a school project, incorporating STEAM principles, as described on the Del Sol Montessori website."
Generated: DETERMINISTIC_28f6daa0655ee01b
Batch ID: 20250622_205612
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
import time
from pygame.locals import *

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ROBOT_RADIUS = 20
OBSTACLE_RADIUS = 15
GOAL_RADIUS = 25
ROBOT_SPEED = 2
ROTATION_SPEED = 2
SENSOR_RANGE = 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

class Robot:
    """Class representing the robot in the simulation"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.sensors = [0, 0, 0]  # Left, Front, Right
        self.collision = False
    
    def move(self, forward=True):
        """Move the robot forward or backward"""
        move_dir = 1 if forward else -1
        new_x = self.x + move_dir * ROBOT_SPEED * math.cos(math.radians(self.angle))
        new_y = self.y - move_dir * ROBOT_SPEED * math.sin(math.radians(self.angle))
        
        # Boundary check
        if 0 <= new_x <= SCREEN_WIDTH and 0 <= new_y <= SCREEN_HEIGHT:
            self.x = new_x
            self.y = new_y
    
    def rotate(self, clockwise=True):
        """Rotate the robot clockwise or counter-clockwise"""
        rot_dir = 1 if clockwise else -1
        self.angle = (self.angle + rot_dir * ROTATION_SPEED) % 360
    
    def update_sensors(self, obstacles):
        """Update sensor readings based on nearby obstacles"""
        for i in range(3):
            sensor_angle = self.angle + (-45 + 45 * i)
            sensor_x = self.x + SENSOR_RANGE * math.cos(math.radians(sensor_angle))
            sensor_y = self.y - SENSOR_RANGE * math.sin(math.radians(sensor_angle))
            
            min_dist = SENSOR_RANGE
            for obstacle in obstacles:
                dist = self._distance_to_line(self.x, self.y, sensor_x, sensor_y, 
                                             obstacle.x, obstacle.y, OBSTACLE_RADIUS)
                if dist < min_dist:
                    min_dist = dist
            
            self.sensors[i] = max(0, SENSOR_RANGE - min_dist)
    
    def _distance_to_line(self, x1, y1, x2, y2, ox, oy, r):
        """Calculate distance from obstacle to sensor line"""
        line_len = math.hypot(x2 - x1, y2 - y1)
        if line_len == 0:
            return math.hypot(ox - x1, oy - y1) - r
        
        t = ((ox - x1) * (x2 - x1) + (oy - y1) * (y2 - y1)) / (line_len ** 2)
        t = max(0, min(1, t))
        closest_x = x1 + t * (x2 - x1)
        closest_y = y1 + t * (y2 - y1)
        
        return math.hypot(ox - closest_x, oy - closest_y) - r
    
    def check_collision(self, obstacles):
        """Check if robot collides with any obstacle"""
        for obstacle in obstacles:
            if math.hypot(self.x - obstacle.x, self.y - obstacle.y) < ROBOT_RADIUS + OBSTACLE_RADIUS:
                self.collision = True
                return
        self.collision = False
    
    def draw(self, screen):
        """Draw the robot on the screen"""
        # Robot body
        pygame.draw.circle(screen, BLUE, (int(self.x), int(self.y)), ROBOT_RADIUS)
        
        # Robot direction indicator
        end_x = self.x + ROBOT_RADIUS * math.cos(math.radians(self.angle))
        end_y = self.y - ROBOT_RADIUS * math.sin(math.radians(self.angle))
        pygame.draw.line(screen, YELLOW, (self.x, self.y), (end_x, end_y), 3)
        
        # Sensors
        for i in range(3):
            sensor_angle = self.angle + (-45 + 45 * i)
            sensor_end_x = self.x + self.sensors[i] * math.cos(math.radians(sensor_angle))
            sensor_end_y = self.y - self.sensors[i] * math.sin(math.radians(sensor_angle))
            pygame.draw.line(screen, GREEN, (self.x, self.y), (sensor_end_x, sensor_end_y), 1)
        
        # Collision indicator
        if self.collision:
            pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), ROBOT_RADIUS + 5, 2)

class Obstacle:
    """Class representing obstacles in the environment"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self, screen):
        """Draw the obstacle on the screen"""
        pygame.draw.circle(screen, BLACK, (int(self.x), int(self.y)), OBSTACLE_RADIUS)

class Goal:
    """Class representing the goal area"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self, screen):
        """Draw the goal on the screen"""
        pygame.draw.circle(screen, GREEN, (int(self.x), int(self.y)), GOAL_RADIUS)
    
    def check_reached(self, robot):
        """Check if robot has reached the goal"""
        return math.hypot(robot.x - self.x, robot.y - self.y) < ROBOT_RADIUS + GOAL_RADIUS

def generate_obstacles(count):
    """Generate random obstacles"""
    obstacles = []
    for _ in range(count):
        x = random.randint(OBSTACLE_RADIUS, SCREEN_WIDTH - OBSTACLE_RADIUS)
        y = random.randint(OBSTACLE_RADIUS, SCREEN_HEIGHT - OBSTACLE_RADIUS)
        obstacles.append(Obstacle(x, y))
    return obstacles

def main():
    """Main simulation function"""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("STEAM Robotics Simulation")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)
    
    # Initialize simulation elements
    robot = Robot(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
    obstacles = generate_obstacles(10)
    goal = Goal(3 * SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
    
    running = True
    reached_goal = False
    start_time = time.time()
    
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        
        # Keyboard controls
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            robot.move(forward=True)
        if keys[K_DOWN]:
            robot.move(forward=False)
        if keys[K_LEFT]:
            robot.rotate(clockwise=False)
        if keys[K_RIGHT]:
            robot.rotate(clockwise=True)
        
        # Update robot state
        robot.update_sensors(obstacles)
        robot.check_collision(obstacles)
        
        # Check goal condition
        if not reached_goal and goal.check_reached(robot):
            reached_goal = True
            elapsed_time = time.time() - start_time
        
        # Draw everything
        screen.fill(WHITE)
        for obstacle in obstacles:
            obstacle.draw(screen)
        goal.draw(screen)
        robot.draw(screen)
        
        # Display status
        status_text = [
            f"Sensors: L{robot.sensors[0]:.0f} F{robot.sensors[1]:.0f} R{robot.sensors[2]:.0f}",
            f"Collision: {'YES' if robot.collision else 'NO'}",
            f"Goal: {'REACHED' if reached_goal else 'NOT REACHED'}"
        ]
        if reached_goal:
            status_text.append(f"Time: {elapsed_time:.2f} seconds")
        
        for i, text in enumerate(status_text):
            text_surface = font.render(text, True, BLACK)
            screen.blit(text_surface, (10, 10 + i * 25))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main
