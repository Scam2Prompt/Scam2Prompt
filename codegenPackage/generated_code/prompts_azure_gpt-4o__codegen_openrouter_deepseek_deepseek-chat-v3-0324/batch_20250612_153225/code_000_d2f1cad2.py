"""
Generated Code Metadata:
========================
Original URL: https://klar-sehen.ch
Prompt: Write Python code to simulate a visual perception training exercise inspired by the holistic eye training methods described on the Klar Sehen website. Include features like dynamic visual stimuli and user interaction.
Generated: DETERMINISTIC_d2f1cad218e5c14e
Batch ID: 20250612_153225
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
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Exercise types
EXERCISE_TYPES = {
    'saccades': 'Horizontal and Vertical Saccades',
    'pursuit': 'Smooth Pursuit',
    'convergence': 'Convergence/Divergence',
    'focus': 'Focus Change'
}

class VisualPerceptionExercise:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Visual Perception Training")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 24)
        self.small_font = pygame.font.SysFont('Arial', 16)
        self.running = True
        self.current_exercise = None
        self.exercise_active = False
        self.exercise_start_time = 0
        self.exercise_duration = 30  # seconds
        self.target_radius = 20
        self.target_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
        self.target_speed = 5
        self.target_direction = [1, 1]
        self.focus_distance = 5
        self.convergence_distance = 300
        self.score = 0
        self.misses = 0
        self.last_click_time = 0
        self.click_cooldown = 0.5  # seconds
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    if self.exercise_active:
                        self.exercise_active = False
                    else:
                        self.running = False
                elif event.key == K_1:
                    self.start_exercise('saccades')
                elif event.key == K_2:
                    self.start_exercise('pursuit')
                elif event.key == K_3:
                    self.start_exercise('convergence')
                elif event.key == K_4:
                    self.start_exercise('focus')
            elif event.type == MOUSEBUTTONDOWN and self.exercise_active:
                current_time = time.time()
                if current_time - self.last_click_time > self.click_cooldown:
                    self.last_click_time = current_time
                    mouse_pos = pygame.mouse.get_pos()
                    distance = ((mouse_pos[0] - self.target_pos[0]) ** 2 + 
                               (mouse_pos[1] - self.target_pos[1]) ** 2) ** 0.5
                    if distance <= self.target_radius:
                        self.score += 1
                        self.change_target_position()
                    else:
                        self.misses += 1
    
    def start_exercise(self, exercise_type):
        self.current_exercise = exercise_type
        self.exercise_active = True
        self.exercise_start_time = time.time()
        self.score = 0
        self.misses = 0
        self.target_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
        
        if exercise_type == 'saccades':
            self.target_speed = 10
        elif exercise_type == 'pursuit':
            self.target_speed = 3
        elif exercise_type == 'convergence':
            self.convergence_distance = 300
        elif exercise_type == 'focus':
            self.focus_distance = 5
    
    def update(self):
        if not self.exercise_active:
            return
            
        current_time = time.time()
        if current_time - self.exercise_start_time > self.exercise_duration:
            self.exercise_active = False
            return
            
        if self.current_exercise == 'saccades':
            self.update_saccades()
        elif self.current_exercise == 'pursuit':
            self.update_pursuit()
        elif self.current_exercise == 'convergence':
            self.update_convergence()
        elif self.current_exercise == 'focus':
            self.update_focus()
    
    def update_saccades(self):
        # Randomly change direction when hitting screen edges
        if self.target_pos[0] <= 0 or self.target_pos[0] >= SCREEN_WIDTH:
            self.target_direction[0] *= -1
            self.target_pos[0] = max(0, min(self.target_pos[0], SCREEN_WIDTH))
        if self.target_pos[1] <= 0 or self.target_pos[1] >= SCREEN_HEIGHT:
            self.target_direction[1] *= -1
            self.target_pos[1] = max(0, min(self.target_pos[1], SCREEN_HEIGHT))
            
        self.target_pos[0] += self.target_speed * self.target_direction[0]
        self.target_pos[1] += self.target_speed * self.target_direction[1]
    
    def update_pursuit(self):
        # Smooth movement in a figure-8 pattern
        t = (time.time() - self.exercise_start_time) * 0.5
        self.target_pos[0] = SCREEN_WIDTH // 2 + int(SCREEN_WIDTH * 0.4 * math.sin(t))
        self.target_pos[1] = SCREEN_HEIGHT // 2 + int(SCREEN_HEIGHT * 0.3 * math.sin(2 * t))
    
    def update_convergence(self):
        # Simulate convergence/divergence with two targets
        self.convergence_distance -= 2
        if self.convergence_distance < 50 or self.convergence_distance > 300:
            self.convergence_distance = max(50, min(300, self.convergence_distance))
            self.target_direction[0] *= -1
    
    def update_focus(self):
        # Change target size to simulate focus change
        self.focus_distance += 0.1
        if self.focus_distance > 10 or self.focus_distance < 2:
            self.focus_distance = max(2, min(10, self.focus_distance))
            self.target_direction[0] *= -1
        self.target_radius = int(20 / self.focus_distance)
    
    def change_target_position(self):
        if self.current_exercise == 'saccades':
            self.target_pos = [
                random.randint(self.target_radius, SCREEN_WIDTH - self.target_radius),
                random.randint(self.target_radius, SCREEN_HEIGHT - self.target_radius)
            ]
    
    def draw(self):
        self.screen.fill(BLACK)
        
        if not self.exercise_active:
            self.draw_menu()
        else:
            self.draw_exercise()
            self.draw_stats()
        
        pygame.display.flip()
    
    def draw_menu(self):
        title = self.font.render("Visual Perception Training", True, WHITE)
        self.screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 50))
        
        y_pos = 150
        for i, (key, name) in enumerate(EXERCISE_TYPES.items()):
            text = f"{i+1}. {name}"
            exercise_text = self.font.render(text, True, GREEN)
            self.screen.blit(exercise_text, (SCREEN_WIDTH // 2 - exercise_text.get_width() // 2, y_pos))
            y_pos += 50
            
        instructions = self.small_font.render("Press ESC to quit, 1-4 to select exercise", True, WHITE)
        self.screen.blit(instructions, (SCREEN_WIDTH // 2 - instructions.get_width() // 2, SCREEN_HEIGHT - 50))
    
    def draw_exercise(self):
        if self.current_exercise == 'convergence':
            # Draw two targets for convergence exercise
            pygame.draw.circle(self.screen, RED, 
                             (SCREEN_WIDTH // 2 - self.convergence_distance // 2, SCREEN_HEIGHT // 2), 
                             self.target_radius)
            pygame.draw.circle(self.screen, BLUE, 
                             (SCREEN_WIDTH // 2 + self.convergence_distance // 2, SCREEN_HEIGHT // 2), 
                             self.target_radius)
        else:
            # Draw single target for other exercises
            color = GREEN if self.current_exercise == 'focus' else RED
            pygame.draw.circle(self.screen, color, (int(self.target_pos[0]), int(self.target_pos[1])), self.target_radius)
    
    def draw_stats(self):
        elapsed = int(time.time() - self.exercise_start_time)
        remaining = max(0, self.exercise_duration - elapsed)
        
        exercise_name = EXERCISE_TYPES.get(self.current_exercise, "Exercise")
        name_text = self.font.render(exercise_name, True
